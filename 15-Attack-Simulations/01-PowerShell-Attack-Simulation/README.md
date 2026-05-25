# 🚨 Remote PowerShell Payload Execution Simulation

This attack simulation demonstrates a realistic adversary workflow where a Linux attacker VM stages and remotely executes a suspicious PowerShell payload on a Windows victim VM.

The simulation was designed to generate:
- realistic attacker telemetry
- PowerShell Operational logs
- suspicious execution traces
- Sentinel detections
- incident generation workflows

This implementation demonstrates:
- attacker-to-victim payload delivery
- remote PowerShell execution
- suspicious PowerShell telemetry generation
- behavior-based detection engineering
- Microsoft Sentinel monitoring & investigation

---

# 🎯 Objective

The objective of this simulation was to emulate:
- attacker payload staging
- remote payload delivery
- suspicious PowerShell execution
- attacker artifact creation
- SOC detection workflows

without causing:
- malware execution
- persistence
- system compromise
- destructive behavior

---

# 🏗️ Lab Architecture

```text
Linux Attacker VM
↓
Suspicious PowerShell Payload Creation
↓
Payload Delivery via SCP
↓
Remote Execution via SSH
↓
Windows Victim VM
↓
PowerShell Operational Logs
↓
Microsoft Sentinel
↓
Analytics Rule Correlation
↓
Incident Generation
```

---

# 🧠 Attack Story

A suspicious PowerShell payload was created on the Linux attacker VM and transferred to the Windows victim machine using SCP over SSH.

The attacker then remotely executed the payload from the Linux machine using SSH remote execution.

The payload generated multiple suspicious PowerShell behaviors including:
- execution policy bypass
- encoded PowerShell execution
- hidden PowerShell execution
- suspicious folder creation
- PowerShell process spawning

These activities generated telemetry which was ingested into Microsoft Sentinel and correlated against custom PowerShell IOC watchlists.

---

# ⚔️ Cyber Kill Chain Mapping

| Kill Chain Phase | Activity |
|---|---|
| Reconnaissance | Internal VM discovery |
| Weaponization | Suspicious PowerShell payload creation |
| Delivery | SCP payload transfer to victim |
| Exploitation | Remote PowerShell execution |
| Installation | Suspicious folder creation |
| Command & Control | SSH remote command execution |
| Actions on Objectives | PowerShell telemetry generation |

---

# 🛡️ MITRE ATT&CK Mapping

| Technique ID | Technique Name |
|---|---|
| T1059.001 | PowerShell |
| T1021.004 | SSH |
| T1105 | Ingress Tool Transfer |
| T1059 | Command and Scripting Interpreter |
| T1562.001 | Impair Defenses (Execution Policy Bypass Simulation) |
| T1140 | Deobfuscate/Decode Files or Information |
| T1027 | Obfuscated/Compressed Files and Information |

---

# 🟥 Linux Attacker VM — Payload Creation

A suspicious PowerShell payload was created on the Linux attacker VM.

Directory used:

```text
~/AttackSimulation/
```

Payload name:

```text
Invoke-SuspiciousActivity.ps1
```

---

# 📄 Payload Content

```powershell
Write-Host "Initializing suspicious activity simulation..."

New-Item -Path "C:\Temp\SuspiciousFolder" -ItemType Directory -Force

powershell.exe -ExecutionPolicy Bypass
powershell.exe -NoProfile
powershell.exe -EncodedCommand SGVsbG8=
powershell.exe -WindowStyle Hidden

Write-Host "Simulation completed."
```

---

# 📸 Screenshot Section

Add screenshots for:
- Linux attacker VM
- PowerShell payload creation
- payload content

Suggested filenames:

```text
01-attacker-payload-creation.png
02-payload-content.png
```

---

# 🚀 Payload Delivery

The payload was transferred from the Linux attacker VM to the Windows victim machine using SCP over SSH.

Transfer destination:

```text
C:\Users\Pavan\Desktop\
```

Example transfer command:

```bash
scp ~/AttackSimulation/Invoke-SuspiciousActivity.ps1 USERNAME@WINDOWS_PRIVATE_IP:C:/Users/Pavan/Desktop/
```

This simulated:
- attacker staging
- remote payload delivery
- lateral movement behavior

---

# 📸 Screenshot Section

