# Windows Inventory Specification v0.1

Last updated: 2026-04-23

## Facts Proved

- The project target is a Windows local environment.
- Inventory is a prerequisite for safe MCP capability design.
- Two roots are verified to exist as FileSystem directories (`Test-Path` + `Get-Item`):
  - `C:\AppSogelink\ERAS_Connect_2026`
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Hypotheses

- Existing workstation state includes custom scripts/configurations impacting automation strategy.

## Open Questions

- Which inventory fields are mandatory for MVP acceptance versus optional?
- Are some data classes restricted from export outside local machine?

## Decisions

- Inventory specification is schema-first to keep future scan scripts deterministic.
- Sensitive values should be tagged for redaction in report views.
- Verified roots are tracked as seed paths; no version/capability inference is allowed from path names.

## Proposed Inventory Schema (High Level)

| Section | Example Fields | Sensitivity |
|---|---|---|
| host | os_version, build_number, architecture, timezone | low |
| user_context | username, domain, privilege_hint | medium |
| software | name, version, install_path, publisher | medium |
| services_processes | name, state, executable_path | medium |
| registry | hive, key_path, value_name | high |
| paths | workspace roots, config dirs, script dirs | medium |
| artifacts | path, extension, size, modified_utc | medium/high |

## Initial Verified Seed Paths

- `C:\AppSogelink\ERAS_Connect_2026`
- `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Minimum Acceptance Criteria (v0.1)

- Schema covers host, software, runtime, registry, paths, and artifacts.
- Sensitivity classification exists for each section.
- Report-ready subset and raw subset are both identified.

## Planned Evidence

- `docs/evidence/ev-001-windows-scan-baseline.md`
- `docs/reports/windows_inventory_schema_review_<date>.md`
- `artifacts/inventories/windows_inventory_<timestamp>.json`

## Worker B Update (2026-04-23)

- Added executable read-only scan tooling at `scripts/windows_scan/Invoke-WindowsReadOnlyInventory.ps1`.
- Tool now accepts explicit verified roots via `-VerifiedRoots`, including:
  - `C:\AppSogelink\ERAS_Connect_2026`
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`
- Timestamped outputs are written to `artifacts/inventories/windows_scan_<timestamp>/` and `artifacts/logs/windows_scan_<timestamp>.log` with basic secret redaction.
