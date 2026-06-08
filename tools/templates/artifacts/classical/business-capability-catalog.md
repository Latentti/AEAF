---
artifact: business-capability-catalog
title: Business Capability Catalog / Map
type: catalog
phase: 2
domain: [B]
status: stub
owner: "TBD"
version: 0.1
links: [capability-automation-frontier-map, human-agent-raci, autonomy-level-classification, agent-catalog]
---

# Business Capability Catalog / Map

**Classical artifact; changed for the Agentic Enterprise.** Each capability gains its **current performer mix and autonomy level** — the hook the Capability Automation-Frontier Map overlays. Capabilities stay **outcome-named and actor-agnostic** ("Settle a claim", not "a handler settles a claim"); the actor-agnosticism is precisely what lets work be reallocated between humans and agents without rewriting the model. (→ Book 1 Table 21.1, §4.5.)

## Template — one capability (leaf) per row

| Field | What to record |
|---|---|
| **Capability ID** | `CAP-nnn`. |
| **Capability (outcome name)** | Actor-agnostic outcome. |
| **Parent / level** | Position in the capability hierarchy. |
| **Performer mix** *(new)* | human / agent / hybrid, with proportion if split by sub-case. |
| **Autonomy level** *(new, if agent/hybrid)* | `L0`–`L4` (→ `autonomy-level-classification`). |
| **Accountability owner** *(new, if agent/hybrid)* | Named human. |
| **Agent(s)** *(new)* | `AG-nnn` performing it (→ `agent-catalog`). |

## Filled rows

<!-- example -->

| Capability ID | Capability (outcome name) | Parent / level | Performer mix | Autonomy level | Accountability owner | Agent(s) |
|---|---|---|---|---|---|---|
| `CAP-001` | *(routine outcome)* | *(L2 leaf)* | agent | `L3` | *(named human)* | `AG-001` |
| `CAP-009` | *(high-consequence outcome)* | *(L2 leaf)* | human | n/a | *(named human)* | — |

**Watch.** Keep the capability name actor-agnostic. If it names a performer, moving it to an agent forces a model change; defined outcome-first, the allocation simply changes.
