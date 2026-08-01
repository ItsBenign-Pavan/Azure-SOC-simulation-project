# 15 - Attack Simulations

This directory contains comprehensive threat simulation scenarios designed to demonstrate real-world attack techniques and their detection methodologies within a SOC environment. Each module provides practical examples, detection strategies, and monitoring guidance.

---

## 01 - PowerShell Attack Simulation

PowerShell is a powerful scripting language frequently abused by attackers for reconnaissance, execution, and persistence. This module simulates common PowerShell-based attack techniques and demonstrates how to detect suspicious PowerShell activities through log analysis and behavioral monitoring.

**Key Topics:**
- PowerShell execution policies and bypass techniques
- Obfuscation and encoding detection
- Script block logging and transcription
- Anomalous PowerShell process behaviors
- Command line parameter analysis

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./01-PowerShell-Attack-Simulation)

---

## 02 - Reverse Shell & C2 Callback Simulation & Detection

This module focuses on simulating reverse shell connections and Command & Control (C2) callback communications. It covers the detection and monitoring of compromised systems attempting to establish outbound connections to attacker-controlled infrastructure.

**Key Topics:**
- Reverse shell establishment and detection
- C2 callback communication patterns
- Network-based threat detection (DNS, HTTP, raw TCP/UDP)
- Process-to-network correlation analysis
- Indicators of Compromise (IoCs) for C2 infrastructure
- Beaconing detection and analysis

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./02-Reverse-Shell-C2-Callback-Simulation-Detection)

---

## 03 - LOLBins Certutil Abuse

Living Off the Land Binaries (LOLBins) are legitimate Windows system binaries that attackers abuse to evade detection. This module specifically focuses on `certutil.exe` abuse, a common technique used for malware download and execution without triggering traditional security alerts.

**Key Topics:**
- Certutil abuse techniques and variants
- LOLBins concept and detection strategies
- File download and transfer detection
- Process execution and parent-child relationships
- Encoding/decoding abuse patterns
- Application whitelisting evasion

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./03-LOLBins-Certutil-Abuse)

---

## 04 - ClickFix RunMRU Detection Simulation

ClickFix is a social engineering attack that tricks users into executing malicious commands via the Windows Run dialog. This module simulates ClickFix attacks and demonstrates detection through RunMRU (Run Most Recently Used) registry key analysis and user activity monitoring.

**Key Topics:**
- ClickFix attack mechanics and user interaction patterns
- RunMRU registry monitoring and forensics
- Social engineering detection signals
- User activity correlation
- Registry key change tracking
- Behavioral analytics for suspicious executions

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./04-ClickFix-RunMRU-Detection-Simulation)

---

## 05 - Multi-Stage Malware Delivery & Persistence Simulation

This advanced module simulates sophisticated multi-stage malware attacks that involve initial delivery, execution, persistence establishment, and lateral movement. It provides a holistic view of the attack chain and detection opportunities at each stage.

**Key Topics:**
- Initial access vectors (phishing, drive-by downloads)
- Staged payload delivery mechanisms
- Persistence techniques (Run keys, scheduled tasks, WMI, services)
- Process injection and code execution
- File system and registry modifications
- Behavioral threat indicators across the attack chain
- End-to-end detection strategy

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./05-Multi-Stage-Malware-Delivery-Persistence-Simulation)

---

## Getting Started

1. Review the [main repository README](../README.md) for overall project context
2. Ensure your Azure Sentinel environment is properly configured with data connectors
3. Start with the PowerShell simulation to understand basic attack detection
4. Progress through each module sequentially to build comprehensive detection capabilities
5. Integrate detection rules from [08 - Scheduled Query Analytics Rules](../08%20-%20Scheduled%20Query%20Analytics%20Rules) and [09 - NRT Analytics Rules](../09%20-%20NRT%20Analytics%20Rules%20and%20Incident%20Creation) to create alerts for these simulations

## Detection and Response

Each simulation module includes:
- Attack execution scripts and techniques
- Expected telemetry and log artifacts
- KQL queries for detection in Azure Sentinel
- Response playbooks and investigation guidance
- Recommended automation and playbook actions

## Best Practices

- Execute simulations in isolated lab environments only
- Coordinate with security teams before running simulations in production
- Document all simulation activities and findings
- Use these simulations to validate your detection engineering efforts
- Continuously refine detection rules based on simulation results

---

**Previous Module:** [14 - Watchlists](../14%20-%20Watchlists)  
**Next Module:** [16 - Network Security and Firewalling](../16%20-%20Network%20Security%20and%20Firewalling)
