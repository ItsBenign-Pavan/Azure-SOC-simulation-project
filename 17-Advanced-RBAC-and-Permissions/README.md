# Azure RBAC & Identity Access Management

## Overview

Azure Role-Based Access Control (Azure RBAC) is Microsoft's authorization system for managing access to Azure resources. Combined with Microsoft Entra ID, it enables organizations to implement secure, scalable, and least-privilege access control across cloud environments.

This learning path explores the core concepts of Azure RBAC and identity management, progressing from foundational role assignments to advanced authentication mechanisms such as Service Principals and Managed Identities.

Throughout these modules, I implemented practical Azure RBAC scenarios using Microsoft Entra ID, Azure Virtual Machines, Microsoft Sentinel, and Azure CLI to understand how Azure authorizes users, applications, and services.

---

# Learning Objectives

After completing this learning path, I was able to:

- Understand Azure RBAC architecture
- Configure built-in Azure roles
- Implement Microsoft Sentinel RBAC
- Create and manage Custom RBAC roles
- Work with Service Principals
- Configure Managed Identities
- Delegate permissions securely
- Apply the Principle of Least Privilege (PoLP)
- Understand Azure authorization flow

---

# Module Navigation

| # | Module | Description |
|---|--------|-------------|
| 01 | [Azure RBAC Fundamentals](./01-Azure-RBAC-Fundamentals) | Understand Azure RBAC architecture, built-in roles, scopes, and authorization flow. |
| 02 | [Microsoft Sentinel Roles](./02-Microsoft-Sentinel-Roles) | Configure and validate Microsoft Sentinel built-in roles for SOC operations. |
| 03 | [Custom RBAC Roles](./03-Custom-RBAC-Roles) | Create, assign, and validate custom Azure RBAC roles following the Principle of Least Privilege. |
| 04 | [Service Principals and App Registrations](./04-Service-Principals-and-App-Registrations) | Register applications, create Service Principals, authenticate using Azure CLI, and validate RBAC permissions. |
| 05 | [Managed Identities](./05-Managed-Identities) | Enable System-assigned Managed Identities, authenticate without secrets, and validate Azure RBAC access. |
| 06 | [Permission Delegation](./06-Permission-Delegation) | Delegate Azure RBAC permissions, understand scope inheritance, and analyze effective permissions. |

---

# Skills Demonstrated

- Azure Role-Based Access Control (RBAC)
- Microsoft Entra ID
- Microsoft Sentinel RBAC
- Azure IAM
- Service Principals
- Managed Identities
- Azure CLI Authentication
- Azure Authorization
- Permission Delegation
- Principle of Least Privilege (PoLP)

---

# Practical Highlights

Throughout this learning path, I successfully:

- Assigned Azure built-in roles
- Configured Microsoft Sentinel permissions
- Created and tested Custom RBAC roles
- Registered Microsoft Entra applications
- Authenticated using Azure Service Principals
- Enabled Managed Identities on Azure VMs
- Authenticated using `az login --identity`
- Delegated Azure permissions to additional users
- Validated Azure RBAC enforcement
- Explored effective permissions and scope inheritance

---

# Key Takeaways

Azure RBAC separates authentication from authorization by integrating Microsoft Entra ID identities with Azure role assignments. Every authorization decision is based on three fundamental components:

- Security Principal
- Role Definition
- Scope

Understanding these concepts is essential for designing secure Azure environments, implementing least-privilege access, and managing enterprise-scale cloud resources.

---

# Related Modules

- Microsoft Sentinel
- Microsoft Defender XDR
- Azure Monitor
- Microsoft Entra ID
- Azure Security
