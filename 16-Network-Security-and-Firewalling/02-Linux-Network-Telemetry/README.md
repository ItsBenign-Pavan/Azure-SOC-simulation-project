# Linux Network Telemetry

## Overview

This section focuses on collecting, monitoring, and analyzing Linux network security telemetry using UFW Firewall, Syslog, Azure Monitor Agent (AMA), and Microsoft Sentinel.

The objective is to understand how network security events generated on Linux systems can be ingested into a SIEM platform and leveraged for threat hunting, security monitoring, and incident investigation.

---

## Architecture

```text
Ubuntu Linux VM
        │
        ▼
UFW Firewall
        │
        ▼
Kernel Logs (LOG_KERN)
        │
        ▼
Syslog
        │
        ▼
Azure Monitor Agent (AMA)
        │
        ▼
Data Collection Rule (DCR)
        │
        ▼
Microsoft Sentinel
        │
        ▼
KQL Threat Hunting
```

---

## Learning Objectives

- Deploy and configure UFW Firewall
- Enable and validate Linux firewall logging
- Collect Syslog telemetry using Azure Monitor Agent
- Ingest Linux network telemetry into Microsoft Sentinel
- Investigate firewall allow, audit, and block events
- Perform threat hunting using KQL
- Troubleshoot Syslog ingestion issues

---

## Lab Workflow

### Phase 1 — UFW Firewall Deployment

- Installed and configured UFW
- Applied default deny inbound policy
- Allowed management ports
- Enabled firewall logging

### Phase 2 — Log Collection

- Validated UFW events in Syslog
- Configured Syslog collection through AMA
- Verified log ingestion into Sentinel

### Phase 3 — Blocked Traffic Analysis

- Generated blocked network connections
- Validated UFW BLOCK events
- Investigated events using KQL
- Performed threat hunting exercises

---

## Key Troubleshooting Performed

### Issue

UFW firewall events were visible on the Linux VM but were not appearing in Microsoft Sentinel.

### Investigation

Validation confirmed:

- UFW logging was enabled
- Events existed in `/var/log/syslog`
- Events existed in `/var/log/kern.log`
- Sentinel was receiving Syslog data

However, firewall events were still missing.

### Root Cause

The Data Collection Rule (DCR) Syslog configuration did not include:

```text
LOG_KERN
```

Since UFW generates firewall telemetry through the Linux kernel facility, these events were never collected by AMA.

### Resolution

Added:

```text
LOG_KERN
```

to the Syslog facilities within the Data Collection Rule.

### Result

Successful ingestion of:

```text
UFW ALLOW
UFW AUDIT
UFW BLOCK
```

events into Microsoft Sentinel.

---

## Module Navigation

| Module | Description |
|----------|-------------|
| [01-UFW-Firewall-Deployment](./01-UFW-Firewall-Deployment) | Deploy and configure UFW Firewall |
| [02-UFW-Log-Collection](./02-UFW-Log-Collection) | Collect Linux network telemetry using Syslog and AMA |
| [03-UFW-Blocked-Traffic-Analysis](./03-UFW-Blocked-Traffic-Analysis) | Analyze blocked traffic and perform threat hunting |

---

## Skills Demonstrated

- Linux Administration
- Firewall Management
- Syslog Analysis
- Azure Monitor Agent
- Data Collection Rules
- Microsoft Sentinel
- KQL Threat Hunting
- Security Monitoring
- Troubleshooting & Root Cause Analysis

---

## Next Section

➡️ Continue to **03-Windows-Network-Telemetry** to collect and analyze Windows firewall and network security telemetry within Microsoft Sentinel.
