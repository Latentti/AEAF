---
artifact: requirements-intent-catalog
title: Requirements & Intent Catalog
type: catalog
phase: 1
domain: [B, I]
status: stub
owner: "TBD"
version: 0.1
links: [eval-suite-specification, guardrail-policy-catalog, assurance-case]
---

# Requirements & Intent Catalog

**Classical artifact; changed for the Agentic Enterprise.** The Requirements Catalog is **supplemented, not replaced**, by **Intent** records for non-deterministic work. A deterministic requirement specifies *what to build and how it must behave*, case by case, verified by testing. An **intent** declares *what outcome to achieve and within what limits*, and is measured by evals — the right tool for probabilistic work where the steps cannot be fully specified. Intent pairs with assurance. (→ Book 1 Table 21.1; Book 1 §4.6.2, §17.)

## Template — requirements and intents

**Deterministic requirements** (classical, unchanged):

| Req ID | Requirement | Acceptance test | Priority (MoSCoW) |
|---|---|---|---|
| `REQ-nnn` | *(specified behaviour)* | *(pass/fail test)* | Must |

**Intent records** (new, for agent/probabilistic work):

| Field | What to record |
|---|---|
| **Intent ID** | `INT-nnn`. |
| **Outcome** | What good looks like (the desired outcome). |
| **Bounds** | The hard limits ("never exceed €X without approval"; "always cite the clause"). |
| **Acceptance signal** | The eval dimension + threshold that says it is met (→ `eval-suite-specification`). |
| **Enforced by** | The guardrails that hold the bounds (→ `guardrail-policy-catalog`). |
| **Assured by** | The assurance case (→ `assurance-case`). |

## Filled intent

<!-- example -->

| Field | Value |
|---|---|
| **Intent ID** | `INT-001` |
| **Outcome** | *(resolve the request fairly and within policy; correct result + clear explanation)* |
| **Bounds** | *(never exceed the disputed amount; never exceed €500 goodwill without escalation; always cite policy)* |
| **Acceptance signal** | Quality ≥ 95%, safety out-of-policy = 0% (`EV-001`) |
| **Enforced by** | `G-1`, `G-2` |
| **Assured by** | `AC-001` |

**Watch.** Do not write a probabilistic agent's behaviour as a fully-specified requirement — you cannot enumerate its steps. Declare intent + bounds, then evaluate. Putting a probabilistic component behind a "tested once, signed off" gate is a category error.
