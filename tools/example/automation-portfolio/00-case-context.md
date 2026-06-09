---
artifact: case-context
title: "Aava Software Oy — AI automation portfolio: case context"
type: reference
status: approved
version: 1.0
links: []
---

# Aava Software Oy — case context

**In brief.** This is the second AEAF worked example, and it teaches the decision the first one assumes is already made: *where does a capability sit on the determinism spectrum, and should it use an LLM at all?* A fictional B2B SaaS vendor, **Aava Software Oy**, gets a board "AI efficiency mandate" and is tempted — as almost everyone is — to put an LLM on everything. AEAF's architecture vision instead places each candidate capability deliberately: rules where the right answer is specifiable, an LLM only where the value is genuinely probabilistic, and a human wherever the consequence demands it. The result is *less* AI than the mandate imagined, and a portfolio the team actually trusts.

> **Fictional.** Aava Software Oy, its staff, and its figures are invented for this worked example. The cautionary anchor (an LLM ticket-classifier replaced by a rules engine, with accuracy and trust both rising) is a real, widely-shared practitioner account, used here as the pattern this example exists to prevent.

## The company

Aava Software Oy is a Nordic B2B SaaS vendor — project-management software for mid-market teams — with around 120 staff. Its 15-person support team handles roughly 90–100 tickets a day through Zendesk: each ticket needs a category, a priority, and routing to the right queue, and many need a first response and the occasional refund or account fix.

## The mandate, and the trap

The board issued an "AI efficiency mandate": automate the support operation with AI. The obvious reading — and the one Aava nearly took — is "put an LLM in the middle of everything." The cautionary tale on the wall: a peer company built exactly that for ticket routing. In production the LLM was right about **92%** of the time — roughly 7–8 misroutes a day — and when a ticket landed in the wrong queue, *nobody could explain why*. There was no rule to point at; the model just decided. Within weeks the team was spot-checking every classification — doing the work twice — and a **shadow process** grew beside the tool, which became expensive decoration. The fix was to *remove* the LLM: ~30 transparent rules plus a dropdown for the rest took accuracy to **99%**, latency to instant, API cost to **zero**, and — decisively — gave the team logic they could trace and trust.

## What AEAF does instead

AEAF treats "which capabilities get AI" as an **architecture-vision decision**, made on the determinism spectrum, not a default. The portfolio (six candidate capabilities) is placed in the Determinism-Fit Map (`artifacts/supporting/determinism-fit-map.md`):

| Capability | Placement | AEAF decision |
|---|---|---|
| Ticket categorisation & routing | deterministic | rules + dropdown — **no LLM** |
| Priority / SLA scoring | mostly deterministic | rules + flag edge cases — no LLM |
| First-response / KB-answer drafting | probabilistic | LLM, suggest-only (L0–L1) — **the right place for an LLM** |
| Churn-risk / sentiment flagging | probabilistic, low-consequence | classifier, flags for review (L3) |
| Refund / credit decision | deterministic policy + exceptions | rules + human-alone out-of-policy — no LLM |
| Knowledge-base staleness detection | hybrid | rules detect age; LLM only suggests review |

Two of six capabilities are genuinely agentic; four are best served by rules and humans. That ratio is the point.

## The three things this example demonstrates

1. **Determinism-fit is a design-time decision.** Where a capability sits on the spectrum dictates the component (rules / LLM / hybrid) *and* the assurance model (test vs eval) *and* the explainability — and it must be decided before building, not discovered after a demo.
2. **Explainability is an architecture driver, not a nicety.** A decision a human must trust but cannot trace becomes a shadow process. Traceability is what lets the team *stop* checking the work.
3. **AEAF's right answer is sometimes less AI.** AEAF is governance, not AI-maximalism. Placing four of six capabilities outside the LLM is not a failure of ambition; it is the architecture doing its job.

## How to read this folder

Start with `walkthrough.md` (the method run, vision-first), then the **Architecture Vision** in `deliverables/`, then the signature **Determinism-Fit Map**. The just-do-it contrast — LLM-by-default vs AEAF-allocated — is `the-default-trap.md`. Everything is cross-linked by ID and `aeaf-validate` confirms it is coherent.
