# 🚨 Suspicious IP Watchlist Detection & IOC Correlation

This section demonstrates implementation of custom IOC-based threat detection using Microsoft Sentinel Watchlists, KQL correlation, and Analytics Rules.

A custom suspicious IP watchlist was created and later used to detect authentication activity originating from the attacker Linux VM.

This implementation demonstrates:
- IOC ingestion
- watchlist-driven detection engineering
- KQL-based IOC correlation
- incident generation using custom threat intelligence
- attacker-to-victim simulation workflow

---

# 🧠 Objective

The goal of this implementation was to:
- create a custom suspicious IP repository
- correlate SecurityEvent logs against IOC data
- simulate attacker authentication activity
- trigger Microsoft Sentinel incidents automatically

---

# 🖥️ Linux Attacker VM GUI Configuration

Initially, the Linux VM was terminal-only (headless).  
To simulate a realistic attacker workstation environment, a graphical desktop interface was configured using XFCE and XRDP.

This allowed:
- GUI-based RDP operations
- remote desktop access into Linux VM
- attacker workstation simulation
- generation of authentication telemetry from attacker VM public IP

---

# 🚀 XFCE & XRDP Installation

## Step 1 — Update Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Step 2 — Install XFCE Desktop

```bash
sudo apt install xfce4 xfce4-goodies -y
```

---

## Step 3 — Install XRDP

```bash
sudo apt install xrdp -y
```

---

## Step 4 — Configure XFCE Session

```bash
echo xfce4-session > ~/.xsession
```

---

## Step 5 — Add XRDP User To SSL Group

```bash
sudo adduser xrdp ssl-cert
```

---

## Step 6 — Restart & Enable XRDP

```bash
sudo systemctl restart xrdp
sudo systemctl enable xrdp
```

---

# 🔐 NSG Configuration

Inbound NSG rule was configured to allow RDP access (TCP 3389) only from the administrator public IP.

This enabled secure remote desktop connectivity to the Linux attacker VM.

---

# 🚀 Watchlist Creation

A custom suspicious IP watchlist was created inside Microsoft Sentinel.

The watchlist contained:
- malicious IP examples
- attacker Linux VM public IP
- IOC metadata
- threat severity information

---

# 📄 Watchlist CSV Structure

```csv
IPAddress,Description,ThreatLevel
185.220.101.1,Tor Exit Node,High
45.155.205.233,Suspicious Scanner,Medium
103.235.46.172,Known Malicious Activity,High
91.214.124.84,Brute Force Source,High
**.**.**.**,Linux Attacker VM,High
```

---

# 📸 Screenshot Section

Add screenshots for:
- watchlist creation
- uploaded CSV
- watchlist overview page

---

# 🔍 Watchlist Validation Using KQL

The following query was used to validate successful watchlist ingestion:

```kusto
_GetWatchlist('suspicious_ip_watchlist')
```

This verified:
- successful IOC ingestion
- correct alias configuration
- accessible watchlist records

---

# 📸 Screenshot Section

Add screenshots for:
- successful watchlist KQL query results

---

# 🚀 Analytics Rule Creation

A scheduled analytics rule was created to correlate SecurityEvent logs against suspicious IPs stored in the watchlist.

The rule detects:
- authentication activity
- remote logon events
- IOC matches originating from suspicious IP addresses

---

# 🔍 Detection Query

```kusto
let suspiciousIPs = (
_GetWatchlist('suspicious_ip_watchlist')
| project IPAddress
);

SecurityEvent
| where IpAddress in (suspiciousIPs)
| project
    TimeGenerated,
    Computer,
    Account,
    IpAddress,
    Activity
| sort by TimeGenerated desc
```

---

# ⚙️ Rule Configuration

| Setting | Value |
|---|---|
| Rule Type | Scheduled Query Rule |
| Severity | High |
| Query Frequency | 5 Minutes |
| Lookup Data | Last 5 Minutes |
| Incident Creation | Enabled |
| Alert Grouping | Disabled |

---

# 🧩 Entity Mapping

Entity mapping was configured for:
- IP Address entity

This enables:
- investigation graph integration
- entity-centric investigation
- IOC enrichment inside incidents

---

# 📸 Screenshot Section

Add screenshots for:
- analytics rule configuration
- detection query
- entity mapping configuration
- successful rule creation

---

# 🚨 Attack Simulation & IOC Correlation

The Linux attacker VM public IP was intentionally added into the suspicious IP watchlist.

Authentication activity was then generated from the attacker VM toward the Windows victim VM using:
- RDP logon attempts
- SSH connectivity attempts

This generated SecurityEvent logs containing:
- attacker IP address
- authentication telemetry
- remote logon activity

---

# 📸 Screenshot Section

Add screenshots for:
- successful RDP connection from Linux VM
- attack simulation activity
- Windows VM authentication events

---

# 🔍 Log Validation

The following KQL query was used to validate IOC correlation telemetry:

```kusto
SecurityEvent
| where IpAddress == "20.207.203.163"
| sort by TimeGenerated desc
```

This confirmed:
- successful log ingestion
- attacker IP visibility
- IOC telemetry generation

---

# 📸 Screenshot Section

Add screenshots for:
- SecurityEvent query results
- attacker IP visibility inside logs

---

# 🚨 Incident Generation

After log ingestion and rule execution:
- Microsoft Sentinel successfully correlated the suspicious IP
- analytics rule triggered automatically
- high-severity incident was generated

This demonstrated:
- watchlist-driven detection
- IOC-based analytics
- end-to-end threat correlation workflow

---

# 📸 Screenshot Section

Add screenshots for:
- generated Sentinel incident
- incident overview
- incident entities
- incident investigation graph

---

# 🎯 Key Learning Outcomes

This implementation demonstrated:
- Microsoft Sentinel Watchlists
- IOC ingestion workflows
- KQL-based IOC correlation
- custom analytics rule development
- entity mapping
- authentication telemetry analysis
- attacker-to-victim simulation
- incident generation workflows
- detection engineering concepts
- SOC investigation workflows

---

# 🧠 Final Architecture

```text
Linux Attacker VM
↓
Authentication Activity
↓
SecurityEvent Log Generation
↓
Microsoft Sentinel Ingestion
↓
Watchlist IOC Correlation
↓
Analytics Rule Trigger
↓
Incident Creation
```

This implementation transformed the lab environment into a realistic SOC detection engineering workflow using custom threat intelligence and attacker simulation.
