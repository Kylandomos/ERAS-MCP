from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .models import AnalysisCopy, DatabaseCandidate, SchemaAnalysis


def _timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_discovery_manifest(
    export_dir: str | Path,
    candidates: Iterable[DatabaseCandidate],
    copies: Iterable[AnalysisCopy],
) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_DISCOVERY.csv"
    copy_by_source = {item.source_path: item for item in copies}

    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "source_path",
                "extension",
                "file_size_bytes",
                "modified_utc",
                "source_sha256",
                "analysis_path",
                "analysis_sha256",
                "hash_match",
            ]
        )
        for candidate in candidates:
            copied = copy_by_source.get(candidate.source_path)
            writer.writerow(
                [
                    str(candidate.source_path),
                    candidate.extension,
                    candidate.file_size_bytes,
                    candidate.modified_utc,
                    candidate.sha256,
                    str(copied.analysis_path) if copied else "",
                    copied.analysis_sha256 if copied else "",
                    (
                        copied.analysis_sha256 == copied.source_sha256
                        if copied
                        else False
                    ),
                ]
            )
    return target


def write_scan_context_markdown(
    export_dir: str | Path,
    root_entries: Iterable[tuple[Path, str]],
) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_SCAN_CONTEXT.md"
    lines: list[str] = [
        "# ERAS MDB Scan Context",
        "",
        f"_Generated (UTC): {_timestamp_utc()}_",
        "",
        "## Discovery Roots",
        "",
        "| Root Path | Provenance |",
        "|---|---|",
    ]
    for root, provenance in root_entries:
        lines.append(f"| {root} | {provenance} |")
    lines.append("")
    lines.append("- Source MDB/ACCDB files are never modified.")
    lines.append("- Analysis runs only against hashed copies in the work area.")
    lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_tables_csv(export_dir: str | Path, analyses: Iterable[SchemaAnalysis]) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_TABLES.csv"
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "database_path",
                "table_name",
                "row_count",
                "column_count",
                "primary_key_columns",
                "index_count",
            ]
        )
        for analysis in analyses:
            for table in analysis.tables:
                writer.writerow(
                    [
                        str(analysis.database_path),
                        table.table_name,
                        table.row_count if table.row_count is not None else "",
                        len(table.columns),
                        ",".join(table.primary_keys),
                        len(table.indexes),
                    ]
                )
    return target


