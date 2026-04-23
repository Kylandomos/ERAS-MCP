# EV-003 - ERAS MDB Read-Only Schema

Status: validated-partial

## Claim Supported

ERAS MDB discovery and schema extraction are performed copy-first and read-only, with partial schema extraction available.

## Evidence

- Curated schema report: `docs/schemas/ERAS_MDB_SCHEMA.md`
- Curated field dictionary: `docs/schemas/ERAS_MDB_FIELD_DICTIONARY.md`
- Curated risks: `docs/schemas/ERAS_MDB_RISKS.md`
- Summary report: `docs/reports/mvp_readonly_baseline_20260423.md`

## Facts Proved

- MDB/ACCDB candidates discovered: `54`
- Analysis copies hash matched: `54/54`
- Extracted table rows: `183`
- Databases with extracted tables: `20`
- ODBC UTF-16 warning count: `32`

## Limits

- The authoritative ERAS database is not identified yet.
- The 32 warning cases remain P1 follow-up work.

