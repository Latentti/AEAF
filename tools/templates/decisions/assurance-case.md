---
artifact: assurance-case
title: "Assurance Case — AC-nnn"
type: decision
phase: 6
domain: [I]
status: stub
owner: "TBD — runtime assurance owner"
accountable: "TBD — named human"
as_of: TBD
version: 0.1
links: [eval-suite-specification, guardrail-policy-catalog, trust-accountability-matrix, requirements-intent-catalog]
---

# AC-nnn — Assurance Case for (agent)

**What it is.** The structured argument and evidence that an agent is **fit to operate within its bounds**, with residual risk stated. It is the document an auditor or a board reads — not a one-time sign-off memo but a **living argument, reviewed and dated**. Assurance is a continuing state, not an event: an agent that passed its evals in one quarter can drift in the next, which is why the case carries a review date and is refreshed by the runtime loop. (→ Book 1 §4.6.3, §17; Book 2 §15.8.)

| Field | Entry |
|---|---|
| **Case ID** | `AC-nnn` |
| **Agent** | `AG-nnn` |
| **Autonomy level claimed** | `L0`–`L4` |
| **As of** | `YYYY-MM-DD` |
| **Review date** | `YYYY-MM-DD` |
| **Accountability owner** | *(named human)* |

## The claim
*"This agent operates at `Ln` because …" — state the autonomy level the case justifies.*

## The argument and evidence
| Claim | Evidence | Source |
|---|---|---|
| Quality holds above threshold | *(eval pass-rate)* | `eval-suite-specification` `EV-nnn` |
| Hard bounds are enforced | *(guardrail veto log; no breach in N days)* | `guardrail-policy-catalog` |
| Sensitive cases route correctly | *(alignment eval ≥ threshold)* | `EV-nnn` alignment dimension |
| Actions are reversible / compensable | *(design + incident record)* | architecture record |

## Residual risk
*What the evidence does **not** yet cover — stated honestly. "No residual risk" is almost always false. The residual-risk line filled honestly is what turns a future incident from a surprise into a known gap surfacing.*

## Accepted by
*Named accountability owner, with date. Acceptance is of the stated residual risk at the stated autonomy level, until the review date.*
