# 04 - Custom Detection Engineering: Detecting LSASS Targeting

## Overview

This module demonstrates the complete process of developing a custom detection for monitoring processes targeting the Local Security Authority Subsystem Service (LSASS) using **Sysmon Process Access (Event ID 10)** and **Microsoft Sentinel**.

Unlike previous modules that focused on deploying existing Sigma rules, this module emphasizes **custom detection engineering** by designing a Sigma rule from scratch, validating it, converting it into Kusto Query Language (KQL), adapting it for Microsoft Sentinel, and deploying it as a Scheduled Analytics Rule.

The objective is to understand how raw telemetry collected by Sysmon can be transformed into actionable detections capable of generating alerts and incidents within Microsoft Sentinel.

---

# Objectives

By completing this module, you will learn how to:

- Enable Sysmon Process Access (Event ID 10) telemetry
- Generate LSASS targeting events
- Build a custom Sigma rule
- Validate Sigma rule syntax
- Convert Sigma into Kusto Query Language (KQL)
- Adapt Sigma-generated KQL for Microsoft Sentinel
- Create a Scheduled Analytics Rule
- Generate alerts and incidents
- Understand the fundamentals of custom detection engineering

---

# Detection Workflow

```
                Process Targets LSASS
                         │
                         ▼
              Sysmon Event ID 10 Generated
                         │
                         ▼
            Windows Event Log (Sysmon)
                         │
                         ▼
             Azure Monitor Agent (AMA)
                         │
                         ▼
              Microsoft Sentinel Event Table
                         │
                         ▼
            Custom KQL Detection Logic
                         │
                         ▼
           Scheduled Analytics Rule
                         │
                         ▼
                    Alert Generated
                         │
                         ▼
                  Incident Created
```

---

# Lab Environment

| Component | Value |
|-----------|------|
| SIEM | Microsoft Sentinel |
| Endpoint | Windows Server 2022 |
| Telemetry | Sysmon |
| Sysmon Event | Event ID 10 (Process Access) |
| Detection Language | Sigma |
| Query Language | Kusto Query Language (KQL) |
| Analytics Type | Scheduled Analytics Rule |

---

# Prerequisites

Before starting this module, ensure the following components are already configured:

- Azure Subscription
- Microsoft Sentinel Workspace
- Windows Server onboarded to Microsoft Sentinel
- Azure Monitor Agent (AMA)
- Sysmon installed
- Sysmon logs successfully ingested into Microsoft Sentinel
- Sigma CLI installed
- pySigma configured for Kusto conversion

---
# Implementation

## Step 1 – Enable Sysmon Process Access (Event ID 10)

By default, the Sysmon configuration used in this lab did not log **Process Access (Event ID 10)** events because the `ProcessAccess` section contained no include rules.

The configuration was updated to specifically monitor access to **LSASS**, reducing unnecessary telemetry while enabling credential access monitoring.

### Modified Sysmon Configuration

```xml
<!--SYSMON EVENT ID 10 : INTER-PROCESS ACCESS [ProcessAccess]-->
<RuleGroup name="" groupRelation="or">
    <ProcessAccess onmatch="include">
        <TargetImage condition="is">C:\Windows\System32\lsass.exe</TargetImage>
    </ProcessAccess>
</RuleGroup>
```

After updating the configuration, Sysmon was reloaded.

```powershell
Sysmon64 -c ".\sysmonconfig.xml"
```

Successful reload was confirmed by the following output:

```
Configuration file validated.
Configuration updated.
```

> **Screenshot:** `01-sysmon-processaccess-configuration.png`

> **Screenshot:** `02-sysmon-configuration-updated.png`

---

# Step 2 – Validate Event ID 10 Generation

To verify that the updated Sysmon configuration was working correctly, **Process Explorer** was executed with administrative privileges. Process Explorer accesses LSASS to retrieve process information, generating **Sysmon Event ID 10** telemetry.

