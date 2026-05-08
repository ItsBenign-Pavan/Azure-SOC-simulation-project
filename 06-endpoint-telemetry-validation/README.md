# Endpoint Telemetry Validation

## 🎯 Objective
To validate successful log ingestion from Windows and Linux Virtual Machines into Microsoft Sentinel using Azure Monitor Agent (AMA) and Data Collection Rules (DCR).

This step confirms that endpoint telemetry is successfully reaching the Log Analytics Workspace and is available for security monitoring and analysis.

---

## 🔍 Validation Approach

The validation process included:

- Verifying endpoint connectivity using Heartbeat logs
- Confirming Windows Security Event ingestion
- Confirming Linux Syslog ingestion
- Reviewing data freshness and telemetry availability
- Validating cross-platform monitoring capabilities within Microsoft Sentinel

---

## ❤️ Heartbeat Validation

### KQL Query
```kql
Heartbeat
| summarize LastHeartbeat=max(TimeGenerated) by Computer
```

#### 📸 Screenshot
<img src="screenshots/heartbeat-validation.png" width="80%"/>

#### 📌 Purpose
To verify that monitored endpoints are actively communicating with the Log Analytics Workspace.

#### 📌 Observation
Heartbeat logs are successfully received from both Windows and Linux Virtual Machines, confirming healthy agent connectivity.

---

## 🖥️ Windows Security Events Validation

### KQL Query
```kql
SecurityEvent
| summarize count() by EventID
| sort by count_ desc
```

#### 📸 Screenshot
<img src="screenshots/windows-securityevent-validation.png" width="80%"/>

#### 📌 Purpose
To validate ingestion of Windows Security Events from the Windows Server endpoint.

#### 📌 Observation
Security events are successfully visible within Microsoft Sentinel, confirming proper Windows event collection through AMA and DCR configuration.

---

## 🐧 Linux Syslog Validation

### KQL Query
```kql
Syslog
| summarize count() by Facility
| sort by count_ desc
```

#### 📸 Screenshot
<img src="screenshots/linux-syslog-validation.png" width="80%"/>

#### 📌 Purpose
To validate ingestion of Linux Syslog events from the Ubuntu Virtual Machine.

#### 📌 Observation
Linux system logs are successfully ingested into Sentinel, confirming operational Syslog collection from the Linux endpoint.

---

## 🕒 Data Freshness Validation

### KQL Query
```kql
union SecurityEvent, Syslog
| summarize LatestLog=max(TimeGenerated) by Type
```

#### 📸 Screenshot
<img src="screenshots/data-freshness-validation.png" width="80%"/>

#### 📌 Purpose
To verify that telemetry data is being ingested in near real-time from monitored endpoints.

#### 📌 Observation
Recent timestamps confirm continuous and active telemetry ingestion into the Log Analytics Workspace.

---

## 📂 Observed Tables

| Table Name     | Description                                      |
|----------------|--------------------------------------------------|
| SecurityEvent  | Windows authentication and security events       |
| Syslog         | Linux system and authentication logs             |
| Heartbeat      | Endpoint connectivity and AMA health monitoring  |

---

## 🌐 Cross-Platform Monitoring

Successfully validated telemetry ingestion from both:
- Windows-based endpoints
- Linux-based endpoints

This establishes centralized security visibility across heterogeneous operating systems within Microsoft Sentinel.

---

## ⚠️ Observations

- Azure Monitor Agent (AMA) successfully forwarded logs from both operating systems
- Data Collection Rules controlled telemetry ingestion behavior
- Windows and Linux endpoints generated distinct telemetry types
- Heartbeat logs proved useful for validating endpoint connectivity status

---

## 🔐 Security Relevance

- Windows Security Events provide visibility into authentication activity and system events
- Linux Syslog events support monitoring of system-level and authentication-related activity
- Centralized telemetry collection enables correlation, threat hunting, and detection engineering within Microsoft Sentinel

---

## ✅ Outcome

- Successfully validated endpoint telemetry ingestion from Windows and Linux Virtual Machines
- Confirmed operational status of AMA and DCR configurations
- Verified visibility of SecurityEvent, Syslog, and Heartbeat tables within Microsoft Sentinel
- Established readiness for attack simulation and detection use cases

---

## 🔗 Next Step

Proceeding to generate authentication-based attack scenarios and analyze resulting security events within Microsoft Sentinel.
