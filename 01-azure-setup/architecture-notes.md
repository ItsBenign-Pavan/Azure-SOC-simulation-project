# Architecture Notes

## Design Approach
The lab is designed to simulate a centralized SOC monitoring system where logs from endpoints are collected and analyzed.

## Planned Flow
Virtual Machine → Log Analytics Workspace → Microsoft Sentinel

## Considerations
- Centralized logging for visibility
- Scalability for adding more endpoints later
- Separation of resources using Resource Groups
