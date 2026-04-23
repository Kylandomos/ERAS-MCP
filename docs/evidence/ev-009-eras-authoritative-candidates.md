# EV-009 - ERAS Authoritative Candidate Ranking

Status: validated-candidate-ranking

## Claim Supported

ERAS MDB candidates can be ranked deterministically from metadata-only evidence, without declaring an authoritative database.

## Evidence

- Ranking report: `docs/reports/eras_mdb_authoritative_candidates_20260423.md`
- Scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- Ranking implementation: `src/services/eras_mdb_ranking.py`
- Facade/CLI: `src/mcp_server/facade.py`, `src/mcp_server/cli.py`

## Facts Proved

- Candidates ranked: `54`
- Top candidate by current score: `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb`
- Top score: `66`
- Candidates with schema warnings: `32`
- Candidates with no extracted tables: `32`
- Unique analysis path strings: `52`
- Unique normalized analysis keys: `51`

## Limits

- Ranking is not an authoritative decision.
- No business row values or data samples were read.
- ODBC warning-heavy candidates remain P1 follow-up work.
- Human review packaging is tracked separately in `docs/evidence/ev-010-eras-mdb-human-review-pack.md`.
