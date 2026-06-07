# 🛡️ 02-Suricata-Rule-Management

---

# 🎯 Objective

The objective of this project is to understand how Suricata detection rules work, investigate existing signatures, and create custom detection rules.

In the previous module, Suricata was successfully deployed and validated. However, an Intrusion Detection System is only as effective as the rules it uses.

This project focuses on:

- Understanding Suricata rule structure
- Investigating existing detection signatures
- Learning how alerts map to rules
- Creating custom detection rules
- Loading custom rules into Suricata
- Triggering and validating custom alerts

By the end of this module, the lab moves beyond simply running Suricata and begins performing basic detection engineering activities.

---

# 🧠 What are Suricata Rules?

Suricata rules are detection signatures that define what network activity should generate an alert.

Each rule contains logic that specifies:

- Protocol
- Source
- Destination
- Traffic Direction
- Content Matching
- Severity
- Metadata
- Alert Message

When network traffic matches a rule, Suricata generates an alert.

---

# 📋 Prerequisites

Before starting this module:

- Suricata must be installed
- Suricata service must be running
- Emerging Threats rules must be downloaded
- Alert generation must be validated
- Access to Suricata rule files must be available

---

# 🔍 Investigating Existing Rules

Before creating custom detections, it is important to understand how existing rules are written.

Suricata alerts contain a Signature ID (SID).

Example:

```text
[1:2001330:10]
```

Where:

```text
GID = 1
SID = 2001330
REV = 10
```

The SID uniquely identifies the rule responsible for generating an alert.

---

# 🔎 Investigating an RDP Alert

During the previous module, Suricata generated the following alert:

```text
ET INFO RDP - Response To External Host
```

To locate the rule responsible for this alert:

## Command

```bash
grep "sid:2001330" /var/lib/suricata/rules/suricata.rules
```

## Result

The corresponding rule was identified within the Suricata rule set.

### 📸 Screenshot

![RDP Rule Investigation](images/01-rule-investigation-rdp.png)

---

# 🔎 Investigating a ZIP Exfiltration Alert

A second alert was also investigated:

```text
ET HUNTING ZIP file exfiltration over raw TCP
```

To locate the corresponding rule:

## Command

```bash
grep "sid:2035478" /var/lib/suricata/rules/suricata.rules
```

## Result

The detection rule responsible for the alert was successfully identified.

### 📸 Screenshot

![ZIP Rule Investigation](images/02-rule-investigation-zip-exfil.png)

---

# 🧩 Understanding Rule Anatomy

Example Rule:

```text
alert tcp $HOME_NET 3389 -> $EXTERNAL_NET any
(msg:"ET INFO RDP - Response To External Host";
 flow:established,to_client;
 classtype:misc-activity;
 sid:2001330;
 rev:10;)
```

Key Components:

| Component | Purpose |
|------------|----------|
| alert | Action performed |
| tcp | Protocol inspected |
| $HOME_NET | Source network |
| $EXTERNAL_NET | Destination network |
| msg | Alert name |
| flow | Traffic direction |
| classtype | Alert category |
| sid | Signature identifier |
| rev | Rule version |

---

# Why Rule Investigation Matters

SOC analysts frequently start with an alert and work backwards.

Investigation workflow:

```text
Alert
    ↓
SID
    ↓
Rule
    ↓
Detection Logic
    ↓
Validation
```

Understanding this workflow is critical for:

- Alert triage
- Detection engineering
- Rule tuning
- False positive analysis

---
---

# ⚙️ Creating a Custom Detection Rule

After understanding existing rules, the next step is creating a custom detection.

Custom rules allow security teams to:

- Detect organization-specific activity
- Monitor internal policies
- Create hunting detections
- Build tailored security monitoring

---

# 📝 Creating a Local Rule File

A dedicated local rule file was used to store custom detections.

## Command

```bash
sudo nano /var/lib/suricata/rules/local.rules
```

A custom ICMP detection rule was added:

```text
alert icmp any any -> any any (msg:"CUSTOM RULE - ICMP Ping Detected"; sid:1000001; rev:1;)
```

### Rule Explanation

| Component | Purpose |
|------------|----------|
| alert | Generate an alert |
| icmp | Monitor ICMP traffic |
| any any | Match any source |
| any any | Match any destination |
| msg | Alert message |
| sid | Unique custom identifier |
| rev | Rule version |

### 📸 Screenshot

![Custom Rule Creation](images/03-custom-rule-created.png)

---

# 📂 Loading Custom Rules

By default, Suricata only loaded:

```yaml
rule-files:
  - suricata.rules
```

The custom rule file needed to be added manually.

## Configuration File

```bash
sudo nano /etc/suricata/suricata.yaml
```

The rule section was modified:

```yaml
rule-files:
  - suricata.rules
  - local.rules
```

This ensured that custom signatures would be loaded during startup.

---

# ✅ Validating Rule Configuration

Before restarting Suricata, the configuration was validated.

## Command

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

## Expected Result

```text
Configuration provided was successfully loaded
```

Successful validation confirms:

- Rule syntax is correct
- Configuration is valid
- Detection engine can load the custom rule

### 📸 Screenshot

![Custom Rule Validation](images/04-custom-rule-validation.png)

---

# 🔄 Restarting Suricata

After loading the custom rule, Suricata was restarted.

## Command

```bash
sudo systemctl restart suricata
```

## Verification

```bash
sudo systemctl status suricata
```

Expected output:

```text
Active: active (running)
```

### 📸 Screenshot

