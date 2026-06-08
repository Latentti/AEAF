---
artifact: application-portfolio-catalog
title: Application Portfolio Catalog
type: catalog
phase: 4
domain: [A]
status: stub
owner: "TBD"
version: 0.1
links: [agent-catalog, technology-portfolio-catalog]
---

# Application Portfolio Catalog

**Classical artifact; changed for the Agentic Enterprise.** An application that **hosts an agent runtime** gains a `hostsAgents` link to the Agent Catalog. The application is the runtime; the agent is modelled separately. One application can host many agents. (→ Book 1 Table 21.1; Book 1 §4.2 — agent ≠ application.)

## Template — one application per row

| Field | What to record |
|---|---|
| **App ID** | `APP-nnn`. |
| **Name** | Application/service name. |
| **Purpose** | What the service does. |
| **Hosts agents** *(new)* | `AG-nnn` it hosts (→ `agent-catalog`). |
| **Integration points** | APIs/contracts it exposes/consumes. |
| **TIME disposition** | Tolerate / Invest / Migrate / Eliminate. |
| **Owner** | Service owner. |

## Filled rows

<!-- example -->

| App ID | Name | Purpose | Hosts agents | Integration points | TIME | Owner |
|---|---|---|---|---|---|---|
| `APP-001` | *(agent runtime service)* | hosts and serves the support agents | `AG-001`, `AG-002` | telephony, tool webhooks | Invest | *(named owner)* |

**Watch.** Do not collapse "we changed the AI" into the application record. A model swap is a Model Portfolio change, a new tool is an Agent Catalog change, a re-platform is an application change — three different changes, three different owners, three traceability paths.
