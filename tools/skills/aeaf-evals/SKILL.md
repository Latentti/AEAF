---
name: aeaf-evals
description: Build an Eval-Suite Specification — the continuously-run tests, dimensions, and thresholds that assure an agent's or model's behaviour (Phase 6). Use when the user needs to define how an agent is evaluated and what bar it must clear — e.g. "design the eval suite for this agent", "what thresholds for the hardship agent", "set up assurance for our support bot". Produces the Eval-Suite Specification across five dimensions (quality, safety, alignment, performance, cost) with thresholds fixed before the run and a held-out golden set.
---

# AEAF Evals

Replace the one-time test plan with a continuously-run suite. Define how you know the agent is behaving within its intent, and the bar it must clear — the evidentiary backbone of the assurance case.

## When to use
- Phase 6, for every agent capability.
- Whenever the model, prompt, corpus, or intent changes — the suite re-runs.

## Inputs you need
- The agent's intent (outcome + bounds) from the Requirements & Intent Catalog.
- The guardrails it must respect (from `aeaf-guardrails`) — each needs a verifying eval.
- A source of cases: logged real cases, and a held-out golden set the team does **not** tune against.

## Procedure
1. **Write the header** — suite ID, the agent/model and intent it evaluates, the case-set provenance (golden set + sampled live cases), the run cadence (pre-merge, pre-prod, online).
2. **Define one row per dimension** — do not collapse them into one accuracy number:
   - **Quality** — is the output one a competent human would produce?
   - **Safety** — does it avoid the unsafe / out-of-policy action?
   - **Alignment** — does it handle edge/sensitive cases honestly, not to look productive? (this dimension catches the drift quality and speed hide)
   - **Performance** — fast enough to clear the queue?
   - **Cost** — economical at volume?
3. **Set the metric and threshold for each dimension *before* the run.** A threshold chosen after seeing the score is rationalisation.
4. **Name the gate each dimension governs** — design-time (pre-merge/pre-prod) and/or runtime (online watching distributions).
5. **Keep the golden set sealed** — a set the team trains against measures memorisation, not behaviour.

## Templates it drives
- `tools/templates/artifacts/new/eval-suite-specification.md`
- feeds `tools/templates/decisions/assurance-case.md`

## Quality bar
- **Five dimensions, not one score.** The alignment dimension is the one that catches silent mis-routing.
- **Thresholds fixed before results.**
- **Golden set held out and never tuned against.**
- **Continuous, not once** — the online gate watches distributions, not single cases.

## Hand off to
- `aeaf-govern` — eval thresholds + the assurance case are gate row 3.
