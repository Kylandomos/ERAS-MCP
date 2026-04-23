# MVP Read-Only Baseline Report

Generated: 2026-04-23

## Facts Proved

- The project has a read-only MCP facade under `src/mcp_server/`.
- The facade exposes artifact-backed tools only; it does not execute Bentley/OpenCities commands.
- Direct runtime dependencies are pinned in `requirements.txt` and `pyproject.toml`:
  - `mcp==1.27.0`
  - `pyodbc==5.3.0`
- `create_mcp_stdio_server()` initializes successfully when dependencies are installed.
- Unit tests pass: `13` tests OK.

## ERAS MDB Baseline

- Discovery root: `C:\AppSogelink\ERAS_Connect_2026`
- MDB/ACCDB candidates discovered: `54`
- Analysis copies created and hash matched: `54/54`
- Table rows extracted: `183`
- Databases with extracted tables: `20`
- ODBC schema warnings: `32`

## OpenCities / PowerMap Baseline

- Verified root: `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`
- Executables found by read-only inventory: `2`
- Workspace candidates found by bounded smoke scan: `2`
- Python Manager found: `false`
- Remaining PowerMap gap count: `1`

## Curated Evidence Sources

- `docs/schemas/ERAS_MDB_SCHEMA.md`
- `docs/schemas/ERAS_MDB_FIELD_DICTIONARY.md`
- `docs/schemas/ERAS_MDB_RELATIONSHIPS.md`
- `docs/schemas/ERAS_MDB_RISKS.md`
- `docs/reports/mvp_gap_report_20260423.md`

## Excluded From Git

- Raw inventory JSON and scan logs under `artifacts/inventories/**` and `artifacts/logs/**`.
- Analysis database copies under `artifacts/work/**`.
- Generated raw exports under `artifacts/exports/**`.
- Raw Access files (`*.mdb`, `*.accdb`, lock files).

