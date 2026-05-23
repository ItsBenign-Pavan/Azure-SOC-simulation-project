# 🚨 Microsoft Sentinel Watchlists & Detection Engineering

This folder contains hands-on implementations of custom watchlists, IOC correlation, analytics rule engineering, and behavior-based detections using Microsoft Sentinel.

The implementations demonstrate:
- custom IOC watchlists
- KQL-based correlation
- attack simulation workflows
- PowerShell behavior monitoring
- authentication telemetry detection
- incident generation using Sentinel analytics rules

The detections were built and validated using:
- Windows victim VM
- Linux attacker VM
- Azure Monitor Agent (AMA)
- Microsoft Sentinel
- Log Analytics Workspace
- PowerShell Operational Logs

---

# 📂 Folder Navigation

## 1️⃣ Suspicious IP Watchlist Detection

Demonstrates:
- suspicious IP IOC ingestion
- Linux attacker VM simulation
- authentication telemetry correlation
- Sentinel analytics rule creation
- incident generation workflows

📄 [01-Suspicious-IP-Watchlist-Detection.md](01-Suspicious-IP-Watchlist-Detection.md)

---

## 2️⃣ Suspicious PowerShell Behavior Detection

Demonstrates:
- PowerShell Operational logging
- suspicious PowerShell execution monitoring
- behavior-based threat detection
- custom PowerShell IOC watchlists
- KQL-based correlation
- Sentinel incident generation

📄 [02-Suspicious-PowerShell-Behavior-Detection.md](02-Suspicious-PowerShell-Behavior-Detection.md)

---

# 📁 Supporting Files

## Suspicious PowerShell Watchlist CSV

Custom IOC watchlist used for:
- suspicious PowerShell pattern matching
- analytics rule correlation
- behavior-based detections

📄 [suspicious-powershell-watchlist.csv](suspicious-powershell-watchlist.csv)

---

# 🧠 Detection Engineering Concepts Covered

- Watchlist Engineering
- IOC Correlation
- KQL Querying
- PowerShell Operational Telemetry
- Authentication Monitoring
- Analytics Rule Development
- Sentinel Incident Generation
- Attack Simulation
- Security Event Analysis
- Behavior-Based Detection
- Threat Hunting Foundations

---

# 🛡️ Detection Workflow

```text
Attack Simulation
↓
Telemetry Generation
↓
Azure Monitor Agent (AMA)
↓
Microsoft Sentinel Ingestion
↓
Watchlist Correlation
↓
Analytics Rule Trigger
↓
Incident Creation
```

---

# ⚠️ Disclaimer

All attack simulations and PowerShell commands used in this project were:
- intentionally harmless
- executed in isolated Azure lab infrastructure
- used strictly for SOC learning and detection engineering practice
