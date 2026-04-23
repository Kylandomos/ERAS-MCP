from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DatabaseCandidate:
    source_path: Path
    extension: str
    file_size_bytes: int
    modified_utc: str
    sha256: str


@dataclass(frozen=True)
class AnalysisCopy:
    source_path: Path
    analysis_path: Path
    source_sha256: str
    analysis_sha256: str


@dataclass(frozen=True)
class QueryValidationResult:
    is_valid: bool
    reason: str


@dataclass
class TableColumn:
    table_name: str
    column_name: str
    type_name: str
    nullable: bool
    ordinal_position: int
    size: int | None = None
    decimal_digits: int | None = None


@dataclass
class TableSchema:
    table_name: str
    columns: list[TableColumn] = field(default_factory=list)
    row_count: int | None = None
    primary_keys: list[str] = field(default_factory=list)
    indexes: list[str] = field(default_factory=list)


@dataclass
class Relationship:
    fk_table: str
    fk_column: str
    pk_table: str
    pk_column: str
    relation_name: str | None = None


@dataclass
class SchemaAnalysis:
    database_path: Path
    driver_name: str | None
    pyodbc_available: bool
    tables: list[TableSchema] = field(default_factory=list)
    relationships: list[Relationship] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def as_summary(self) -> dict[str, Any]:
        return {
            "database_path": str(self.database_path),
            "driver_name": self.driver_name,
            "pyodbc_available": self.pyodbc_available,
            "table_count": len(self.tables),
            "relationship_count": len(self.relationships),
            "warnings": self.warnings,
        }
