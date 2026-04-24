# EV-011 - ERAS MDB Human Decisions

Status: validated-decision-artifact-initialized

Date: 2026-04-24

## Claim Supported

The ERAS MDB candidate ranking now has a versioned human decision artifact and a read-only validation tool, without declaring an authoritative MDB.

## Evidence Sources

- Decision artifact: `docs/reviews/ERAS_MDB_HUMAN_DECISIONS_20260424.csv`
- Decision status report: `docs/reports/eras_mdb_human_decision_status_20260424.md`
- Scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- API/CLI implementation: `src/mcp_server/facade.py`, `src/mcp_server/cli.py`, `src/mcp_server/server.py`
- Validation service: `src/services/eras_mdb_review.py`
- Tests: `tests/unit/test_eras_mdb_review.py`, `tests/unit/test_mcp_facade_readonly.py`

## Facts Recorded

- Decision rows initialized: `54`
- Scorecard candidates matched: `54`
- Default review status: `needs_followup`
- Accepted reviews: `0`
- Rejected reviews: `0`
- Invalid statuses: `0`
- Global status: `human_review_pending`

## Validation

- `eras_review_status()` returns the standard read-only envelope.
- `eras-review-status` validates status values, duplicate source paths, unknown paths, missing decisions, and incomplete `accept_review` rows.
- A ready accepted review requires `reviewer`, `reviewed_at_utc`, and `decision_basis`.

## Limits

- No authoritative MDB is declared by automation.
- All current rows require human follow-up.
- No business row values or data samples were read.
- Decision intake behavior is tracked separately in `docs/evidence/ev-012-eras-mdb-decision-intake.md`.
