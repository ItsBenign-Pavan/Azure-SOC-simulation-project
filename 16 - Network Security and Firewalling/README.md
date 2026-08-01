# 16 - Network Security and Firewalling

This directory contains comprehensive network security monitoring and threat detection modules designed to enhance visibility into network traffic, firewall activities, and advanced threat detection capabilities. Each module focuses on different aspects of network security and telemetry collection within a SOC environment.

---

## 01 - Suricata IDS Telemetry

Suricata is a powerful open-source Intrusion Detection System (IDS) and Intrusion Prevention System (IPS) that analyzes network traffic for suspicious patterns and known threats. This module covers Suricata deployment, rule configuration, alert generation, and integration with Azure Sentinel for centralized threat monitoring.

**Key Topics:**
- Suricata IDS/IPS deployment and configuration
- Custom rule creation and threat detection
- Alert generation and parsing
- Network traffic analysis and anomaly detection
- Protocol analysis and inspection
- Integration with Azure Sentinel for log ingestion

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./01-Suricata-IDS-Telemetry)

---

## 02 - Linux Network Telemetry

This module focuses on comprehensive network telemetry collection from Linux systems. It covers various tools and methods for capturing, analyzing, and monitoring network activities on Linux endpoints, including firewall logs, connection tracking, DNS queries, and packet captures.

**Key Topics:**
- Linux firewall configuration (iptables, ufw, firewalld)
- Network flow monitoring and netflow integration
- DNS query logging and analysis
- Connection tracking and TCP/UDP monitoring
- Packet capture and analysis (tcpdump, tshark)
- Syslog and kernel log integration
- Performance monitoring and baselines

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./02-Linux-Network-Telemetry)

---

## 03 - Windows Network Telemetry

This module provides in-depth coverage of network telemetry collection from Windows systems. It demonstrates how to collect network connection data, firewall events, DNS queries, and network performance metrics from Windows endpoints to enable comprehensive network security monitoring.

**Key Topics:**
- Windows Firewall configuration and event collection
- Network connection tracking and monitoring
- DNS query logging and analysis
- Event ID analysis for network security events
- Windows Filtering Platform (WFP) telemetry
- Network adapter and performance metrics
- RDP and SMB activity monitoring
- Sysmon network event tracking

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./03-Windows-Network-Telemetry)

---

## 04 - Network Threat Hunting

This advanced module provides practical threat hunting methodologies and techniques for network-based investigations. It includes KQL queries, hunting strategies, and analysis techniques to uncover suspicious network patterns, lateral movement indicators, and advanced threats within your network environment.

**Key Topics:**
- Network threat hunting fundamentals and methodology
- Suspicious network pattern identification
- Command & Control (C2) detection and analysis
- Data exfiltration investigation
- Lateral movement detection through network traffic
- Anomalous DNS activity hunting
- Beaconing and periodic communication detection
- Network baseline establishment and deviation analysis
- Threat intelligence integration with network data

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./04-Network-Threat-Hunting)

---

## Getting Started

1. Review the [main repository README](../README.md) for overall project context
2. Ensure your Azure Sentinel environment is properly configured with data connectors
3. Start with Suricata IDS Telemetry to understand network-based threat detection
4. Configure Linux and Windows network telemetry collection on your VMs
5. Validate telemetry ingestion in Azure Sentinel before proceeding to threat hunting
6. Integrate network detection rules from [08 - Scheduled Query Analytics Rules](../08%20-%20Scheduled%20Query%20Analytics%20Rules) and [09 - NRT Analytics Rules](../09%20-%20NRT%20Analytics%20Rules%20and%20Incident%20Creation) to create alerts
7. Use threat hunting techniques for proactive security investigations

## Network Security Monitoring

Each module provides:
- Configuration scripts and deployment guides
- Telemetry collection methodology and validation
- KQL queries for network data analysis in Azure Sentinel
- Threat hunting playbooks and investigation guides
- Detection rules for common network-based attacks
- Alert tuning and false positive reduction strategies

## Best Practices

- Implement network segmentation and micro-segmentation
- Enable comprehensive logging at firewalls and network devices
- Establish network baselines for anomaly detection
- Regularly review and update IDS/IPS rules
- Coordinate threat hunting activities with incident response teams
- Use network telemetry to correlate with endpoint and application logs
- Document all network security investigations and findings
- Continuously validate detection effectiveness against real-world threats

## Network Diagram and Architecture

Network telemetry flows through multiple collection points:
- **Endpoint telemetry** → Windows/Linux agents → Azure Sentinel
- **Network appliances** → Firewall/IDS logs → Syslog/Azure Sentinel
- **Packet captures** → Suricata/IDS → Alert pipeline
- **DNS/Flow data** → Network monitoring tools → Log ingestion

---

**Previous Module:** [15 - Attack Simulations](../15%20-%20Attack%20Simulations)  
**Next Module:** [17 - Advanced RBAC and Permissions](../17%20-%20Advanced%20RBAC%20and%20Permissions)
