[CmdletBinding()]
param(
    [string]$InventoryRoot = '',
    [string]$LogRoot = '',
    [string[]]$AdditionalRoots = @(),
    [string[]]$VerifiedRoots = @(),
    [string]$ErasRoot = '',
    [string]$MapPowerViewRoot = '',
    [int]$MaxArtifactsPerType = 150,
    [int]$MaxFilesScanned = 30000,
    [switch]$SkipArtifactDiscovery,
    [switch]$SkipPowerMapDiscovery
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
if ([string]::IsNullOrWhiteSpace($InventoryRoot)) {
    $InventoryRoot = Join-Path $repoRoot 'artifacts\inventories'
}

if ([string]::IsNullOrWhiteSpace($LogRoot)) {
    $LogRoot = Join-Path $repoRoot 'artifacts\logs'
}

$scanTimestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$scanDirectory = Join-Path $InventoryRoot "windows_scan_$scanTimestamp"
New-Item -ItemType Directory -Force -Path $scanDirectory | Out-Null
New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null

$logPath = Join-Path $LogRoot "windows_scan_$scanTimestamp.log"
New-Item -ItemType File -Force -Path $logPath | Out-Null

function Write-ScanLog {
    param([string]$Message)

    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ssK'), $Message
    Add-Content -LiteralPath $logPath -Value $line
}

function Invoke-Safe {
    param(
        [Parameter(Mandatory = $true)][scriptblock]$Script,
        [object]$Default = $null
    )

    try {
        & $Script
    }
    catch {
        Write-ScanLog -Message ("Warning: {0}" -f $_.Exception.Message)
        $Default
    }
}

function Protect-SecretValue {
    param(
        [string]$Name,
        [object]$Value
    )

    if ($null -eq $Value) {
        return $null
    }

    $namePattern = '(?i)(pass(word)?|secret|token|api[_-]?key|client[_-]?secret|connectionstring|credential|license|serial|pwd)'
    if ($Name -match $namePattern) {
        return '<REDACTED>'
    }

    if ($Value -is [string]) {
        $text = $Value
        $text = [regex]::Replace($text, '(?i)(password|pwd|secret|token|api[_-]?key)\s*=\s*[^;,\s]+', '$1=<REDACTED>')
        return $text
    }

    return $Value
}

function Get-RegistrySnapshot {
    param(
        [string]$Path,
        [int]$MaxSubKeys = 60
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return [pscustomobject]@{
            path = $Path
            exists = $false
            values = @{}
            subkeys = @()
        }
    }

    $propertyObject = Invoke-Safe -Default $null -Script { Get-ItemProperty -LiteralPath $Path -ErrorAction Stop }
    $values = [ordered]@{}
    if ($null -ne $propertyObject) {
        foreach ($property in $propertyObject.PSObject.Properties) {
            if ($property.Name -like 'PS*') {
                continue
            }

            $values[$property.Name] = Protect-SecretValue -Name "$Path::$($property.Name)" -Value $property.Value
        }
    }

    $subkeys = Invoke-Safe -Default @() -Script {
        Get-ChildItem -LiteralPath $Path -ErrorAction SilentlyContinue |
            Select-Object -ExpandProperty PSChildName -First $MaxSubKeys
    }

    [pscustomobject]@{
        path = $Path
        exists = $true
        values = $values
        subkeys = @($subkeys)
    }
}

function Get-ObjectPropertyValue {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string]$PropertyName
    )

    $property = $Object.PSObject.Properties[$PropertyName]
    if ($null -eq $property) {
        return $null
    }

    $property.Value
}

function New-FileRecord {
    param(
        [System.IO.FileInfo]$File,
        [string]$Root
    )

    [pscustomobject]@{
        name = $File.Name
        path = $File.FullName
        extension = $File.Extension
        size_bytes = $File.Length
        last_write_utc = $File.LastWriteTimeUtc.ToString('o')
        root = $Root
    }
}

