---
artifact: requirements-intent-specification
title: Architecture Requirements & Intent Specification
type: deliverable
phase: 1
domain: [B, I]
status: stub
owner: "TBD — lead architect"
version: 0.1
links: [requirements-intent-catalog, eval-suite-specification, guardrail-policy-catalog]
---

# Architecture Requirements & Intent Specification

**Deliverable.** The formal, reviewable statement of what the architecture must satisfy. In AEAF it carries two kinds of requirement: **deterministic requirements** (specified, tested) and **intent records** (outcome + bounds, evaluated) — because probabilistic work cannot be fully specified. It assembles the Requirements & Intent Catalog and binds each intent to its acceptance evidence.

## Sections

| Section | What to record / assemble |
|---|---|
| **Deterministic requirements** | The classical, testable requirements (MoSCoW). |
| **Intent records** *(+I)* | Per intent: outcome, bounds, acceptance signal (→ `requirements-intent-catalog`). |
| **Acceptance evidence** | The eval suite + thresholds that say each intent is met (→ `eval-suite-specification`). |
| **Enforced bounds** | The guardrails that hold the intent's hard bounds (→ `guardrail-policy-catalog`). |
| **Traceability** | Each requirement/intent → the artifact and the assurance that satisfies it. |
| **Sign-off** | Architecture board. |

**The discipline this deliverable enforces:** an intent without an acceptance signal is a wish; a hard bound without a guardrail is unenforced. Every row resolves to evidence.