The following PowerShell command was used to confirm that Process Access events were being generated locally.

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" |
Where-Object {$_.Id -eq 10} |
Select-Object -First 5
```

The generated event confirmed that:

- Source process was Process Explorer
- Target process was **LSASS**
- Granted access rights were successfully captured
- Sysmon Event ID 10 logging was functioning correctly

Example event fields included:

- SourceImage
- TargetImage
- GrantedAccess
- SourceUser
- TargetUser

> **Screenshot:** `03-eventid10-generated-local.png`

> **Screenshot:** `04-eventid10-details.png`

---

# Step 3 – Validate Telemetry in Microsoft Sentinel

After confirming local event generation, the next step was to verify successful ingestion into Microsoft Sentinel.

Since Sysmon events are stored within the **Event** table, the Process Access fields needed to be extracted from the `RenderedDescription` field.

The following KQL was used to parse the required fields.

```kusto
Event
| where EventID == 10
| extend
    SourceImage = extract(@"SourceImage:\s*(.*?)\s+TargetProcessGUID:", 1, RenderedDescription),
    TargetImage = extract(@"TargetImage:\s*(.*?)\s+GrantedAccess:", 1, RenderedDescription),
    GrantedAccess = extract(@"GrantedAccess:\s*(.*?)\s+CallTrace:", 1, RenderedDescription)
| project
    TimeGenerated,
    Computer,
    SourceImage,
    TargetImage,
    GrantedAccess
| sort by TimeGenerated desc
```

Successful parsing confirmed that:

- Process Access events reached Microsoft Sentinel
- Required fields were extracted successfully
- Telemetry was ready for custom detection development

> **Screenshot:** `05-eventid10-kql-validation.png`

---

# Step 4 – Develop a Custom Sigma Rule

Unlike previous modules that relied on existing SigmaHQ rules, this module focused on creating a **custom Sigma rule** for detecting processes targeting LSASS.

Rule file:

```
proc_access_win_lsass_targeting.yml
```

The Sigma rule was designed using the following detection logic:

- Windows platform
- Sysmon Process Access events
- Target process ends with `lsass.exe`

Core detection section:

```yaml
detection:
  selection:
    TargetImage|endswith: '\lsass.exe'
  condition: selection
```

The rule was enriched with:

- MITRE ATT&CK mapping
- Description
- False positives
- Severity
- References
- Unique UUID

After creation, the rule was validated using the Sigma CLI.

```bash
sigma check proc_access_win_lsass_targeting.yml
```

Validation completed successfully with:

```
Found 0 errors, 0 condition errors and 0 issues.
```

> **Screenshot:** `06-custom-sigma-rule.png`

---

# Step 5 – Convert Sigma Rule to KQL

After validating the Sigma rule, it was converted into Kusto Query Language (KQL) using **pySigma**.

```bash
sigma convert -t kusto proc_access_win_lsass_targeting.yml
```

The generated KQL represented the Sigma detection logic:

```kusto
TargetImage endswith "\\lsass.exe"
```

Although the conversion was successful, the generated query assumed native Sysmon field mappings, which differ from the Microsoft Sentinel Event table used in this lab.

Therefore, the generated query served as the baseline detection logic before being adapted for Sentinel.

> **Screenshot:** `07-sigma-kql-conversion.png`

---

# Step 6 – Adapt KQL for Microsoft Sentinel

To preserve the Sigma detection logic while supporting the Event table schema, the required fields were extracted from `RenderedDescription`.

Final adapted KQL:

```kusto
Event
| where EventID == 10
| extend
    SourceImage = extract(@"SourceImage:\s*(.*?)\s+TargetProcessGUID:", 1, RenderedDescription),
    TargetImage = extract(@"TargetImage:\s*(.*?)\s+GrantedAccess:", 1, RenderedDescription),
    GrantedAccess = extract(@"GrantedAccess:\s*(.*?)\s+CallTrace:", 1, RenderedDescription)
| where TargetImage endswith @"\lsass.exe"
| project
    TimeGenerated,
    Computer,
    SourceImage,
    TargetImage,
    GrantedAccess
