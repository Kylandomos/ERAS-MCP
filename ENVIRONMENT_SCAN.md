# Environment Scan Plan v0.1

Last updated: 2026-04-23

## Facts Proved

- Kickoff scope requires a reproducible Windows environment scan before advanced development.
- Scan outputs must be evidence-backed and safe (non-destructive).
- Two initial roots are verified to exist as FileSystem directories (`Test-Path` + `Get-Item`):
  - `C:\AppSogelink\ERAS_Connect_2026`
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Hypotheses

- Relevant artifacts can be discovered through file, process, service, and registry inventory.

## Open Questions

- Which roots should be scanned first to reduce runtime while preserving coverage?
- Which scan operations need admin rights versus standard user rights?

## Decisions

- Define scan outputs and evidence contracts before implementing scripts.
- Keep scans read-only and timestamped, with redaction in report derivatives.
- Use these verified directories as initial scan seed roots.

## Required Scan Domains

1. Host baseline: OS version, hostname, architecture, timezone.
2. Execution context: current user, group/privilege hints, environment variables.
3. Software footprint: installed Bentley/OpenCities, ERAS, Access/ODBC related components.
4. Runtime footprint: processes/services/tasks related to Bentley and ERAS.
5. Configuration footprint: registry keys, config paths, workspace/workset clues.
6. Artifact discovery: target extensions (`.mdb`, `.accdb`, `.dgn`, `.cfg`, `.ini`, `.py`, `.ps1`, logs, exports).

## Initial Known Roots (Verified Directories)

- `C:\AppSogelink\ERAS_Connect_2026`
- `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Planned Outputs

- `artifacts/inventories/windows_inventory_<timestamp>.json`
- `artifacts/snapshots/environment_snapshot_<timestamp>.json`
- `docs/reports/environment_scan_summary_<date>.md`

## Acceptance Criteria (v0.1 Plan)

- All six scan domains have explicit expected output fields.
- Output paths and naming conventions align with `EVIDENCE_INDEX.md`.
- Safety constraints and exclusions are documented before script implementation.

## Evidence References

- `EVIDENCE_INDEX.md#ev-001`
- `EVIDENCE_INDEX.md#ev-007`
