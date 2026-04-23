# Windows/OpenCities Read-Only Scan Tooling

This folder contains reproducible, read-only PowerShell tooling for Windows + OpenCities/MicroStation environment discovery.

## Entry point

- `Invoke-WindowsReadOnlyInventory.ps1`

## Safety model

- Read-only discovery only.
- No Bentley/OpenCities command execution.
- No destructive filesystem or registry operations.
- Obvious secret-like values are redacted in outputs.
- Filesystem caps are enforced during traversal (streaming enumeration with early stop).

## Output locations

Each run creates timestamped outputs under:

- `artifacts/inventories/windows_scan_yyyyMMdd_HHmmss/`
  - `inventory.json`
  - `WINDOWS_INVENTORY.md`
  - `POWEMAP_AUTOMATION_SURFACE.md`
- `artifacts/logs/windows_scan_yyyyMMdd_HHmmss.log`

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows_scan\Invoke-WindowsReadOnlyInventory.ps1
```

### With explicit verified roots

Use this when roots are already verified with `Test-Path` and should be tagged as `user_provided_verified` in the output:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows_scan\Invoke-WindowsReadOnlyInventory.ps1 `
  -VerifiedRoots @(
    'C:\AppSogelink\ERAS_Connect_2026',
    'C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView'
  )
```

### With explicit named roots

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows_scan\Invoke-WindowsReadOnlyInventory.ps1 `
  -ErasRoot 'C:\AppSogelink\ERAS_Connect_2026' `
  -MapPowerViewRoot 'C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView'
```

### Optional controls

- `-SkipArtifactDiscovery`: skip filesystem artifact scan.
- `-SkipPowerMapDiscovery`: skip `scripts/powermap/Get-PowerMapReadOnlyInventory.ps1`.
- `-MaxArtifactsPerType 200`: cap sampled files per category.
- `-MaxFilesScanned 40000`: cap total file enumeration volume; traversal stops when this threshold is reached.
- `-AdditionalRoots @('D:\Custom\Path')`: add extra scan roots.
