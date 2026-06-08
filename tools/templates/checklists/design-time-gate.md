---
artifact: design-time-gate
title: Design-Time Gate Checklist (Phase 9)
type: checklist
phase: 9
domain: [B, I]
status: approved
version: 1.0
links: [architecture-contract, guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, assurance-case]
---

# Design-Time Gate Checklist

**What it is.** The instrument the **architecture board** runs at Phase 9, per agent, before it operates. Row 0 is the classical Phase-G compliance review; rows 1–6 are AEAF's additions. An agent does not cross from *Gated* to *Operating* until every applicable row clears **with its evidence reference** and the agentic architecture contract is signed. A check with no evidence reference does not count. (→ Book 2 §17.5; Book 1 §20.)

| # | Gate check | Cleared when | Owner | Evidence |
|---|---|---|---|---|
| 0 | **Architecture compliance** | Conforms to principles, standards, target architecture. | Architecture board | Compliance review record |
| 1 | **Guardrails** | Every hard bound enforced by a deployed guardrail at a named enforcement point, fail-closed where consequence demands. | Guardrail/Policy owner | `guardrail-policy-catalog`; guardrails live |
| 2 | **Autonomy level** | The level on the L0–L4 scale is justified against consequence; required controls present. | Architecture board | `autonomy-level-classification` |
| 3 | **Eval thresholds** | Thresholds fixed before results were seen; assurance case argues they are met. | Runtime assurance owner | `eval-suite-specification`; signed `assurance-case` |
| 4 | **Oversight mode** | in/on/out-of-the-loop chosen for the consequence, with a defined escalation path. | Accountability owner | `trust-accountability-matrix`; escalation design |
| 5 | **Accountability owner** | Exactly one named human/role, recorded before the agent acts. | Named at the gate | `human-agent-raci` |
| 6 | **Handoff readiness** | Guardrails deployed, monitoring + decision-trail capture live, owner notified. | Runtime assurance owner | Monitoring dashboard live; veto log writing |

- [ ] All applicable rows above cleared, each with its evidence reference
- [ ] **Agentic architecture contract signed and stored** (`CON-nnn`) — the classical contract plus rows 1–6
- [ ] Gate weight matched to consequence (light subset for a reversible in-the-loop copilot; every row + full assurance + red-team for a high-consequence out-of-the-loop agent)
- [ ] Lifecycle state moved **Gated → Operating** only on full clearance

**Common failure.** A box checked without an evidence reference. The reviewer's standing question is the cheapest quality control AEAF has: *show me the artifact that makes this true.*
