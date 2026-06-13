# Windows Firewall Log Collection

## Overview

This module focuses on collecting Windows Firewall telemetry and validating its visibility through local firewall logs and Microsoft Sentinel.

The objective is to establish an end-to-end telemetry pipeline that enables monitoring of Windows network activity and firewall-related events.

---

## Objectives

- Validate Windows Firewall log generation
- Verify local firewall log creation
- Confirm AMA collection
- Validate Microsoft Sentinel ingestion
- Establish visibility into Windows network activity

---

## Log Verification

### Firewall Log Location

```text
C:\Windows\System32\LogFiles\Firewall\pfirewall.log
```

### Verify Firewall Log Generation

```powershell
Get-Content "C:\Windows\System32\LogFiles\Firewall\pfirewall.log" -Tail 20
```

Expected Result:

```text
ALLOW
DROP
TCP
UDP
```

entries recorded in the firewall log.

---

## Sentinel Validation

### Verify Windows Firewall Security Events

```kusto
SecurityEvent
| where EventID in (5152,5156,5157)
| order by TimeGenerated desc
| take 20
```

---

## Telemetry Flow

```text
Windows Defender Firewall
            │
            ▼
Windows Event Logs
            │
            ▼
Azure Monitor Agent
            │
            ▼
Microsoft Sentinel
```

---

## Validation Results

Successfully verified:

- Firewall log generation
- Local firewall event recording
- AMA log collection
- Sentinel ingestion
- Security event visibility

---

## Screenshots

### Windows Firewall Log Validation

<img src="02-windows-firewall-log-validation.png" width="100%">

---

### Windows Firewall Events in Sentinel

<img src="05-sentinel-firewall-events.png" width="100%">

---

## Skills Demonstrated

- Windows Logging
- Windows Firewall Monitoring
- Azure Monitor Agent
- Microsoft Sentinel
- Security Event Collection
- Endpoint Telemetry Analysis
