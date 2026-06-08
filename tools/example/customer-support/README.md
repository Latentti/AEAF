# Worked example — Parkki Nordic Oy agentic support line

A fully-filled AEAF artifact set for one fictional engagement: **Parkki Nordic Oy**, a Nordic parking operator running an **agentic customer-support line**, brought under AEAF. This is the **target-state, AEAF-governed** version of the service. The just-do-it version it is compared against is `../the-drift/` (Pass 4).

It seeds from a real proof-of-concept (a voice support agent on a model + telephony + tool webhooks); the company, people, figures, and the five-agent fleet are invented for the example.

## How to read it

1. **`00-case-context.md`** — the company, the decision, the agent fleet, what stays human.
2. **`walkthrough.md`** — the AEAF Method run phase by phase for this case (the *why* behind each artifact). Start here for understanding.
3. **`artifacts/new/`** — the nine new AEAF artifacts, filled. The **Agent Catalog** is the hub.
4. **`artifacts/classical/`** — the changed classical artifacts (principles, capabilities, actors, roles, applications, data entities, technology, requirements/intent, process).
5. **`decisions/`** — `ADR-001` (why Gate-Ops is L2), `ADR-002` (EU AI Act risk classification), `CON-001` (the signed contract), `AC-001` (the assurance case).
6. **`checklists/`** — the filled design-time gate for the Gate-Ops agent.
7. **`artifacts/supporting/`** — the **Regulatory Obligations Register** (GDPR / EU AI Act / ePrivacy / PSD2 / EAA → principle → guardrail → evidence). A supporting view, not a core artifact.
8. **`deliverables/`** — the packaged board documents assembled from the artifacts: **Architecture Vision**, **Architecture Definition Document (BDAT+I)**, **Roadmap & Migration Plan**. These are what you hand a board; the artifacts carry the detail they reference.

## Trace one ID across the set

Take `AG-002` (Gate-Ops): it runs model `M-001`, draws on corpora `KC-002`/`KC-001`, is bounded by guardrails `G-1`/`G-3`/`G-4`/`G-5`/`G-6`/`G-7`, sits at autonomy `L2`, is assured by eval suite `EV-002` and assurance case `AC-001`, is permitted by contract `CON-001`, and is answerable through the Support Operations Lead in the RACI and the Trust & Accountability Matrix. Every one of those IDs resolves — that is the coherence test.

## Validate it

This set is checked by the deterministic linter:

```sh
python3 ../../validate/aeaf_validate.py . --report
```

It passes with zero errors — every cross-reference resolves, no accountability owner is an agent, oversight modes are consistent with autonomy levels, and every runtime principle compiles to a guardrail. The example is provably coherent, not just plausibly so.
