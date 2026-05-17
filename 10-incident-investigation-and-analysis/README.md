# 📂 Investigation Documentation

This milestone demonstrates a complete SOC-style incident handling and threat hunting workflow using Microsoft Sentinel and Microsoft Defender XDR.

The investigation was performed against a brute-force authentication detection generated from repeated failed login attempts on a Windows virtual machine.

---

## 📘 Investigation Workflow

📄 [`Investigation.md`](./Investigation.md)

Covers the initial incident investigation workflow performed through the Microsoft Defender portal, including:

- Incident overview
- Incident assignment
- Attack story analysis
- Investigation graph review
- Evidence validation
- Entity investigation
- Re-running analytics rule logic

---

## 🔎 Advanced Threat Hunting

📄 [`Advanced-Hunting.md`](./Advanced-Hunting.md)

Focuses on advanced KQL-based threat hunting and telemetry correlation, including:

- Alert validation using `AlertInfo` and `AlertEvidence`
- Authentication hunting
- Device & user pivoting
- Timeline analysis
- Brute-force validation
- Alert correlation
- Incident telemetry analysis

---

## 📋 SOC Investigation Conclusion

📄 [`SOC-Investigation-Conclusion.md`](./SOC-Investigation-Conclusion.md)

Documents the final investigation findings and incident closure workflow, including:

- Investigation summary
- Impact assessment
- Root cause analysis
- Analyst verdict
- Incident classification
- Lessons learned
- Final security conclusion

---

## 🎯 Skills Demonstrated

- Microsoft Sentinel Investigation
- Microsoft Defender XDR
- SOC Incident Handling
- KQL Threat Hunting
- Alert Correlation
- Detection Engineering
- Incident Triage
- Entity Investigation
- MITRE ATT&CK Mapping
- Security Monitoring
