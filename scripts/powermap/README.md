# PowerMap Read-Only Discovery Helper

`Get-PowerMapReadOnlyInventory.ps1` exposes `Get-PowerMapReadOnlyInventory`, used by the Windows scanner to collect OpenCities/MicroStation evidence without executing automation commands.

Collected evidence includes:

- Bentley/OpenCities process and service snapshots
- Bentley/OpenCities registry key snapshots
- Executable/version metadata from known install roots
- Workspace/config path candidates
- Python script, example, VBA/macro, and key-in file inventories
- Safe read action candidates and discovery gaps/fallbacks

Traversal is bounded by `-MaxFilesPerCategory` and enforced during recursive enumeration.

The function is read-only and intended to be dot-sourced from:

- `scripts/windows_scan/Invoke-WindowsReadOnlyInventory.ps1`
