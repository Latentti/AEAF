---
artifact: process-function-catalog
title: Process / Function Catalog
type: catalog
phase: 2
domain: [B]
status: stub
owner: "TBD"
version: 0.1
links: [business-capability-catalog, agent-catalog, human-agent-raci]
---

# Process / Function Catalog

**Classical artifact; changed for the Agentic Enterprise.** A process step gains the **actor-type** that performs it and, where an agent, its **oversight mode** and **escalation** path. (→ Book 1 Table 21.1.)

## Template — one process step per row

| Field | What to record |
|---|---|
| **Step ID** | `PRC-nnn`. |
| **Process · step** | The process and the step within it. |
| **Capability** | Capability it realises (→ `business-capability-catalog`). |
| **Actor-type** *(new)* | human / agent / hybrid. |
| **Oversight mode** *(new, if agent)* | in / on / out-of-the-loop. |
| **Escalation path** *(new, if agent)* | trigger → target → fallback. |
| **Behaviour on model fail / low confidence** *(new, if agent)* | the defined fallback. |

## Filled rows

<!-- example -->

| Step ID | Process · step | Capability | Actor-type | Oversight mode | Escalation path | On model fail / low confidence |
|---|---|---|---|---|---|---|
| `PRC-001` | *(intake · verify)* | `CAP-001` | agent | on-the-loop | low match → advisor → hold | route to human, preserve context |
| `PRC-002` | *(decide · sensitive)* | `CAP-009` | human | — | — | — |

**Watch.** Every agent-touched step needs a defined behaviour when the model fails or returns low-confidence output — this is the Phase 4 non-determinism design surfacing at the process level.
