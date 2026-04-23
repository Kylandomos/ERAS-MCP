# EV-001 - Baseline Root Directory Verification

Date: 2026-04-23
Status: validated

## Claim

The two initial roots are present on local disk as FileSystem directories.

## Method (Safe)

- `Test-Path`
- `Get-Item`

## Observations

- `C:\AppSogelink\ERAS_Connect_2026` -> Exists=True, ItemType=Directory
- `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView` -> Exists=True, ItemType=Directory

## Limits

- This evidence confirms directory existence only.
- No product version, installed feature set, or automation capability is inferred.
