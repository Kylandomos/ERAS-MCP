from __future__ import annotations

import contextlib
import io
import json
import sys
from pathlib import Path
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mcp_server.facade import MCPFacade
from mcp_server import cli as cli_module
from services import ArtifactStore, SearchBounds


def _write_inventory(path: Path, scan_id: str, generated_at_utc: str, scan_root: Path) -> None:
    payload = {
        "metadata": {
            "scan_id": scan_id,
            "generated_at_utc": generated_at_utc,
            "read_only": True,
        },
        "scan_roots": [
            {
                "path": str(scan_root),
                "source": "user_provided_verified",
                "exists": True,
            }
        ],
        "powermap": {
            "generated_at_utc": generated_at_utc,
            "workspace_path_candidates": [str(scan_root / "workspace")],
            "discovered_executables": [{"path": "C:\\Program Files\\Bentley\\MapPowerView.exe"}],
            "config_files": [],
            "python_manager": {"found": False, "scripts": [], "executables": []},
            "macro_inventory": {"vba_files": [], "keyin_files": []},
            "safe_read_action_candidates": [{"action": "Read metadata"}],
            "gaps_and_fallbacks": [],
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


class TestArtifactStoreInventorySelection(unittest.TestCase):
    def test_latest_inventory_path_uses_timestamped_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            root = repo / "sample_root"
            root.mkdir(parents=True, exist_ok=True)
            _write_inventory(
                repo / "artifacts" / "inventories" / "windows_scan_20260423_120000" / "inventory.json",
                "windows_scan_20260423_120000",
                "2026-04-23T12:00:00Z",
                root,
            )
            _write_inventory(
                repo / "artifacts" / "inventories" / "windows_scan_20260423_130000" / "inventory.json",
                "windows_scan_20260423_130000",
                "2026-04-23T13:00:00Z",
                root,
            )
            store = ArtifactStore(repo)
            latest = store.latest_inventory_path()
            self.assertIsNotNone(latest)
            self.assertEqual(latest.parent.name, "windows_scan_20260423_130000")


class TestMcpFacadeReadOnly(unittest.TestCase):
    def test_find_artifacts_enforces_bounds_and_allowed_roots(self) -> None:
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as outside_tmp:
            repo = Path(repo_tmp)
            allowed_root = repo / "allowed"
            allowed_root.mkdir(parents=True, exist_ok=True)
            for index in range(5):
                (allowed_root / f"sample_{index}.mdb").write_text("x", encoding="utf-8")
            outside_root = Path(outside_tmp)
            (outside_root / "outside.mdb").write_text("x", encoding="utf-8")

            _write_inventory(
                repo / "artifacts" / "inventories" / "windows_scan_20260423_140000" / "inventory.json",
                "windows_scan_20260423_140000",
                "2026-04-23T14:00:00Z",
                allowed_root,
            )

            facade = MCPFacade(
                repo_root=repo,
                search_bounds=SearchBounds(max_roots=8, max_files_scanned=3, max_results=2),
            )

            result = facade.find_artifacts(
                patterns=["*.mdb"],
                roots=[str(outside_root), str(allowed_root)],
            )

            self.assertTrue(result["stopped_by_limits"])
            self.assertLessEqual(result["files_scanned"], 4)
            self.assertLessEqual(len(result["matches"]), 2)
            rejected = {entry["root"]: entry["reason"] for entry in result["rejected_roots"]}
            self.assertEqual(rejected.get(str(outside_root.resolve())), "outside_allowed_bounds")
            for match in result["matches"]:
                self.assertTrue(str(match["path"]).startswith(str(allowed_root.resolve())))

    def test_eras_database_and_table_loading_from_exports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)

            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "\n".join(
                    [
                        "source_path,extension,file_size_bytes,modified_utc,source_sha256,analysis_path,analysis_sha256,hash_match",
                        r"C:\src\a.mdb,.mdb,10,2026-04-23T10:00:00Z,sha1,C:\work\a.mdb,sha1,True",
                        r"C:\src\b.mdb,.mdb,20,2026-04-23T10:00:00Z,sha2,C:\work\b.mdb,sha2,True",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "\n".join(
                    [
                        "database_path,table_name,row_count,column_count,primary_key_columns,index_count",
                        r"C:\work\a.mdb,Asset,12,5,id,1",
                        r"C:\work\b.mdb,Site,30,4,,0",
                    ]
                ),
                encoding="utf-8",
            )

            facade = MCPFacade(repo_root=repo)
            dbs = facade.eras_list_databases()
            tables = facade.eras_list_tables(database_filter="a.mdb")

            self.assertTrue(dbs["read_only"])
            self.assertIn("source_artifact", dbs)
            self.assertIn("generated_at_utc", dbs)
            self.assertEqual(dbs["counts"]["database_count"], 2)
            self.assertTrue(tables["read_only"])
            self.assertIn("warnings", tables)
            self.assertEqual(tables["counts"]["table_count"], 1)
            self.assertEqual(dbs["database_count"], 2)
            self.assertEqual(tables["table_count"], 1)
            self.assertEqual(tables["tables"][0]["table_name"], "Asset")

    def test_eras_database_counts_distinguish_candidates_paths_and_keys(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)
            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "\n".join(
                    [
                        "source_path,extension,file_size_bytes,modified_utc,source_sha256,analysis_path,analysis_sha256,hash_match",
                        r"C:\src\a.mdb,.mdb,10,2026-04-23T10:00:00Z,sha1,C:\work\a.mdb,sha1,True",
                        r"C:\src\a-copy.mdb,.mdb,10,2026-04-23T10:00:00Z,sha1,C:\work\a.mdb,sha1,True",
                        r"C:\src\b.mdb,.mdb,20,2026-04-23T10:00:00Z,sha2,C:\work\B.mdb,sha2,True",
                        r"C:\src\b-lower.mdb,.mdb,20,2026-04-23T10:00:00Z,sha2,C:\work\b.mdb,sha2,True",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "database_path,table_name,row_count,column_count,primary_key_columns,index_count\n",
                encoding="utf-8",
            )

            facade = MCPFacade(repo_root=repo)
            status = facade.env_status()
            databases = facade.eras_list_databases()

            self.assertEqual(status["counts"]["eras_candidate_count"], 4)
            self.assertEqual(status["counts"]["eras_unique_analysis_path_count"], 3)
            self.assertEqual(status["counts"]["eras_unique_analysis_key_count"], 2)
            self.assertEqual(databases["counts"]["candidate_count"], 4)
            self.assertEqual(databases["counts"]["unique_analysis_path_count"], 3)
            self.assertEqual(databases["counts"]["unique_analysis_key_count"], 2)

    def test_powermap_status_and_workspaces_from_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            root = repo / "scan_root"
            root.mkdir(parents=True, exist_ok=True)
            _write_inventory(
                repo / "artifacts" / "inventories" / "windows_scan_20260423_150000" / "inventory.json",
                "windows_scan_20260423_150000",
                "2026-04-23T15:00:00Z",
                root,
            )

            facade = MCPFacade(repo_root=repo)
            status = facade.powermap_status()
            workspaces = facade.powermap_list_workspaces()

            self.assertTrue(status["read_only"])
            self.assertIn("source_artifact", status)
            self.assertEqual(status["counts"]["workspace_count"], 1)
            self.assertTrue(workspaces["read_only"])
            self.assertEqual(workspaces["counts"]["workspace_count"], 1)
            self.assertEqual(status["workspace_count"], 1)
            self.assertFalse(status["python_manager_found"])
            self.assertEqual(workspaces["workspace_count"], 1)

    def test_env_status_and_gap_report_use_standard_envelope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            root = repo / "scan_root"
            root.mkdir(parents=True, exist_ok=True)
            _write_inventory(
                repo / "artifacts" / "inventories" / "windows_scan_20260423_160000" / "inventory.json",
                "windows_scan_20260423_160000",
                "2026-04-23T16:00:00Z",
                root,
            )
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)
            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "source_path,analysis_path,hash_match\n"
                r"C:\src\a.mdb,C:\work\a.mdb,True",
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "database_path,table_name,row_count,column_count,primary_key_columns,index_count\n"
                r"C:\work\a.mdb,Asset,12,5,id,1",
                encoding="utf-8",
            )

            facade = MCPFacade(repo_root=repo)
            status = facade.env_status()
            gaps = facade.build_gap_report()

            self.assertTrue(status["read_only"])
            self.assertIn("source_artifact", status)
            self.assertEqual(status["counts"]["eras_database_count"], 1)
            self.assertIn("generated_at_utc", gaps)
            self.assertTrue(gaps["read_only"])
            self.assertIn("warnings", gaps)
            self.assertEqual(gaps["counts"]["gap_count"], gaps["gap_count"])

    def test_eras_rank_databases_uses_standard_envelope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)
            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "\n".join(
                    [
                        "source_path,extension,file_size_bytes,modified_utc,source_sha256,analysis_path,analysis_sha256,hash_match",
                        r"C:\App\CLIENT\a.mdb,.mdb,100,2026-04-20T00:00:00+00:00,sha1,C:\work\a.mdb,sha1,True",
                        r"C:\App\SYSTEME\b_.mdb,.mdb,200,2026-04-19T00:00:00+00:00,sha2,C:\work\b_.mdb,sha2,True",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "\n".join(
                    [
                        "database_path,table_name,row_count,column_count,primary_key_columns,index_count",
                        r"C:\work\a.mdb,T1,1000,2,,0",
                        r"C:\work\a.mdb,T2,1,2,,0",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_SCHEMA.md").write_text(
                "\n".join(
                    [
                        r"## Database: `C:\work\b_.mdb`",
                        "- ODBC schema read failed: example",
                    ]
                ),
                encoding="utf-8",
            )

            facade = MCPFacade(repo_root=repo)
            result = facade.eras_rank_databases(limit=1)

            self.assertTrue(result["read_only"])
            self.assertEqual(result["decision_status"], "candidate_ranking_only")
            self.assertEqual(result["counts"]["candidate_count"], 2)
            self.assertEqual(result["counts"]["returned_count"], 1)
            self.assertEqual(result["candidates"][0]["source_path"], r"C:\App\CLIENT\a.mdb")

    def test_eras_explain_database_returns_metadata_only_details(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)
            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "\n".join(
                    [
                        "source_path,extension,file_size_bytes,modified_utc,source_sha256,analysis_path,analysis_sha256,hash_match",
                        r"C:\App\CLIENT\a.mdb,.mdb,100,2026-04-20T00:00:00+00:00,sha1,C:\work\a.mdb,sha1,True",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "\n".join(
                    [
                        "database_path,table_name,row_count,column_count,primary_key_columns,index_count",
                        r"C:\work\a.mdb,Asset,12,5,id,1",
                        r"C:\work\a.mdb,Site,30,4,,0",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_SCHEMA.md").write_text("", encoding="utf-8")

            facade = MCPFacade(repo_root=repo)
            result = facade.eras_explain_database(r"C:\App\CLIENT\a.mdb")

            self.assertTrue(result["read_only"])
            self.assertEqual(result["decision_status"], "candidate_ranking_only")
            self.assertEqual(result["data_policy"], "metadata_only_no_business_row_values")
            self.assertEqual(result["match_strategy"], "exact_source_path")
            self.assertEqual(result["counts"]["match_count"], 1)
            self.assertEqual(result["counts"]["table_count"], 2)
            self.assertEqual(result["candidate"]["source_path"], r"C:\App\CLIENT\a.mdb")
            self.assertEqual(result["tables"][0]["table_name"], "Asset")
            self.assertNotIn("row_values", result)
            self.assertNotIn("sample_rows", json.dumps(result))

    def test_eras_explain_database_reports_ambiguous_basename(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            exports = repo / "artifacts" / "exports"
            exports.mkdir(parents=True, exist_ok=True)
            (exports / "ERAS_MDB_DISCOVERY.csv").write_text(
                "\n".join(
                    [
                        "source_path,extension,file_size_bytes,modified_utc,source_sha256,analysis_path,analysis_sha256,hash_match",
                        r"C:\App\CLIENT\a.mdb,.mdb,100,2026-04-20T00:00:00+00:00,sha1,C:\work\a1.mdb,sha1,True",
                        r"C:\App\SYSTEME\a.mdb,.mdb,100,2026-04-20T00:00:00+00:00,sha2,C:\work\a2.mdb,sha2,True",
                    ]
                ),
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_TABLES.csv").write_text(
                "database_path,table_name,row_count,column_count,primary_key_columns,index_count\n",
                encoding="utf-8",
            )
            (exports / "ERAS_MDB_SCHEMA.md").write_text("", encoding="utf-8")

            result = MCPFacade(repo_root=repo).eras_explain_database("a.mdb")

            self.assertIsNone(result["candidate"])
            self.assertEqual(result["match_strategy"], "basename")
            self.assertEqual(result["counts"]["match_count"], 2)
            self.assertIn("disambiguate", result["warnings"][0])

    def test_cli_eras_explain_database_dispatches_to_facade(self) -> None:
        class FakeFacade:
            def eras_explain_database(self, database_path: str) -> dict[str, object]:
                return {
                    "generated_at_utc": "2026-04-23T00:00:00+00:00",
                    "read_only": True,
                    "source_artifact": {},
                    "warnings": [],
                    "counts": {"match_count": 1},
                    "decision_status": "candidate_ranking_only",
                    "database_path": database_path,
                }

        original_facade = cli_module.MCPFacade
        cli_module.MCPFacade = FakeFacade  # type: ignore[assignment]
        try:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                exit_code = cli_module.main(
                    ["eras-explain-database", "--path", r"C:\App\CLIENT\a.mdb"]
                )
        finally:
            cli_module.MCPFacade = original_facade

        self.assertEqual(exit_code, 0)
        payload = json.loads(stdout.getvalue())
        self.assertEqual(payload["database_path"], r"C:\App\CLIENT\a.mdb")
        self.assertEqual(payload["decision_status"], "candidate_ranking_only")


if __name__ == "__main__":
    unittest.main()
