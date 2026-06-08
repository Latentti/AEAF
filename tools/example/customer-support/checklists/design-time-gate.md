---
artifact: design-time-gate
title: "Design-Time Gate — Gate-Ops Agent (AG-002)"
type: checklist
phase: 9
domain: [B, I]
status: approved
version: 1.0
links: [architecture-contract, guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, assurance-case]
---

# Design-Time Gate — Gate-Ops Agent (`AG-002`), 2026-04-02

The architecture board's gate run for `AG-002`. Every row cleared **with its evidence reference**; a box without evidence does not count.

| # | Gate check | Cleared when | Owner | Evidence | ✓ |
|---|---|---|---|---|---|
| 0 | Architecture compliance | Conforms to `P-1…P-7`, target architecture | Architecture board | Compliance review 2026-04-01 | ✅ |
| 1 | Guardrails | `G-1`/`G-5`/`G-6` live on `TC-007`, fail-closed | Support Operations Lead | `guardrail-policy-catalog`; vetoes writing to `TC-008` | ✅ |
| 2 | Autonomy level | `L2` justified vs consequence; controls present; L3 withheld | Architecture board | `autonomy-level-classification`; `ADR-001` | ✅ |
| 3 | Eval thresholds | `EV-002` thresholds fixed before run; assurance case argues they hold | Runtime assurance owner | `eval-suite-specification`; `AC-001` | ✅ |
| 4 | Oversight mode | In-the-loop; operator confirms each open; escalation defined | Support Operations Lead | `trust-accountability-matrix`; `PRC-004` | ✅ |
| 5 | Accountability owner | One named human (Support Operations Lead) | Named at gate | `human-agent-raci` | ✅ |
| 6 | Handoff readiness | Guardrails deployed; monitoring + decision trail live; owner notified | Runtime assurance owner | dashboard live 2026-04-02; `TC-008` writing | ✅ |

- [x] All applicable rows cleared, each with its evidence reference
- [x] **Agentic architecture contract signed and stored** — `CON-001`
- [x] Gate weight matched to consequence — full rows run because the agent opens a physical gate
- [x] Lifecycle state moved **Gated → Operating (L2)** on full clearance

*The board explicitly did **not** clear row 2 for L3: the evidence (Helsinki daytime only) does not cover the autonomy requested. L2 was granted, L3 deferred to the 2026-09-01 review — the gate doing its job, not rubber-stamping.*
