# 03 - Windows Network Telemetry

This directory provides comprehensive guidance on collecting, configuring, and analyzing network telemetry from Windows systems. It covers Windows Firewall configuration, log collection methodologies, event analysis, and integration with Azure Sentinel for centralized network security monitoring and threat detection.

---

## 01 - Windows Firewall Configuration

This module covers the configuration of Windows Firewall (Windows Defender Firewall) to enable enhanced logging and telemetry collection. It demonstrates how to configure firewall rules, enable advanced logging, and optimize firewall policies for security monitoring without impacting system performance.

**Key Topics:**
- Windows Firewall architecture and components
- Firewall rule creation and management
- Inbound and outbound rule configuration
- Advanced security logging enablement
- Connection security rules (IPSec)
- Group Policy configuration for firewall policies
- Application-specific firewall rules
- Performance impact assessment and optimization

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./01-Windows-Firewall-Configuration)

---

## 02 - Windows Firewall Log Collection

This module focuses on collecting and centralizing Windows Firewall logs from multiple endpoints. It covers log file locations, parsing methodologies, custom log ingestion pipelines, and integration with Azure Sentinel to aggregate firewall events for comprehensive network security monitoring.

**Key Topics:**
- Windows Firewall log file locations and formats
- Log parsing and field extraction
- Custom log ingestion to Azure Sentinel
- Log Analytics agent configuration
- Syslog forwarding and CEF format conversion
- Real-time log monitoring and alerting
- Log retention and archival policies
- Troubleshooting log collection issues
- Performance considerations for high-volume logging

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./02-Windows-Firewall-Log-Collection)

---

## 03 - Windows Network Event Analysis

This advanced module provides deep analysis of Windows network-related events captured in Event Viewer. It covers Event IDs related to network connections, DNS resolution, RDP connections, network adapter changes, and other critical network security indicators that can be extracted from Windows Event Logs.

**Key Topics:**
- Windows Event Log network-related Event IDs
- Network connection tracking and correlation
- DNS query logging and analysis
- RDP session monitoring and anomaly detection
- SMB activity and file share access tracking
- DHCP client events and IP configuration changes
- Network adapter and connectivity status monitoring
- TCP/IP and networking stack events
- Sysmon network events (ProcessCreate with network parameters, NetworkConnect)
- KQL queries for network event analysis
- Behavioral anomaly detection in network patterns
- Threat hunting using network event telemetry

[![Visit Module](https://img.shields.io/badge/Visit%20Module-→-blue?style=for-the-badge)](./03-Windows-Network-Event-Analysis)

---

## Getting Started

1. Review the parent module [16 - Network Security and Firewalling](../) for overall context
2. Start with Windows Firewall Configuration to understand how to enable telemetry
3. Configure Windows Firewall logging on all Windows VMs in your environment
4. Set up log collection using the Windows Firewall Log Collection module
5. Validate log ingestion in Azure Sentinel before proceeding to analysis
6. Use the Windows Network Event Analysis module to create detection rules
7. Integrate with [15 - Attack Simulations](../../15%20-%20Attack%20Simulations) to test network-based detections

## Network Telemetry Collection

This module provides:
- Step-by-step configuration guides for Windows Firewall
- Log ingestion scripts and custom parsers
- KQL queries for network event analysis
- Detection rules for suspicious network activities
- Visualization and hunting templates
- Baseline establishment and anomaly detection methods

## Windows Network Events Overview

| Event Category | Key Event IDs | Purpose |
|---|---|---|
| Firewall Changes | 4950, 4951, 4952, 4953, 4954, 4955, 4956, 4957, 4958 | Monitor firewall policy changes |
| Network Connections | 3, 5156, 5157, 5158, 5159 (Firewall) | Track inbound/outbound connections |
| DNS Events | 3008 (Sysmon), 22 (Sysmon) | Monitor DNS queries and resolutions |
| RDP Events | 4624, 4625, 4634 (Logon) | Track remote desktop sessions |
| Network Adapter | 4698, 4699, 4700, 4701, 4702 | Monitor network configuration changes |

## Best Practices

- Enable Windows Firewall on all systems, even if using third-party firewalls
- Use Group Policy to enforce consistent firewall configurations across the organization
- Regularly review and update firewall rules to minimize alerts and false positives
- Correlate Windows Firewall events with endpoint telemetry (Sysmon, Event Tracing)
- Establish baseline network patterns before implementing advanced analytics
- Use network event data to validate detection rules and identify blind spots
- Implement tiered logging (different levels for different rule categories)
- Archive firewall logs for compliance and forensic investigation
- Monitor for suspicious firewall rule additions or deletions

## Security Considerations

- Disabled firewall events are critical indicators - alert on any firewall disablement
- Monitor for rapid firewall rule changes (potential compromise indicators)
- Track failed connection attempts to identify reconnaissance activities
- Correlate firewall logs with process execution logs for context
- Look for uncommon destination ports and protocols
- Identify beaconing patterns in firewall connection logs

---

**Parent Module:** [16 - Network Security and Firewalling](../)  
**Previous Sibling:** [02 - Linux Network Telemetry](../02-Linux-Network-Telemetry)  
**Next Sibling:** [04 - Network Threat Hunting](../04-Network-Threat-Hunting)
