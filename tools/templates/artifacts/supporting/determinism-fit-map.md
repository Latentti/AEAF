---
artifact: determinism-fit-map
title: Determinism-Fit Map
type: catalog
phase: 2
domain: [B, A, I]
status: stub
owner: "TBD — lead architect"
as_of: TBD
version: 0.1
links: [business-capability-catalog, requirements-intent-catalog, autonomy-level-classification]
---

# Determinism-Fit Map

**Supporting view — not a tenth core artifact.** AEAF defines exactly nine core artifacts; this is a *supporting governance view* like the Technology Radar (→ Book 1 §21.6). It does not instantiate a new meta-model entity — it records, per capability, a **design-time decision**: where the work sits on the **determinism spectrum** (→ Book 1 §4.4), and therefore which kind of component and which assurance model fit. It is the artifact that answers the question current AI practice skips: *should this capability use an LLM at all?*

**Phase boundary.** The determinism *placement* (deterministic ↔ probabilistic) and the *approach class* (rules / LLM / hybrid / human) are a **Phase 2** allocation decision and belong here. The realized *metrics* — accuracy, latency, cost — are **Phase 4–5** technology and operational outcomes; do not quote them in this map, and do not pre-state them in the Phase 1 Vision.

**Why it exists.** The most common failure is a **category error in either direction**: putting a *probabilistic* component (an LLM) on work that is specifiable and testable — which is a black box that passes the demo, then drifts, and which people stop trusting and route around — or demanding continuous evaluation of a *deterministic* rule engine, which wastes effort on behaviour that cannot vary (→ Book 1 §4.2). The Determinism-Fit Map forces the placement to be made deliberately, at design time, and written down.

## Template — one capability per row

| Field | What to record |
|---|---|
| **Fit ID** | e.g. `DFM-nnn`. |
| **Capability** | The capability being placed (→ `business-capability-catalog`). |
| **Determinism placement** | Where it sits: `deterministic` / `mostly-deterministic` / `hybrid` / `probabilistic`. The question is whether the *right* output is specifiable. |
| **Chosen approach** | `rules` / `LLM` / `hybrid` / `human` — the component that fits the placement. |
| **Assurance model** | `test` (pass/fail on defined cases) for deterministic; `eval` (measured behaviour + monitoring) for probabilistic (→ `requirements-intent-catalog`). |
| **Explainability requirement** | How a user can see *why* the system did what it did (a named rule, a cited source, a confidence + reason). Required wherever a human must trust the output. |
| **Autonomy** | For an agentic placement, the level (→ `autonomy-level-classification`); `n/a` for rules/human. |
| **Rationale** | One line: why this placement, and (if not an LLM) why AI was *not* used here. |

## Filled row

<!-- example — replace with your own capabilities -->

| Fit ID | Capability | Determinism placement | Chosen approach | Assurance | Explainability | Autonomy | Rationale |
|---|---|---|---|---|---|---|---|
| `DFM-001` | *(routing / classification)* | deterministic | rules + dropdown fallback | test | the matched rule is shown | n/a | the right queue is specifiable; an LLM would be an unexplainable black box |
| `DFM-002` | *(natural-language drafting)* | probabilistic | LLM (suggest-only) | eval + guardrails | source cited; human edits | `L1` | no single correct output; generation is genuinely probabilistic value |

## Common mistakes

- **Reaching for an LLM by default.** If the right output is specifiable, the spectrum says rules + test, not LLM + eval. AI is used where probabilistic value justifies it, not because it is available.
- **No explainability where trust is needed.** A decision a user must trust but cannot trace becomes a shadow process — the team checks the work twice and the tool becomes expensive decoration. Explainability is an adoption requirement, not a nicety.
- **Mismatched assurance.** A probabilistic component behind a "tested once, signed off" gate will drift in production; a deterministic rule engine does not need continuous eval. Match the assurance model to the placement.
- **A "hybrid" with no boundary.** If a capability is part-deterministic and part-probabilistic, state *which part* is which (e.g. rules decide, the LLM only drafts the explanation) — not a vague blend.
