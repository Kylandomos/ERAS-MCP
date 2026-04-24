# ERAS MDB Human Decision Status

Generated: 2026-04-24

## Decision Status

- `human_review_pending`
- No authoritative MDB declared by automation.
- The decision file is initialized for human review only.
- Data policy: metadata only. No business row values or sample rows were read.

## Sources

- Human decisions: `docs/reviews/ERAS_MDB_HUMAN_DECISIONS_20260424.csv`
- Scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- Review pack: `docs/reports/eras_mdb_candidate_review_20260423.md`
- Evidence: `docs/evidence/ev-011-eras-mdb-human-decisions.md`
- Decision intake evidence: `docs/evidence/ev-012-eras-mdb-decision-intake.md`

## Summary

- Scorecard candidates: `54`
- Decision rows: `54`
- `needs_followup`: `54`
- `accept_review`: `0`
- `reject_review`: `0`
- Ready accepted reviews: `0`
- Invalid statuses: `0`
- Duplicate source paths: `0`
- Unknown source paths: `0`
- Missing decision rows: `0`

## Top Candidates Still Pending

| Rank | Score | Confidence | Source path | Tables | Rows | Current status |
|---:|---:|---|---|---:|---:|---|
| 1 | 66 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb` | 6 | 1680 | needs_followup |
| 2 | 63 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv4\ITRv4.mdb` | 6 | 799 | needs_followup |
| 3 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\c11_201.mdb` | 17 | 40248 | needs_followup |
| 4 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Comac.mdb` | 10 | 38419 | needs_followup |
| 5 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\ITRv3.mdb` | 6 | 836 | needs_followup |
| 6 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv2\ITRv2.mdb` | 6 | 807 | needs_followup |
| 7 | 55 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\SYSTEME.mdb` | 7 | 37 | needs_followup |
| 8 | 50 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Atlog\Atlog.mdb` | 6 | 1665 | needs_followup |
| 9 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\ENEDIS23\ENEDIS23.mdb` | 6 | 799 | needs_followup |
| 10 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\enedis23\enedis23.mdb` | 6 | 795 | needs_followup |

## Accepted Reviews

None.

## Rejected Reviews

None.

## Required Human Fields

An `accept_review` decision is not considered ready unless it includes:

- `reviewer`
- `reviewed_at_utc`
- `decision_basis`

The validation tool reports missing fields as warnings and keeps the global status out of `human_review_ready`.

## Regeneration

- Dry-run preview: `eras-mcp-readonly eras-set-review-decision --source-path "<source_path>" --status accept_review --reviewer "<reviewer>" --decision-basis "<basis>" --dry-run`
- Write mode updates only the decision CSV and this status report.
- Even when `human_review_ready` is reached, automation does not declare an authoritative MDB.
