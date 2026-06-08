---
artifact: organization-actor-catalog
title: Organization / Actor Catalog
type: catalog
phase: 2
domain: [B]
status: stub
owner: "TBD"
version: 0.1
links: [agent-catalog, role-catalog, actor-role-matrix]
---

# Organization / Actor Catalog

**Classical artifact; changed for the Agentic Enterprise.** Now lists **agent actors and hybrid teams** alongside human actors, and gains an **actor-type** attribute (human / agent / hybrid). An agent's row links out to its Agent Catalog entry — the depth lives there; this catalog stays lightweight. (→ Book 1 Table 21.1.)

## Template — one actor per row

| Field | What to record |
|---|---|
| **Actor ID** | `ACT-nnn`. |
| **Name** | Actor / role / team name. |
| **Actor type** *(new)* | human / agent / hybrid team. |
| **Org unit** | Where it sits. |
| **Agent Catalog link** *(new, if agent/hybrid)* | `AG-nnn` (→ `agent-catalog`). |
| **Accountability owner** *(if agent/hybrid)* | Named human answerable. Never an agent. |

## Filled rows

<!-- example -->

| Actor ID | Name | Actor type | Org unit | Agent Catalog link | Accountability owner |
|---|---|---|---|---|---|
| `ACT-001` | *(human role)* | human | Service Ops | — | — |
| `ACT-002` | *(agent name)* | agent | Service Ops | `AG-001` | *(named human)* |
| `ACT-003` | *(team name)* | hybrid team | Service Ops | `AG-001` + humans | *(named human)* |

**Watch.** The new object is the *agent actor* and the *hybrid team*; model them as actors, not as applications. The single most consequential field is the accountability owner for any agent/hybrid row — always a named human.
