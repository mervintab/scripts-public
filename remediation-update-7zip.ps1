# Get the script's directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Define the expected installer name
$installerName = "7zip_installer.exe"
$installerPath = Join-Path $scriptDir $installerName

# Check if the installer exists in the script's folder
if (-Not (Test-Path $installerPath)) {
    Write-Output "Installer not found in the script directory. Please ensure $installerName is present."
    exit 1
}

Write-Output "Forcing installation using: $installerPath"

# Silent install (force reinstall)
Start-Process -FilePath $installerPath -ArgumentList "/S" -Wait -NoNewWindow

Write-Output "7-Zip installation/update forced successfully."

# Check installed 7-Zip version
$7zipPath = (Get-ItemProperty "HKLM:\SOFTWARE\7-Zip" -ErrorAction SilentlyContinue).Path
if ($7zipPath) {
    $output = & "$7zipPath\7z.exe" | Select-String "7-Zip"
    Write-Output "Installed 7-Zip version: $output"
} else {
    Write-Output "7-Zip installation verification failed. Please check manually."
}