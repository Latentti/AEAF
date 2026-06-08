---
artifact: phase-00-preliminary
title: "Phase P · Preliminary — worksheet"
type: worksheet
phase: P
domain: [B, I]
status: stub
owner: "TBD — architecture board"
version: 0.1
links: [principles-catalog, autonomy-level-classification, agent-catalog, model-portfolio, guardrail-policy-catalog]
---

# Phase P · Preliminary

**Purpose.** Stand up the architecture capability; establish principles, governance, and the repository; characterize the agentic operating context and risk appetite. **ADM analogue:** Preliminary. **Agentic addition:** define the autonomy-level scheme and the accountability model up front, and add agentic principles (incl. runtime-enforced). (→ Book 1 §9; Book 2 §17.3.)

## Inputs
- Enterprise strategy, regulatory exposure, existing EA capability (if any).

## Steps
1. Stand up the architecture capability; assign roles, **including the new agentic roles** (agent owner, runtime assurance owner, AI-risk). **[+I]**
2. Establish architecture principles, **each with an Enforcement attribute** (advisory / design-time / runtime). **[+I]**
3. Provision the repository and stub the agentic artifact set (Agent Catalog, Model Portfolio, Guardrail/Policy Catalog, others). **[+I]**
4. Characterize the agentic operating context: where agents will act, the consequence/risk appetite, regulatory exposure. **[+I]**
5. Adopt the **Autonomy-Level Classification scale** (the canonical L0–L4) for the enterprise. **[+I]**
6. Define the **accountability model**: accountability is held by a named human/role per capability and never transfers to an agent. **[+I]**

## Produces
- `principles-catalog` (with Enforcement) · `autonomy-level-classification` Part A (the scale) · stubbed `agent-catalog`, `model-portfolio`, `guardrail-policy-catalog`.

## Exit gate (must be true before Phase 1)
- [ ] Architecture capability stood up; agentic roles assigned **[+I]**
- [ ] Principles established, each with an Enforcement attribute **[+I]**
- [ ] Repository + agentic artifact set provisioned **[+I]**
- [ ] Agentic operating context + risk appetite characterized **[+I]**
- [ ] Autonomy-Level Classification scheme adopted **[+I]**
- [ ] Accountability model defined (named human per capability; never an agent) **[+I]**
