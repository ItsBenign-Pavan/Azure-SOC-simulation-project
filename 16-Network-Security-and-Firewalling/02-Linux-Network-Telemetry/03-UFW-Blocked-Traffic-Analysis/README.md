# UFW Blocked Traffic Analysis

## Overview

This module focuses on generating firewall block events, validating their ingestion into Microsoft Sentinel, and performing security investigations using Kusto Query Language (KQL).

The objective is to simulate unauthorized network activity, observe firewall enforcement, and analyze security telemetry from a SOC analyst perspective.

---

## Objectives

- Generate blocked network traffic
- Validate UFW BLOCK events
- Verify Sentinel ingestion
- Investigate firewall telemetry
- Perform KQL-based threat hunting
- Troubleshoot log collection issues

---

## Attack Simulation

Blocked traffic was intentionally generated from an external system targeting ports that were not allowed through the Linux firewall.

### Traffic Generation

```powershell
Test-NetConnection <Linux-VM-IP> -Port 4444
```

Result:

```text
TcpTestSucceeded : False
```

---

## Local Validation

### Verify UFW Block Events

```bash
sudo grep "UFW BLOCK" /var/log/syslog
```

### Verify Kernel Logs

```bash
sudo tail -100 /var/log/kern.log | grep UFW
```

Example Event:

```text
kernel: [UFW BLOCK]
SRC=40.119.76.8
DST=10.0.0.5
PROTO=TCP
```

---

## Sentinel Validation

### Verify Firewall Block Events

```kusto
Syslog
| where ProcessName == "kernel"
| where SyslogMessage contains "UFW BLOCK"
| order by TimeGenerated desc
```

---

## Threat Hunting Query

```kusto
Syslog
| where ProcessName == "kernel"
| where SyslogMessage contains "UFW BLOCK"
| project TimeGenerated, Computer, SyslogMessage
| order by TimeGenerated desc
```

---

## Troubleshooting Performed

### Issue

UFW firewall events were successfully generated on the Linux VM but were not visible inside Microsoft Sentinel.

### Investigation

Validation confirmed:

- UFW logging enabled
- Events present in `/var/log/syslog`
- Events present in `/var/log/kern.log`
- Sentinel receiving Syslog telemetry

However, firewall events were missing.

### Root Cause

The Data Collection Rule (DCR) Syslog configuration did not include:

```text
LOG_KERN
```

UFW generates firewall telemetry through the Linux kernel logging facility.

Without collecting the kernel facility, Sentinel could not receive firewall events.

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

## Screenshots

### UFW Block Event Generated

<img src="04-ufw-blocked-traffic.png" width="100%">

---

### Firewall Block Event Ingested into Sentinel

<img src="05-sentinel-ufw-block-events.png" width="100%">

---

### KQL Threat Hunting

<img src="06-kql-ufw-hunting-query.png" width="100%">

---

## Security Findings

- Unauthorized connection attempts were successfully blocked.
- Firewall telemetry was captured and retained.
- Source IP addresses were recorded.
- Network activity was searchable using KQL.
- Sentinel provided centralized visibility into Linux firewall activity.

---

## Skills Demonstrated

- Linux Firewall Analysis
- Threat Hunting
- Network Security Monitoring
- KQL Investigation
- Microsoft Sentinel
- Data Collection Rules
- Syslog Analysis
- Root Cause Analysis
- Security Troubleshooting