function Get-ArtifactInventory {
    param(
        [string[]]$Roots,
        [int]$MaxPerCategory,
        [int]$MaxFiles
    )

    $categories = [ordered]@{
        mdb_accdb = @()
        dgn = @()
        config = @()
        scripts = @()
        macros = @()
        logs = @()
        tabular_exports = @()
    }

    $extensionsByCategory = @{
        mdb_accdb = @('.mdb', '.accdb')
        dgn = @('.dgn')
        config = @('.cfg', '.ucf', '.upf', '.ini', '.xml', '.json', '.rdl')
        scripts = @('.ps1', '.bat', '.vbs', '.py')
        macros = @('.mvba', '.vba', '.bas', '.keyin')
        logs = @('.log')
        tabular_exports = @('.csv', '.xls', '.xlsx')
    }

    $scannedCount = 0
    $stoppedByMaxFiles = $false

    :scanRoots foreach ($root in $Roots) {
        if (-not (Test-Path -LiteralPath $root)) {
            continue
        }

        Write-ScanLog -Message "Artifact scan root: $root"
        try {
            foreach ($file in Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue) {
                if ($scannedCount -ge $MaxFiles) {
                    $stoppedByMaxFiles = $true
                    Write-ScanLog -Message "Artifact scan stopped at max file threshold: $MaxFiles"
                    break scanRoots
                }

                $scannedCount += 1
                $extension = $file.Extension.ToLowerInvariant()
                foreach ($category in $extensionsByCategory.Keys) {
                    $categoryExtensions = $extensionsByCategory[$category]
                    if ($extension -in $categoryExtensions -and $categories[$category].Count -lt $MaxPerCategory) {
                        $categories[$category] += (New-FileRecord -File $file -Root $root)
                    }
                }

                if ($file.Name -match '(?i)keyin' -and $categories['macros'].Count -lt $MaxPerCategory) {
                    $categories['macros'] += (New-FileRecord -File $file -Root $root)
                }
            }
        }
        catch {
            Write-ScanLog -Message ("Warning: artifact traversal failed for root {0}: {1}" -f $root, $_.Exception.Message)
        }
    }

    [pscustomobject]@{
        roots_scanned = $Roots
        files_scanned = $scannedCount
        scan_stopped_by_max_files = $stoppedByMaxFiles
        max_files_scanned = $MaxFiles
        max_per_category = $MaxPerCategory
        matches = [pscustomobject]@{
            mdb_accdb = @($categories['mdb_accdb'] | Sort-Object path -Unique)
            dgn = @($categories['dgn'] | Sort-Object path -Unique)
            config = @($categories['config'] | Sort-Object path -Unique)
            scripts = @($categories['scripts'] | Sort-Object path -Unique)
            macros = @($categories['macros'] | Sort-Object path -Unique)
            logs = @($categories['logs'] | Sort-Object path -Unique)
            tabular_exports = @($categories['tabular_exports'] | Sort-Object path -Unique)
        }
    }
}

function Get-ItemCount {
    param($Value)

    if ($null -eq $Value) {
        return 0
    }

    @($Value).Count
}

function ConvertTo-WindowsInventoryMarkdown {
    param([pscustomobject]$Inventory)

    $softwareCount = Get-ItemCount -Value $Inventory.installed_software_hints
    $processCount = Get-ItemCount -Value $Inventory.relevant_processes
    $serviceCount = Get-ItemCount -Value $Inventory.relevant_services
    $registryCount = Get-ItemCount -Value $Inventory.registry_snapshot
    $verifiedRoots = Get-ItemCount -Value ($Inventory.scan_roots | Where-Object { $_.exists })
    $unverifiedRoots = Get-ItemCount -Value ($Inventory.scan_roots | Where-Object { -not $_.exists })

    $lines = @(
        '# Windows Read-Only Inventory',
        '',
        "Generated (UTC): $($Inventory.metadata.generated_at_utc)",
        "Scan ID: $($Inventory.metadata.scan_id)",
        '',
        '## Summary',
        "- Host: $($Inventory.system.hostname)",
        "- User: $($Inventory.system.current_user)",
        "- Windows: $($Inventory.system.windows_caption) ($($Inventory.system.windows_version) build $($Inventory.system.windows_build))",
        "- Installed software hints: $softwareCount",
        "- Relevant processes: $processCount",
        "- Relevant services: $serviceCount",
        "- Registry keys evaluated: $registryCount",
        "- Scan roots (verified/unverified): $verifiedRoots/$unverifiedRoots",
        '- Root existence is treated as path evidence only; capability/version claims require separate evidence.',
        '',
        '## Root Verification',
        '| Path | Source | Status |',
        '|---|---|---|'
    )

    foreach ($root in $Inventory.scan_roots) {
        $status = if ($root.exists) { 'verified' } else { 'unverified' }
        $lines += "| $($root.path) | $($root.source) | $status |"
    }

    $lines += ''
    $lines += '## OpenCities/MicroStation Safe Read Actions'
    foreach ($candidate in $Inventory.powermap.safe_read_action_candidates) {
        $lines += "- $($candidate.action) ($($candidate.method); risk: $($candidate.risk))"
    }

    $lines += ''
    $lines += '## OpenCities/MicroStation Gaps and Fallbacks'
    if ((Get-ItemCount -Value $Inventory.powermap.gaps_and_fallbacks) -eq 0) {
        $lines += '- No critical discovery gaps were reported by the read-only probe.'
    }
    else {
        foreach ($gap in $Inventory.powermap.gaps_and_fallbacks) {
            $lines += "- Gap: $($gap.gap) | Fallback: $($gap.fallback)"
        }
    }

    ($lines -join [Environment]::NewLine)
}

