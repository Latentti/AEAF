---
artifact: role-catalog
title: Role Catalog
type: catalog
phase: 2
domain: [B]
status: stub
owner: "TBD"
version: 0.1
links: [organization-actor-catalog, actor-role-matrix, autonomy-level-classification]
---

# Role Catalog

**Classical artifact; changed for the Agentic Enterprise.** Gains a **permitted-performer-type** attribute: which actor kinds may fill the role — human-only, agent-eligible, or hybrid. A role may now be filled by a human, an agent, or a hybrid team. (→ Book 1 Table 21.1.)

## Template — one role per row

| Field | What to record |
|---|---|
| **Role ID** | `ROLE-nnn`. |
| **Role name** | Outcome-named role. |
| **Permitted performer-type** *(new)* | human-only / agent-eligible / hybrid. |
| **Capabilities** | Capabilities the role performs (→ `business-capability-catalog`). |
| **Notes** | Why a performer-type is constrained (e.g. a regulated decision is human-only). |

## Filled rows

<!-- example -->

| Role ID | Role name | Permitted performer-type | Capabilities | Notes |
|---|---|---|---|---|
| `ROLE-001` | *(routine handler)* | agent-eligible | `CAP-001` | reversible, in-policy |
| `ROLE-002` | *(decision authority)* | human-only | `CAP-009` | irreversible / regulated |

**Watch.** "Agent-eligible" is a permission, not an assignment — the actual autonomy at which an agent fills the role is recorded in the Autonomy-Level Classification and the Actor/Role Matrix.
