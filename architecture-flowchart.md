```mermaid
graph TD
    Start["🚀 Azure SOC Simulation Project"] --> Phase1["<b>PHASE 1: FOUNDATION & INFRASTRUCTURE</b>"]
    
    Phase1 --> Setup1["01. Azure Setup"]
    Phase1 --> Deploy1["05. VM Deployment"]
    
    Setup1 --> Setup1A["✓ Resource Groups<br/>✓ Storage Accounts<br/>✓ Log Analytics Workspace<br/>✓ Networking"]
    Deploy1 --> Deploy1A["✓ Windows VM Config<br/>✓ Linux VM Config<br/>✓ NSG Rules<br/>✓ Identity & Access"]
    
    Setup1A --> Phase2["<b>PHASE 2: DATA COLLECTION & INGESTION</b>"]
    Deploy1A --> Phase2
    
    Phase2 --> Connect["03. Data Connectors"]
    Phase2 --> Ingest["07. Custom Log Ingestion"]
    Phase2 --> Validate["06. Endpoint Telemetry"]
    
    Connect --> ConnectA["✓ Microsoft Defender<br/>✓ Security Events<br/>✓ Syslog Collection<br/>✓ Azure Monitor Agent"]
    Ingest --> IngestA["✓ App Logs<br/>✓ Custom Parsing<br/>✓ Transform Rules<br/>✓ Data Enrichment"]
    Validate --> ValidateA["✓ Windows Event Logs<br/>✓ Syslog Verification<br/>✓ Log Validation<br/>✓ Health Checks"]
    
    ConnectA --> Phase3["<b>PHASE 3: DETECTION ENGINEERING</b>"]
    IngestA --> Phase3
    ValidateA --> Phase3
    
    Phase3 --> Config["02. Sentinel Config"]
    Phase3 --> Validate2["04. Data Validation"]
    Phase3 --> Scheduled["08. Scheduled Rules"]
    Phase3 --> NRT["09. NRT Rules"]
    Phase3 --> KQL["⭐ KQL Mastery"]
    
    Config --> ConfigA["✓ Workspace Setup<br/>✓ RBAC Configuration<br/>✓ Retention Policies<br/>✓ Compliance Setup"]
    Validate2 --> ValidateA2["✓ Data Quality<br/>✓ Format Checks<br/>✓ Anomaly Detection<br/>✓ Parsing Validation"]
    Scheduled --> ScheduledA["✓ Threat Hunting Queries<br/>✓ KQL Development<br/>✓ Hourly Execution<br/>✓ Alert Generation"]
    NRT --> NRTA["✓ Real-Time Detection<br/>✓ Auto-Incident Gen<br/>✓ Zero-Latency Alerts<br/>✓ Immediate Response"]
    KQL --> KQLA["✓ Complex Patterns<br/>✓ Multi-Source Correlation<br/>✓ Performance Optimization<br/>✓ Advanced Analytics"]
    
    ConfigA --> Phase4["<b>PHASE 4: INVESTIGATION & RESPONSE</b>"]
    ValidateA2 --> Phase4
    ScheduledA --> Phase4
    NRTA --> Phase4
    KQLA --> Phase4
    
    Phase4 --> Incident["10. Incident Investigation"]
    Phase4 --> Workbooks["11. Workbooks & Viz"]
    Phase4 --> AutoRules["12. Automation Rules"]
    Phase4 --> Playbooks["13. Logic Apps"]
    Phase4 --> Watchlists["14. Watchlists"]
    
    Incident --> IncidentA["✓ Incident Triage<br/>✓ Root Cause Analysis<br/>✓ Evidence Collection<br/>✓ Investigation Playbooks"]
    Workbooks --> WorkbooksA["✓ KPI Dashboards<br/>✓ Security Posture<br/>✓ Threat Timeline<br/>✓ Custom Reports"]
    AutoRules --> AutoRulesA["✓ Auto-Escalation<br/>✓ Incident Grouping<br/>✓ Status Management<br/>✓ Assignment Rules"]
    Playbooks --> PlaybooksA["✓ Email Alerts<br/>✓ Ticket Creation<br/>✓ Slack Integration<br/>✓ Auto-Remediation"]
    Watchlists --> WatchlistsA["✓ Malicious IPs<br/>✓ Bad File Hashes<br/>✓ Suspicious Domains<br/>✓ User Baselines"]
    
    IncidentA --> Phase5["<b>PHASE 5: THREAT HUNTING & VALIDATION</b>"]
    WorkbooksA --> Phase5
    AutoRulesA --> Phase5
    PlaybooksA --> Phase5
    WatchlistsA --> Phase5
    
    Phase5 --> Attack["15. Attack Simulations"]
    Phase5 --> Network["16. Network Security"]
    
    Attack --> AttackA["✓ Brute Force Attacks<br/>✓ Privilege Escalation<br/>✓ Lateral Movement<br/>✓ Data Exfiltration<br/>✓ C2 Communication<br/>✓ MITRE ATT&CK Mapping"]
    Network --> NetworkA["✓ NSG Rules<br/>✓ Network Threat Hunt<br/>✓ Lateral Movement Analysis<br/>✓ Traffic Pattern Analysis"]
    
    AttackA --> End2["✅ FULL SOC WORKFLOW COMPLETE"]
    NetworkA --> End2
    
    style Start fill:#1e40af,stroke:#1e3a8a,stroke-width:3px,color:#fff
    style Phase1 fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff
    style Phase2 fill:#0891b2,stroke:#0e7490,stroke-width:2px,color:#fff
    style Phase3 fill:#059669,stroke:#047857,stroke-width:2px,color:#fff
    style Phase4 fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
    style Phase5 fill:#dc2626,stroke:#b91c1c,stroke-width:2px,color:#fff
    style End2 fill:#16a34a,stroke:#15803d,stroke-width:3px,color:#fff
    
    classDef moduleBox fill:#f3f4f6,stroke:#9ca3af,stroke-width:2px,color:#000
    classDef detailBox fill:#fff,stroke:#d1d5db,stroke-width:1px,color:#000
    
    class Setup1,Deploy1,Connect,Ingest,Validate,Config,Validate2,Scheduled,NRT,KQL,Incident,Workbooks,AutoRules,Playbooks,Watchlists,Attack,Network moduleBox
    class Setup1A,Deploy1A,ConnectA,IngestA,ValidateA,ConfigA,ValidateA2,ScheduledA,NRTA,KQLA,IncidentA,WorkbooksA,AutoRulesA,PlaybooksA,WatchlistsA,AttackA,NetworkA detailBox
```

This flowchart visualizes your entire Azure SOC Simulation project in a structured, easy-to-understand format showing all 16 modules and their key features.

**Flowchart Highlights:**
- 🏗️ **5 Phases** from infrastructure to threat hunting
- 📦 **16 Modules** with specific implementations
- 🎯 **Color-coded** for easy visual navigation
- ✓ **Detailed features** under each module
- 🔄 **Flow progression** from setup to complete SOC operations
