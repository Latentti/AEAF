---
artifact: requirements-intent-catalog
title: "Requirements & Intent Catalog — Aava automation portfolio"
type: catalog
phase: 1
domain: [B, I]
status: approved
owner: "EA / lead architect (Joonas Mäki)"
version: 1.0
links: [determinism-fit-map, eval-suite-specification, guardrail-policy-catalog]
---

# Requirements & Intent Catalog — Aava automation portfolio

This is where the determinism placement becomes concrete. A capability placed `deterministic` is written as a **requirement** — specified, tested, pass/fail. A capability placed `probabilistic` is written as an **intent** — outcome + bounds, measured by evals. The contrast between `REQ-001` and `INT-001` *is* the lesson.

## Deterministic requirements (rules + test)

| Req ID | Capability | Requirement | Acceptance test | Priority |
|---|---|---|---|---|
| `REQ-001` | `CAP-001` routing | Map ticket keywords to a queue by an ordered rule set (~30 rules); on no match, surface a dropdown for the rep to choose. The applied rule is recorded on the ticket. | golden set of labelled tickets: correct-queue ≥ 99%; **every routed ticket cites the rule that placed it** (100%) | Must |
| `REQ-002` | `CAP-002` priority | Derive priority from the SLA matrix (customer tier × keyword/outage); flag genuinely ambiguous cases to a human. | defined cases pass 100%; flagged-vs-auto split within expected band | Must |
| `REQ-003` | `CAP-005` refund | Apply the refund policy by rule; route any out-of-policy or contested case to a named human. | policy cases pass 100%; **0% out-of-policy auto-approvals** | Must |

*These are testable because the right output is specifiable. Putting an LLM behind any of them would replace a pass/fail test with a probability and an unexplainable decision — the category error the Determinism-Fit Map exists to catch.*

## Intent records (LLM + eval)

| Field | `INT-001` | `INT-002` |
|---|---|---|
| **Capability** | `CAP-003` KB-answer drafting | `CAP-004` churn flagging |
| **Outcome** | A helpful first-draft response grounded in the knowledge base | At-risk accounts surfaced for a human to review |
| **Bounds** | cite the KB article; never invent policy; **suggest only — a human edits and sends**; no PII to the model | flag only — take no account action; surface the signals behind the flag |
| **Acceptance signal** | helpfulness ≥ 85% advisor-accept, hallucinated-policy 0% (`EV-001`) | recall on known churn ≥ 80%, false-flag rate within band (`EV-002`) |
| **Enforced by** | `G-1`, `G-2`, `G-3` | `G-1` |

**The teaching in one line.** `REQ-001` (routing) and `INT-001` (drafting) describe two capabilities in the same support flow — but one is a *requirement* you test once and trust, and the other is an *intent* you evaluate continuously. The determinism placement is what tells you which is which, before you build either.
