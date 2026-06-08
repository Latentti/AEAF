---
artifact: agentic-adr
title: "Agentic Architecture Decision Record — ADR-nnn"
type: decision
phase: TBD
domain: [TBD]
status: stub
owner: "TBD"
version: 0.1
links: []
---

# ADR-nnn — (decision title)

**What it is.** A short, dated record of one significant architecture decision and why it was made — the agentic-era ADR. It records the context, the decision, and the consequences, plus the agentic dimensions a classical ADR has no slot for: the autonomy level, the guardrails, the eval/assurance stance, and who is accountable. One decision per record. (→ Book 2 §16.)

| Field | Entry |
|---|---|
| **ID** | `ADR-nnn` |
| **Date** | `YYYY-MM-DD` |
| **Status** | proposed / accepted / superseded by `ADR-mmm` |
| **Decision owner** | *(named human/role — accountable for the decision)* |

## Context
*What forces the decision — the problem, the constraints, the alternatives considered. State where the relevant component sits on the determinism spectrum (deterministic → probabilistic), because that sets which assurance model applies.*

## Decision
*The decision, in one or two sentences. Name the actor, the bound, the autonomy level.*

## Agentic dimensions *(new vs a classical ADR)*
| Dimension | Entry |
|---|---|
| **Autonomy level** | `L0`–`L4` and why this level for this consequence (→ `autonomy-level-classification`). |
| **Guardrails** | `G-n` that bound the decision (→ `guardrail-policy-catalog`). |
| **Eval / assurance** | The eval suite + thresholds that assure it (→ `eval-suite-specification`). |
| **Accountability owner** | Named human — never an agent. |
| **Oversight mode** | in / on / out-of-the-loop. |

## Consequences
*What becomes easier, what becomes harder, what residual risk is accepted and by whom. State the review date.*

**Common mistakes.** Recording "we changed the AI" as one decision — a model swap, a new tool, and a re-platform are three separate decisions with three owners. Omitting the autonomy level or the accountability owner. No review date on an accepted decision that depends on live assurance.