| sort by TimeGenerated desc
```

# Step 7 – Create the Scheduled Analytics Rule

The adapted KQL query was deployed as a **Scheduled Analytics Rule** in Microsoft Sentinel to automatically detect processes targeting LSASS.

### Rule Configuration

| Property | Value |
|----------|-------|
| Rule Name | **Sigma \| LSASS Process Targeting** |
| Severity | Medium |
| MITRE ATT&CK Tactic | Credential Access |
| MITRE ATT&CK Technique | T1003.001 – LSASS Memory |
| Query Frequency | 5 Minutes |
| Lookup Period | 5 Minutes |
| Trigger Condition | Number of results > 0 |
| Event Grouping | Group all events into a single alert |
| Incident Creation | Enabled |

### Custom Details

The following custom details were added to enrich generated alerts:

| Field | Value |
|-------|-------|
| SourceImage | SourceImage |
| TargetImage | TargetImage |
| GrantedAccess | GrantedAccess |

### Entity Mapping

The **Host** entity was mapped using the `Computer` field to improve investigation and incident context.

Once configured, the analytics rule was enabled and became active.

> **Screenshot:** `09-analytics-rule-configuration.png`

---

# Step 8 – Validate Detection

To validate the newly created analytics rule, **Process Explorer** was executed again with administrative privileges.

This generated another Sysmon **Event ID 10**, which was successfully ingested into Microsoft Sentinel.

The Scheduled Analytics Rule detected the activity during its next execution cycle and generated:

- Microsoft Sentinel Alert
- Microsoft Sentinel Incident

This confirmed that the entire detection pipeline—from telemetry generation to incident creation—was functioning correctly.

Validation Flow:

```
Process Explorer
        │
        ▼
LSASS Process Access
        │
        ▼
Sysmon Event ID 10
        │
        ▼
Windows Event Log
        │
        ▼
Azure Monitor Agent
        │
        ▼
Microsoft Sentinel
        │
        ▼
Scheduled Analytics Rule
        │
        ▼
Alert
        │
        ▼
Incident
```

> **Screenshot:** `10-alert-and-incident-generated.png`

---

# Step 9 – Detection Engineering Observation

During repeated validation, multiple alerts and incidents were generated because the rule was intentionally designed to detect **every process targeting LSASS**.

Since Process Explorer was repeatedly used for validation, each execution resulted in another alert.

This behavior demonstrates an important concept in detection engineering:

> A technically correct detection may still generate excessive operational noise if it does not distinguish between trusted administrative activity and suspicious behavior.

Repeated alert generation highlighted the importance of reviewing detection fidelity before considering a rule suitable for production deployment.

> **Screenshot:** `11-repeated-alert-generation.png`

---

# Results

The following objectives were successfully completed:

- Enabled Sysmon Process Access (Event ID 10)
- Generated LSASS targeting telemetry
- Validated telemetry collection locally
- Verified telemetry ingestion into Microsoft Sentinel
- Developed a custom Sigma rule
- Validated Sigma rule syntax
- Converted Sigma to KQL using pySigma
- Adapted the generated KQL for Microsoft Sentinel
- Created a Scheduled Analytics Rule
- Successfully generated alerts and incidents
- Demonstrated the importance of evaluating detection quality through repeated validation

---

# Key Takeaways

- Sysmon Event ID 10 provides valuable visibility into inter-process memory access.
- Sigma offers a platform-independent approach for developing reusable detections.
- Sigma-generated queries often require adaptation to match the schema of the target SIEM.
- Microsoft Sentinel's `Event` table stores Sysmon fields within `RenderedDescription`, requiring field extraction before detection logic can be applied.
- A complete detection engineering workflow includes telemetry collection, rule development, validation, deployment, and operational evaluation—not just writing a query.

This adaptation preserved the original Sigma detection logic while making it fully compatible with Microsoft Sentinel's Event table.

The adapted query was executed successfully and returned the expected Process Access events.

> **Screenshot:** `08-final-kql-validation.png`

# MITRE ATT&CK Mapping

| Tactic | Technique | Description |
|---------|-----------|-------------|
| Credential Access | T1003.001 – OS Credential Dumping: LSASS Memory | Adversaries may access the Local Security Authority Subsystem Service (LSASS) process to obtain credentials stored in memory. |

---

# Detection Logic Summary

The custom Sigma rule detects any process attempting to access the **LSASS** process using Sysmon **Process Access (Event ID 10)** telemetry.

Detection workflow:

```
Process Access Event
        │
        ▼
Target Process = LSASS
        │
        ▼
