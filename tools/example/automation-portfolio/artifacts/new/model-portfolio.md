---
artifact: model-portfolio
title: "Model Portfolio — Aava automation portfolio"
type: catalog
phase: 5
domain: [T, I]
status: approved
owner: "EA / Platform owner (Joonas Mäki)"
as_of: 2026-06-08
version: 1.0
links: [agent-catalog, eval-suite-specification]
---

# Model Portfolio — Aava automation portfolio

The models behind the two agents. Small portfolio by design — most of Aava's automation is rules, which run no model at all (and cost nothing per call).

| Model ID | Provider · version | Modality | Cost profile | Risk profile | Agents powered | Eval summary | Stance | Review |
|---|---|---|---|---|---|---|---|---|
| `M-001` | Managed inference, EU region · `v2026-05` snapshot | Text | ~€0.02 / drafted response | Data stays in EU; PII filtered at gateway (`G-1`) | `AG-001` | Clears `EV-001` helpfulness + safety | **Invest** — generation is genuine value for first-draft answers | 2026-Q4 |
| `M-002` | Small classification model, EU region · `v2026-04` | Text | ~€0.005 / ticket scored | Cheap; narrow; outputs a flag + signals only | `AG-002` | Clears `EV-002` recall band | **Tolerate** — adequate for low-consequence flagging | 2026-Q4 |

**Note the absence.** Routing, priority, and refund run **no model** — they are rules. The cautionary tale's $180/month API bill was for a model doing work a rules engine does for free; Aava's model spend is confined to the two capabilities where a model earns it.
