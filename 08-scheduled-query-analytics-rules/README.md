# 🚨 Scheduled Query Analytics Rules

## 📌 Objective

The objective of this milestone was to understand and configure **Scheduled Query Analytics Rules** in Microsoft Sentinel using KQL-based detections.

This milestone focused specifically on creating analytics rules that continuously evaluate ingested logs at scheduled intervals to identify suspicious activities and security-related events.

The rules were configured using telemetry from:

- Windows Security Events
- Syslog
- Custom Telemetry Logs

---

# 🏗️ Scheduled Query Rule Workflow

```text
Ingested Logs
      ↓
KQL Query
      ↓
Scheduled Query Analytics Rule
      ↓
Rule Evaluation
      ↓
Detection Logic Validation
```

---

# ⚙️ Scheduled Query Rule Configuration

Analytics Rules were created using the **Scheduled Query Rule** template available in Microsoft Sentinel.

### Configured Parameters

| Setting | Purpose |
|---|---|
| Query Scheduling | Defines execution interval |
| Lookup Data Range | Defines query search window |
| Trigger Threshold | Defines detection condition |
| Severity | Detection prioritization |
| MITRE ATT&CK Mapping | Threat classification |
| Entity Mapping | Maps users/IPs/hosts |

---

# 📸 Scheduled Query Rules Overview

_Add screenshot here_

```md
![Scheduled Query Rules](screenshots/scheduled-query-rules.png)
```

---

# 🚨 Rule 1 — Multiple Failed Login Attempts

## 📌 KQL Query

```kql
SecurityEvent
| where EventID == 4625
| summarize FailedAttempts=count() by IpAddress, Account
| where FailedAttempts >= 5
| sort by FailedAttempts desc
```

---

### 📌 Purpose

To identify repeated failed authentication attempts that may indicate brute-force login activity.

---

### 📸 Rule Configuration

_Add screenshot here_

```md
![Failed Login Rule](screenshots/failed-login-rule.png)
```

---

# 🚨 Rule 2 — Suspicious Administrative Activity

## 📌 KQL Query

```kql
CustomDataIngestionTable_CL
| where Profile == "Admin"
| where Activity contains "Failed"
| project TimeGenerated, User, Activity, ip_address
```

---

### 📌 Purpose

To monitor suspicious or failed activities associated with privileged administrative accounts.

---

### 📸 Rule Configuration

_Add screenshot here_

```md
![Admin Activity Rule](screenshots/admin-activity-rule.png)
```

---

# 🚨 Rule 3 — Port Scan Detection

## 📌 KQL Query

```kql
Syslog
| where SyslogMessage contains "Port scan"
| project TimeGenerated, Computer, SyslogMessage
```

---

### 📌 Purpose

To identify reconnaissance or scanning activity detected through Syslog telemetry.

---

### 📸 Rule Configuration

_Add screenshot here_

```md
![Port Scan Rule](screenshots/portscan-rule.png)
```

---

# 🚨 Rule 4 — Firewall Block Events

## 📌 KQL Query

```kql
Syslog
| where SyslogMessage contains "blocked"
| project TimeGenerated, Computer, SyslogMessage
```

---

### 📌 Purpose

To monitor blocked or denied network connection events generated through Syslog telemetry.

---

### 📸 Rule Configuration

_Add screenshot here_

```md
![Firewall Rule](screenshots/firewall-rule.png)
```

---

# 🧠 Entity Mapping

Entity mapping was configured to improve contextual visibility for future investigation workflows.

### Configured Entities

| Entity Type | Example |
|---|---|
| Account | User |
| IP Address | Source IP |
| Host | VM Name |

---

# 🎯 Skills Demonstrated

- Microsoft Sentinel Analytics Rules
- Scheduled Query Rule Configuration
- KQL-based Detection Logic
- Security Event Monitoring
- Syslog Monitoring
- Custom Log Monitoring
- Detection Engineering Fundamentals
- Entity Mapping
- Threat Detection Concepts

---

# 🧠 Key Learnings

- Learned how Scheduled Query Analytics Rules work in Microsoft Sentinel
- Understood scheduled KQL-based detection workflows
- Configured detection logic across multiple telemetry sources
- Learned how to define thresholds and scheduling intervals
- Practiced translating security scenarios into KQL detections
- Understood the importance of entity mapping in SOC workflows

---

# 🔗 Next Step

Proceeding to simulate attack scenarios and generate security events for validating configured Scheduled Query Analytics Rules.