Add screenshots for:
- SCP transfer
- attacker terminal
- successful payload delivery

Suggested filename:

```text
03-payload-transfer.png
```

---

# 🚀 Remote Payload Execution

The payload was remotely executed from the Linux attacker VM using SSH remote command execution.

Example execution command:

```bash
ssh USERNAME@WINDOWS_PRIVATE_IP "powershell.exe -ExecutionPolicy Bypass -File C:/Users/Pavan/Desktop/Invoke-SuspiciousActivity.ps1"
```

This simulated:
- remote attacker execution
- PowerShell abuse
- suspicious command execution
- attacker-controlled payload launch

---

# 📸 Screenshot Section

Add screenshots for:
- remote execution command
- Linux attacker terminal
- successful execution output

Suggested filename:

```text
04-remote-payload-execution.png
```

---

# 🟦 Victim Machine Activity

The payload execution generated:
- suspicious PowerShell processes
- PowerShell Operational logs
- suspicious folder creation
- encoded PowerShell execution traces
- execution policy bypass telemetry

Artifact created:

```text
C:\Temp\SuspiciousFolder
```

---

# 📸 Screenshot Section

Add screenshots for:
- suspicious folder creation
- payload presence on victim desktop
- PowerShell execution activity

Suggested filenames:

```text
05-payload-on-victim.png
06-suspicious-folder-created.png
```

---

# 📜 PowerShell Operational Logging

PowerShell Operational logs captured:
- execution traces
- encoded command execution
- suspicious PowerShell arguments
- hidden PowerShell activity

Log source:

```text
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ PowerShell
→ Operational
```

---

# 📸 Screenshot Section

Add screenshots for:
- Event Viewer PowerShell logs
- warning/information events
- suspicious PowerShell entries

Suggested filename:

```text
07-powershell-operational-logs.png
```

---

# 🔍 Sentinel Telemetry Validation

The following KQL query was used to validate PowerShell telemetry ingestion:

```kusto
Event
| where EventLog has "PowerShell"
| sort by TimeGenerated desc
```

This confirmed:
- successful telemetry ingestion
- PowerShell Operational visibility
- suspicious execution traces

---

# 📸 Screenshot Section

Add screenshots for:
- Sentinel query results
- suspicious PowerShell events

Suggested filename:

```text
08-sentinel-powershell-query.png
```

---

# 🚨 Detection Correlation

Microsoft Sentinel analytics rules correlated suspicious PowerShell activity against custom IOC watchlists.

Watchlist used:

```text
suspicious_powershell_watchlist
```

Detection query:

```kusto
let suspiciousPatterns = (
_GetWatchlist('suspicious_powershell_watchlist')
| project Pattern
);

Event
| where EventLog has "PowerShell"
| where RenderedDescription has_any (suspiciousPatterns)
| sort by TimeGenerated desc
```

---

# 🚨 Incident Generation

The suspicious PowerShell telemetry successfully triggered Microsoft Sentinel analytics rules and generated incidents automatically.

The generated incidents demonstrated:
- behavior-based detection engineering
- PowerShell abuse monitoring
- IOC correlation
- automated SOC workflows

---

# 📸 Screenshot Section

Add screenshots for:
- Sentinel incident
- incident overview
- entities
- investigation graph

Suggested filename:

```text
10-generated-incident.png
```

---

# 🧠 Key Learning Outcomes

This simulation demonstrated:
- attacker payload staging
- SCP-based payload delivery
- SSH remote execution
- PowerShell abuse simulation
- telemetry generation
- behavior-based detection engineering
- Sentinel analytics workflows
- SOC investigation readiness
- attack chain visibility

---

# 🎯 Final Detection Workflow

```text
Linux Attacker VM
↓
Suspicious Payload Creation
↓
Payload Delivery via SCP
↓
Remote Execution via SSH
↓
Windows Victim VM
↓
PowerShell Operational Logs
↓
Microsoft Sentinel
↓
Watchlist Correlation
↓
Analytics Rule Trigger
↓
Incident Generation
```

---

# ⚠️ Disclaimer

This simulation was created strictly for:
- educational purposes
- SOC skill development
- detection engineering practice
- isolated Azure lab environments

All PowerShell payloads and suspicious commands used in this simulation were intentionally harmless and designed only to generate telemetry safely without compromising the victim system.
