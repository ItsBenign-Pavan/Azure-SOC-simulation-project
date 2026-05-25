# 🔥 Reverse Shell / C2 Callback Detection Simulation

> Simulating realistic command-and-control (C2) callback behavior using Sysmon, Microsoft Sentinel, AMA, and behavioral analytics engineering.

---

# 🎯 Objective

This project demonstrates a realistic reverse shell / command-and-control (C2) callback simulation using:

- Linux Attacker VM
- Windows Victim VM
- Sysmon Endpoint Telemetry
- Azure Monitor Agent (AMA)
- Microsoft Sentinel
- Behavioral + IOC-Based Detection Logic

The objective was to simulate suspicious outbound callback behavior and detect it using advanced telemetry engineering and Microsoft Sentinel analytics rules.

---

# 🏗️ Lab Architecture

```text
Linux Attacker VM
        ↓
Fake C2 Listener (Netcat)
        ↓
Windows Victim Callback
        ↓
Sysmon Event ID 3
        ↓
AMA Ingestion
        ↓
Microsoft Sentinel
        ↓
Analytics Rule Detection
        ↓
Incident Creation
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Microsoft Sentinel | SIEM & Incident Detection |
| Sysmon | Advanced Endpoint Telemetry |
| AMA | Log Ingestion |
| Netcat | Simulated C2 Listener |
| KQL | Detection Engineering |
| Watchlists | IOC Enrichment |
| PowerShell | Victim Callback Execution |

---

# ⚔️ Attack Simulation Overview

This simulation focused on:
- Suspicious outbound network callbacks
- Behavioral detection engineering
- Reverse-shell-like activity
- Network telemetry analysis
- Automated incident generation

Unlike simple PowerShell abuse simulations, this project introduced:
- Network telemetry
- IOC enrichment
- Behavioral correlation
- C2-style communication

---

# 🔍 Step 1 — Sysmon Deployment

Sysmon was installed on the Windows victim VM to enable advanced telemetry collection.

## Enabled Telemetry

- Process Creation
- Network Connections
- Parent-Child Process Chains
- Process Hashes
- PowerShell Visibility

## Sysmon Configuration Used

SwiftOnSecurity Sysmon Config:

```text
https://github.com/SwiftOnSecurity/sysmon-config
```

---

# ☁️ Step 2 — AMA + Sentinel Integration

Azure Monitor Agent (AMA) was configured to ingest Sysmon Operational logs into Microsoft Sentinel.

## XPath Query Used

```xpath
Microsoft-Windows-Sysmon/Operational!*
```

---

# 🧠 Step 3 — Threat Intelligence Watchlist

A custom watchlist was created to simulate suspicious attacker infrastructure.

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

# 🐧 Step 4 — Attacker Listener Setup

The Linux VM was configured to behave like attacker-controlled C2 infrastructure using Netcat.

## Command Used

```bash
nc -lvnp 4444
```

## Purpose

This simulated:
- Reverse shell listener
- Attacker-controlled infrastructure
- C2 callback server

---

# 🪟 Step 5 — Victim Callback Execution

The Windows victim VM initiated an outbound TCP callback connection to the Linux attacker VM.

## PowerShell Callback

```powershell
$client = New-Object System.Net.Sockets.TCPClient("10.0.0.5",4444)
```

---

# 📡 Result

The Linux attacker VM successfully received the callback connection.

This generated:
- Sysmon Event ID 3
- Suspicious outbound PowerShell network activity
- Sentinel telemetry
- Incident creation

---

# 🔎 Step 6 — Sysmon Telemetry Validation

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

| Indicator | Value |
|---|---|
| Destination IP | `10.0.0.5` |
| Destination Port | `4444` |
| Process | `powershell.exe` |

---

# 🚨 Step 7 — Sentinel Detection Rule

## Rule Name

```text
Potential Reverse Shell / C2 Callback Detection
```

## Detection Logic

The analytics rule detects:
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

# 🧬 MITRE ATT&CK Mapping

| Technique | ID |
|---|---|
| PowerShell | T1059.001 |
| Command and Scripting Interpreter | T1059 |
| Application Layer Protocol | T1071 |
| Ingress Tool Transfer | T1105 |

---

# 🚨 Step 8 — Incident Generation

Microsoft Sentinel successfully generated an incident after detecting suspicious outbound callback behavior.

## Detection Highlights

- Suspicious outbound callback detected
- PowerShell network communication observed
- Connection to suspicious infrastructure identified
- Behavioral + IOC-based detection logic triggered

---

# 📸 Screenshots

## Linux Attacker VM
- [ ] Netcat listener active
- [ ] Successful callback received

## Windows Victim VM
- [ ] PowerShell callback execution

## Sentinel Logs
- [ ] Sysmon Event ID 3 telemetry
- [ ] Parsed destination IP & port

## Sentinel Incident
- [ ] Generated incident
- [ ] Alert details
- [ ] Entities

## Analytics Rule
- [ ] Detection query
- [ ] MITRE ATT&CK mapping

---

# 🧠 Detection Engineering Concepts Demonstrated

- Sysmon telemetry engineering
- AMA log ingestion
- KQL field extraction & parsing
- Behavioral analytics engineering
- IOC enrichment using watchlists
- Reverse shell style network detection
- Automated incident generation
- MITRE ATT&CK mapping

---

# 🎯 Outcome

This project successfully demonstrated a realistic reverse shell / command-and-control callback workflow using safe adversary emulation techniques.

The simulation validated:
- Advanced endpoint telemetry collection
- Network-based attack detection
- Behavioral analytics engineering
- Threat intelligence enrichment
- Automated incident generation in Microsoft Sentinel

---

# 🚀 Key Takeaway

This simulation significantly upgraded the SOC lab from:

```text
basic log analysis
```

to:

```text
realistic detection engineering & adversary emulation
```

using enterprise-style telemetry and network-based threat detection workflows.
