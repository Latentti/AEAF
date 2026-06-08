---
artifact: organization-actor-catalog
title: "Organization / Actor Catalog — Parkki Nordic support line"
type: catalog
phase: 2
domain: [B]
status: approved
owner: "Head of Customer Support (Antti Salo)"
version: 1.0
links: [agent-catalog, role-catalog, actor-role-matrix]
---

# Organization / Actor Catalog — Parkki Nordic support line

Human, agent, and hybrid actors in the support line. Agent rows link to the Agent Catalog; the depth lives there.

| Actor ID | Name | Actor type | Org unit | Agent Catalog link | Accountability owner |
|---|---|---|---|---|---|
| `ACT-001` | Support operator | human | Customer Support | — | Support Operations Lead |
| `ACT-002` | Billing operator | human | Billing | — | Billing Lead |
| `ACT-003` | Data / ANPR operator | human | Data Ops | — | Data Lead |
| `ACT-004` | Safety responder (24/7 line) | human | Operations | — | Support Operations Lead |
| `ACT-005` | Triage Agent | agent | Customer Support | `AG-001` | Support Operations Lead |
| `ACT-006` | Gate-Ops Agent | agent | Customer Support | `AG-002` | Support Operations Lead |
| `ACT-007` | Billing-Dispute Agent | agent | Billing | `AG-003` | Billing Lead |
| `ACT-008` | ANPR-Correction Agent | agent | Data Ops | `AG-004` | Data Lead |
| `ACT-009` | Escalation-Router Agent | agent | Customer Support | `AG-005` | Support Operations Lead |
| `ACT-010` | Gate-resolution team | hybrid team | Customer Support | `AG-002` + `ACT-001` | Support Operations Lead |

*Every agent and hybrid row carries a named human accountability owner. The agents are modelled as actors, not as the application that hosts them (that is `APP-001` in the Application Portfolio).*
