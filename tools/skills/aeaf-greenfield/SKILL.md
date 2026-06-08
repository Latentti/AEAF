---
name: aeaf-greenfield
description: Design a new agentic service with AEAF from the start — Vision through the design-time gate (greenfield). Use when no implementation exists yet and the user wants to architect an agentic capability the right way before building it — e.g. "design our new agentic service with AEAF", "we want to build an agent for X, do it properly", "run AEAF on this new idea". Walks the method phases in order, producing the full artifact set and ending at a signed architecture contract, so the build starts from a governed design rather than drifting into a PoC.
---

# AEAF Greenfield (new build)

When the service does not exist yet, design it under AEAF before a line of it ships — so it starts as a governed capability, not a demo that later has to be rescued. The counterpart to `aeaf-retrofit`: same destination, but starting from intent instead of from code.

## When to use
- A new agentic capability is being planned and nothing is built.
- The user wants the design done to AEAF discipline up front.

## Inputs you need
- The business outcome the capability should achieve and its consequence/risk profile.
- The Preliminary foundations (or build them): principles with Enforcement, the autonomy scale, the accountability model.

## Procedure — walk the method (use the phase worksheets)
1. **Preliminary** (`phases/00-preliminary.md`) — stand up principles (with Enforcement), the autonomy scale, the accountability model, the operating context.
2. **Vision** (`phases/01-vision.md`) — drivers, the human–agent ambition, the consequence/risk envelope, the intent records.
3. **Business & Capability** (`phases/02-business-capability.md`) — run `aeaf-allocate`: capability model, allocation, frontier map, RACI, autonomy assignment.
4. **Data & Knowledge** (`phases/03-data-knowledge.md`) — the cognitive substrate and the Knowledge-Corpus Catalog.
5. **Application** (`phases/04-application.md`) — design for non-determinism: bounded outputs, fallback, handoff, observability.
6. **Technology** (`phases/05-technology.md`) — the AI platform and LLMOps substrate; begin the Model Portfolio.
7. **Intelligence & Agency** (`phases/06-intelligence-agency.md`) — the agents, the Model Portfolio, `aeaf-guardrails` for the Guardrail/Policy Catalog, `aeaf-evals` for the Eval-Suite Specification, the autonomy + oversight per capability.
8. **Opportunities & Migration** (`phases/07…`, `08…`) — sequence by trust earned; plan frontier moves and the human transition.
9. **Governance** (`phases/09…`) — `aeaf-govern`: the pre-gate review, then the design-time gate and the signed architecture contract.
10. **Change & Runtime Assurance** (`phases/10…`) — stand up the runtime loop before go-live.

## Outputs
- The full AEAF artifact set for the new capability, ending at a signed agentic architecture contract and a runtime loop ready to operate.

## Quality bar
- **Scope to the work** — a single agent deployment needs Phases 2, 6, 9–10 and the centre; a full transformation uses all of them. Phase 6 and the runtime loop are non-negotiable wherever an agent acts.
- **Intent, not specification** — declare outcome + bounds for the probabilistic work and assure it; do not write a probabilistic agent as a fully-specified requirement.
- All the per-artifact and gate rules apply.

## Hand off to
- `aeaf-allocate`, `aeaf-guardrails`, `aeaf-evals`, `aeaf-govern` at the phases above; `aeaf-maturity` first if the entry point and scope are unclear.
