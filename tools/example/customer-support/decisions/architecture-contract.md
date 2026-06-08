---
artifact: architecture-contract
title: "CON-001 — Agentic Architecture Contract for Gate-Ops Agent"
type: decision
phase: 9
domain: [B, I]
status: approved
owner: "Architecture board"
accountable: "Support Operations Lead (Henna Laaksonen)"
version: 1.0
links: [guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, assurance-case]
---

# CON-001 — Agentic Architecture Contract for Gate-Ops Agent (`AG-002`)

The signed record of what `AG-002` was permitted to be when it crossed from Gated to Operating.

| Field | Entry |
|---|---|
| **Contract ID** | `CON-001` |
| **Agent** | `AG-002` Gate-Ops Agent |
| **Date signed** | 2026-04-02 |
| **Accountability owner** | Support Operations Lead (Henna Laaksonen) |
| **Lifecycle state on signing** | Gated → Operating (L2) |

## Contract terms

| # | Term | What was permitted | Evidence |
|---|---|---|---|
| 0 | Architecture compliance | Conforms to principles `P-1…P-7`, target architecture | Compliance review 2026-04-01 |
| 1 | Guardrails | `G-1` paid-session (pre-action, block+escalate), `G-5` no claimed authority, `G-6` rate limit — all live on `TC-007` | `guardrail-policy-catalog`; vetoes writing to `TC-008` |
| 2 | Autonomy level | `L2` (execute-with-approval); L3 not granted (→ `ADR-001`) | `autonomy-level-classification` Part B |
| 3 | Eval thresholds | `EV-002`: unpaid-open 0%, correct-open ≥ 98%, fixed before run | `eval-suite-specification`; `AC-001` signed |
| 4 | Oversight mode | In-the-loop — operator confirms each open; escalation operator → supervisor | `trust-accountability-matrix`; escalation in `process-function-catalog` `PRC-004` |
| 5 | Accountability owner | Support Operations Lead — one named human | `human-agent-raci` |
| 6 | Handoff readiness | Guardrails live; decision-trail + veto log writing to `TC-008`; owner notified | Monitoring dashboard live 2026-04-02 |

## Signatures
Architecture board (chair: Head of Customer Support) · Support Operations Lead (accountability owner) · Runtime assurance owner.

*A re-gating trigger — a model swap, a new tool, a widening to L3, or a failed `EV-002` — voids this contract and requires a new one before `AG-002` returns to Operating.*
