## This script generates file that has a table of all installed versions of software on the machine. 

# example useage (from insidepowershell):
#	.\getInstalledPrograms.ps1 C:\Users\exampleFilename.txt

# Notes:
# 	to execute powershell scripts you need to set the policy.
# 	Get-ExecutionPolicy
# 	Set-ExecutionPolicy Unrestricted
# 	Set-ExecutionPolicy "Restricted"


param(
[string] $outputFilename
)

Write-Host "Welcome to getInstalledPrograms.ps1"
Write-Output "+ FILE: $outputFilename"

function InstalledPrograms
{
	Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion | Format-List | out-file -encoding utf8 $outputFilename 
}

$command=InstalledPrograms $outputFilename