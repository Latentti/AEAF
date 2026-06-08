---
artifact: eval-suite-specification
title: Eval-Suite Specification
type: spec
phase: 6
domain: [I]
status: stub
owner: "TBD — runtime assurance owner / eval lead"
as_of: TBD
version: 0.1
links: [agent-catalog, model-portfolio, guardrail-policy-catalog, requirements-intent-catalog, assurance-case]
---

# Eval-Suite Specification

**What it is.** The definition of the tests, probes, and thresholds that bound and monitor an agent's or model's behaviour — the replacement for a one-time test plan with a continuously-run suite. It is the evidentiary backbone of the assurance case: "this is how we know the agent is behaving within its intent, and this is the bar it must clear." Evals *measure bounded behaviour*; tests verify deterministic output. Do not collapse the dimensions into one accuracy number — a probabilistic actor can clear quality and speed while quietly mis-routing the cases that matter.
**Produced in.** Phase 6 · Intelligence & Agency, against the Intent set at the centre.
**Instantiates.** `Eval Suite`, measuring an `Intent` and assuring a `Model`/`Agent`; results feed the `Assurance Case`.
**Defined in.** Book 1 §21.4.7 · templated in Book 2 §15.8.

## Template

**Header.** Suite ID · the agent/model and the intent it evaluates · case-set provenance (incl. logged real cases and a **held-out golden set the team does not tune against**) · run cadence.

**Body — one row per evaluation dimension.**

| Dimension | What it measures here | Metric & threshold (set *before* the run) | Case set | Gate (design-time / runtime) |
|---|---|---|---|---|
| **Quality** | | | | |
| **Safety** | | | | |
| **Alignment** | | | | |
| **Performance** | | | | |
| **Cost** | | | | |

## Filled example

<!-- example — replace with your own suite -->

**Header.** `EV-001` · evaluates `AG-001` against Intent `INT-nnn` "*(intent statement)*" · case sets: *(N)*-case held-out golden set (not tuned against) + logged live cases sampled weekly · cadence: pre-merge, pre-prod, and online.

| Dimension | What it measures here | Metric & threshold (set before run) | Case set | Gate |
|---|---|---|---|---|
| **Quality** | *(is the output one a competent human would produce?)* | *(advisor-acceptable rate ≥ 95%)* | golden set | Pre-prod + online |
| **Safety** | *(does it avoid the out-of-policy / unsafe action?)* | *(unsafe-action < 0.1%; out-of-policy 0%)* | golden + adversarial | Pre-merge + online |
| **Alignment** | *(does it route edge/sensitive cases honestly, not to look productive?)* | *(correct routing ≥ 99.5%)* | golden + cohort probes | Pre-prod + online |
| **Performance** | *(fast enough to clear the queue?)* | *(median < 3 min; p99 < 8 min)* | live timing | Online |
| **Cost** | *(economical at volume?)* | *(cost per resolved request < €0.40)* | live billing | Online |

## Common mistakes (→ Book 2 §15.8)

- **A single "accuracy" score.** The alignment dimension exists to catch what quality and speed hide. Do not collapse the five into one number.
- **Setting thresholds after seeing the results.** Thresholds set before the run are evidence; thresholds set after are rationalisation. Record them up front.
- **Tuning against the golden set.** A held-out set the team trains against measures memorisation, not behaviour. Keep it sealed.
- **An eval that runs once at the gate and never again.** Evals are continuous; the online gate watches *distributions*, not single cases.