![Suricata Restarted](images/05-suricata-restarted.png)

---

# 🧪 Verifying Detection Engine

After restart, the configuration was validated once more.

## Command

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

This confirmed that the custom rule remained successfully loaded.

### 📸 Screenshot

![ICMP Rule Validation](images/06-icmp-custom-rule-validation.png)

---
---

# 🚨 Monitoring Alerts

To observe alert generation in real time, Suricata's fast.log was monitored.

## Command

```bash
sudo tail -f /var/log/suricata/fast.log
```

## Why are we doing this?

The fast.log file provides a human-readable view of alerts generated by Suricata.

It allows analysts to quickly verify:

- Rule matches
- Alert names
- Source and destination information
- Classification
- Severity

---

# 🎯 Triggering the Custom Rule

After loading the custom ICMP rule, network traffic was generated to intentionally trigger the detection.

## Command

```bash
ping 8.8.8.8 -c 4
```

## Why ICMP?

ICMP traffic is:

- Easy to generate
- Easy to identify
- Reliable for testing
- Commonly used in detection validation

The ping command generated ICMP packets that matched the custom rule.

---

# 🔍 Alert Verification

Once the ICMP traffic was generated, Suricata immediately produced an alert.

Example:

```text
CUSTOM RULE - ICMP Ping Detected
```

This confirmed that:

```text
Traffic
    ↓
Rule Match
    ↓
Alert Generation
    ↓
Logging
```

was functioning correctly.

### 📸 Screenshot

![Custom Alert Triggered](images/07-custom-alert-triggered.png)

---

# 🧠 Detection Engineering Workflow

This project demonstrated the complete detection engineering lifecycle.

```text
Investigate Existing Alert
            ↓
Locate Rule
            ↓
Understand Rule Logic
            ↓
Create Custom Rule
            ↓
Load Rule
            ↓
Validate Configuration
            ↓
Restart Detection Engine
            ↓
Generate Traffic
            ↓
Trigger Alert
            ↓
Verify Detection
```

This workflow mirrors how security teams develop and maintain detections in production environments.

---

# 🎓 Key Learnings

During this project, the following concepts were learned and validated.

## Rule Investigation

Understanding how Suricata alerts map back to specific signatures through the Signature ID (SID).

---

## Rule Structure

Learning the purpose of:

- alert
- protocol
- source
- destination
- msg
- sid
- rev
- classtype
- flow

---

## Signature IDs (SID)

Understanding that every Suricata rule has a unique identifier used during investigations.

---

## Rule Management

Learning how custom rule files are:

- Created
- Loaded
- Maintained
- Validated

---

## Configuration Validation

Understanding the importance of validating configuration before restarting the detection engine.

---

## Detection Engineering

Creating custom detections based on specific traffic patterns.

---

## Alert Validation

Generating controlled traffic and verifying that detections trigger as expected.

---
---

# 🎉 Outcome

Successfully completed Suricata Rule Management and Custom Detection Engineering.

## Achievements

- ✅ Investigated Existing Suricata Alerts
- ✅ Located Detection Rules Using SID
- ✅ Understood Rule Anatomy
- ✅ Analyzed Real Detection Signatures
- ✅ Created a Custom Detection Rule
- ✅ Added Custom Rule File to Suricata Configuration
- ✅ Validated Rule Syntax
- ✅ Restarted Detection Engine Successfully
- ✅ Generated Test Traffic
- ✅ Triggered Custom Detection
- ✅ Verified Alert Generation in fast.log

---

# 📊 Skills Developed

This project introduced several real-world SOC and Detection Engineering concepts.

### SOC Analyst Skills

- Alert Investigation
- Signature Analysis
- Detection Validation
- Log Analysis

### Detection Engineering Skills

- Rule Creation
- Rule Management
- SID Tracking
- Alert Testing
- Detection Lifecycle Management

### Network Security Skills

- ICMP Traffic Analysis
- Network-Based Detection
- IDS Operations
- Signature-Based Detection

---

# 🔐 Real-World Relevance

In enterprise environments, security teams rarely rely entirely on vendor-provided signatures.

Custom detections are frequently developed to:

- Monitor internal applications
- Detect organization-specific threats
- Identify suspicious user behavior
- Reduce false positives
- Improve visibility into critical assets

Understanding how to create and manage custom Suricata rules is therefore a valuable skill for:

- SOC Analysts
- Detection Engineers
- Threat Hunters
- Security Engineers

---

# 📁 Project Deliverables

The following artifacts were produced during this project:

### Screenshots

- 01-rule-investigation-rdp.png
- 02-rule-investigation-zip-exfil.png
- 03-custom-rule-created.png
- 04-custom-rule-validation.png
- 05-suricata-restarted.png
- 06-icmp-custom-rule-validation.png
- 07-custom-alert-triggered.png

### Configuration Files

```text
/etc/suricata/suricata.yaml
/var/lib/suricata/rules/local.rules
```

### Validation Logs

```text
/var/log/suricata/fast.log
/var/log/suricata/eve.json
```

---

# 🚀 Next Project

➡️ **03-Suricata-Alert-Analysis**

The next module focuses on understanding and analyzing Suricata alerts in greater depth.

Topics include:

- fast.log Analysis
- eve.json Analysis
- Alert Severity
- Alert Classification
- Protocol Metadata
- Source/Destination Investigation
- Alert Triage Workflow
- Analyst Investigation Techniques

This will further develop SOC analyst skills before integrating Suricata telemetry into Microsoft Sentinel.

---
