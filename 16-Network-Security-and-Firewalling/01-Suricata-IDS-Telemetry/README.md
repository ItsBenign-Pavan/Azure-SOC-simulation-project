# Suricata IDS Telemetry

## Overview

This section focuses on deploying, configuring, and analyzing network-based intrusion detection telemetry using **Suricata IDS**. The goal is to understand how intrusion detection systems generate security alerts, monitor network activity, and support SOC investigations.

The lab environment was built on Ubuntu Linux, where Suricata was deployed, configured, and validated through multiple detection scenarios. Network events were generated and analyzed using Suricata logs to simulate real-world SOC monitoring workflows.

---

## Learning Objectives

- Understand the role of Intrusion Detection Systems (IDS)
- Deploy and configure Suricata IDS on Linux
- Manage and validate detection rules
- Generate and investigate IDS alerts
- Analyze EVE JSON and Fast Log outputs
- Develop practical network monitoring skills used in SOC environments

---

## Module Navigation

| Module | Description |
|----------|-------------|
| [01-Suricata-Deployment](./01-Suricata-Deployment) | Deploy and configure Suricata IDS on Ubuntu Linux |
| [02-Suricata-Rule-Management](./02-Suricata-Rule-Management) | Create, modify, and validate Suricata detection rules |
| [03-Suricata-Alert-Analysis](./03-Suricata-Alert-Analysis) | Investigate and analyze Suricata-generated security alerts |

---

## Technologies Used

- Suricata IDS
- Ubuntu Linux
- EVE JSON
- Fast Log
- Syslog
- TCP/IP
- ICMP
- RDP

---

## Skills Demonstrated

- Network Security Monitoring
- IDS Deployment & Administration
- Rule Development & Validation
- Alert Investigation
- Log Analysis
- Threat Detection
- Security Event Analysis

---

## Repository Structure

```text
01-Suricata-IDS-Telemetry
│
├── 01-Suricata-Deployment
├── 02-Suricata-Rule-Management
├── 03-Suricata-Alert-Analysis
│
└── README.md
```

---

## Key Outcomes

- Successfully deployed and configured Suricata IDS
- Created and validated custom detection rules
- Generated and analyzed network security alerts
- Investigated EVE JSON and Fast Log telemetry
- Simulated IDS monitoring workflows used in modern SOC environments

---

## Next Module

➡️ Continue to **02-Linux-Network-Telemetry** to explore Linux firewall logging, Syslog collection, and network telemetry analysis in Microsoft Sentinel.
