from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

# Keep script runnable without package installation.
REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
VERIFIED_DEFAULT_SCAN_ROOT = Path(r"C:\AppSogelink\ERAS_Connect_2026")
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from adapters.eras_mdb.discovery import (  # noqa: E402
    collect_database_candidates,
    copy_candidates_for_analysis,
)
from adapters.eras_mdb.odbc_access import analyze_database_schema  # noqa: E402
from adapters.eras_mdb.reporting import (  # noqa: E402
    write_discovery_manifest,
    write_field_dictionary_markdown,
    write_relationships_markdown,
    write_risks_markdown,
    write_sample_queries_sql,
    write_scan_context_markdown,
    write_schema_markdown,
    write_tables_csv,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Discover ERAS MDB/ACCDB files, copy them to a read-only analysis area, "
            "and generate schema reports."
        )
    )
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help=(
            "Discovery root path. Repeat for multiple roots. "
            r"Example: --root C:\AppSogelink\ERAS_Connect_2026. "
            r"If omitted, defaults to verified root C:\AppSogelink\ERAS_Connect_2026."
        ),
    )
    parser.add_argument(
        "--work-dir",
        default=str(REPO_ROOT / "artifacts" / "work" / "eras_mdb"),
        help="Directory where hashed analysis copies are stored.",
    )
    parser.add_argument(
        "--export-dir",
        default=str(REPO_ROOT / "artifacts" / "exports"),
        help="Directory for generated discovery/schema reports.",
    )
    parser.add_argument(
        "--docs-dir",
        default=str(REPO_ROOT / "docs" / "schemas"),
        help="Optional docs directory for copied markdown/sql report snapshots.",
    )
    parser.add_argument(
        "--copy-reports-to-docs",
        action="store_true",
        help="Copy generated markdown/sql reports into docs/schemas for review.",
    )
    parser.add_argument(
        "--driver",
        default=None,
        help="Optional explicit ODBC driver name override.",
    )
    parser.add_argument(
        "--skip-schema-analysis",
        action="store_true",
        help="Skip ODBC schema extraction and generate discovery-only outputs.",
    )
    parser.add_argument(
        "--sample-limit",
        type=int,
        default=25,
        help="TOP N used in generated sample SELECT statements.",
    )
    return parser.parse_args()


def _resolve_roots(raw_roots: list[str]) -> tuple[list[Path], list[tuple[Path, str]]]:
    if raw_roots:
        roots = [Path(root).expanduser().resolve() for root in raw_roots]
        entries = [(root, "explicit_root_input") for root in roots]
        return roots, entries
    roots = [VERIFIED_DEFAULT_SCAN_ROOT]
    entries = [(VERIFIED_DEFAULT_SCAN_ROOT, "verified_local_directory")]
    return roots, entries


def _copy_report_snapshots(export_dir: Path, docs_dir: Path) -> list[Path]:
    docs_dir.mkdir(parents=True, exist_ok=True)
    copied: list[Path] = []
    for name in [
        "ERAS_MDB_SCHEMA.md",
        "ERAS_MDB_FIELD_DICTIONARY.md",
        "ERAS_MDB_RELATIONSHIPS.md",
        "ERAS_MDB_SAMPLE_QUERIES.sql",
        "ERAS_MDB_RISKS.md",
    ]:
        source = export_dir / name
        if not source.exists():
            continue
        destination = docs_dir / name
        shutil.copy2(source, destination)
        copied.append(destination)
    return copied


def main() -> int:
    args = _parse_args()
    roots, root_entries = _resolve_roots(args.root)

    candidates = collect_database_candidates(roots)
    copies = copy_candidates_for_analysis(candidates, args.work_dir)

    analyses = []
    if not args.skip_schema_analysis:
        for copied in copies:
            analyses.append(
                analyze_database_schema(copied.analysis_path, driver_name=args.driver)
            )

    export_dir = Path(args.export_dir).expanduser().resolve()
    export_dir.mkdir(parents=True, exist_ok=True)

    outputs = [
        write_scan_context_markdown(export_dir, root_entries),
        write_discovery_manifest(export_dir, candidates, copies),
        write_tables_csv(export_dir, analyses),
        write_schema_markdown(export_dir, analyses),
        write_field_dictionary_markdown(export_dir, analyses),
        write_relationships_markdown(export_dir, analyses),
        write_sample_queries_sql(export_dir, analyses, sample_limit=max(args.sample_limit, 1)),
        write_risks_markdown(export_dir, analyses),
    ]

    copied_docs: list[Path] = []
    if args.copy_reports_to_docs:
        copied_docs = _copy_report_snapshots(
            export_dir=export_dir,
            docs_dir=Path(args.docs_dir).expanduser().resolve(),
        )

    summary = {
        "roots": [str(root) for root in roots],
        "candidate_count": len(candidates),
        "analysis_copy_count": len(copies),
        "schema_analysis_count": len(analyses),
        "outputs": [str(path) for path in outputs],
        "docs_copies": [str(path) for path in copied_docs],
        "read_only_policy": (
            "source files never modified; analysis is performed only on copied files"
        ),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
