# EV-010 - ERAS MDB Human Review Pack

Status: validated-review-pack

Date: 2026-04-23

## Claim Supported

The ERAS MDB candidate ranking has been converted into a human review pack and ODBC warning triage without declaring an authoritative database and without reading business row values.

## Evidence Sources

- Review pack: `docs/reports/eras_mdb_candidate_review_20260423.md`
- Warning triage: `docs/reports/eras_mdb_odbc_warning_triage_20260423.md`
- Ranking report: `docs/reports/eras_mdb_authoritative_candidates_20260423.md`
- Scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- API/CLI implementation: `src/mcp_server/facade.py`, `src/mcp_server/cli.py`, `src/mcp_server/server.py`
- Tests: `tests/unit/test_mcp_facade_readonly.py`

## Facts Recorded

- Candidate rows retained for review: `54`
- Unique analysis path strings: `52`
- Unique normalized analysis keys: `51`
- ODBC warning candidates triaged: `32`
- Top candidate remains `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb`.
- New metadata-only explanation tool: `eras-explain-database`.

## Validation

- `eras_explain_database()` returns the standard read-only envelope.
- CLI dispatch for `eras-explain-database --path` is covered by unit tests.
- Explanation output includes table metadata only: table name, row count, column count, primary key metadata, and index count.
- Explanation output does not include business row values or sample rows.

## Limits

- Human review statuses are placeholders until a reviewer records `accept_review`, `reject_review`, or `needs_followup`.
- ODBC warning candidates remain incomplete and may require alternate extraction only after human prioritization.
- Rank `1` is still not an authoritative decision.
