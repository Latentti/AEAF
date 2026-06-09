---
artifact: guardrail-policy-catalog
title: "Guardrail/Policy Catalog — Aava automation portfolio"
type: catalog
phase: 6
domain: [I, T]
status: approved
owner: "AI-risk reviewer (Riikka Talvitie)"
as_of: 2026-06-08
version: 1.0
links: [agent-catalog, principles-catalog, eval-suite-specification]
---

# Guardrail/Policy Catalog — Aava automation portfolio

Guardrails for the two agents only — the rules-based capabilities need tests, not runtime guardrails. Each traces to a principle, names its enforcement point, and has a verifying eval.

| ID | Guardrail | Policy / principle | Scope | Trigger | Enforcement point | Fail action | Owner | Verifying eval |
|---|---|---|---|---|---|---|---|---|
| `G-1` | No customer PII past the model gateway | `P-4` (runtime) | `AG-001`, `AG-002` | PII pattern in egress | Model gateway | Block + log | EA / Platform owner | gateway probe (in `EV-001`) |
| `G-2` | Answer must cite a KB article; no policy stated that is not in the cited source | `P-2` (runtime, explainability) | `AG-001` | Draft contains a policy claim with no citation | Output check | Block + flag for human | Support Team Lead | `EV-001` safety |
| `G-3` | Draft is suggest-only; the agent cannot send to the customer | `P-5` (runtime) | `AG-001` | Any attempt to send rather than draft | Tool permission | Block | Support Team Lead | `EV-001` safety |

**The explainability guardrail.** `G-2` is the runtime face of principle `P-2`: a KB-answer draft that asserts policy with no citation is blocked, because an unsourced answer is exactly the untraceable output that erodes trust. Explainability here is enforced, not hoped for.