function ConvertTo-PowerMapMarkdown {
    param([pscustomobject]$PowerMapInventory)

    $lines = @(
        '# POWEMAP Automation Surface (Read-Only)',
        '',
        "Generated (UTC): $($PowerMapInventory.generated_at_utc)",
        '',
        '## Discovery Summary',
        "- Executables discovered: $(Get-ItemCount -Value $PowerMapInventory.discovered_executables)",
        "- Workspace path candidates: $(Get-ItemCount -Value $PowerMapInventory.workspace_path_candidates)",
        "- Config files sampled: $(Get-ItemCount -Value $PowerMapInventory.config_files)",
        "- Python scripts sampled: $(Get-ItemCount -Value $PowerMapInventory.python_manager.scripts)",
        "- VBA/macro files sampled: $(Get-ItemCount -Value $PowerMapInventory.macro_inventory.vba_files)",
        "- Key-in files sampled: $(Get-ItemCount -Value $PowerMapInventory.macro_inventory.keyin_files)",
        '',
        '## Python Manager',
        "- Found: $($PowerMapInventory.python_manager.found)"
    )

    if ((Get-ItemCount -Value $PowerMapInventory.python_manager.executables) -gt 0) {
        $lines += '- Executables:'
        foreach ($exe in $PowerMapInventory.python_manager.executables) {
            $lines += "  - $($exe.path) ($($exe.product_version))"
        }
    }

    $lines += ''
    $lines += '## Safe Read Action Candidates'
    foreach ($candidate in $PowerMapInventory.safe_read_action_candidates) {
        $lines += "- $($candidate.action) ($($candidate.method); risk: $($candidate.risk))"
    }

    $lines += ''
    $lines += '## Gaps and Fallbacks'
    if ((Get-ItemCount -Value $PowerMapInventory.gaps_and_fallbacks) -eq 0) {
        $lines += '- None'
    }
    else {
        foreach ($gap in $PowerMapInventory.gaps_and_fallbacks) {
            $lines += "- Gap: $($gap.gap) | Fallback: $($gap.fallback)"
        }
    }

    ($lines -join [Environment]::NewLine)
}

Write-ScanLog -Message 'Starting read-only Windows inventory.'

$targetRegex = '(?i)(bentley|opencities|open\s*cities|microstation|powermap|eras|sogelink|access|msaccess)'
$scanRoots = @(
    [pscustomobject]@{ path = (Join-Path $env:ProgramFiles 'Bentley'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path ${env:ProgramFiles(x86)} 'Bentley'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path $env:ProgramData 'Bentley'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path $env:LOCALAPPDATA 'Bentley'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path $env:APPDATA 'Bentley'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path $env:USERPROFILE 'Documents'); source = 'default' },
    [pscustomobject]@{ path = (Join-Path $env:PUBLIC 'Documents'); source = 'default' }
)

if (-not [string]::IsNullOrWhiteSpace($ErasRoot)) {
    $scanRoots += [pscustomobject]@{ path = $ErasRoot; source = 'user_provided_eras' }
}

if (-not [string]::IsNullOrWhiteSpace($MapPowerViewRoot)) {
    $scanRoots += [pscustomobject]@{ path = $MapPowerViewRoot; source = 'user_provided_map_powerview' }
}

foreach ($root in $AdditionalRoots) {
    if (-not [string]::IsNullOrWhiteSpace($root)) {
        $scanRoots += [pscustomobject]@{ path = $root; source = 'user_provided_additional' }
    }
}

foreach ($root in $VerifiedRoots) {
    if (-not [string]::IsNullOrWhiteSpace($root)) {
        $scanRoots += [pscustomobject]@{ path = $root; source = 'user_provided_verified' }
    }
}

$scanRoots = $scanRoots |
    Where-Object { -not [string]::IsNullOrWhiteSpace($_.path) } |
    Group-Object path | ForEach-Object { $_.Group[0] }

$scanRootsVerified = foreach ($entry in $scanRoots) {
    [pscustomobject]@{
        path = $entry.path
        source = $entry.source
        exists = (Test-Path -LiteralPath $entry.path)
    }
}

