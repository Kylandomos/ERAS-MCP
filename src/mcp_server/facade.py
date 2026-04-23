from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from adapters.powermap import PowerMapArtifactAdapter
from services import (
    ArtifactStore,
    SearchBounds,
    find_artifacts_safe,
    rank_mdb_candidates,
)

DEFAULT_PATTERNS = [
    "*.mdb",
    "*.accdb",
    "*.dgn",
    "*.cfg",
    "*.ucf",
    "*.upf",
    "*.ini",
    "*.xml",
    "*.json",
    "*.ps1",
    "*.bat",
    "*.vbs",
    "*.py",
    "*.mvba",
    "*.vba",
    "*.bas",
    "*.keyin",
    "*.log",
    "*.csv",
    "*.xls",
    "*.xlsx",
]


def _as_int(value: str | int | None) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


class MCPFacade:
    """Read-only facade over generated scanner/MDB artifacts."""

    def __init__(
        self,
        repo_root: str | Path | None = None,
        *,
        search_bounds: SearchBounds | None = None,
    ) -> None:
        self.store = ArtifactStore(repo_root)
        self.repo_root = self.store.repo_root
        self.search_bounds = search_bounds or SearchBounds()

    def _latest_inventory(self) -> dict[str, Any] | None:
        return self.store.load_inventory(latest=True)

    def _allowed_search_roots(self, inventory: dict[str, Any] | None) -> list[Path]:
        roots: list[Path] = [self.repo_root, self.store.artifacts_root]
        roots.extend(self.store.known_scan_roots(inventory))
        unique: dict[str, Path] = {}
        for root in roots:
            unique[str(root).lower()] = root
        return list(unique.values())

    def _default_search_roots(self, inventory: dict[str, Any] | None) -> list[Path]:
        known = self.store.known_scan_roots(inventory)
        if known:
            return known
        return [self.store.artifacts_root]

    def _export_path(self, filename: str) -> Path:
        return self.store.exports_root / filename

    def _schema_warning_count(self) -> int:
        schema_path = self._export_path("ERAS_MDB_SCHEMA.md")
        if not schema_path.is_file():
            return 0
        try:
            return schema_path.read_text(encoding="utf-8-sig").count(
                "ODBC schema read failed"
            )
        except OSError:
            return 0

    def _schema_text(self) -> str:
        schema_path = self._export_path("ERAS_MDB_SCHEMA.md")
        if not schema_path.is_file():
            return ""
        try:
            return schema_path.read_text(encoding="utf-8-sig")
        except OSError:
            return ""

    def _powermap_warnings(self, inventory: dict[str, Any] | None) -> list[str]:
        powermap = PowerMapArtifactAdapter(inventory).powermap
        warnings: list[str] = []
        for gap in powermap.get("gaps_and_fallbacks", []) or []:
            if not isinstance(gap, dict):
                continue
            text = str(gap.get("gap", "")).strip()
            if text:
                warnings.append(text)
        return warnings

    def env_status(self) -> dict[str, Any]:
        inventory_path = self.store.latest_inventory_path()
        inventory = self._latest_inventory()
        powermap = PowerMapArtifactAdapter(inventory)
        discovery_rows = self.store.read_export_csv("ERAS_MDB_DISCOVERY.csv")
        table_rows = self.store.read_export_csv("ERAS_MDB_TABLES.csv")
        schema_warning_count = self._schema_warning_count()
        warnings = self._powermap_warnings(inventory)
        if schema_warning_count:
            warnings.append(
                f"{schema_warning_count} ERAS MDB schema analyses reported ODBC warnings."
            )
        counts = {
            "eras_database_count": len(
                {
                    row.get("analysis_path") or row.get("source_path")
                    for row in discovery_rows
                    if row.get("analysis_path") or row.get("source_path")
                }
            ),
            "eras_table_count": len(table_rows),
            "schema_warning_count": schema_warning_count,
            "powermap_gap_count": powermap.status().get("gap_count", 0),
        }

        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": {
                "inventory": str(inventory_path) if inventory_path else None,
                "eras_discovery": str(self._export_path("ERAS_MDB_DISCOVERY.csv")),
                "eras_tables": str(self._export_path("ERAS_MDB_TABLES.csv")),
            },
            "warnings": warnings,
            "counts": counts,
            "repo_root": str(self.repo_root),
            "inventory_available": inventory is not None,
            "latest_inventory_path": str(inventory_path) if inventory_path else None,
            "inventory_scan_id": (
                inventory.get("metadata", {}).get("scan_id") if inventory else None
            ),
            "eras_discovery_available": bool(discovery_rows),
            "eras_tables_available": bool(table_rows),
            "eras_database_count": counts["eras_database_count"],
            "eras_table_count": counts["eras_table_count"],
            "powermap": powermap.status(),
        }

    def env_inventory(self, latest: bool = True) -> dict[str, Any]:
        if latest:
            path = self.store.latest_inventory_path()
            inventory = self._latest_inventory()
            return {
                "generated_at_utc": _now_utc(),
                "read_only": True,
                "source_artifact": str(path) if path else None,
                "warnings": [] if inventory else ["No inventory artifact is available."],
                "counts": {
                    "inventory_count": 1 if inventory else 0,
                    "scan_root_count": len(inventory.get("scan_roots", [])) if inventory else 0,
                },
                "latest": True,
                "inventory_path": str(path) if path else None,
                "inventory": inventory,
            }
        summaries = self.store.load_inventory_summaries()
        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": str(self.store.inventories_root),
            "warnings": [],
            "counts": {"inventory_count": len(summaries)},
            "latest": False,
            "inventories": summaries,
        }

    def find_artifacts(
        self,
        patterns: Iterable[str] | None = None,
        roots: Iterable[str] | None = None,
    ) -> dict[str, Any]:
        inventory = self._latest_inventory()
        safe_patterns = [pattern for pattern in (patterns or DEFAULT_PATTERNS) if pattern]
        if not safe_patterns:
            safe_patterns = DEFAULT_PATTERNS.copy()

        requested_roots: list[Path]
        if roots:
            requested_roots = [Path(root).expanduser() for root in roots if str(root).strip()]
        else:
            requested_roots = self._default_search_roots(inventory)

        normalized_roots: list[Path] = []
        for root in requested_roots:
            try:
                normalized_roots.append(root.resolve())
            except Exception:
                continue

        allowed_roots = self._allowed_search_roots(inventory)
        search = find_artifacts_safe(
            patterns=safe_patterns,
            roots=normalized_roots,
            allowed_roots=allowed_roots,
            bounds=self.search_bounds,
        )
        search["allowed_roots"] = [str(root) for root in allowed_roots]
        search["generated_at_utc"] = _now_utc()
        search["read_only"] = True
        search["source_artifact"] = {
            "inventory": str(self.store.latest_inventory_path())
            if self.store.latest_inventory_path()
            else None,
            "filesystem_roots": [str(root) for root in normalized_roots],
        }
        search["warnings"] = [
            f"Rejected root {entry['root']}: {entry['reason']}"
            for entry in search.get("rejected_roots", [])
        ]
        search["counts"] = {
            "accepted_root_count": len(search.get("accepted_roots", [])),
            "rejected_root_count": len(search.get("rejected_roots", [])),
            "files_scanned": search.get("files_scanned", 0),
            "match_count": len(search.get("matches", [])),
        }
        return search

    def eras_list_databases(self) -> dict[str, Any]:
        rows = self.store.read_export_csv("ERAS_MDB_DISCOVERY.csv")
        databases: list[dict[str, Any]] = []
        seen_keys: set[str] = set()

        for row in rows:
            preferred_path = row.get("analysis_path") or row.get("source_path")
            if not preferred_path:
                continue
            lowered = preferred_path.lower()
            if lowered in seen_keys:
                continue
            seen_keys.add(lowered)
            databases.append(
                {
                    "source_path": row.get("source_path"),
                    "analysis_path": row.get("analysis_path") or None,
                    "extension": row.get("extension"),
                    "file_size_bytes": _as_int(row.get("file_size_bytes")),
                    "modified_utc": row.get("modified_utc"),
                    "source_sha256": row.get("source_sha256"),
                    "analysis_sha256": row.get("analysis_sha256"),
                    "hash_match": str(row.get("hash_match", "")).lower() == "true",
                }
            )

        hash_mismatch_count = len(
            [item for item in databases if not item.get("hash_match")]
        )
        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": str(self._export_path("ERAS_MDB_DISCOVERY.csv")),
            "warnings": (
                [f"{hash_mismatch_count} database analysis copies failed hash match."]
                if hash_mismatch_count
                else []
            ),
            "counts": {
                "database_count": len(databases),
                "hash_match_count": len(databases) - hash_mismatch_count,
                "hash_mismatch_count": hash_mismatch_count,
            },
            "database_count": len(databases),
            "databases": sorted(
                databases,
                key=lambda item: (
                    (item.get("analysis_path") or item.get("source_path") or "").lower()
                ),
            ),
        }

    def eras_list_tables(self, database_filter: str | None = None) -> dict[str, Any]:
        rows = self.store.read_export_csv("ERAS_MDB_TABLES.csv")
        filter_value = (database_filter or "").strip().lower()
        tables: list[dict[str, Any]] = []

        for row in rows:
            database_path = row.get("database_path", "")
            if filter_value and filter_value not in database_path.lower():
                continue
            tables.append(
                {
                    "database_path": database_path,
                    "table_name": row.get("table_name"),
                    "row_count": _as_int(row.get("row_count")),
                    "column_count": _as_int(row.get("column_count")),
                    "primary_key_columns": row.get("primary_key_columns") or "",
                    "index_count": _as_int(row.get("index_count")),
                }
            )

        database_count = len({table["database_path"] for table in tables if table["database_path"]})
        schema_warning_count = self._schema_warning_count()
        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": str(self._export_path("ERAS_MDB_TABLES.csv")),
            "warnings": (
                [f"{schema_warning_count} ERAS MDB schema analyses reported ODBC warnings."]
                if schema_warning_count
                else []
            ),
            "counts": {
                "database_count": database_count,
                "table_count": len(tables),
                "schema_warning_count": schema_warning_count,
            },
            "database_filter": database_filter,
            "database_count": database_count,
            "table_count": len(tables),
            "tables": tables,
        }

    def eras_rank_databases(
        self, limit: int = 10, include_all: bool = False
    ) -> dict[str, Any]:
        safe_limit = max(1, min(int(limit or 10), 100))
        discovery_rows = self.store.read_export_csv("ERAS_MDB_DISCOVERY.csv")
        table_rows = self.store.read_export_csv("ERAS_MDB_TABLES.csv")
        schema_text = self._schema_text()
        ranked = rank_mdb_candidates(
            discovery_rows=discovery_rows,
            table_rows=table_rows,
            schema_text=schema_text,
        )
        selected = ranked if include_all else ranked[:safe_limit]
        warning_count = len([item for item in ranked if item.has_schema_warning])
        incomplete_count = len([item for item in ranked if item.table_count == 0])

        warnings: list[str] = []
        if warning_count:
            warnings.append(
                f"{warning_count} ranked MDB candidates have ODBC schema warnings."
            )
        if incomplete_count:
            warnings.append(
                f"{incomplete_count} ranked MDB candidates have no extracted tables."
            )

        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": {
                "eras_discovery": str(self._export_path("ERAS_MDB_DISCOVERY.csv")),
                "eras_tables": str(self._export_path("ERAS_MDB_TABLES.csv")),
                "eras_schema": str(self._export_path("ERAS_MDB_SCHEMA.md")),
            },
            "warnings": warnings,
            "counts": {
                "candidate_count": len(ranked),
                "returned_count": len(selected),
                "schema_warning_count": warning_count,
                "incomplete_schema_count": incomplete_count,
            },
            "decision_status": "candidate_ranking_only",
            "limit": safe_limit,
            "include_all": include_all,
            "candidates": [item.to_dict() for item in selected],
        }

    def powermap_status(self) -> dict[str, Any]:
        inventory = self._latest_inventory()
        inventory_path = self.store.latest_inventory_path()
        status = PowerMapArtifactAdapter(inventory).status()
        status.update(
            {
                "generated_at_utc": _now_utc(),
                "read_only": True,
                "source_artifact": str(inventory_path) if inventory_path else None,
                "warnings": self._powermap_warnings(inventory),
                "counts": {
                    "executable_count": status.get("executable_count", 0),
                    "workspace_count": status.get("workspace_count", 0),
                    "gap_count": status.get("gap_count", 0),
                },
            }
        )
        return status

    def powermap_list_workspaces(self) -> dict[str, Any]:
        inventory = self._latest_inventory()
        workspaces = PowerMapArtifactAdapter(inventory).list_workspaces()
        return {
            "generated_at_utc": _now_utc(),
            "read_only": True,
            "source_artifact": str(self.store.latest_inventory_path())
            if self.store.latest_inventory_path()
            else None,
            "warnings": self._powermap_warnings(inventory),
            "counts": {"workspace_count": len(workspaces)},
            "workspace_count": len(workspaces),
            "workspaces": workspaces,
        }

    def build_gap_report(self) -> dict[str, Any]:
        now_utc = _now_utc()
        inventory = self._latest_inventory()
        discovery = self.eras_list_databases()
        tables = self.eras_list_tables()
        powermap_inventory = PowerMapArtifactAdapter(inventory).powermap

        gaps: list[dict[str, str]] = []
        if inventory is None:
            gaps.append(
                {
                    "area": "environment",
                    "gap": "No inventory artifact found under artifacts/inventories/**/inventory.json.",
                    "suggested_action": "Run scripts/windows_scan/Invoke-WindowsReadOnlyInventory.ps1 once.",
                }
            )

        if discovery["database_count"] == 0:
            gaps.append(
                {
                    "area": "eras_mdb",
                    "gap": "No ERAS_MDB_DISCOVERY.csv entries were loaded.",
                    "suggested_action": "Generate artifacts/exports/ERAS_MDB_DISCOVERY.csv from the existing pipeline.",
                }
            )

        if tables["table_count"] == 0:
            gaps.append(
                {
                    "area": "eras_mdb",
                    "gap": "No ERAS_MDB_TABLES.csv entries were loaded.",
                    "suggested_action": "Generate artifacts/exports/ERAS_MDB_TABLES.csv from read-only analysis outputs.",
                }
            )

        schema_warning_count = self._schema_warning_count()
        if schema_warning_count:
            gaps.append(
                {
                    "area": "eras_mdb",
                    "gap": f"{schema_warning_count} MDB schema analyses reported UTF-16 ODBC decode warnings.",
                    "suggested_action": "Classify warning cases and use candidate ranking as review guidance, not a final authoritative decision.",
                }
            )

        if powermap_inventory:
            for gap in powermap_inventory.get("gaps_and_fallbacks", []) or []:
                if not isinstance(gap, dict):
                    continue
                gaps.append(
                    {
                        "area": "powermap",
                        "gap": str(gap.get("gap", "")).strip(),
                        "suggested_action": str(gap.get("fallback", "")).strip(),
                    }
                )
        else:
            gaps.append(
                {
                    "area": "powermap",
                    "gap": "No powermap section was found in the latest inventory.",
                    "suggested_action": "Run inventory script with PowerMap discovery enabled.",
                }
            )

        return {
            "generated_at_utc": now_utc,
            "read_only": True,
            "source_artifact": {
                "inventory": str(self.store.latest_inventory_path())
                if self.store.latest_inventory_path()
                else None,
                "eras_discovery": str(self._export_path("ERAS_MDB_DISCOVERY.csv")),
                "eras_tables": str(self._export_path("ERAS_MDB_TABLES.csv")),
                "eras_schema": str(self._export_path("ERAS_MDB_SCHEMA.md")),
            },
            "warnings": [gap["gap"] for gap in gaps if gap.get("gap")],
            "counts": {"gap_count": len(gaps)},
            "gap_count": len(gaps),
            "gaps": gaps,
        }


