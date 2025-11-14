import subprocess
import winreg

path = winreg.HKEY_LOCAL_MACHINE

defender = winreg.OpenKeyEx(path, r"SOFTWARE\\Policies\\Microsoft\\Windows Defender\\")
try:
  winreg.DeleteValue(defender,r"DisableAntiSpyware\\")
  winreg.DeleteValue(defender,r"DisableAntiVirus\\")
  winreg.SetValueEx(defender,r"PUAProtection\\", 0, winreg.REG_DWORD, 1)
#Defender Registry Policy

policy = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Policies\\System\\")

winreg.SetValueEx(policy,r"TypeofAdminApprovalMode\\", 0, winreg.REG_DWORD, 2)



print("Success!")
