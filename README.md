## 🎯 Project Objectives

This project is designed to simulate a real-world SOC environment by focusing on **threat detection, investigation, and response** rather than just resource deployment.

Key objectives include:

- 🔍 **Simulate Real Attack Scenarios**
  - Generate brute-force login attempts (Event ID 4625)
  - Emulate suspicious activity on a monitored VM

- 📥 **Centralize and Normalize Logs**
  - Ingest Windows Security Events into Log Analytics Workspace
  - Ensure visibility across endpoints using Microsoft Sentinel

- 🧠 **Develop Threat Detection Logic**
  - Write KQL queries to identify anomalies and suspicious patterns
  - Detect brute-force attempts, account misuse, and abnormal behaviors

- 🚨 **Build Detection & Alerting Mechanisms**
  - Create analytics rules to trigger alerts based on attack patterns
  - Tune rules to reduce false positives

- 🧾 **Perform Incident Investigation**
  - Analyze alerts generated in Microsoft Sentinel
  - Correlate logs to understand attack timeline and impact

- ⚡ **Automate Response (SOAR)**
  - Design playbooks using Logic Apps
  - Automate actions like alert notifications or IP blocking

- 🎯 **Map Detections to MITRE ATT&CK Framework**
  - Align attack simulations with real-world tactics (e.g., Credential Access, Initial Access)

- 📊 **Build Security Visibility**
  - Create dashboards/workbooks for monitoring threats and trends

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
