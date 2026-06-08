---
artifact: autonomy-level-classification
title: Autonomy-Level Classification
type: map
phase: P
domain: [I]
status: stub
owner: "TBD — architecture board (scale); capability owner (assignment)"
as_of: TBD
version: 0.1
links: [agent-catalog, human-agent-raci, eval-suite-specification, trust-accountability-matrix]
---

# Autonomy-Level Classification

**What it is.** Two things in one artifact: the **scale** of autonomy levels the enterprise uses (defined once, with required controls per level), and the **assignment** of a level to each agent capability. It stops autonomy being an ad-hoc per-agent judgement. The scale is **canonical (L0–L4) and not re-invented** — use the AEAF Autonomy-Level Classification from Book 1 §4. The level is **per capability, not per agent**: the same agent may run at L1 for high-value cases and L3 for small ones. Controls are **cumulative** — each level inherits the controls below it.
**Produced in.** The **scale** in the Preliminary phase; the **assignment** in Phases 2 and 6.
**Instantiates.** `Autonomy Level` (scale) and `Capability Allocation` (assignment); each level sets an `Oversight Control` mode.
**Defined in.** Book 1 §4 (canonical scale) & §21.4.6 · templated in Book 2 §15.7.

## Part A — the canonical scale (Book 1 §4, Table 4.4)

Record, per level your enterprise actually uses, the controls it demands and the evidence that gates entry to it. Do not invent ad-hoc levels.

| Level | Name | What the agent does | Required controls (minimum, cumulative) | Default oversight | Gating evidence to reach it |
|---|---|---|---|---|---|
| `L0` | Assistive | Suggests, drafts, retrieves; takes no action itself. | Output disclosure ("AI-generated"); source attribution. | In-the-loop | None beyond build |
| `L1` | Recommend | Proposes a specific action + reasoning; does not execute. | Confidence surfaced; clear approve/reject; full audit log. | In-the-loop | Golden-set evals pass + shadow run within threshold |
| `L2` | Execute-with-approval | Prepares/stages an action; executes only after explicit human sign-off. | Pre-execution preview; reversible staging; per-action veto. | In-the-loop | L0–L1 controls in place; staging proven |
| `L3` | Act-and-report | Executes within bounds without prior approval; reports every action. | Runtime guardrails; spend/rate limits; full action log; reversibility/compensation; escalation on low confidence; ≥ sampled review. | On-the-loop | A quarter of L1 evidence holds; assurance case approved |
| `L4` | Autonomous-within-bounds | Acts freely toward its objective inside hard guardrails; no human in the runtime path. | Hard runtime guardrails with veto; continuous evals; drift detection; incident response; defined escalation; assurance case. | Out-of-the-loop | Sustained assurance, incident-free, owner sign-off |

*"Autonomous" (L4) means autonomous **within bounds**, never unbounded — there is no level at which guardrails are removed.*

## Part B — per-capability assignment

| Capability / agent | Assigned level | Effective from | Assurance that justifies the level (→ `eval-suite-specification`, `trust-accountability-matrix`) |
|---|---|---|---|
<!-- example -->
| *(leaf capability)* (`AG-001`) | `L3` | 2026-02 | *(identity-match eval ≥ 99%, `EV-001`)* |
| *(assess step)* (`AG-001`) | `L1` (→ L3 target) | 2026-01 | *(eval cleared one quarter)* |

## Common mistakes (→ Book 2 §15.7)

- **Inventing a new scale per agent.** The scale is set once for the enterprise; agents are *assigned* to it.
- **A level with no required controls.** "L3 = on-the-loop" is a label until you state the controls (sampled review %, drift monitor) the gate checks before granting it.
- **Assigning a level offline-only evidence cannot justify.** L3 needs live evidence; do not let "the evals passed" approve a level the evidence does not cover.
- **No effective-from date.** An assignment with no date cannot be reconciled against an incident timeline.