$envSnapshot = Invoke-Safe -Default @() -Script {
    Get-ChildItem Env: | Sort-Object Name | ForEach-Object {
        [pscustomobject]@{
            name = $_.Name
            value = Protect-SecretValue -Name $_.Name -Value $_.Value
        }
    }
}

$os = Invoke-Safe -Default $null -Script { Get-CimInstance -ClassName Win32_OperatingSystem }
$computer = Invoke-Safe -Default $null -Script { Get-CimInstance -ClassName Win32_ComputerSystem }
$isAdmin = Invoke-Safe -Default $false -Script {
    $principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

$uninstallPaths = @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
)

$installedSoftwareHints = @()
foreach ($path in $uninstallPaths) {
    $entries = Invoke-Safe -Default @() -Script { Get-ItemProperty -Path $path -ErrorAction SilentlyContinue }
    foreach ($entry in $entries) {
        $displayName = Get-ObjectPropertyValue -Object $entry -PropertyName 'DisplayName'
        $publisher = Get-ObjectPropertyValue -Object $entry -PropertyName 'Publisher'
        $displayVersion = Get-ObjectPropertyValue -Object $entry -PropertyName 'DisplayVersion'
        $installLocation = Get-ObjectPropertyValue -Object $entry -PropertyName 'InstallLocation'
        $uninstallString = Get-ObjectPropertyValue -Object $entry -PropertyName 'UninstallString'

        if ([string]::IsNullOrWhiteSpace($displayName)) {
            continue
        }

        if ($displayName -notmatch $targetRegex -and $publisher -notmatch $targetRegex) {
            continue
        }

        $installedSoftwareHints += [pscustomobject]@{
            name = $displayName
            version = $displayVersion
            publisher = $publisher
            install_location = Protect-SecretValue -Name 'InstallLocation' -Value $installLocation
            uninstall_hint = Protect-SecretValue -Name 'UninstallString' -Value $uninstallString
        }
    }
}

$installedSoftwareHints = $installedSoftwareHints |
    Sort-Object name, version, publisher -Unique

$relevantProcesses = Invoke-Safe -Default @() -Script {
    Get-CimInstance -ClassName Win32_Process | Where-Object {
        $_.Name -match $targetRegex -or $_.ExecutablePath -match $targetRegex
    } | ForEach-Object {
        [pscustomobject]@{
            name = $_.Name
            process_id = $_.ProcessId
            executable_path = $_.ExecutablePath
            command_line = Protect-SecretValue -Name 'CommandLine' -Value $_.CommandLine
        }
    }
}

$relevantServices = Invoke-Safe -Default @() -Script {
    Get-CimInstance -ClassName Win32_Service | Where-Object {
        $_.Name -match $targetRegex -or $_.DisplayName -match $targetRegex -or $_.PathName -match $targetRegex
    } | ForEach-Object {
        [pscustomobject]@{
            name = $_.Name
            display_name = $_.DisplayName
            state = $_.State
            start_mode = $_.StartMode
            path_name = Protect-SecretValue -Name 'ServicePath' -Value $_.PathName
        }
    }
}

$relevantTasks = Invoke-Safe -Default @() -Script {
    Get-ScheduledTask | Where-Object {
        $_.TaskName -match $targetRegex -or $_.TaskPath -match $targetRegex
    } | ForEach-Object {
        [pscustomobject]@{
            task_name = $_.TaskName
            task_path = $_.TaskPath
            state = $_.State.ToString()
        }
    }
}

$registryTargets = @(
    'HKLM:\SOFTWARE\Bentley',
    'HKLM:\SOFTWARE\WOW6432Node\Bentley',
    'HKCU:\SOFTWARE\Bentley',
    'HKCU:\SOFTWARE\OpenCities',
    'HKLM:\SOFTWARE\Sogelink',
    'HKCU:\SOFTWARE\Sogelink',
    'HKLM:\SOFTWARE\ERAS',
    'HKCU:\SOFTWARE\ERAS',
    'HKLM:\SOFTWARE\Microsoft\Office\Access',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Office\Access'
)

$registrySnapshot = foreach ($registryPath in $registryTargets) {
    Get-RegistrySnapshot -Path $registryPath
}

$artifactRoots = $scanRootsVerified |
    Where-Object { $_.exists } |
    Select-Object -ExpandProperty path -Unique

$artifactInventory = if ($SkipArtifactDiscovery) {
    [pscustomobject]@{
        roots_scanned = $artifactRoots
        files_scanned = 0
        scan_stopped_by_max_files = $false
        max_files_scanned = $MaxFilesScanned
        max_per_category = $MaxArtifactsPerType
        matches = [pscustomobject]@{
            mdb_accdb = @()
            dgn = @()
            config = @()
            scripts = @()
            macros = @()
            logs = @()
            tabular_exports = @()
        }
    }
}
else {
    Get-ArtifactInventory -Roots $artifactRoots -MaxPerCategory $MaxArtifactsPerType -MaxFiles $MaxFilesScanned
}

