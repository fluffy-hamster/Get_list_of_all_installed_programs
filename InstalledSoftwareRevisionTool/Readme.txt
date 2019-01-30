######################################
#### Get Installed Programs v1.0  ####
######################################

## Introduction

This Python script searches the registry for a of list installed programs on your computer (both 32 and 64 bit). It then combines the results into a markdown table with names and versions saved in the 'results' subdirectory. Tested on both Windows 7 and Windows 10.

Example Output:

| Name | Version |
|---------------|----------|
| AxCrypt 2.1.1547.0 | 2.1.1547.0 |
| DB Browser for SQLite | 3.10.1 |
| Deus Ex: Mankind Divided™ | N/A |
| Google Chrome | 72.0.3626.81 |
| Google Update Helper | 1.3.33.23 |
| Microsoft .NET Framework 4 Multi-Targeting Pack | 4.0.30319 |
| Microsoft .NET Framework 4.5 Multi-Targeting Pack | 4.5.50710 |
| Microsoft .NET Framework 4.5.1 Multi-Targeting Pack | 4.5.50932 |
| Microsoft .NET Framework 4.5.2 Multi-Targeting Pack | 4.5.51651 |
| Microsoft .NET Framework 4.6 Targeting Pack | 4.6.00081 |
| Microsoft .NET Framework 4.6.1 SDK | 4.6.01055 |
| Microsoft Web Deploy 4.0 | 10.0.1994 |
| NVIDIA Stereoscopic 3D Driver | 7.17.13.7500 |
| Notepad++ (32-bit x86) | 7.5.9 |

## HOW TO USE

1. Open a the command prompt AS administrator
2. While in the terminal enter:  "powershell Get-ExecutionPolicy". Make a note of this value. 
3. Now enter: "powershell Set-ExecutionPolicy unrestricted"
4. change directory to the software_revision_folder, for example:
	> cd C:\Users\chris\Desktop\InstalledSoftwareRevisionTool
5. Now Enter: python get_installed_programs.py
6. Check the 'results' subdirectory to see in the markdown table has been successfully created.
7. Now Enter: powershell Set-ExecutionPolicy X", where "X" is the value you obtained from step (2).

