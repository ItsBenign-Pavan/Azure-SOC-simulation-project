# Security Data Validation & Log Exploration

## 🎯 Objective
To validate that security data from configured connectors is successfully ingested into Microsoft Sentinel and available for analysis.

This step focuses on verifying data availability, understanding log structure, and performing initial exploration using Kusto Query Language (KQL).

---

## 🔍 Validation Approach

- Verified log ingestion across multiple tables
- Explored data from configured connectors:
  - Microsoft Entra ID (SigninLogs, AuditLogs)
  - Threat Intelligence (ThreatIntelligenceIndicator)
- Ensured logs are queryable within Log Analytics Workspace

---

## 🛠️ Queries Executed

### 1. Validate Sign-in Logs Ingestion
#### 📌 Purpose
To confirm that identity logs from Microsoft Entra ID are being ingested into the workspace.
```kql
SigninLogs
| take 10
```
![Query-1](screenshots/Query-1.png)

### 2. Recent Sign-in Activity
#### 📌 Purpose
To review recent authentication activity and understand log structure including user, application, and source IP.
```kql
SigninLogs
| sort by TimeGenerated desc
| project TimeGenerated, UserPrincipalName, AppDisplayName, IPAddress, ResultType
```
![Query-2](screenshots/Query-2.png)

### 3. Active Threat Intelligence Indicators Overview
#### 📌 Purpose
To retrieve and review all active threat intelligence indicators, including their source, type, and confidence level.
```kql
ThreatIntelIndicators
| where IsActive == true
| project TimeGenerated, ObservableValue, SourceSystem, Type, Confidence, IsDeleted, Tags
| sort by TimeGenerated desc
```
![Query-3](screenshots/Query-3.png)

### 4. High Confidence Threats
#### 📌 Purpose
To identify high-confidence threat intelligence indicators that are more likely to represent genuine threats. This helps prioritize analysis and enables focused detection on the most reliable and critical threat data.
```kql
ThreatIntelIndicators
| where Confidence >= 80
| project ObservableValue, Type, Confidence, IsActive, IsDeleted, Tags
| sort by Confidence desc
```
![Query-4](screenshots/Query-4.png)

---
## 🔌 Data Connectors Validation Summary

| Connector               | Table Name              | Status    | Validation Method                      |
|------------------------|------------------------|----------|----------------------------------------|
| Microsoft Entra ID     | SigninLogs             | ✅ Active | Queried recent sign-in activity        |
| Microsoft Entra ID     | AuditLogs              | ✅ Active | Verified audit events                  |
| Threat Intelligence    | ThreatIntelIndicators  | ✅ Active | Retrieved active threat indicators     |

---

## 🎯 Validation Approach

Each configured data connector was validated by:

- Identifying its corresponding Log Analytics table  
- Running KQL queries to confirm data ingestion  
- Reviewing sample records to understand data structure  
- Verifying data freshness using `TimeGenerated`

---

## 🔍 Connector-wise Validation

### 1. Microsoft Entra ID

- **Tables Validated:** SigninLogs, AuditLogs  
- **Validation Performed:**
  - Checked recent login activity
  - Verified failed login attempts
  - Reviewed administrative operations

#### 📌 Outcome
Identity-related logs are successfully ingested and available for analysis.

---

### 2. Threat Intelligence

- **Table Validated:** ThreatIntelIndicators  
- **Validation Performed:**
  - Queried active indicators
  - Reviewed confidence scores and threat types
  - Verified indicator attributes such as IP/domain

#### 📌 Outcome
Threat intelligence data is successfully ingested and can be used for correlation.

---

## ⚠️ Observations

- Data ingestion depends on connector configuration and activity levels
- Threat Intelligence requires external feeds or manual input
- Log volume varies across connectors

---

## 🔐 Security Relevance

- Entra ID logs help detect authentication anomalies
- Audit logs provide visibility into administrative changes
- Threat intelligence enables correlation with known malicious entities

---

## 🔗 Correlation Readiness

With multiple connectors validated, the environment is now ready for:

- Cross-source correlation (e.g., Sign-in logs + Threat Intelligence)
- Detection rule creation
- Threat hunting activities

---

## ✅ Validation Conclusion

All configured data connectors are successfully ingesting logs into Microsoft Sentinel.  
The SIEM environment is now operational with multiple data sources and ready for advanced security analysis.
