---
artifact: principles-catalog
title: "Principles Catalog — Aava automation portfolio"
type: catalog
phase: P
domain: [B, I]
status: approved
owner: "Architecture board (chair: CTO)"
version: 1.0
links: [guardrail-policy-catalog, determinism-fit-map]
---

# Principles Catalog — Aava automation portfolio

The principles governing Aava's AI automation, with Enforcement attributes. The two that shape this whole example are `P-1` (determinism-fit) and `P-2` (explainability) — they are the reason the portfolio uses less AI than the mandate imagined, and why the team trusts what is left.

| ID | Name | Statement | Enforcement | Compiled guardrails |
|---|---|---|---|---|
| `P-1` | Determinism-fit | Each capability is placed on the determinism spectrum; it gets the component (rules / LLM / hybrid / human) and assurance model (test / eval) that fit. AI is used where probabilistic value justifies it — **not by default**. | design-time | — |
| `P-2` | Explainability | A decision a human must trust is traceable to a named rule or a cited source; an output a human cannot trace is not shipped where trust is required. | **runtime** | `G-2` |
| `P-3` | One accountable human | Every capability has exactly one named human accountability owner; accountability never transfers to an agent or a rule engine. | design-time | — |
| `P-4` | PII boundary | Customer personal data is never sent to a third-party model or held in a knowledge corpus. | **runtime** | `G-1` |
| `P-5` | Suggest, do not act | Where an LLM is used on customer-facing work, it proposes; a human decides and sends. The agent does not take the irreversible action. | **runtime** | `G-3` |
| `P-6` | Human for significant decisions | A decision with material or irreversible effect (an out-of-policy refund, an account change) is made by a human, with the system assisting. | design-time | — |

**Why `P-1` and `P-2` are first-class.** Most AI initiatives have neither, and discover the need for both only after an unexplainable system has lost the team's trust. Aava states them up front: `P-1` stops the reflex to reach for an LLM, and `P-2` makes traceability a build requirement, so the team never has to check the work twice to feel safe.
