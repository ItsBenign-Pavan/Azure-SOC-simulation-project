# 📋 Investigation Conclusion — Failed Login Attempts | Windows

## 📌 Objective

The objective of this phase was to document the final findings, impact assessment, investigation verdict, and overall conclusions derived from the Microsoft Sentinel incident investigation and advanced hunting activities.

This report summarizes the complete investigation lifecycle performed against the generated brute-force authentication incident.

---

# 🏗️ Investigation Lifecycle

```text
Analytics Rule Triggered
        ↓
Incident Created
        ↓
Incident Triage
        ↓
Entity Investigation
        ↓
Advanced Hunting
        ↓
Threat Validation
        ↓
Impact Assessment
        ↓
Incident Closure
```

---

# 🚨 Incident Summary

| Property | Value |
|---|---|
| Incident Name | More than 5 failed login attempts under a minute \| Windows |
| Severity | High |
| Detection Source | Scheduled Query Analytics Rule |
| MITRE Tactic | Credential Access |
| MITRE Technique | T1110 — Brute Force |
| Affected Device | Pavan-VM-Window |
| Affected User | Pavan-VM-Window\Pavan |

---

# 📌 Investigation Activities Performed

The following investigation activities were completed during the incident handling process.

| Investigation Phase | Status |
|---|---|
| Incident Triage | ✅ Completed |
| Alert Validation | ✅ Completed |
| Entity Investigation | ✅ Completed |
| Attack Story Analysis | ✅ Completed |
| Investigation Graph Review | ✅ Completed |
| Evidence Review | ✅ Completed |
| KQL Threat Hunting | ✅ Completed |
| Alert Correlation | ✅ Completed |
| Timeline Investigation | ✅ Completed |
| Incident Validation | ✅ Completed |

---

# 📌 Key Findings

The investigation identified repeated failed authentication attempts targeting the monitored Windows virtual machine within a short timeframe.

### Findings Observed

| Observation | Result |
|---|---|
| Multiple failed logins detected | Yes |
| Repeated authentication attempts | Yes |
| Brute-force behavior indicators | Observed |
| Related suspicious alerts | Not identified |
| Successful compromise detected | No |
| Malware execution observed | No |
| Persistence activity observed | No |
| Privilege escalation observed | No |
| Lateral movement observed | No |

---

# 📌 Alert Correlation Result

Advanced hunting across:

- AlertInfo
- AlertEvidence
- SecurityAlert
- SecurityIncident

did not reveal additional malicious activity associated with the affected device or user account.

The generated alert activity remained isolated to the simulated authentication failure scenario.

---

# 📌 Impact Assessment

The overall impact assessment determined that no successful compromise or malicious persistence was achieved during the observed activity.

### Impact Analysis

| Area | Assessment |
|---|---|
| Account Compromise | Not Observed |
| Host Compromise | Not Observed |
| Malware Infection | Not Observed |
| Data Exposure | Not Observed |
| Persistence Mechanisms | Not Observed |
| Lateral Movement | Not Observed |

---

# 📌 Root Cause Determination

The incident activity was determined to be the result of controlled lab-based authentication failure simulations performed for Microsoft Sentinel detection engineering and SOC investigation learning purposes.

The behavior successfully triggered the scheduled query analytics rule configured to detect brute-force authentication activity.

---

# 📌 Analyst Verdict

| Field | Value |
|---|---|
| Incident Classification | Benign Positive |
| Determination | Security Testing / Lab Activity |
| Final Severity | High |
| Incident Status | Closed |

---

# 📸 Incident Closure

<img src="screenshots/Alert-resolved.png" width="40%">
<img src="screenshots/Inc-resolved.png" width="80%">

---

# 📌 Analyst Notes

The incident was investigated through Microsoft Defender and Microsoft Sentinel telemetry sources. Advanced hunting and alert correlation did not identify evidence of successful compromise, persistence, or additional malicious activity. The observed activity was consistent with controlled authentication failure simulations conducted within the lab environment.

---

# 📌 Lessons Learned

This investigation provided hands-on experience with:

- SOC incident handling workflows
- Microsoft Sentinel incident investigation
- Microsoft Defender portal investigation
- KQL-based threat hunting
- Alert correlation techniques
- Entity-based investigation
- Brute-force attack analysis
- MITRE ATT&CK mapping
- Incident triage methodology
- Incident closure workflows

---

# 📌 Skills Demonstrated

- Microsoft Sentinel
- Microsoft Defender XDR
- SOC Investigation Workflow
- Detection Engineering
- KQL Threat Hunting
- Authentication Threat Analysis
- Alert Correlation
- Incident Management
- Security Monitoring
- Threat Detection

---

# 🧠 Final Conclusion

The investigation successfully validated the end-to-end SOC workflow for handling authentication-based security incidents within Microsoft Sentinel.

The incident demonstrated how Microsoft Sentinel analytics rules, Defender investigation experiences, and KQL-based hunting can be used together to:

- detect suspicious activity
- investigate impacted entities
- correlate alerts and evidence
- validate telemetry
- assess compromise impact
- document investigation outcomes

The activity ultimately remained consistent with controlled lab-generated brute-force authentication simulations and did not result in a confirmed security compromise.

---

# 🔗 Next Step

Proceeding to simulate additional attack scenarios and expand detection coverage using advanced Microsoft Sentinel analytics and threat hunting techniques.
