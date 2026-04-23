from __future__ import annotations

from contextlib import closing
from pathlib import Path
from typing import Any

from .models import Relationship, SchemaAnalysis, TableColumn, TableSchema
from .query_safety import assert_read_only_query

try:
    import pyodbc  # type: ignore[import-untyped]
except Exception:  # pragma: no cover - import availability varies by machine
    pyodbc = None


def list_odbc_drivers() -> list[str]:
    if pyodbc is None:
        return []
    try:
        return [driver for driver in pyodbc.drivers()]
    except Exception:
        return []


def detect_access_driver() -> str | None:
    known_tokens = ("ACCESS DRIVER", "*.MDB", "*.ACCDB")
    for driver in list_odbc_drivers():
        upper_name = driver.upper()
        if all(token in upper_name for token in known_tokens):
            return driver
    return None


def _quote_identifier(identifier: str) -> str:
    return f"[{identifier.replace(']', ']]')}]"


def _fetch_row_count(cursor: Any, table_name: str) -> int | None:
    statement = f"SELECT COUNT(*) AS row_count FROM {_quote_identifier(table_name)}"
    assert_read_only_query(statement)
    try:
        row = cursor.execute(statement).fetchone()
        return int(row[0]) if row else 0
    except Exception:
        return None


def _connect_read_only(database_path: Path, driver_name: str) -> Any:
    connection_string = (
        f"DRIVER={{{driver_name}}};"
        f"DBQ={database_path};"
        "Readonly=1;"
    )
    return pyodbc.connect(connection_string, autocommit=True)


def analyze_database_schema(
    database_path: str | Path,
    driver_name: str | None = None,
) -> SchemaAnalysis:
    db_path = Path(database_path).expanduser().resolve()
    analysis = SchemaAnalysis(
        database_path=db_path,
        driver_name=driver_name,
        pyodbc_available=pyodbc is not None,
    )

    if pyodbc is None:
        analysis.warnings.append("pyodbc is not installed; schema analysis skipped.")
        return analysis

    driver = driver_name or detect_access_driver()
    analysis.driver_name = driver
    if not driver:
        analysis.warnings.append(
            "No Microsoft Access ODBC driver detected. Install Access Database Engine."
        )
        return analysis

    try:
        with closing(_connect_read_only(db_path, driver)) as connection:
            cursor = connection.cursor()
            tables_by_name: dict[str, TableSchema] = {}
            for table_row in cursor.tables():
                table_type = str(getattr(table_row, "table_type", "")).upper()
                table_name = str(getattr(table_row, "table_name", "")).strip()
                if table_type != "TABLE" or not table_name:
                    continue
                if table_name.startswith("MSYS"):
                    continue
                tables_by_name[table_name] = TableSchema(table_name=table_name)

            for table_name, table_schema in tables_by_name.items():
                for column_row in cursor.columns(table=table_name):
                    column_name = str(getattr(column_row, "column_name", "")).strip()
                    if not column_name:
                        continue
                    table_schema.columns.append(
                        TableColumn(
                            table_name=table_name,
                            column_name=column_name,
                            type_name=str(getattr(column_row, "type_name", "")),
                            nullable=bool(getattr(column_row, "nullable", True)),
                            ordinal_position=int(
                                getattr(column_row, "ordinal_position", 0) or 0
                            ),
                            size=(
                                int(getattr(column_row, "column_size", 0))
                                if getattr(column_row, "column_size", None) is not None
                                else None
                            ),
                            decimal_digits=(
                                int(getattr(column_row, "decimal_digits", 0))
                                if getattr(column_row, "decimal_digits", None) is not None
                                else None
                            ),
                        )
                    )

                table_schema.columns.sort(key=lambda col: col.ordinal_position)
                table_schema.row_count = _fetch_row_count(cursor, table_name)
                try:
                    table_schema.primary_keys.extend(
                        str(key_row.column_name)
                        for key_row in cursor.primaryKeys(table=table_name)
                    )
                except Exception:
                    pass
                try:
                    table_schema.indexes.extend(
                        str(idx_row.index_name)
                        for idx_row in cursor.statistics(table=table_name)
                        if getattr(idx_row, "index_name", None)
                    )
                    table_schema.indexes = sorted(set(table_schema.indexes))
                except Exception:
                    pass

            analysis.tables = sorted(
                tables_by_name.values(), key=lambda table: table.table_name.lower()
            )

            for table_schema in analysis.tables:
                try:
                    for rel_row in cursor.foreignKeys(table=table_schema.table_name):
                        analysis.relationships.append(
                            Relationship(
                                fk_table=str(getattr(rel_row, "fk_table_name", "")),
                                fk_column=str(getattr(rel_row, "fk_column_name", "")),
                                pk_table=str(getattr(rel_row, "pk_table_name", "")),
                                pk_column=str(getattr(rel_row, "pk_column_name", "")),
                                relation_name=str(getattr(rel_row, "fk_name", "")) or None,
                            )
                        )
                except Exception:
                    continue
    except Exception as exc:
        analysis.warnings.append(f"ODBC schema read failed: {exc}")

    return analysis


def run_read_only_query(
    database_path: str | Path,
    query: str,
    params: list[Any] | tuple[Any, ...] | None = None,
    driver_name: str | None = None,
) -> list[dict[str, Any]]:
    assert_read_only_query(query)

    db_path = Path(database_path).expanduser().resolve()
    if pyodbc is None:
        raise RuntimeError("pyodbc is not installed.")

    driver = driver_name or detect_access_driver()
    if not driver:
        raise RuntimeError("No Microsoft Access ODBC driver detected.")

    with closing(_connect_read_only(db_path, driver)) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query, params or [])
        columns = [str(column[0]) for column in result.description or []]
        rows: list[dict[str, Any]] = []
        for raw_row in result.fetchall():
            rows.append(
                {
                    column_name: raw_row[idx]
                    for idx, column_name in enumerate(columns)
                }
            )
        return rows