_DEFAULT_FACADE = MCPFacade()


def env_status() -> dict[str, Any]:
    return _DEFAULT_FACADE.env_status()


def env_inventory(latest: bool = True) -> dict[str, Any]:
    return _DEFAULT_FACADE.env_inventory(latest=latest)


def find_artifacts(
    patterns: Iterable[str] | None = None,
    roots: Iterable[str] | None = None,
) -> dict[str, Any]:
    return _DEFAULT_FACADE.find_artifacts(patterns=patterns, roots=roots)


def eras_list_databases() -> dict[str, Any]:
    return _DEFAULT_FACADE.eras_list_databases()


def eras_list_tables(database_filter: str | None = None) -> dict[str, Any]:
    return _DEFAULT_FACADE.eras_list_tables(database_filter=database_filter)


def eras_rank_databases(limit: int = 10, include_all: bool = False) -> dict[str, Any]:
    return _DEFAULT_FACADE.eras_rank_databases(limit=limit, include_all=include_all)


def powermap_status() -> dict[str, Any]:
    return _DEFAULT_FACADE.powermap_status()


def powermap_list_workspaces() -> dict[str, Any]:
    return _DEFAULT_FACADE.powermap_list_workspaces()


def build_gap_report() -> dict[str, Any]:
    return _DEFAULT_FACADE.build_gap_report()
