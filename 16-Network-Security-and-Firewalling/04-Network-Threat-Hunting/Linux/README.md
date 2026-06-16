# Linux Network Threat Hunting

## Overview

This section focuses on detecting, investigating, and analyzing suspicious network activity on Linux systems using UFW firewall telemetry, Syslog collection, and Microsoft Sentinel.

The objective is to simulate realistic attacker behavior and develop threat hunting techniques that help security analysts identify reconnaissance, unauthorized access attempts, suspicious external communication, and lateral movement indicators.

All scenarios were performed in a controlled Azure SOC Lab environment and investigated using KQL within Microsoft Sentinel.

---

## Learning Objectives

Through these exercises, analysts learn how to:

- Monitor Linux firewall activity
- Investigate unauthorized connection attempts
- Identify suspicious external IP addresses
- Detect network reconnaissance activity
- Hunt for lateral movement indicators
- Correlate Syslog events with security activity
- Develop KQL-based investigations
- Map findings to MITRE ATT&CK techniques

---

## Lab Architecture

```text
Windows Attack Host
          │
          ▼
Linux VM (UFW + Syslog)
          │
          ▼
Azure Monitor Agent
          │
          ▼
Microsoft Sentinel
          │
          ▼
Threat Hunting & Investigation
```

---

## Modules

### 01 – Port Scanning Detection

**Objective**

Detect network reconnaissance activity against the Linux host.

**Activities**

- Nmap scanning simulation
- UFW telemetry collection
- Syslog analysis
- Sentinel-based hunting

**Skills**

- Network Reconnaissance Detection
- UFW Log Analysis
- Port Scan Investigation

**MITRE ATT&CK**

- T1046 – Network Service Discovery
- T1595 – Active Scanning

---

### 02 – Unauthorized Connection Investigation

**Objective**

Investigate repeated unauthorized connection attempts targeting a protected service.

**Activities**

- Connection attempt generation
- Firewall telemetry collection
- Source IP investigation
- Connection frequency analysis

**Skills**

- Firewall Event Investigation
- Connection Analysis
- Sentinel Hunting

**MITRE ATT&CK**

- T1046 – Network Service Discovery
- T1595 – Active Scanning

---

### 03 – Suspicious External IP Analysis

**Objective**

Identify and investigate suspicious external IP addresses interacting with the Linux server.

**Activities**

- Source IP profiling
- Timeline analysis
- Destination port analysis
- Activity correlation

**Skills**

- Threat Hunting
- IP Reputation Investigation
- Network Traffic Analysis

**MITRE ATT&CK**

- T1595 – Active Scanning
- T1046 – Network Service Discovery
- T1590 – Gather Victim Network Information

---

### 04 – Lateral Movement Hunting

**Objective**

Detect indicators of lateral movement through authentication, privilege escalation, persistence, and staging activities.

**Activities**

- Failed SSH authentication
- Successful SSH authentication
- Privilege escalation
- Host reconnaissance
- Account creation
- Privilege assignment
- Staging directory creation

**Skills**

- SSH Threat Hunting
- Authentication Analysis
- Privilege Escalation Detection
- Persistence Detection
- Post-Compromise Investigation

**MITRE ATT&CK**

- T1021.004 – Remote Services: SSH
- T1078 – Valid Accounts
- T1068 – Privilege Escalation
- T1136 – Create Account
- T1074 – Data Staged

---

## Navigation

| Module | Description |
|----------|----------|
| [01-Port-Scanning-Detection](./01-Port-Scanning-Detection) | Detect network reconnaissance and port scanning activity using UFW firewall telemetry and Sentinel hunting. |
| [02-Unauthorized-Connection-Investigation](./02-Unauthorized-Connection-Investigation) | Investigate repeated unauthorized connection attempts targeting protected services. |
| [03-Suspicious-External-IP-Analysis](./03-Suspicious-External-IP-Analysis) | Analyze suspicious external IP addresses, timelines, and targeted services. |
| [04-Lateral-Movement-Hunting](./04-Lateral-Movement-Hunting) | Detect SSH-based lateral movement, privilege escalation, persistence, and staging activity. |

---

## Key Data Sources

The following Linux telemetry sources were used throughout the investigations:

| Source | Purpose |
|----------|----------|
| UFW | Firewall monitoring |
| Syslog | Centralized event collection |
| auth.log | Authentication monitoring |
| sshd | SSH activity analysis |
| sudo | Privilege escalation detection |
| useradd/usermod/userdel | Account management monitoring |

---

## Microsoft Sentinel Capabilities Used

- Log Analytics Workspace
- Syslog Connector
- Azure Monitor Agent
- KQL Threat Hunting
- Timeline Analysis
- Event Correlation
- Security Investigations

---

## MITRE ATT&CK Coverage

| Technique | Description |
|------------|------------|
| T1595 | Active Scanning |
| T1046 | Network Service Discovery |
| T1590 | Gather Victim Network Information |
| T1021.004 | Remote Services: SSH |
| T1078 | Valid Accounts |
| T1068 | Privilege Escalation |
| T1087 | Account Discovery |
| T1136 | Create Account |
| T1074 | Data Staged |

---

## Skills Demonstrated

- Linux Security Monitoring
- Firewall Monitoring
- Network Threat Hunting
- Syslog Analysis
- SSH Investigation
- Privilege Escalation Detection
- Account Management Monitoring
- Persistence Detection
- Threat Intelligence Investigation
- Microsoft Sentinel
- KQL Development
- SOC Investigation Workflow
- MITRE ATT&CK Mapping

---

## Directory Structure

```text
Linux
├── 01-Port-Scanning-Detection
│   ├── screenshots
│   └── README.md
│
├── 02-Unauthorized-Connection-Investigation
│   ├── screenshots
│   └── README.md
│
├── 03-Suspicious-External-IP-Analysis
│   ├── screenshots
│   └── README.md
│
└── 04-Lateral-Movement-Hunting
    ├── screenshots
    └── README.md
```
