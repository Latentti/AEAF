---
artifact: human-agent-raci
title: Human-Agent RACI / Decision-Authority Matrix
type: matrix
phase: 2
domain: [B, I]
status: stub
owner: "TBD — capability owner"
accountable: "TBD — named human; never an agent"
as_of: TBD
version: 0.1
links: [autonomy-level-classification, trust-accountability-matrix, capability-automation-frontier-map, agent-catalog]
---

# Human-Agent RACI / Decision-Authority Matrix

**What it is.** The split of Responsibility and Accountability between human and agent actors per capability, and — its decision-authority face — which decisions an agent may make alone, which need a human, and which a human makes with agent input. It makes the rule **accountability never transfers to an agent** operational: an agent may be *Responsible* for execution; it is never *Accountable*. Rows are capabilities or decisions; columns are the actors involved.
**Produced in.** Phase 2 · Business & Capability.
**Instantiates.** `Capability Allocation` × `Actor`, anchored by `Accountability Owner`; decision rights expressed against `Oversight Control`.
**Defined in.** Book 1 §21.4.5 · templated in Book 2 §15.6.

## Template — capability/decision rows × actor columns

Each cell is **R / A / C / I**, with the binding rule: **A is always a named human.** For each agent-Responsible cell, also record the **autonomy level** and **oversight mode** that apply.

| Capability / decision | Agent | Human role(s) | Accountability owner | Decision-authority band | Escalation target |
|---|---|---|---|---|---|
| *(capability or decision)* | R / C / I *(+ level, oversight)* | R / A / C / I | **A** *(named human)* | agent-alone / agent-proposes-human-approves / human-alone | *(who/what it escalates to)* |

## Filled rows

<!-- example — replace with your own capability decomposition -->

| Capability / decision | Agent `AG-001` | Human advisor | Owner *(named)* | AI-risk reviewer | Decision-authority band | Escalation target |
|---|---|---|---|---|---|---|
| *(routine, reversible step)* | **R** (L3, on-loop) | C | **A** | I | agent-alone | Advisor on mismatch |
| *(assess / decide step, standard)* | **R** (L1→L3) | C → I | **A** | I | agent-proposes-human-approves | Advisor |
| *(sensitive / vulnerable case)* | I (routes only) | **R** | **A** | C | **human-alone** (principle `P-n`) | Senior advisor |
| *(high-consequence, irreversible)* | I | C | **R / A** | C | **human-alone** (board appetite) | Committee |
| Set/raise the agent's autonomy level | I | I | C | **R** (recommends) | governance gate decides | Architecture gate |

*In every row the **A** sits on a human. The agent is **R** only where the work is routine and reversible; the human-alone rows are the frontier the enterprise pre-decided the agent can never cross.*

## Common mistakes (→ Book 2 §15.6)

- **Putting an A on the agent.** The most consequential error in the set. An agent is never Accountable. If a cell tempts you to mark the agent A, you have not yet named the human who answers for it.
- **One RACI for the whole capability.** Decompose to the decision level — "offer a standard arrangement" and "approve a write-off" have opposite allocations.
- **Recording responsibility but not the decision band.** "Agent is R" does not say whether it acts alone or proposes-for-approval.
- **No escalation target.** A row with no escalation path has no designed handoff. Escalation is a designed path, not a failure.
