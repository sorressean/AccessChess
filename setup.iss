[Setup]
AppName=Access Chess
AppMutex=Access Chess
AppVersion=1.0
WizardStyle=modern
DefaultDirName={autopf}\Access Chess
DefaultGroupName=Access Chess
UninstallDisplayIcon={app}\main.exe
Compression=lzma2/ultra64 
 SolidCompression=yes
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=setup
[Files]
Source: "main.dist\*"; DestDir: "{app}"
[Icons]
Name: "{group}\Access Chess"; Filename: "{app}\main.exe"
