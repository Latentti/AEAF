---
artifact: phase-09-implementation-governance
title: "Phase 9 · Implementation Governance — worksheet"
type: worksheet
phase: 9
domain: [B, I]
status: stub
owner: "TBD — architecture board"
version: 0.1
links: [architecture-contract, trust-accountability-matrix, guardrail-policy-catalog, eval-suite-specification, autonomy-level-classification, human-agent-raci]
---

# Phase 9 · Implementation Governance

**Purpose.** Compliance reviews; architecture contracts; the **design-time gate**. **ADM analogue:** G. **Agentic addition:** the gate now also approves **guardrails, autonomy level, eval thresholds, oversight mode, and accountability owner**, and authorises the **handoff to the runtime loop**. (→ Book 1 §9, §20; Book 2 §13, §14, §17.5.) Run the **design-time gate checklist** (`checklists/design-time-gate.md`) per agent.

## Inputs
- The reviewed agent designs; the migration plan.

## Steps
1. Complete the architecture compliance review (classical Phase G).
2. Run the **design-time gate** per agent; clear every applicable row with its evidence reference.
3. Produce and sign the **agentic architecture contract** (classical contract + guardrails, autonomy, eval thresholds, oversight, accountability owner).
4. Confirm the **handoff to the runtime loop**: guardrails deployed, monitoring live, owner notified.
5. Move the agent's lifecycle state **Gated → Operating** only on full clearance.

## Produces
- Signed `architecture-contract` (`CON-nnn`) per agent · approved `trust-accountability-matrix` rows · gate decision record.

## Exit gate (must be true before Phase 10)
- [ ] Architecture compliance review completed
- [ ] Design-time gate cleared per agent; agentic architecture contract signed **[+I]**
- [ ] Handoff to the runtime loop confirmed (guardrails deployed, monitoring live, owner notified) **[+I]**
