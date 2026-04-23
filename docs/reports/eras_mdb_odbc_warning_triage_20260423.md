# ERAS MDB ODBC UTF-16 Warning Triage

Generated: 2026-04-23

## Scope

- This report triages the `32` MDB candidates that produced ODBC UTF-16 schema warnings.
- It uses only metadata from curated ranking outputs and local read-only exports.
- It does not read business row values or sample rows.
- The warning class remains P1 because these candidates may be under-scored until extraction is improved.

## Summary

- Warning candidates: `32`
- Warning candidates with extracted tables: `0`
- Warning candidates with `CLIENT` path signal: `7`
- Warning candidates with `SYSTEME` path signal: `9`
- Warning candidates with `SEED` path signal: `16`
- Highest warning candidate score: `5`
- Highest warning candidates: `GLOBLUTI.mdb`, `ITRv3_.mdb`, `ITRv4_.mdb`, `ITRv2_.mdb`

## Triage Buckets

| Bucket | Rule | Priority | Suggested action |
|---|---|---|---|
| Client warning candidates | `CLIENT` source path and ODBC warning | P1-A | Validate whether underscore/high-volume files are active working DBs; retry schema extraction only after review. |
| System warning candidates | `SYSTEME` source path and ODBC warning | P1-B | Check whether they are catalogs/templates before investing in alternate extraction. |
| Seed/model/sheet warning candidates | `SEED`, `modele`, `dgn_sht`, or `sheet` signals | P1-C | Keep as lower-priority warning cases unless a human reviewer marks one as operationally relevant. |

## Warning Candidates

| Rank | Score | Bucket | Source path | Tables | Rows | Review status |
|---:|---:|---|---|---:|---:|---|
| 22 | 5 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\GLOBLUTI.mdb` | 0 | 0 | needs_followup |
| 23 | 5 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\ITRv3_.mdb` | 0 | 0 | needs_followup |
| 24 | 5 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv4\ITRv4_.mdb` | 0 | 0 | needs_followup |
| 25 | 5 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv2\ITRv2_.mdb` | 0 | 0 | needs_followup |
| 27 | -2 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\enedADL_cel.mdb` | 0 | 0 | needs_followup |
| 28 | -2 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\ITRv3\SAUVE\enedADL_cel.mdb` | 0 | 0 | needs_followup |
| 29 | -3 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\ENEDIS23\ENEDIS23_.mdb` | 0 | 0 | needs_followup |
| 30 | -3 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\ENEDIS22\ENEDIS22_.mdb` | 0 | 0 | needs_followup |
| 31 | -3 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\enedis\enedis_.mdb` | 0 | 0 | needs_followup |
| 32 | -3 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\globlsys.mdb` | 0 | 0 | needs_followup |
| 33 | -10 | P1-A | `C:\AppSogelink\ERAS_Connect_2026\CLIENT\enedis23\enedis23_.mdb` | 0 | 0 | needs_followup |
| 34 | -18 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\Atlog\Atlog_.mdb` | 0 | 0 | needs_followup |
| 35 | -18 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\FTTH\FTTH_.mdb` | 0 | 0 | needs_followup |
| 36 | -18 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\EauAss\eauAss_.mdb` | 0 | 0 | needs_followup |
| 37 | -18 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\SOURCE\SOURCE_.mdb` | 0 | 0 | needs_followup |
| 38 | -18 | P1-B | `C:\AppSogelink\ERAS_Connect_2026\SYSTEME\EauAss\ext-champion- eu-ep-250_dwg.mdb` | 0 | 0 | needs_followup |
| 39 | -40 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ENEDIS23_DGN.mdb` | 0 | 0 | needs_followup |
| 40 | -40 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\enedis22_DGN.mdb` | 0 | 0 | needs_followup |
| 41 | -40 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\enedis_DGN.mdb` | 0 | 0 | needs_followup |
| 42 | -40 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\Affaires.mdb` | 0 | 0 | needs_followup |
| 43 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\modele.mdb` | 0 | 0 | needs_followup |
| 44 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\modelevide.mdb` | 0 | 0 | needs_followup |
| 45 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\modeleAff.mdb` | 0 | 0 | needs_followup |
| 46 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ERDFAER2012_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 47 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ERDFAER_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 48 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ENEDIS23_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 49 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\enedis22_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 50 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\enedis_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 51 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\FTTH_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 52 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ERDFSOUT2012_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 53 | -50 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\ERDFSOUT_DGN_sht.mdb` | 0 | 0 | needs_followup |
| 54 | -60 | P1-C | `C:\AppSogelink\ERAS_Connect_2026\SEED\Sheet.mdb` | 0 | 0 | needs_followup |

## Interpretation

- The warning penalty and zero-table penalty keep all warning cases below the extracted-schema candidates.
- The top warning cases are still worth human review because they have `CLIENT` path signals and recent modification timestamps.
- `SEED`, `modele`, `dgn_sht`, and `sheet` candidates are lower priority unless human evidence says they are operational.

## Next Safe Step

Use `eras-mcp-readonly eras-explain-database --path "<source_path>"` for a metadata-only explanation of any candidate before deciding whether alternate MDB extraction work is worth scheduling.
