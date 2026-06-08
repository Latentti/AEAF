---
artifact: phase-06-intelligence-agency
title: "Phase 6 · Intelligence & Agency — worksheet"
type: worksheet
phase: 6
domain: [I]
status: stub
owner: "TBD"
version: 0.1
links: [agent-catalog, model-portfolio, guardrail-policy-catalog, eval-suite-specification, autonomy-level-classification]
---

# Phase 6 · Intelligence & Agency

**Purpose (the new domain).** Architect the population of **models, agents, orchestration, knowledge use, guardrails, evals, and autonomy levels** — where agents are designed as actors, not features. **ADM analogue:** none (new). **Non-negotiable wherever an agent acts.** (→ Book 1 §9, §15; Book 2 §9, §10, §12, §17.3.) This phase's output goes through the **agentic architecture review** (`checklists/agentic-architecture-review.md`) before the gate.

## Inputs
- Capability allocations + autonomy assignments (Phase 2); cognitive substrate (Phase 3); AI platform (Phase 5); intents (the centre).

## Steps
1. Populate the **Agent Catalog**: per agent — purpose, model, tools, autonomy level, guardrails, accountability owner. **[+I]**
2. Populate the **Model Portfolio**: models, providers, costs, risk, agents each powers, TIME stance. **[+I]**
3. Design **orchestration**: how agents, tools, and humans hand work between each other. **[+I]**
4. Populate the **Guardrail/Policy Catalog**: each machine-enforceable policy and the guardrail that enforces it at a named enforcement point; compile runtime-enforced principles into guardrails. **[+I]**
5. Produce the **Eval-Suite Specification** per agent capability: dimensions, cases, thresholds (set before the run). **[+I]**
6. Assign the **autonomy level** per capability on the adopted scale, with the controls each level requires. **[+I]**
7. Choose the **oversight mode** per capability (in/on/out-of-the-loop), with the escalation path. **[+I]**

## Produces
- `agent-catalog` · `model-portfolio` (rationalization side) · `guardrail-policy-catalog` · `eval-suite-specification` · `autonomy-level-classification` Part B · oversight/escalation design.

## Exit gate (must be true before Phase 7)
- [ ] Agent Catalog populated **[+I]**
- [ ] Model Portfolio populated **[+I]**
- [ ] Orchestration designed **[+I]**
- [ ] Guardrail/Policy Catalog populated; runtime principles compiled to guardrails **[+I]**
- [ ] Eval-Suite Specification produced per capability (thresholds fixed before results) **[+I]**
- [ ] Autonomy level assigned per capability, with required controls **[+I]**
- [ ] Oversight mode chosen per capability, with escalation path **[+I]**
- [ ] Agentic architecture review passed (independent reviewer) **[+I]**
