# 🏷️ High Severity Incident Tagging

This automation rule was created to automatically tag high severity incidents generated within Microsoft Sentinel in order to improve SOC prioritization, investigation visibility, and incident categorization workflows.

The automation helps analysts quickly identify critical incidents requiring immediate attention by automatically applying investigation and prioritization tags during incident creation.

---

# 📌 Automation Rule Information

| Property | Value |
|---|---|
| Automation Rule Name | High Severity Incident Tagging |
| Trigger Type | When incident is created |
| Action Type | Add Tags |
| Status | Enabled |

---

# 🚀 Automation Configuration

The automation rule was configured with the following settings:

## Basic Information

| Field | Value |
|---|---|
| Name | High Severity Incident Tagging |
| Order | 2 |
| Status | Enabled |

---

## Trigger Configuration

| Setting | Value |
|---|---|
| Trigger | When incident is created |

---

## Condition Configuration

| Property | Operator | Value |
|---|---|---|
| Severity | Equals | High |

---

## Actions Configured

| Action | Purpose |
|---|---|
| Add Tags | Automatically classify and prioritize incidents |

Configured Tags:

```text
High-Priority
Immediate-Investigation
Critical-Asset
```

---

# 📸 Automation Rule Configuration

<img src="screenshots/AR-2.1.png" width="80%">
<img src="screenshots/AR-2.2.png" width="100%">

---

# 🚀 Automation Validation

To validate the automation workflow:
- a high severity incident was generated within Microsoft Sentinel
- the automation rule triggered automatically
- investigation and prioritization tags were applied successfully
- the incident was categorized automatically for SOC visibility

---

# 📸 Automation Result

<img src="screenshots/AR-2 result1.png" width="90%">
<img src="screenshots/AR-2 result2.png" width="90%">

---

# 🧠 Security Benefits

This automation workflow helps:
- improve incident prioritization
- enhance SOC visibility
- accelerate investigation workflows
- standardize incident categorization
- reduce manual tagging effort

---

# 🛠️ Features Demonstrated

| Feature | Demonstrated |
|---|---|
| Sentinel Automation Rules | ✅ |
| Incident Enrichment | ✅ |
| Automatic Tagging | ✅ |
| Conditional Automation Logic | ✅ |
| SOC Workflow Automation | ✅ |

---

# 🧠 Key Learnings

- Created Microsoft Sentinel automation rules
- Configured severity-based automation conditions
- Automated incident enrichment workflows
- Applied investigation and prioritization tags automatically
- Improved SOC operational visibility using Sentinel automation capabilities

---
