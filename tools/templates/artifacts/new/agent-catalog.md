---
artifact: agent-catalog
title: Agent Catalog
type: catalog
phase: 6
domain: [I]
status: stub
owner: "TBD — named human/role answerable for this catalog's currency"
as_of: TBD
version: 0.1
links: [model-portfolio, knowledge-corpus-catalog, guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, capability-automation-frontier-map]
---

# Agent Catalog

**What it is.** The authoritative register of every agent actor in the enterprise — what each is for, what powers it, what bounds it, and who answers for it. It is the **hub** of the artifact set: an auditor, an incident responder, or an architect starts here and follows the links to the other eight artifacts. One row per agent actor (not per service).
**Produced in.** Phase 6 · Intelligence & Agency, seeded by the Phase 2 capability allocations.
**Instantiates.** `Agent Actor`, with foreign keys to `Model`, `Knowledge Corpus`, `Guardrail`, `Autonomy Level`, `Action/Tool`, `Eval Suite`, `Accountability Owner`.
**Defined in.** Book 1 §21.4.1 · templated in Book 2 §15.2.

## Template — one agent per row

| Field | What to record |
|---|---|
| **Agent ID** | Stable identifier, e.g. `AG-nnn`. Never reuse on retirement. |
| **Name** | Human-readable agent name. |
| **Purpose / objective** | One sentence: the outcome it pursues **and what it explicitly does *not* do**. |
| **Capability(ies) performed** | The capability-model leaf/leaves it is allocated to (→ `business-capability-catalog`, `capability-automation-frontier-map`). |
| **Model(s) run** | Model ID(s) from the Model Portfolio (→ `model-portfolio`). |
| **Knowledge corpora** | Corpus ID(s) it retrieves from (→ `knowledge-corpus-catalog`). |
| **Tools / actions** | Each action it may invoke, with permission and reversibility (read / write / irreversible-write). |
| **Guardrails** | Guardrail IDs that bound it (→ `guardrail-policy-catalog`). |
| **Autonomy level** | Assigned level from the scale (→ `autonomy-level-classification`), with go-live vs. target. |
| **Oversight mode** | in / on / out-of-the-loop at the current level. |
| **Eval suite** | Suite ID that assures it (→ `eval-suite-specification`). |
| **Accountability owner** | Named human/role answerable (→ `trust-accountability-matrix`). **Never an agent.** |
| **Lifecycle status** | proposed / gated / operating / contained / retired. |

## Filled row

<!-- example — replace with your own agents -->

| Field | Value |
|---|---|
| **Agent ID** | `AG-001` |
| **Name** | *(agent name)* |
| **Purpose / objective** | *(one sentence: outcome pursued; explicit "does not …")* |
| **Capability(ies) performed** | `CAP-nnn` *(leaf capability names)* |
| **Model(s) run** | `M-nnn` |
| **Knowledge corpora** | `KC-nnn` |
| **Tools / actions** | *(tool — read / write / irreversible-write)* |
| **Guardrails** | `G-1 … G-n` |
| **Autonomy level** | `L1` at go-live; `L3` target on assurance |
| **Oversight mode** | In-the-loop |
| **Eval suite** | `EV-nnn` |
| **Accountability owner** | *(named human/role)* |
| **Lifecycle status** | operating |

## Common mistakes (→ Book 2 §15.2)

- **Cataloguing the application, not the agent.** The runtime that hosts the agent is an Application Component; the agent is a separate entity. One row per agent actor.
- **Leaving the accountability owner as a team or "the platform."** It must be one named human or role.
- **Recording the model inline instead of by reference.** Put the model in the Model Portfolio and link by ID, so a model change is made in one place.
- **A "general AI assistant" row with no bounded purpose.** If the purpose cannot be stated in one sentence with an explicit *not*, the agent is not yet specified enough to catalog.
