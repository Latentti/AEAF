---
artifact: role-catalog
title: "Role Catalog — Parkki Nordic support line"
type: catalog
phase: 2
domain: [B]
status: approved
owner: "Head of Customer Support (Antti Salo)"
version: 1.0
links: [organization-actor-catalog, actor-role-matrix, autonomy-level-classification]
---

# Role Catalog — Parkki Nordic support line

Roles with their permitted performer-type. "Agent-eligible" is a permission; the actual autonomy is set in the Autonomy-Level Classification.

| Role ID | Role name | Permitted performer-type | Capabilities | Notes |
|---|---|---|---|---|
| `ROLE-001` | Contact triager | agent-eligible | `CAP-001` | reversible routing |
| `ROLE-002` | Gate resolver | hybrid | `CAP-002` | physical action; operator confirms at go-live |
| `ROLE-003` | Billing explainer | agent-eligible | `CAP-003` | read-only explanation |
| `ROLE-004` | Refund approver (≤ €50) | hybrid | `CAP-007` | agent recommends, human approves |
| `ROLE-005` | Refund approver (> €50 / contested) | human-only | `CAP-007` | money + dispute (`P-4`) |
| `ROLE-006` | ANPR corrector | hybrid | `CAP-004` | bounded record change |
| `ROLE-007` | Account / GDPR handler | human-only | `CAP-005` | regulated |
| `ROLE-008` | Safety responder | human-only | `CAP-006` | safety (`P-2`) |
| `ROLE-009` | Escalation router | agent-eligible | `CAP-008` | reversible routing |
