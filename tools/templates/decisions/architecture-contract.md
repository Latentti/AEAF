---
artifact: architecture-contract
title: "Agentic Architecture Contract — CON-nnn"
type: decision
phase: 9
domain: [B, I]
status: stub
owner: "TBD — architecture board"
accountable: "TBD — named human; never an agent"
version: 0.1
links: [guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, assurance-case]
---

# CON-nnn — Agentic Architecture Contract for (agent)

**What it is.** The signed record, produced at the design-time gate (Phase 9), of **what an agent was permitted to be**. It is the classical architecture contract **plus** the six agentic rows the gate approves: guardrails, autonomy level, eval thresholds, oversight mode, accountability owner, and handoff readiness. An agent does not cross from *Gated* to *Operating* until this is signed. (→ Book 2 §17.5; Book 1 §20.)

| Field | Entry |
|---|---|
| **Contract ID** | `CON-nnn` |
| **Agent** | `AG-nnn` (→ `agent-catalog`) |
| **Date signed** | `YYYY-MM-DD` |
| **Accountability owner** | *(named human/role — never an agent)* |
| **Lifecycle state on signing** | Gated → Operating |

## The contract terms

| # | Term | What was permitted | Evidence |
|---|---|---|---|
| 0 | **Architecture compliance** | Conforms to principles, standards, target architecture. | Compliance review record |
| 1 | **Guardrails** | The guardrails deployed, each at a named enforcement point, fail-closed where consequence demands. | `guardrail-policy-catalog` entries; guardrails live |
| 2 | **Autonomy level** | The level on the L0–L4 scale, justified against consequence; required controls present. | `autonomy-level-classification` entry |
| 3 | **Eval thresholds** | The thresholds (fixed before results); the assurance case argues they are met. | `eval-suite-specification`; signed `assurance-case` |
| 4 | **Oversight mode** | in / on / out-of-the-loop, with the escalation path. | `trust-accountability-matrix` entry; escalation design |
| 5 | **Accountability owner** | Exactly one named human/role. | `human-agent-raci` entry |
| 6 | **Handoff readiness** | Guardrails deployed, monitoring + decision-trail capture live, owner notified. | Monitoring dashboard live; veto log writing |

## Signatures
*Architecture board · accountability owner · runtime assurance owner.*

**The contract is the record of what the agent was permitted to be.** A re-gating trigger (material change / widened autonomy / failed assurance) voids it and requires a new contract before the agent returns to Operating.
