Set-StrictMode -Version Latest

function Get-PowerMapReadOnlyInventory {
    [CmdletBinding()]
    param(
        [string[]]$AdditionalRoots = @(),
        [int]$MaxFilesPerCategory = 200,
        [scriptblock]$RedactValue = { param([string]$Name, [object]$Value) $Value }
    )

    $powerMapRegex = '(?i)(bentley|opencities|open\s*cities|microstation|powermap|powerview|map\s*powerview)'

    function Invoke-Safe {
        param(
            [Parameter(Mandatory = $true)][scriptblock]$Script,
            [object]$Default = $null
        )

        try {
            & $Script
        }
        catch {
            $Default
        }
    }

    function Invoke-Redaction {
        param(
            [string]$Name,
            [object]$Value
        )

        try {
            & $RedactValue $Name $Value
        }
        catch {
            $Value
        }
    }

    function New-FileRecord {
        param([System.IO.FileInfo]$File)

        [pscustomobject]@{
            name = $File.Name
            path = $File.FullName
            extension = $File.Extension
            size_bytes = $File.Length
            last_write_utc = $File.LastWriteTimeUtc.ToString('o')
        }
    }

    function Find-Files {
        param(
            [string[]]$Roots,
            [scriptblock]$Predicate,
            [int]$MaxResults = 200
        )

        $matches = @()
        $seenPaths = New-Object System.Collections.Generic.HashSet[string] ([System.StringComparer]::OrdinalIgnoreCase)
        :scanRoots foreach ($root in $Roots) {
            if ($matches.Count -ge $MaxResults) {
                break
            }

            if (-not (Test-Path -LiteralPath $root)) {
                continue
            }

            try {
                foreach ($file in Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue) {
                    if ($matches.Count -ge $MaxResults) {
                        break scanRoots
                    }

                    if (& $Predicate $file) {
                        if ($seenPaths.Add($file.FullName)) {
                            $matches += (New-FileRecord -File $file)
                        }
                    }
                }
            }
            catch {
                # Ignore inaccessible subtrees; this inventory remains best-effort and read-only.
            }
        }

        @($matches)
    }

    function Get-RegistrySnapshot {
        param([string]$Path)

        $exists = Test-Path -LiteralPath $Path
        if (-not $exists) {
            return [pscustomobject]@{
                path = $Path
                exists = $false
                values = @{}
                subkeys = @()
            }
        }

        $item = Invoke-Safe -Script { Get-Item -LiteralPath $Path -ErrorAction Stop }
        $propertyObject = Invoke-Safe -Script { Get-ItemProperty -LiteralPath $Path -ErrorAction Stop } -Default $null
        $valueTable = [ordered]@{}

        if ($null -ne $propertyObject) {
            foreach ($property in $propertyObject.PSObject.Properties) {
                if ($property.Name -like 'PS*') {
                    continue
                }

                $redacted = Invoke-Redaction -Name "$Path::$($property.Name)" -Value $property.Value
                $valueTable[$property.Name] = $redacted
            }
        }

        $subKeys = Invoke-Safe -Default @() -Script {
            Get-ChildItem -LiteralPath $Path -ErrorAction SilentlyContinue |
                Select-Object -ExpandProperty PSChildName -First 80
        }

        [pscustomobject]@{
            path = $item.Name
            exists = $true
            values = $valueTable
            subkeys = @($subKeys)
        }
    }

    $candidateRoots = @(
        (Join-Path $env:ProgramFiles 'Bentley'),
        (Join-Path ${env:ProgramFiles(x86)} 'Bentley'),
        (Join-Path $env:ProgramData 'Bentley'),
        (Join-Path $env:LOCALAPPDATA 'Bentley'),
        (Join-Path $env:APPDATA 'Bentley'),
        (Join-Path $env:PUBLIC 'Documents\Bentley'),
        (Join-Path $env:USERPROFILE 'Documents\Bentley'),
        (Join-Path $env:USERPROFILE 'Documents')
    ) + $AdditionalRoots

    $roots = $candidateRoots |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) } |
        Select-Object -Unique

    $existingRoots = $roots | Where-Object { Test-Path -LiteralPath $_ }

    $processSnapshot = Invoke-Safe -Default @() -Script {
        Get-Process | Where-Object { $_.ProcessName -match $powerMapRegex } | ForEach-Object {
            [pscustomobject]@{
                process_name = $_.ProcessName
                pid = $_.Id
                path = Invoke-Safe -Default $null -Script { $_.Path }
                start_time_utc = Invoke-Safe -Default $null -Script { $_.StartTime.ToUniversalTime().ToString('o') }
            }
        }
    }

    $serviceSnapshot = Invoke-Safe -Default @() -Script {
        Get-Service | Where-Object { $_.Name -match $powerMapRegex -or $_.DisplayName -match $powerMapRegex } | ForEach-Object {
            [pscustomobject]@{
                name = $_.Name
                display_name = $_.DisplayName
                status = $_.Status.ToString()
                start_type = Invoke-Safe -Default $null -Script { $_.StartType.ToString() }
            }
        }
    }

    $installRoots = @(
        (Join-Path $env:ProgramFiles 'Bentley'),
        (Join-Path ${env:ProgramFiles(x86)} 'Bentley'),
        (Join-Path $env:ProgramData 'Bentley')
    ) + $AdditionalRoots

    $installRoots = $installRoots |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) -and (Test-Path -LiteralPath $_) } |
        Sort-Object -Unique

    $productExecutables = Find-Files -Roots $installRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.Name -match '(?i)(microstation|opencities|open\s*cities|powermap|powerview|map\s*powerview|ustation|pythonmanager).*\.exe$'
    } | ForEach-Object {
        $versionInfo = Invoke-Safe -Script { (Get-Item -LiteralPath $_.path).VersionInfo } -Default $null

        [pscustomobject]@{
            name = $_.name
            path = $_.path
            file_version = if ($null -ne $versionInfo) { $versionInfo.FileVersion } else { $null }
            product_version = if ($null -ne $versionInfo) { $versionInfo.ProductVersion } else { $null }
            last_write_utc = $_.last_write_utc
        }
    }

    $workspaceDirectorySet = New-Object System.Collections.Generic.HashSet[string] ([System.StringComparer]::OrdinalIgnoreCase)
    :workspaceRoots foreach ($root in $existingRoots) {
        if ($workspaceDirectorySet.Count -ge $MaxFilesPerCategory) {
            break
        }

        try {
            foreach ($directory in Get-ChildItem -LiteralPath $root -Directory -Recurse -ErrorAction SilentlyContinue) {
                if ($workspaceDirectorySet.Count -ge $MaxFilesPerCategory) {
                    break workspaceRoots
                }

                if ($directory.Name -match '(?i)(workspace|workset|configuration|standards|macros|python|examples?)') {
                    [void]$workspaceDirectorySet.Add($directory.FullName)
                }
            }
        }
        catch {
            # Ignore inaccessible subtrees; this inventory remains best-effort and read-only.
        }
    }

    $workspaceDirectories = @($workspaceDirectorySet)

    $configFiles = Find-Files -Roots $existingRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.Extension -in @('.cfg', '.ucf', '.upf', '.ini', '.xml', '.json')
    }

    $pythonScripts = Find-Files -Roots $existingRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.Extension -eq '.py' -or $file.FullName -match '(?i)python'
    }

    $vbaFiles = Find-Files -Roots $existingRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.Extension -in @('.mvba', '.vba', '.bas')
    }

    $keyinFiles = Find-Files -Roots $existingRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.Name -match '(?i)keyin' -or $file.Extension -eq '.keyin'
    }

    $exampleFiles = Find-Files -Roots $existingRoots -MaxResults $MaxFilesPerCategory -Predicate {
        param($file)
        $file.FullName -match '(?i)example|sample|template' -and $file.Extension -in @('.py', '.mvba', '.vba', '.cfg', '.txt')
    }

    $pythonManagerExecutables = $productExecutables | Where-Object { $_.name -match '(?i)pythonmanager' }
    $safeReadActions = @(
        [pscustomobject]@{
            action = 'Enumerate installed Bentley/OpenCities executables and versions'
            method = 'Read executable metadata from known install paths'
            risk = 'low'
        },
        [pscustomobject]@{
            action = 'Enumerate MicroStation/OpenCities workspace and config files'
            method = 'Read-only filesystem scan for .cfg/.ucf/.upf/.ini/.xml'
            risk = 'low'
        },
        [pscustomobject]@{
            action = 'Inventory Python scripts and VBA/macro artifacts'
            method = 'Read filenames and metadata only; no script execution'
            risk = 'low'
        },
        [pscustomobject]@{
            action = 'Capture relevant registry values for Bentley products'
            method = 'Read HKLM/HKCU Bentley-related keys'
            risk = 'low'
        }
    )

    $gapsAndFallbacks = @()
    if (-not $productExecutables) {
        $gapsAndFallbacks += [pscustomobject]@{
            gap = 'No OpenCities/MicroStation executables discovered in scanned install roots.'
            fallback = 'Add explicit install roots through -AdditionalRoots and rerun inventory.'
        }
    }

    if (-not $pythonManagerExecutables) {
        $gapsAndFallbacks += [pscustomobject]@{
            gap = 'Python Manager executable not found by read-only scan.'
            fallback = 'Inspect OpenCities installation media or app launcher settings manually.'
        }
    }

    if (-not $workspaceDirectories) {
        $gapsAndFallbacks += [pscustomobject]@{
            gap = 'No workspace/workset directories were detected in scanned roots.'
            fallback = 'Collect active workspace path from user profile variables or OpenCities session settings.'
        }
    }

    $registryPaths = @(
        'HKLM:\SOFTWARE\Bentley',
        'HKLM:\SOFTWARE\WOW6432Node\Bentley',
        'HKCU:\SOFTWARE\Bentley',
        'HKCU:\SOFTWARE\OpenCities',
        'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\MicroStation.exe',
        'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OpenCitiesMap.exe'
    )

    $registrySnapshot = @()
    foreach ($path in $registryPaths) {
        $registrySnapshot += Get-RegistrySnapshot -Path $path
    }

    [pscustomobject]@{
        scan_type = 'powermap_read_only_inventory'
        generated_at_utc = (Get-Date).ToUniversalTime().ToString('o')
        scanned_roots = $roots
        existing_roots = $existingRoots
        process_snapshot = @($processSnapshot)
        service_snapshot = @($serviceSnapshot)
        registry_snapshot = @($registrySnapshot)
        discovered_executables = @($productExecutables)
        workspace_path_candidates = @($workspaceDirectories)
        config_files = @($configFiles)
        python_manager = [pscustomobject]@{
            found = (@($pythonManagerExecutables).Count -gt 0)
            executables = @($pythonManagerExecutables)
            scripts = @($pythonScripts)
            examples = @($exampleFiles)
        }
        macro_inventory = [pscustomobject]@{
            vba_files = @($vbaFiles)
            keyin_files = @($keyinFiles)
        }
        safe_read_action_candidates = @($safeReadActions)
        gaps_and_fallbacks = @($gapsAndFallbacks)
    }
}
