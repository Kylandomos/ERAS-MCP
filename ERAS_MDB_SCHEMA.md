# ERAS MDB Schema Discovery Plan v0.1 (Read-Only)

Last updated: 2026-04-23

## Facts Proved

- MDB analysis is a core workstream and must be performed in read-only mode initially.
- Kickoff requires schema outputs and clear separation of certainty levels.
- An ERAS root directory is verified to exist (`Test-Path` + `Get-Item`):
  - `C:\AppSogelink\ERAS_Connect_2026`

## Hypotheses

- One or more ERAS `.mdb` databases exist and contain structurally meaningful core tables.

## Open Questions

- Which `.mdb` is authoritative when multiple candidates are found?
- Is encrypted/protected Access content present?
- Which relation clues are explicit (constraints/indexes) vs inferred?

## Decisions

- Enforce copy-first: source MDB fingerprint + analysis copy fingerprint before introspection.
- Separate structural facts (tables/columns/indexes) from semantic hypotheses (business meaning).
- Keep sample extraction minimal and privacy-aware.
- Use the verified ERAS directory as a first discovery root, without inferring schema/capabilities.

## Planned Read-Only Workflow

1. Discover candidate MDB paths and metadata.
2. Generate source fingerprint.
3. Copy to controlled analysis workspace.
4. Generate copy fingerprint and verify match.
5. Extract schema objects (tables, fields, types, indexes).
6. Compute row-count overview and relation hints.
7. Produce structured and narrative reports.

## Initial Verified Directory Root

- `C:\AppSogelink\ERAS_Connect_2026`

## Planned Outputs

- `docs/schemas/eras_mdb_tables_<date>.csv`
- `docs/schemas/eras_mdb_relationships_<date>.md`
- `docs/schemas/eras_mdb_field_dictionary_<date>.md`
- `docs/reports/eras_mdb_schema_summary_<date>.md`
- `artifacts/exports/eras_mdb_schema_<timestamp>.json`

## Acceptance Criteria (v0.1 Plan)

- Workflow explicitly prevents writes to production MDB.
- Output set includes both machine-readable export and human-readable summary.
- Structural facts, hypotheses, and open questions are separated in reporting.

## Evidence References

- `EVIDENCE_INDEX.md#ev-003`
- `EVIDENCE_INDEX.md#ev-004`

## Worker C Note (2026-04-23)

- Added read-only MDB discovery/analyzer tooling at `scripts/eras/eras_mdb_discovery.py`.
- Latest generated exports are in `artifacts/exports/` (including schema, dictionary, relationships, sample queries, and risks).
- Local environment now has `pyodbc 5.3.0` and a 64-bit `Microsoft Access Driver (*.mdb, *.accdb)` available.
- Extraction is now partial (183 table rows documented across 20 databases); 32 database analyses still emit UTF-16 decode warnings (`illegal UTF-16 surrogate`), tracked as an active risk.
