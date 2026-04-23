# ERAS MDB Authoritative Candidate Ranking

Generated: 2026-04-23

## Decision Status

- `candidate_ranking_only`
- This report does **not** declare an authoritative ERAS MDB.
- Ranking uses metadata only: discovery paths, file metadata, copy hash status, extracted table counts, row counts, and schema warning markers.
- No business row values or samples were read for this ranking.

## Scoring Rules

| Signal | Weight |
|---|---:|
| Hash match | +20 |
| ODBC schema warning | -30 |
| Path segment `CLIENT` | +20 |
| Path segment `SYSTEME` | +12 |
| Path segment `SEED` | -10 |
| Path/name contains `temp`, `sample`, or `sheet` | -20 |
| Path/name contains `modele` or `dgn_sht` | -10 |
| Modified within 30 days | +15 |
| Modified within one year | +8 |
| At least 10 extracted tables | +15 |
| At least 6 extracted tables | +8 |
| No extracted tables | -20 |
| Total row count at least 1000 | +10 |

## Summary

- Candidates ranked: `54`
- Candidates returned in scorecard: `54`
- Candidates with ODBC schema warning: `32`
- Candidates with no extracted tables: `32`
- Top score: `66`
- Top candidate: `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb`

## Candidate Accounting

- The scorecard keeps `54` discovered source candidate rows.
- Current metadata exposes `52` unique analysis path strings and `51` normalized analysis keys.
- This difference is expected because some repeated source paths share the same hash-derived analysis copy.
- Human review uses the `54` source candidates because source location is part of the decision evidence.

## Top Candidates

| Rank | Score | Confidence | Source path | Tables | Rows | Warning |
|---:|---:|---|---|---:|---:|---|
| 1 | 66 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb` | 6 | 1680 | false |
| 2 | 63 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv4\ITRv4.mdb` | 6 | 799 | false |
| 3 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\c11_201.mdb` | 17 | 40248 | false |
| 4 | 57 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Comac.mdb` | 10 | 38419 | false |
| 5 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\ITRv3.mdb` | 6 | 836 | false |
| 6 | 56 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv2\ITRv2.mdb` | 6 | 807 | false |
| 7 | 55 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\SYSTEME.mdb` | 7 | 37 | false |
| 8 | 50 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Atlog\Atlog.mdb` | 6 | 1665 | false |
| 9 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\ENEDIS23\ENEDIS23.mdb` | 6 | 799 | false |
| 10 | 48 | high | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\enedis23\enedis23.mdb` | 6 | 795 | false |

## Interpretation

- `CLIENT\client.mdb` ranks first because it combines a hash-matched analysis copy, a `CLIENT` path, recent modification within one year, extracted schema, and row counts above 1000.
- Large underscore-suffixed files such as `GLOBLUTI.mdb`, `ITRv3_.mdb`, and `ITRv4_.mdb` are not promoted because current ODBC extraction returns warnings and no extracted tables.
- `SEED` and model/template-like databases are intentionally penalized because they are less likely to be active operational stores.

## Curated Data

- Full scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
- Schema evidence: `docs/schemas/ERAS_MDB_SCHEMA.md`
- Human review pack: `docs/reports/eras_mdb_candidate_review_20260423.md`
- ODBC warning triage: `docs/reports/eras_mdb_odbc_warning_triage_20260423.md`
- Discovery source: local-only `artifacts/exports/ERAS_MDB_DISCOVERY.csv`
- Tables source: local-only `artifacts/exports/ERAS_MDB_TABLES.csv`

## Next Review Questions

- Confirm whether `CLIENT\client.mdb` is operationally meaningful or only a client configuration/reference DB.
- Confirm whether higher-score `SYSTEME` databases represent shared catalogs rather than project/business state.
- Decide whether warning-heavy underscore files require alternate Access/ODBC handling before semantic modeling.
