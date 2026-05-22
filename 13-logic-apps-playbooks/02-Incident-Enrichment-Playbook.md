# 🧠 Incident Enrichment Playbook

This playbook was created using Azure Logic Apps and Microsoft Sentinel to automate incident enrichment workflows during the initial stages of SOC investigation.

The playbook automatically adds an enrichment comment to newly created Microsoft Sentinel incidents containing important investigation details such as incident title, severity, status, and creation time.

This implementation demonstrates a practical SOAR (Security Orchestration, Automation, and Response) workflow used by SOC teams to automate incident triage and improve investigation efficiency.

---

# 📌 Playbook Information

| Property | Value |
|---|---|
| Playbook Name | Enrich-Sentinel-Incident |
| Trigger Type | Microsoft Sentinel Incident Trigger |
| Workflow Type | Logic App (Consumption) |
| Action Performed | Add Comment to Incident |
| Status | Operational |

---

# 🚀 Playbook Workflow

```text
Microsoft Sentinel Incident
        ↓
Automation Rule Triggered
        ↓
Logic App Playbook Executed
        ↓
Incident Enrichment Comment Added
```

---

# 🛠️ Playbook Creation Steps

## Step 1 — Create Playbook

Navigate to:

```text
Microsoft Sentinel
→ Automation
→ Create
→ Playbook with incident trigger
```

Configure:
- playbook name
- resource group
- region
- consumption plan

---

## Step 2 — Configure Logic App Designer

Inside Logic App Designer:
- Microsoft Sentinel incident trigger was automatically added
- a new Microsoft Sentinel action was added using `Add comment to incident`

---

## Step 3 — Configure Incident Identifier

The `Incident ARM ID` field was configured using Sentinel dynamic content to ensure the playbook updates the correct incident automatically.

---

## Step 4 — Configure Automated Enrichment Comment

A dynamic enrichment message was configured containing:
- incident title
- severity
- status
- created time

This enrichment data is automatically added into the incident comments section during workflow execution.

---

## Step 5 — Configure RBAC Permissions

Initially, the playbook failed with a `Forbidden` error because the Logic App identity lacked permission to modify Sentinel incidents.

To resolve this:
- System Assigned Managed Identity was enabled
- `Microsoft Sentinel Contributor` role was assigned to the Logic App identity within the resource group

This allowed the playbook to successfully update Sentinel incidents.

---

# 📸 Logic App Configuration

<img src="screenshots/enrichment-playbook-designer.png" width="100%">

---

# 📸 RBAC Permission Configuration

<img src="screenshots/enrichment-rbac.png" width="100%">

---

# 🚀 Automation Rule Integration

An automation rule was created to automatically execute the playbook whenever a new Microsoft Sentinel incident is created.

Automation Workflow:
- trigger type configured as `When incident is created`
- action configured as `Run playbook`
- linked with `Enrich-Sentinel-Incident`

---

# 📸 Automation Rule Configuration

<img src="screenshots/enrichment-automation-rule.png" width="100%">

---

# 🚀 Playbook Validation

To validate the workflow:
- a new Sentinel incident was generated
- the automation rule triggered automatically
- the Logic App executed successfully
- the playbook added an enrichment comment to the incident

The comment contained dynamically generated incident information.

---

# 📸 Successful Playbook Execution

<img src="screenshots/enrichment-run-history.png" width="100%">

---

# 📸 Incident Enrichment Result

<img src="screenshots/enrichment-comment-result.png" width="100%">

---

# 🧠 Features Demonstrated

| Feature | Demonstrated |
|---|---|
| Microsoft Sentinel Playbooks | ✅ |
| Azure Logic Apps | ✅ |
| SOAR Workflow Automation | ✅ |
| Automated Incident Enrichment | ✅ |
| Dynamic Incident Content | ✅ |
| Automation Rules Integration | ✅ |
| RBAC Troubleshooting | ✅ |
| Managed Identity Configuration | ✅ |

---

# 🧠 Key Learnings

- Created Microsoft Sentinel enrichment playbooks using Logic Apps
- Configured Sentinel incident triggers
- Added automated comments to Sentinel incidents
- Used dynamic incident fields inside Logic App workflows
- Implemented Sentinel RBAC permissions for Logic Apps
- Configured System Assigned Managed Identity
- Integrated automation rules with Sentinel playbooks
- Validated end-to-end incident enrichment workflows

---
