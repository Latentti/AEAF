---
artifact: model-portfolio
title: "Model Portfolio — Parkki Nordic support line"
type: catalog
phase: 5
domain: [T, I]
status: approved
owner: "EA / Platform owner (Joonas Mäkinen)"
as_of: 2026-06-03
version: 1.0
links: [agent-catalog, eval-suite-specification, technology-portfolio-catalog]
---

# Model Portfolio — Parkki Nordic support line

The reasoning models the agents run, governed as portfolio assets. Speech-to-text and text-to-speech sit in the Technology Portfolio, not here — this catalog is the reasoning layer. Each model is a pinned version, because a silent version bump invalidates the eval evidence behind every agent that runs it.

| Model ID | Provider · version | Modality | Context | Cost profile | Risk profile | Agents powered | Eval summary | Stance | Review |
|---|---|---|---|---|---|---|---|---|---|
| `M-001` | Managed inference, EU region · `v2026-04` snapshot | Text | 200k | ~€0.28 / resolved contact (per-token) | Data stays in EU boundary; moderate vendor dependency; degrades on heavy dialect input | `AG-002`, `AG-003`, `AG-004` | Clears `EV-002`/`EV-003`/`EV-004` quality + safety | **Invest** — fits high-volume routine resolution at acceptable cost | 2026-Q4 |
| `M-002` | Frontier model, EU region · `v2026-05` | Text | 256k | ~€1.90 / call | Higher cost; stronger on ambiguous routing and summarisation | `AG-005` | Clears `EV-005`; used only for routing/summarising, not resolution | **Tolerate** — held for escalation routing; not allocated to resolution | 2026-Q4 |
| `M-003` | Small fast model, EU region · `v2026-04` | Text | 32k | ~€0.04 / contact | Cheap; narrow; weaker on long reasoning (acceptable — it only classifies and routes) | `AG-001` | Clears `EV-001` routing accuracy | **Invest** — right-sized for triage classification | 2026-Q4 |

**Why three models, not one.** Triage is a cheap classification job (`M-003`); resolution needs stronger reasoning (`M-001`); ambiguous escalation routing occasionally needs the frontier model (`M-002`). Matching model to job is a cost and a quality decision — and the "agents powered" back-link answers "if we retire `M-001`, what breaks?" in one read: three agents.
