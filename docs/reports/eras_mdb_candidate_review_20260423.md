# ERAS MDB Candidate Human Review Pack

Generated: 2026-04-23

## Decision Status

- `candidate_ranking_only`
- This review pack does not declare an authoritative ERAS MDB.
- Human validation is required before any semantic modeling or operational assumption.
- Data policy: metadata only. No business row values or sample rows were read.

## Sources

- Ranking scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- Ranking report: `docs/reports/eras_mdb_authoritative_candidates_20260423.md`
- Discovery artifact: local-only `artifacts/exports/ERAS_MDB_DISCOVERY.csv`
- Table metadata artifact: local-only `artifacts/exports/ERAS_MDB_TABLES.csv`
- Schema warning artifact: local-only `artifacts/exports/ERAS_MDB_SCHEMA.md`

## Count Clarification

- Discovered/scored MDB candidates: `54`
- Unique analysis path strings: `52`
- Unique normalized analysis keys: `51`
- Cause: two duplicate analysis-copy groups were detected from repeated source candidates:
  - `enedADL_cel__3b7acb984e91.mdb` has two source paths.
  - `Modele_SIG__27dc1b587e20.mdb` / `modele_sig__27dc1b587e20.mdb` has three source paths, two case-preserving analysis path strings, and one normalized analysis key.
- Current review policy: keep `54` candidate rows for human validation, because source location is part of the evidence.

## Review Queue

| Rank | Score | Confidence | Source path | Tables | Rows | Warning | Review status | Human note |
|---:|---:|---|---|---:|---:|---|---|---|
| 1 | 66 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb` | 6 | 1680 | false | needs_followup | Confirm whether this is operational client state or configuration/reference data. |
| 2 | 63 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv4\ITRv4.mdb` | 6 | 799 | false | needs_followup | Check whether it is version-specific working data. |
| 3 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\c11_201.mdb` | 17 | 40248 | false | needs_followup | Check if it is shared catalog/system reference. |
| 4 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Comac.mdb` | 10 | 38419 | false | needs_followup | Check if it is shared catalog/system reference. |
| 5 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\ITRv3.mdb` | 6 | 836 | false | needs_followup | Compare with ITRv4 and ITRv2 lineage. |
| 6 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv2\ITRv2.mdb` | 6 | 807 | false | needs_followup | Compare with ITRv4 and ITRv3 lineage. |
| 7 | 55 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\SYSTEME.mdb` | 7 | 37 | false | needs_followup | Likely system configuration; confirm role before use. |
| 8 | 50 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Atlog\Atlog.mdb` | 6 | 1665 | false | needs_followup | Check whether this is domain-specific reference data. |
| 9 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\ENEDIS23\ENEDIS23.mdb` | 6 | 799 | false | needs_followup | Check relationship with client `enedis23`. |
| 10 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\enedis23\enedis23.mdb` | 6 | 795 | false | needs_followup | Check relationship with system `ENEDIS23`. |

## Top Candidate Explanation

Candidate: `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb`

Score: `66`

Applied scoring reasons:

- `+20 hash match`
- `+20 CLIENT path`
- `+8 modified within 1 year`
- `+8 >=6 tables extracted`
- `+10 >=1000 total rows`

Extracted metadata for this candidate:

| Table | Row count | Column count | Index count |
|---|---:|---:|---:|
| `cells` | 147 | 2 | 1 |
| `Famille` | 4 | 3 | 1 |
| `FiltreNiveau` | 923 | 5 | 1 |
| `fonts` | 31 | 3 | 0 |
| `levels` | 562 | 6 | 1 |
| `version` | 13 | 3 | 0 |

Interpretation:

- The candidate is strong on integrity, path signal, extracted schema, and row-count volume.
- The table names suggest configuration/reference-like content may be present.
- A human reviewer must confirm whether it represents authoritative business state, active client configuration, or only supporting reference data.

## Required Human Decisions

For each reviewed candidate, record one of:

- `accept_review`: candidate is suitable for the next semantic modeling pass.
- `reject_review`: candidate is not relevant for authoritative ERAS data selection.
- `needs_followup`: candidate needs additional safe evidence before classification.

No automated workflow should convert rank `1` into an authoritative decision without an explicit recorded human decision.
