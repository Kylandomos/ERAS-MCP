# OpenCities/PowerMap Automation Surface v0.1

Last updated: 2026-04-23

## Facts Proved

- Kickoff requires documenting real automation capability from local observation, not assumptions.
- Early phase must focus on safe read/probe actions.
- A MapPowerView root directory is verified to exist (`Test-Path` + `Get-Item`):
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Hypotheses

- The environment may expose multiple automation channels (Python, macros, key-ins, config-driven behaviors).

## Open Questions

- Is Python Manager available and enabled on the target installation?
- Which existing scripts/macros are trusted and currently used in operations?
- What probe set can run without mutating drawings/workspaces?

## Decisions

- Capture capability inventory first, then define a safe probe subset.
- Separate "detected capability" from "validated capability" in reporting.
- Use the verified directory path as an initial discovery seed, without inferring capabilities.

## Discovery Buckets

1. Installation metadata (version, edition, install roots).
2. Workspace/workset and configuration paths.
3. Script/macro/key-in inventory.
4. Existing custom tooling and extensions.
5. Safe read probe candidates.
6. Gaps and fallback strategies.

## Initial Verified Directory Root

- `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`

## Expected Deliverable Artifacts (Future)

- `docs/reports/powermap_capability_inventory_<date>.md`
- `docs/reports/powermap_safe_read_actions_<date>.md`
- `docs/reports/powermap_gaps_fallbacks_<date>.md`
- `artifacts/logs/powermap_probe_<timestamp>.log`

## Acceptance Criteria (v0.1 Plan)

- Capability inventory template clearly distinguishes detected vs validated status.
- Safe read action list explicitly excludes any mutating operations.
- Unknowns and blockers are tracked as questions, not hidden as assumptions.

## Evidence References

- `EVIDENCE_INDEX.md#ev-002`
- `EVIDENCE_INDEX.md#ev-004`

## Worker B Update (2026-04-23)

- Added read-only OpenCities/MicroStation discovery helper at `scripts/powermap/Get-PowerMapReadOnlyInventory.ps1`.
- Helper inventories registry/process/services, executable metadata, workspace/config/script/macro artifacts, safe read action candidates, and gaps/fallbacks.
- Integrated into `scripts/windows_scan/Invoke-WindowsReadOnlyInventory.ps1`; no Bentley/OpenCities automation commands are executed.
