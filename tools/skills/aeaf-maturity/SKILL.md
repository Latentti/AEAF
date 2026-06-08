---
name: aeaf-maturity
description: Assess an organisation's blended-workforce / agentic-architecture maturity and recommend where to start (Book 1 §22 maturity model, Book 2 §5–§6). Use when the user wants to know how ready they are to adopt AEAF, where on the maturity curve they sit, or what the minimum viable adoption is for their context — e.g. "assess our AEAF maturity", "where should we start", "what's the smallest coherent AEAF subset for us". Produces a maturity assessment and a tailored entry-point / minimum-viable-adoption recommendation.
---

# AEAF Maturity

Find where an organisation sits on the blended-workforce maturity curve and recommend the smallest coherent place to start — so adoption is matched to capability, not over-scoped.

## When to use
- Before a first AEAF engagement, to set the entry point.
- Periodically, to track movement and re-target the next increment.

## Inputs you need
- How agents are used today (in production? governed? evaluated?).
- The existing EA capability and governance.
- The consequence profile of the work agents touch.

## Procedure
1. **Assess against the maturity model** (Book 1 §22) — score the dimensions: capability allocation, autonomy governance, guardrails/enforcement, evaluation/assurance, accountability, runtime governance. Be honest; an over-stated score over-scopes the adoption.
2. **Locate the entry point** (Book 2 §5) — the maturity level sets which phases and artifacts are realistic now.
3. **Recommend the minimum viable adoption** (Book 2 §6) — the smallest coherent subset that still works. Phase 6 (Intelligence & Agency) and the runtime loop are **non-negotiable wherever an agent acts**; everything else is scoped to the work.
4. **Match governance weight to consequence** — a reversible in-the-loop copilot needs light gating; a money-moving out-of-the-loop agent needs the full gate and a strong runtime loop.
5. **State the next increment** — the one capability and the evidence that would justify moving up.

## Outputs
- A maturity assessment (scored dimensions, current level, honest gaps).
- A tailored entry-point + minimum-viable-adoption recommendation, with the non-negotiable agentic items called out.

## Quality bar
- **Tailor the depth, never the presence** — do not drop the agentic items wherever an agent acts; that is dropping the governance, not trimming paperwork.
- **No score without evidence** — maturity is what the artifacts show, not what the team hopes.

## Hand off to
- `aeaf-greenfield` (new build) or `aeaf-retrofit` (existing service) to run the recommended scope; `aeaf-allocate` to start Phase 2.
