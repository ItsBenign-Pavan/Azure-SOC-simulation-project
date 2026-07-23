# 01 - Sigma Fundamentals & Rule Anatomy

## Overview

Sigma is an open-source, vendor-neutral rule format for describing detection logic in a standardized way. Instead of writing separate detection rules for each SIEM platform, Sigma allows detection engineers to define a rule once in YAML format and convert it into platform-specific queries such as Microsoft Sentinel (KQL), Splunk (SPL), Elastic (EQL), QRadar (AQL), and many others.

This module introduces the Sigma ecosystem, explores the official SigmaHQ repository, and explains the anatomy of a Sigma rule. By understanding the structure and purpose of each field, you'll build the foundation required to create, customize, and deploy Sigma rules in later modules.

---

## Learning Objectives

After completing this module, you will be able to:

- Understand the purpose and benefits of Sigma.
- Explain the concept of Detection-as-Code.
- Navigate the official SigmaHQ repository.
- Understand how Sigma rules are organized.
- Read and interpret any Sigma rule.
- Explain the purpose of each major Sigma rule field.
- Understand the basics of Sigma detection logic.

---

# Step 1 – Introduction to Sigma

## What is Sigma?

Sigma is a generic and vendor-independent rule format used to describe security detections. It enables security teams to write detection logic once and convert it into queries for multiple SIEM and EDR platforms.

Unlike platform-specific detection languages, Sigma focuses on **what should be detected**, rather than **how a specific platform performs the detection**.

### Benefits of Sigma

- Vendor-neutral detection format
- Detection-as-Code approach
- Easy collaboration through Git
- Large community-maintained rule repository
- Reusable detection logic across multiple SIEM platforms

---

# Step 2 – Exploring the SigmaHQ Repository

The official Sigma rules are maintained by the SigmaHQ community on GitHub.

Repository:

https://github.com/SigmaHQ/sigma

The repository contains thousands of production-ready detection rules covering Windows, Linux, Cloud, Network, Web, and Application telemetry.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| `rules/` | Sigma detection rules |
| `docs/` | Documentation |
| `tests/` | Rule validation resources |
| `tools/` | Supporting utilities |

Detection rules are organized by **telemetry source**, allowing engineers to quickly locate rules relevant to a specific operating system or technology.

### Screenshot

![SigmaHQ Repository Structure](images/01-SigmaHQ-Repository-Structure.png)

---

# Step 3 – Sigma Rule Anatomy

To understand how Sigma works, we analyzed a real production-ready Sigma rule from the SigmaHQ repository.

A typical Sigma rule consists of the following sections:

| Field | Purpose |
|--------|---------|
| `title` | Human-readable rule name |
| `id` | Unique rule identifier (UUID) |
| `status` | Rule maturity level |
| `description` | Detection purpose |
| `references` | External documentation and research |
| `author` | Rule creator |
| `date` | Creation date |
| `tags` | MITRE ATT&CK mapping and categorization |
| `logsource` | Target telemetry source |
| `detection` | Detection logic |
| `condition` | Evaluation condition |
| `falsepositives` | Expected legitimate matches |
| `level` | Recommended alert severity |

Understanding these fields allows Detection Engineers to evaluate, customize, and maintain Sigma rules effectively.

### Screenshot

![Sigma Rule Anatomy](images/02-Sigma-Rule-Anatomy.png)

---

# Step 4 – Detection Logic Fundamentals

The **detection** section is the core of every Sigma rule. It specifies the conditions that must be satisfied for an event to be considered suspicious.

Common components include:

- **selection** – Defines the events or field values to match.
- **filter** – Excludes known benign activity.
- **condition** – Combines selections and filters into the final detection logic.

Example conditions include:

- `selection`
- `selection and not filter`
- `1 of selection*`

More advanced detection logic and rule creation will be covered in the next module.

---

# Key Takeaways

- Sigma is a vendor-neutral detection rule format written in YAML.
- Sigma follows the Detection-as-Code approach.
- The SigmaHQ repository provides a large collection of community-maintained detection rules.
- Sigma rules are organized by telemetry source rather than SIEM platform.
- Every Sigma rule follows a standardized structure consisting of metadata, log source information, detection logic, and supporting information.
- Understanding rule anatomy is essential before creating or converting Sigma rules.

---

# Knowledge Check

### 1. What problem does Sigma solve?

**Answer:** Sigma provides a vendor-neutral format for writing detection rules, eliminating the need to create separate detections for each SIEM platform.

---

### 2. What language are Sigma rules written in?

**Answer:** YAML.

---

### 3. Where are official Sigma rules maintained?

**Answer:** The SigmaHQ GitHub repository.

---

### 4. Which section defines the telemetry source for a Sigma rule?

**Answer:** `logsource`

---

### 5. Which section contains the detection criteria?

**Answer:** `detection`

---

### 6. What is the purpose of the `condition` field?

**Answer:** It defines how the detection logic is evaluated.

---

### 7. Why are `falsepositives` important?

**Answer:** They help analysts understand legitimate scenarios that may trigger the rule and assist in tuning detections.

---

## Next Module

➡️ **02 - Building & Converting Sigma Rules**

In the next module, you'll install the Sigma CLI, validate Sigma rules, create custom rules, and convert them into Microsoft Sentinel KQL.
