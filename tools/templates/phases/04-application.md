---
artifact: phase-04-application
title: "Phase 4 · Application — worksheet"
type: worksheet
phase: 4
domain: [A, I]
status: stub
owner: "TBD"
version: 0.1
links: [application-portfolio-catalog, process-function-catalog, agent-catalog]
---

# Phase 4 · Application

**Purpose.** Application portfolio, integration, services. **ADM analogue:** C (app). **Agentic addition:** design for **non-determinism** — bounded outputs, fallback paths, human handoff, idempotency, observability of probabilistic components. (→ Book 1 §9, §13; Book 2 §17.3.)

## Inputs
- Capability allocations; the cognitive substrate.

## Steps
1. Document the application portfolio, integration, and services.
2. Design for **non-determinism**: bounded outputs, fallback paths, human-handoff points, idempotency, observability of probabilistic components. **[+I]**
3. For each agent-touched flow, define the behaviour when the model fails or returns low-confidence output. **[+I]**

## Produces
- `application-portfolio-catalog` (with `hostsAgents` links) · non-determinism design notes in `process-function-catalog`.

## Exit gate (must be true before Phase 5)
- [ ] Application portfolio, integration, services documented
- [ ] Non-determinism designed for (bounded outputs, fallback, handoff, idempotency, observability) **[+I]**
- [ ] Each agent-touched flow has a defined behaviour on model fail / low confidence **[+I]**
