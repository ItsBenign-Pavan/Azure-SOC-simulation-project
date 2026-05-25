# Reverse Shell / C2 Callback Simulation Detection

## Overview

This attack simulation demonstrates a realistic reverse shell / command-and-control (C2) callback scenario using a Linux attacker VM and Windows victim VM inside an Azure environment. The objective was to simulate suspicious outbound communication behavior and detect it using Sysmon, Azure Monitor Agent (AMA), Microsoft Sentinel analytics rules, and watchlist enrichment.

This simulation focuses on network-based adversary behavior rather than simple PowerShell execution telemetry.

---

# Lab Architecture

| Component | Purpose |
|---|---|
| Linux VM | Simulated attacker / C2 listener |
| Windows Server VM | Victim machine |
| Sysmon | Advanced endpoint telemetry |
| AMA | Log ingestion into Sentinel |
| Microsoft Sentinel | Detection & incident generation |
| Watchlist | Suspicious infrastructure enrichment |

---

# Attack Scenario

The Linux attacker VM was configured to behave like a command-and-control (C2) server by starting a TCP listener using Netcat.

The Windows victim machine initiated an outbound TCP callback connection to the attacker infrastructure using PowerShell TCP client functionality.

This generated:
- Sysmon Event ID 3 (Network Connection)
- Suspicious outbound communication telemetry
- PowerShell network activity
- Sentinel incident generation

---

# MITRE ATT&CK Mapping

| Technique | ID |
|---|---|
| PowerShell | T1059.001 |
| Command and Scripting Interpreter | T1059 |
| Application Layer Protocol | T1071 |
| Ingress Tool Transfer | T1105 |

---

# Step 1 — Sysmon Deployment

Sysmon was installed on the Windows victim VM to provide enhanced endpoint telemetry.

## Telemetry Enabled
- Process Creation
- Network Connections
- Parent-Child Relationships
- Process Hashes
- PowerShell Activity

## Sysmon Configuration Used
SwiftOnSecurity Sysmon Configuration:
https://github.com/SwiftOnSecurity/sysmon-config

---

# Step 2 — AMA & Sentinel Integration

Azure Monitor Agent (AMA) was configured to ingest Sysmon Operational logs into Microsoft Sentinel.

## DCR XPath Query

```xpath
Microsoft-Windows-Sysmon/Operational!*
```

---

# Step 3 — Threat Intelligence Watchlist

A watchlist was created to simulate suspicious attacker infrastructure.

## Watchlist Name

```text
suspicious_c2_ips
```

## Sample CSV

```csv
IPAddress,Description
10.0.0.5,Internal Attacker C2 Listener
10.0.0.8,Simulated Rogue Admin Workstation
10.0.0.12,Potential Lateral Movement Host
172.16.5.20,Untrusted Internal Pivot Node
192.168.56.101,Lab Persistence Simulation Node
```

---

# Step 4 — Attacker Listener Setup

A fake C2 listener was started on the Linux attacker VM using Netcat.

## Command

```bash
nc -lvnp 4444
```

## Purpose

This simulated:
- Reverse shell listener
- Command-and-control infrastructure
- Attacker callback server

---

# Step 5 — Victim Callback Execution

The Windows victim VM initiated an outbound TCP callback to the attacker infrastructure.

## PowerShell Callback Command

```powershell
$client = New-Object System.Net.Sockets.TCPClient("10.0.0.5",4444)
```

## Result

The Linux attacker VM successfully received the callback connection.

This generated:
- Sysmon Event ID 3
- Suspicious outbound PowerShell network activity
- Sentinel telemetry

---

# Step 6 — Sysmon Telemetry Validation

## Validation Query

```kusto
Event
| where EventLog == "Microsoft-Windows-Sysmon/Operational"
| where EventID == 3
| extend DestinationIp = extract(@"DestinationIp:\s+([^\r\n]+)", 1, RenderedDescription)
| extend DestinationPort = extract(@"DestinationPort:\s+([^\r\n]+)", 1, RenderedDescription)
| extend Image = extract(@"Image:\s+([^\r\n]+)", 1, RenderedDescription)
| project TimeGenerated, Computer, Image, DestinationIp, DestinationPort
| sort by TimeGenerated desc
```

## Observed Indicators

- Destination IP: `10.0.0.5`
- Destination Port: `4444`
- Process: `powershell.exe`

---

# Step 7 — Sentinel Detection Rule

## Rule Name

```text
Potential Reverse Shell / C2 Callback Detection
```

## Detection Logic

This analytics rule detects:
- Suspicious scripting engines
- Outbound network communication
- Uncommon destination ports
- Connections to suspicious infrastructure

## Detection Query

```kusto
let suspiciousIPs = (
_GetWatchlist('suspicious_c2_ips')
| project IPAddress
);

let suspiciousProcesses = dynamic([
    "powershell.exe",
    "cmd.exe",
    "wscript.exe",
    "cscript.exe",
    "mshta.exe",
    "python.exe",
    "nc.exe",
    "curl.exe",
    "certutil.exe"
]);

Event
| where EventLog == "Microsoft-Windows-Sysmon/Operational"
| where EventID == 3
| extend DestinationIp = extract(@"DestinationIp:\s+([^\r\n]+)", 1, RenderedDescription)
| extend DestinationPort = extract(@"DestinationPort:\s+([^\r\n]+)", 1, RenderedDescription)
| extend Image = extract(@"Image:\s+([^\r\n]+)", 1, RenderedDescription)
| where Image has_any (suspiciousProcesses)
| where DestinationIp in (suspiciousIPs)
| where DestinationPort !in ("80","443","53")
| project TimeGenerated, Computer, Image, DestinationIp, DestinationPort
| sort by TimeGenerated desc
```

---

# Step 8 — Incident Generation

Microsoft Sentinel successfully generated an incident after detecting suspicious outbound callback behavior.

## Detection Highlights

- Outbound callback detected
- Suspicious PowerShell network activity
- Connection to known suspicious infrastructure
- Behavioral + IOC-based detection logic

---

# Detection Engineering Concepts Demonstrated

- Sysmon telemetry engineering
- AMA log ingestion
- KQL parsing & field extraction
- Behavioral detection logic
- IOC enrichment using watchlists
- Reverse shell style network detection
- Sentinel incident generation
- MITRE ATT&CK mapping

---

# Screenshots

## Suggested Screenshots

### Linux Attacker VM
- Netcat listener active
- Successful callback received

### Windows Victim VM
- PowerShell callback execution

### Sentinel Logs
- Sysmon Event ID 3 telemetry
- Parsed destination IP and port

### Sentinel Analytics Rule
- Detection query
- MITRE ATT&CK mapping

### Sentinel Incident
- Generated incident
- Alert details
- Entities

---

# Outcome

This simulation successfully demonstrated a realistic reverse shell / command-and-control callback workflow using safe adversary emulation techniques.

The project validated:
- Advanced endpoint telemetry collection
- Network-based attack detection
- Behavioral analytics engineering
- Threat intelligence enrichment
- Automated incident generation in Microsoft Sentinel

This simulation significantly enhanced the SOC lab by introducing enterprise-style detection engineering and network telemetry analysis capabilities.
