import subprocess

def set_audit_policy(category):
    command = f'auditpol /set /category:"{category}" /success:enable /failure:enable'
    subprocess.run(command, shell=True, capture_output=True, text=True)
    

set_audit_policy("Account Logon")
set_audit_policy("account management")
set_audit_policy("directory service access")
set_audit_policy("logon events")
set_audit_policy("object access")
set_audit_policy("policy change")
set_audit_policy("privilege use")
set_audit_policy("process tracking")
set_audit_policy("system events")

def set_subcategory_audit_policy(subcategory):
    command = f'auditpol /set /subcategory:"{subcategory}" /success:enable /failure:enable'
    subprocess.run(command, shell=True, capture_output=True, text=True)

set_subcategory_audit_policy("Account Logon")
set_subcategory_audit_policy("account management")
set_subcategory_audit_policy("directory service access")
set_subcategory_audit_policy("logon events")
set_subcategory_audit_policy("object access")
set_subcategory_audit_policy("policy change")
set_subcategory_audit_policy("privilege use")
set_subcategory_audit_policy("process tracking")
set_subcategory_audit_policy("system events")

#System Audit
set_subcategory_audit_policy("Security System Extension")
set_subcategory_audit_policy("System Integrity")
set_subcategory_audit_policy("IPsec Driver")
set_subcategory_audit_policy("Other System Events")
set_subcategory_audit_policy("Security State Change")


#Logon/Logoff Audit
set_subcategory_audit_policy("Logon")
set_subcategory_audit_policy("Logoff")
set_subcategory_audit_policy("Account Lockout")
set_subcategory_audit_policy("IPsec Main Mode")
set_subcategory_audit_policy("IPsec Quick Mode")
set_subcategory_audit_policy("IPsec Extended Mode")
set_subcategory_audit_policy("Special Logon")
set_subcategory_audit_policy("Other Logon/Logoff Events")
set_subcategory_audit_policy("Network Policy Server")
set_subcategory_audit_policy("User / Device Claims")
set_subcategory_audit_policy("Group Membership")

#Object Access Audit
set_subcategory_audit_policy("File System")
set_subcategory_audit_policy("Registry")
set_subcategory_audit_policy("Kernel Object")
set_subcategory_audit_policy("SAM")
set_subcategory_audit_policy("Certification Services")
set_subcategory_audit_policy("Application Generated")
set_subcategory_audit_policy("Handle Manipulation")
set_subcategory_audit_policy("File Share")
set_subcategory_audit_policy("Filtering Platform Packet Drop")
set_subcategory_audit_policy("Filtering Platform Connection")
set_subcategory_audit_policy("Other Object Access Events")
set_subcategory_audit_policy("Detailed File Share")
set_subcategory_audit_policy("Removable Storage")
set_subcategory_audit_policy("Central Policy Staging")

#Detailed Tracking Audit
set_subcategory_audit_policy("Process Creation")
set_subcategory_audit_policy("Process Termination")
set_subcategory_audit_policy("DPAPI Activity")
set_subcategory_audit_policy("RPC Events")
set_subcategory_audit_policy("Plug and Play Events")
set_subcategory_audit_policy("Token Right Adjusted Events")

#Policy Change, No need to Audit Check Main

#Account Management, No need to Audit Check Main

#DS Access

set_subcategory_audit_policy("Directory Service Changes")
set_subcategory_audit_policy("Directory Service Replication")
set_subcategory_audit_policy("Detailed Directory Service Replication")

#Account Logon, No need to Audit Check Main


import os
os.system("auditpol.exe /get /category:*")