Sigma Detection Logic
        │
        ▼
Sigma → KQL Conversion
        │
        ▼
Microsoft Sentinel Adaptation
        │
        ▼
Scheduled Analytics Rule
        │
        ▼
Alert
        │
        ▼
Incident
```

The core Sigma detection logic is intentionally simple:

```yaml
detection:
  selection:
    TargetImage|endswith: '\lsass.exe'
  condition: selection
```

The equivalent detection logic in Microsoft Sentinel identifies Sysmon Event ID 10 records where the **TargetImage** field resolves to **lsass.exe** after parsing the Event table.

---

# Detection Engineering Considerations

This module focused on building and validating a custom detection rather than producing a production-ready analytic.

During validation, **Process Explorer** was intentionally used to generate Sysmon Event ID 10 telemetry. As a result, repeated executions generated multiple alerts because the rule detects **all** processes targeting LSASS.

In an enterprise environment, detection engineers would typically refine the rule to reduce false positives by:

- Excluding trusted administrative utilities (for example, Process Explorer).
- Excluding approved security software such as EDR or antivirus agents.
- Filtering on suspicious access rights (`GrantedAccess`) commonly associated with credential dumping.
- Combining Process Access telemetry with additional indicators such as unsigned binaries, suspicious parent processes, or command-line arguments.
- Correlating multiple telemetry sources to improve detection fidelity.

These tuning activities were intentionally deferred to the next module, where the detection will be validated against a simulated adversary technique as part of an end-to-end detection engineering workflow.

---

# Conclusion

In this module, a complete custom detection engineering workflow was implemented using Microsoft Sentinel and Sysmon telemetry.

Starting from raw endpoint telemetry, a custom Sigma rule was authored, validated, converted into Kusto Query Language (KQL), adapted for Microsoft Sentinel, and deployed as a Scheduled Analytics Rule. The detection was successfully validated by generating Sysmon Process Access events, resulting in automated alert and incident creation within Microsoft Sentinel.

This exercise demonstrates how vendor-neutral detection logic can be transformed into operational analytics while highlighting the importance of telemetry validation, field mapping, and deployment within a SIEM platform.

The next module extends this work by validating the detection against a realistic attack simulation and exploring advanced detection engineering techniques.

---

# Knowledge Check

### 1. Which Sysmon Event ID records Process Access activity?

**Answer:** Event ID **10**.

---

### 2. Why was Sysmon Event ID 10 enabled in this module?

**Answer:** To monitor processes accessing **LSASS**, enabling detection of potential credential access activity.

---

### 3. What was the primary purpose of the custom Sigma rule?

**Answer:** To detect any process targeting **lsass.exe** using Sysmon Process Access telemetry.

---

### 4. Why couldn't the Sigma-generated KQL be used directly in Microsoft Sentinel?

**Answer:** The generated query assumes native Sysmon field mappings, whereas this lab stores Sysmon events in the **Event** table with fields embedded in `RenderedDescription`. Field extraction was required before applying the detection logic.

---

### 5. What utility was used to validate the detection in this module?

**Answer:** **Process Explorer**, which generated legitimate Sysmon Event ID 10 telemetry by accessing LSASS.

---

### 6. What MITRE ATT&CK technique does this detection map to?

**Answer:** **T1003.001 – OS Credential Dumping: LSASS Memory**.

---

### 7. Why did repeated validation generate multiple alerts?

**Answer:** Because the detection intentionally alerts on **every process targeting LSASS**, including the repeated use of the validation tool (Process Explorer).

---

### 8. What is the primary advantage of using Sigma for detection engineering?

**Answer:** Sigma provides a **vendor-neutral detection format** that can be converted into queries for multiple SIEM platforms while maintaining consistent detection logic.

---

### 9. What are some common production tuning strategies for this detection?

**Answer:**

- Exclude trusted administrative tools.
- Exclude approved security software.
- Filter on suspicious access rights.
- Correlate with additional telemetry sources.
- Continuously refine detections based on operational feedback.

---

### 10. What will the next module focus on?

**Answer:** Building upon this custom detection by performing an **end-to-end detection engineering exercise**, validating the detection against a realistic attack simulation and analyzing the resulting alerts and incidents.
