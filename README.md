# 🔐 Azure SOC Lab

## 📌 Overview
This project is a hands-on **Azure Security Operations Center (SOC) lab** where I implement and demonstrate real-world cloud security practices using Microsoft Azure.

The lab focuses on building a monitoring and detection environment using **Microsoft Sentinel**, simulating security events, and performing log analysis and incident response.

---

## 🎯 Objectives
- Deploy and configure Azure resources (VM, networking)
- Set up and configure Microsoft Sentinel (SIEM)
- Ingest and analyze logs using Log Analytics
- Write KQL queries for threat detection
- Create analytics rules and alerts
- Simulate attacks (e.g., failed logins, brute force)
- Perform basic incident investigation and response

---

## 🛠️ Tools & Services Used
- Microsoft Azure
- Microsoft Sentinel
- Log Analytics Workspace
- Azure Virtual Machines (Windows)
- Network Security Groups (NSG)
- Kusto Query Language (KQL)

---

## 🏗️ Lab Architecture
*(Add architecture diagram in `/architecture` folder)*

**Example flow:**
VM → Log Analytics Agent → Log Analytics Workspace → Microsoft Sentinel → Alerts & Incidents

---

## 📂 Project Structure
azure-soc-lab/
│
├── README.md
├── architecture/
├── screenshots/
│
├── 01-azure-setup/
├── 02-virtual-machine/
├── 03-sentinel-setup/
├── 04-log-ingestion/
├── 05-kql-queries/
├── 06-detection-rules/
├── 07-incident-response/
├── 08-playbooks/


---

## 🚀 Project Milestones

### 1️⃣ Azure Environment Setup
- Created Azure account and configured resource group

### 2️⃣ Virtual Machine Deployment
- Deployed Windows VM  
- Configured RDP access and NSG rules  

### 3️⃣ Microsoft Sentinel Setup
- Created Log Analytics Workspace  
- Enabled Microsoft Sentinel  

### 4️⃣ Log Ingestion
- Connected VM to Log Analytics  
- Verified security logs ingestion  

### 5️⃣ KQL Queries
- Wrote queries to detect:
  - Failed login attempts
  - Suspicious activity  

### 6️⃣ Detection Rules
- Created analytics rules based on KQL queries  
- Generated alerts for suspicious events  

### 7️⃣ Incident Response
- Investigated alerts inside Sentinel  
- Analyzed logs and event patterns  

### 8️⃣ Playbooks (Optional/Upcoming)
- Automating response using Logic Apps  

---

## 🔍 Sample KQL Query
```kql
SecurityEvent
| where EventID == 4625
| summarize FailedAttempts = count() by Account
| sort by FailedAttempts desc
