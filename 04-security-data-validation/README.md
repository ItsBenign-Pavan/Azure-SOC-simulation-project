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
