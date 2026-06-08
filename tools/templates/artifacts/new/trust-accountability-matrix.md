---
artifact: trust-accountability-matrix
title: Trust & Accountability Matrix
type: matrix
phase: 9
domain: [B, I]
status: runtime
owner: "TBD — capability owner"
accountable: "TBD — named human; never an agent"
as_of: TBD
version: 0.1
links: [agent-catalog, autonomy-level-classification, eval-suite-specification, human-agent-raci, capability-automation-frontier-map]
---

# Trust & Accountability Matrix

**What it is.** The single **standing view** that ties each capability to its named accountability owner, the oversight mode its agent runs under, and the *live* assurance evidence behind it right now. Where the Human-Agent RACI sets the split at design time, this matrix is the standing answer to "who is answerable for this agent right now, how is it overseen, and what is the live evidence it is fit to operate." It is what the governance gate and an auditor read. It is **refreshed by the runtime loop, not filed once** — a stale matrix asserts a fitness the live evidence no longer supports. Stamp `as_of` on every render.
**Produced in.** Phase 2 (initial) and Phase 9 · Governance, refreshed continuously by the runtime loop.
**Instantiates.** `Capability` × `Accountability Owner` × `Oversight Control` × `Assurance`.
**Defined in.** Book 1 §21.4.8 · templated in Book 2 §15.9.

## Template — one capability/agent per row

| Field | What to record |
|---|---|
| **Capability / agent** | The capability and the agent ID (→ `agent-catalog`). |
| **Accountability owner** | Named human/role answerable now. |
| **Oversight mode** | in / on / out-of-the-loop currently. |
| **Current autonomy level** | The live level (→ `autonomy-level-classification`). |
| **Assurance status** | Current eval pass-rate, last incident, assurance-case review date (→ `eval-suite-specification`). |
| **Residual risk** | What the evidence does *not* yet cover. |
| **Escalation path** | Where it hands control on a bound/veto/incident. |

## Filled rows

<!-- example — a live view as of a stated date -->

| Capability / agent | Accountability owner | Oversight mode | Autonomy | Assurance status | Residual risk | Escalation path |
|---|---|---|---|---|---|---|
| *(routine capability)* (`AG-001`) | *(named owner)* | On-the-loop, 20% sampled | `L3` | Quality ~96%; no open incident; case reviewed 2026-05 | *(cohort under-represented in golden set)* | Auto step-down to L1 → advisor → AI-risk reviewer |
| *(assess step)* (`AG-001`) | *(named owner)* | In-the-loop | `L1` | Eval clear; no incident | *(new categories untested)* | Advisor |
| *(sensitive case)* | *(named owner)* | Human-only | n/a (agent routes only) | n/a — not agent-performed | — | Senior advisor |

## Common mistakes (→ Book 2 §15.9)

- **Treating it as a point-in-time document.** This is a *standing view* refreshed by the runtime loop, not a sign-off filed once.
- **Copying the RACI's design-time split into it.** The RACI says what *should* happen; this says what *is* happening, including the current incident and live pass-rate.
- **An empty residual-risk cell.** "No residual risk" is almost always false; filled honestly it turns a future incident from a surprise into a known gap surfacing.
- **Oversight mode that disagrees with the Agent Catalog.** Reconcile — the live matrix wins, and the catalog is updated.
