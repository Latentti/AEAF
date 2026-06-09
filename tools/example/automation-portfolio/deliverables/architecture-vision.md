---
artifact: architecture-vision
title: "Architecture Vision — Aava AI automation portfolio"
subtitle: "Phase 1 deliverable — where AI belongs, and where it does not"
type: deliverable
phase: 1
domain: [B, I]
status: approved
owner: "CTO (Aava Software Oy)"
version: 1.0
links: [determinism-fit-map, requirements-intent-catalog, principles-catalog, business-capability-catalog]
---

# Architecture Vision — Aava AI automation portfolio

**Deliverable (Phase 1).** The board's "AI efficiency mandate" asks the support operation to be automated with AI. This Vision answers a sharper question first: *for each capability, where does it sit on the determinism spectrum, and should it use an LLM at all?* The answer is a portfolio that uses AI deliberately and sparingly — and is trusted because it can be traced.

## Problem & drivers
Support handles ~90–100 tickets/day with 15 people. The pressure is real and the temptation is to put an LLM in the middle of everything. The cautionary tale (a peer's LLM ticket-router that hit 92%, became an unexplainable black box, and was routed around by its own team until the LLM was removed) is the failure this Vision is built to avoid.

## Stakeholders & concerns
The support team (whose trust determines whether any tool is actually used, not worked around); the customers (correct routing, fast first response, fair refunds); Billing and Customer Success; the board (efficiency); the CTO (an architecture that lasts).

## Human–agent ambition (+I)
A portfolio where the component fits the work: **rules where the right answer is specifiable**, **an LLM only where the value is genuinely probabilistic** (suggest-only, with a human owning the consequential step), and **a human wherever consequence demands it**. How many capabilities fall on each side is the Phase 2 allocation's work to determine — the Vision sets the rule, not the count.

## The governing decision rule: determinism-fit
The Vision's spine is two principles (→ `principles-catalog`):
- **`P-1` Determinism-fit** — each capability is placed on the spectrum and gets the component and assurance model that fit; AI is used where probabilistic value justifies it, not by default.
- **`P-2` Explainability** — a decision a human must trust is traceable to a named rule or a cited source; an untraceable output is not shipped where trust is required.

What the Vision commits to is the **decision rule**, not a pre-judged answer: *is the right output specifiable?* — if yes, rules and a test; if no, an LLM and an eval, placed suggest-only; if part each, a hybrid with the boundary named. **Applying this rule to the six capabilities is Phase 2 work** (Business & Capability), recorded in the Determinism-Fit Map (→ `determinism-fit-map`) and the capability catalog (→ `business-capability-catalog`). The Vision does not pre-empt that placement here.

## Target value
Faster, consistent handling of routine tickets; a useful first-draft answer where generation genuinely helps; fair, in-policy refunds with exceptions to a human; and — the value that makes the rest real — **a team that can trace why the system did what it did, and therefore trusts it enough to stop checking its work.** The accuracy, latency, and cost this yields are a *technology outcome*, designed in Phases 4–5 and confirmed in operation — not numbers committed here.

## Why deliberate placement, not AI-by-default
The Vision's stance is that AI is placed where probabilistic value justifies it, never applied by default. An LLM on specifiable work buys a black box, a drift risk, and a shadow process; the spectrum-correct component for such work is a rule the team can trace. Whether that leaves the portfolio with more rules than agents — and what accuracy, latency, and cost result — follows from the Phase 2 placement and the Phase 4–5 technology architecture; it is an outcome of the work, not a target set at the Vision. AEAF's job here is to commit to saying *no* to AI where AI is the wrong tool, and *yes*, precisely, where it is the right one. The count and the measured results come after.

## Sign-off
Architecture board (chair: CTO), 2026-04-14. Proceed to Phase 2 allocation on the determinism-fit placement above.
