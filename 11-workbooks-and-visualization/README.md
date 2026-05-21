# 📊 Workbooks & Visualization

This milestone focuses on building interactive Microsoft Sentinel workbooks for SOC monitoring, security visibility, authentication analysis, incident tracking, and telemetry visualization using Kusto Query Language (KQL).

The workbooks were created using real telemetry generated from the lab environment and demonstrate how SOC analysts use dashboards to monitor security events, investigate suspicious activity, analyze authentication trends, and improve operational visibility within Microsoft Sentinel.

The dashboards cover multiple areas including:
- failed authentication monitoring
- incident management
- Windows security telemetry
- alert visibility
- VM activity monitoring
- endpoint authentication analysis

All workbook visualizations were created using KQL queries and Sentinel workbook components such as:
- pie charts
- bar charts
- time charts
- donut charts
- grid/table visualizations

---

# 📂 Workbook Navigation

| Workbook | Description |
|---|---|
| [01-Failed-Login-Monitoring-Workbook.md](01-Failed-Login-Monitoring-Workbook.md) | Monitoring failed login attempts, authentication spikes, brute-force patterns, and authentication telemetry using SecurityEvent logs |
| [02-Incident-Management-Workbook.md](02-Incident-Management-Workbook.md) | SOC-focused incident monitoring dashboard for tracking severity, incident lifecycle, ownership, and investigation status |
| [03-Security-Events-Workbook.md](03-Security-Events-Workbook.md) | Windows security telemetry monitoring dashboard covering Event IDs, authentication activity, log clearing events, and security event distribution |
| [04-Alert-Monitoring-Workbook.md](04-Alert-Monitoring-Workbook.md) | Alert and detection visibility dashboard for monitoring Sentinel alerts, analytics rule activity, affected entities, and incident-linked detections |
| [05-VM-Activity-Workbook.md](05-VM-Activity-Workbook.md) | Endpoint-focused dashboard for monitoring VM activity, user authentication behavior, failed logins, and host-level telemetry |

---

# 🛠️ Technologies & Features Used

- Microsoft Sentinel
- Azure Monitor
- Log Analytics Workspace
- Kusto Query Language (KQL)
- SecurityEvent Table
- Event Table
- SecurityAlert Table
- SecurityIncident Table
- Interactive Workbook Visualizations
- SOC Monitoring Dashboards

---

# 🧠 Skills Demonstrated

- Security telemetry analysis
- Authentication monitoring
- Alert and incident visualization
- Windows event monitoring
- Endpoint activity monitoring
- KQL query development
- SOC dashboard engineering
- Security operations visibility
- Threat monitoring and investigation

---

# 📸 Key Areas Covered

The workbooks demonstrate:
- authentication trend monitoring
- brute-force activity visualization
- failed login analysis
- incident lifecycle tracking
- alert severity analysis
- Windows security event monitoring
- endpoint telemetry visibility
- security operations monitoring

---

# 🚀 Outcome

By completing this milestone, a complete set of SOC-focused dashboards was created within Microsoft Sentinel to improve operational visibility, monitor security telemetry, analyze incidents, and visualize authentication and endpoint activity using real telemetry collected from the lab environment.

---

# 🔗 Next Step

Proceeding to implement automation and incident response workflows using Microsoft Sentinel Automation Rules and Logic Apps.
