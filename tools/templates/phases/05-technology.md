---
artifact: phase-05-technology
title: "Phase 5 · Technology — worksheet"
type: worksheet
phase: 5
domain: [T, I]
status: stub
owner: "TBD"
version: 0.1
links: [technology-portfolio-catalog, model-portfolio, guardrail-policy-catalog]
---

# Phase 5 · Technology

**Purpose.** Infrastructure, platforms, security. **ADM analogue:** D. **Agentic addition:** the **AI platform** — inference, model gateways, vector stores, orchestration/agent runtime, the LLMOps substrate. (→ Book 1 §9, §14; Book 2 §11, §17.3.)

## Inputs
- Application architecture; the cognitive substrate; the models needed.

## Steps
1. Document infrastructure, platforms, and security architecture.
2. Specify the **AI platform**: inference, model gateway, vector store, and the orchestration / agent runtime. **[+I]**
3. Specify the **LLMOps substrate**: where evals run, where guardrails are enforced, where decision trails are captured. **[+I]**
4. Begin the **Model Portfolio** (platform and gateways side).

## Produces
- `technology-portfolio-catalog` (AI platform components; guardrail-enforcement points) · `model-portfolio` (platform side).

## Exit gate (must be true before Phase 6)
- [ ] Infrastructure, platforms, security documented
- [ ] AI platform specified (inference, gateway, vector store, agent runtime) **[+I]**
- [ ] LLMOps substrate specified (evals, guardrail enforcement, decision-trail capture) **[+I]**
