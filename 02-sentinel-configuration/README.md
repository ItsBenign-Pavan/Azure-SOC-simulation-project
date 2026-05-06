# Microsoft Sentinel Configuration

## 🎯 Objective
To deploy and configure Microsoft Sentinel as a SIEM platform for centralized log collection, monitoring, and threat detection.

---

## 🛠️ Steps Performed

### 1. Log Analytics Workspace Creation
- Created a Log Analytics Workspace to store and analyze security logs
- Ensured it is aligned with the existing Resource Group

![Log Workspace](screenshots/Log-workspace.png)

### 2. Microsoft Sentinel Enablement
- Enabled Microsoft Sentinel on the created workspace
- Verified successful deployment and accessibility

### 3. Initial Exploration
- Navigated through Sentinel dashboard
- Reviewed sections like:
  - Data Connectors
  - Analytics
  - Incidents
  - Workbooks

---

## ⚙️ Configuration Details

- Workspace Name: <your-workspace-name>
- Region: <your-region>
- Resource Group: <your-rg-name>

---

## 🧠 Key Concepts

- Microsoft Sentinel is a **cloud-native SIEM**
- Log Analytics Workspace acts as the **data storage layer**
- Sentinel provides:
  - Threat detection
  - Log analysis
  - Incident management

---

## 🔌 Data Connectors Overview

- Explored available connectors
- Identified Windows Security Events as primary data source (to be configured in next phase)

---

## 📸 Screenshots
(Add images in `/screenshots` folder)

- Sentinel Overview
- Log Analytics Workspace
- Data Connectors Page

Example:
![Sentinel Dashboard](screenshots/sentinel-dashboard.png)

---

## ✅ Outcome
Successfully deployed Microsoft Sentinel and prepared the environment for ingesting security logs.

---

## 🔐 Security Perspective

- Centralized logging is essential for SOC visibility
- Without log ingestion, detection is not possible
- Sentinel enables proactive threat monitoring

---

## 🔗 Next Step
Proceeding to deploy a Virtual Machine to generate security events and enable log ingestion. 