def write_schema_markdown(export_dir: str | Path, analyses: Iterable[SchemaAnalysis]) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_SCHEMA.md"
    lines: list[str] = [
        "# ERAS MDB Schema",
        "",
        f"_Generated (UTC): {_timestamp_utc()}_",
        "",
    ]
    for analysis in analyses:
        lines.append(f"## Database: `{analysis.database_path}`")
        lines.append("")
        lines.append(f"- ODBC driver: `{analysis.driver_name or 'not detected'}`")
        lines.append(f"- pyodbc available: `{analysis.pyodbc_available}`")
        lines.append(f"- Tables discovered: `{len(analysis.tables)}`")
        lines.append("")
        if analysis.warnings:
            lines.append("### Warnings")
            lines.append("")
            for warning in analysis.warnings:
                lines.append(f"- {warning}")
            lines.append("")
        for table in analysis.tables:
            lines.append(f"### Table `{table.table_name}`")
            lines.append("")
            lines.append(
                f"- Row count: `{table.row_count if table.row_count is not None else 'unknown'}`"
            )
            lines.append(f"- Columns: `{len(table.columns)}`")
            lines.append(
                f"- Primary keys: `{', '.join(table.primary_keys) if table.primary_keys else 'none detected'}`"
            )
            lines.append("")
            lines.append("| Column | Type | Nullable |")
            lines.append("|---|---|---|")
            for column in table.columns:
                lines.append(
                    f"| {column.column_name} | {column.type_name} | {column.nullable} |"
                )
            lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_field_dictionary_markdown(
    export_dir: str | Path, analyses: Iterable[SchemaAnalysis]
) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_FIELD_DICTIONARY.md"
    lines: list[str] = [
        "# ERAS MDB Field Dictionary",
        "",
        f"_Generated (UTC): {_timestamp_utc()}_",
        "",
        "This dictionary is technical and read-only. Business meaning must be confirmed with users.",
        "",
    ]
    for analysis in analyses:
        lines.append(f"## `{analysis.database_path}`")
        lines.append("")
        lines.append("| Table | Field | Type | Notes |")
        lines.append("|---|---|---|---|")
        for table in analysis.tables:
            for column in table.columns:
                notes = "Primary key candidate." if column.column_name in table.primary_keys else ""
                lines.append(
                    f"| {table.table_name} | {column.column_name} | {column.type_name} | {notes} |"
                )
        lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_relationships_markdown(
    export_dir: str | Path, analyses: Iterable[SchemaAnalysis]
) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_RELATIONSHIPS.md"
    lines: list[str] = [
        "# ERAS MDB Relationships",
        "",
        f"_Generated (UTC): {_timestamp_utc()}_",
        "",
    ]
    for analysis in analyses:
        lines.append(f"## `{analysis.database_path}`")
        lines.append("")
        if not analysis.relationships:
            lines.append("- No explicit foreign keys were returned by ODBC.")
            lines.append("")
            continue
        lines.append("| FK Table | FK Column | PK Table | PK Column | Relation Name |")
        lines.append("|---|---|---|---|---|")
        for relationship in analysis.relationships:
            lines.append(
                "| "
                + " | ".join(
                    [
                        relationship.fk_table,
                        relationship.fk_column,
                        relationship.pk_table,
                        relationship.pk_column,
                        relationship.relation_name or "",
                    ]
                )
                + " |"
            )
        lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_sample_queries_sql(
    export_dir: str | Path, analyses: Iterable[SchemaAnalysis], sample_limit: int = 25
) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_SAMPLE_QUERIES.sql"
    lines: list[str] = [
        "-- ERAS MDB sample read-only queries",
        f"-- Generated (UTC): {_timestamp_utc()}",
        "",
    ]
    for analysis in analyses:
        lines.append(f"-- Database: {analysis.database_path}")
        for table in analysis.tables:
            lines.append(f"SELECT TOP {sample_limit} * FROM [{table.table_name}];")
            lines.append(f"SELECT COUNT(*) AS row_count FROM [{table.table_name}];")
            lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def write_risks_markdown(export_dir: str | Path, analyses: Iterable[SchemaAnalysis]) -> Path:
    export_root = _ensure_dir(Path(export_dir).expanduser().resolve())
    target = export_root / "ERAS_MDB_RISKS.md"
    lines: list[str] = [
        "# ERAS MDB Risks",
        "",
        f"_Generated (UTC): {_timestamp_utc()}_",
        "",
        "## Current Risks",
        "",
    ]
    risk_items: list[str] = []
    for analysis in analyses:
        if not analysis.pyodbc_available:
            risk_items.append(
                "pyodbc dependency is unavailable, so schema extraction is incomplete."
            )
        if analysis.pyodbc_available and not analysis.driver_name:
            risk_items.append(
                "No Access ODBC driver detected, preventing direct MDB/ACCDB introspection."
            )
        risk_items.extend(analysis.warnings)

    if not risk_items:
        risk_items.append(
            "No immediate technical blockers detected during read-only extraction."
        )

    seen: set[str] = set()
    for item in risk_items:
        if item in seen:
            continue
        seen.add(item)
        lines.append(f"- {item}")

    lines.append("")
    lines.append("## Safety Guarantees")
    lines.append("")
    lines.append("- Source databases are copied before analysis.")
    lines.append("- SQL helpers are restricted to read-only SELECT/WITH queries.")
    lines.append("- No compact/repair/migration operation is performed.")
    lines.append("")
    target.write_text("\n".join(lines), encoding="utf-8")
    return target