$powerMapInventory = [pscustomobject]@{
    generated_at_utc = (Get-Date).ToUniversalTime().ToString('o')
    discovered_executables = @()
    workspace_path_candidates = @()
    config_files = @()
    python_manager = [pscustomobject]@{ found = $false; executables = @(); scripts = @(); examples = @() }
    macro_inventory = [pscustomobject]@{ vba_files = @(); keyin_files = @() }
    safe_read_action_candidates = @()
    gaps_and_fallbacks = @(
        [pscustomobject]@{
            gap = 'PowerMap discovery was skipped or unavailable.'
            fallback = 'Run scan again without -SkipPowerMapDiscovery and ensure helper script exists.'
        }
    )
}

if (-not $SkipPowerMapDiscovery) {
    $powerMapScriptPath = Join-Path $PSScriptRoot '..\powermap\Get-PowerMapReadOnlyInventory.ps1'
    if (Test-Path -LiteralPath $powerMapScriptPath) {
        . $powerMapScriptPath
        $powerMapInventory = Invoke-Safe -Default $powerMapInventory -Script {
            Get-PowerMapReadOnlyInventory `
                -AdditionalRoots ($scanRoots | Select-Object -ExpandProperty path) `
                -MaxFilesPerCategory $MaxArtifactsPerType `
                -RedactValue { param([string]$Name, [object]$Value) Protect-SecretValue -Name $Name -Value $Value }
        }
    }
    else {
        Write-ScanLog -Message "PowerMap helper script not found at $powerMapScriptPath"
    }
}

$inventory = [pscustomobject]@{
    metadata = [pscustomobject]@{
        scan_id = "windows_scan_$scanTimestamp"
        generated_at_utc = (Get-Date).ToUniversalTime().ToString('o')
        read_only = $true
        script_path = $PSCommandPath
        max_artifacts_per_type = $MaxArtifactsPerType
        max_files_scanned = $MaxFilesScanned
        log_path = $logPath
    }
    system = [pscustomobject]@{
        hostname = $env:COMPUTERNAME
        current_user = $env:USERNAME
        user_domain = $env:USERDOMAIN
        is_admin = [bool]$isAdmin
        windows_caption = if ($null -ne $os) { $os.Caption } else { $null }
        windows_version = if ($null -ne $os) { $os.Version } else { $null }
        windows_build = if ($null -ne $os) { $os.BuildNumber } else { $null }
        windows_install_date_utc = if ($null -ne $os) { $os.InstallDate.ToUniversalTime().ToString('o') } else { $null }
        powershell_version = $PSVersionTable.PSVersion.ToString()
        manufacturer = if ($null -ne $computer) { $computer.Manufacturer } else { $null }
        model = if ($null -ne $computer) { $computer.Model } else { $null }
    }
    scan_roots = @($scanRootsVerified)
    environment_variables = @($envSnapshot)
    installed_software_hints = @($installedSoftwareHints)
    relevant_processes = @($relevantProcesses)
    relevant_services = @($relevantServices)
    relevant_scheduled_tasks = @($relevantTasks)
    registry_snapshot = @($registrySnapshot)
    artifacts = $artifactInventory
    powermap = $powerMapInventory
}

$jsonPath = Join-Path $scanDirectory 'inventory.json'
$windowsReportPath = Join-Path $scanDirectory 'WINDOWS_INVENTORY.md'
$powermapReportPath = Join-Path $scanDirectory 'POWEMAP_AUTOMATION_SURFACE.md'

$inventory | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $jsonPath -Encoding UTF8
(ConvertTo-WindowsInventoryMarkdown -Inventory $inventory) | Set-Content -LiteralPath $windowsReportPath -Encoding UTF8
(ConvertTo-PowerMapMarkdown -PowerMapInventory $powerMapInventory) | Set-Content -LiteralPath $powermapReportPath -Encoding UTF8

Write-ScanLog -Message "Inventory JSON written to $jsonPath"
Write-ScanLog -Message "Windows report written to $windowsReportPath"
Write-ScanLog -Message "PowerMap report written to $powermapReportPath"
Write-ScanLog -Message 'Read-only Windows inventory completed.'

[pscustomobject]@{
    scan_id = "windows_scan_$scanTimestamp"
    inventory_json = $jsonPath
    windows_report = $windowsReportPath
    powermap_report = $powermapReportPath
    log_path = $logPath
}
