---
artifact: business-capability-catalog
title: "Business Capability Catalog — Aava automation portfolio"
type: catalog
phase: 2
domain: [B]
status: approved
owner: "Head of Support (Liisa Aalto)"
version: 1.0
links: [determinism-fit-map, requirements-intent-catalog, agent-catalog, human-agent-raci]
---

# Business Capability Catalog — Aava automation portfolio

The six candidate capabilities of the AI mandate, with performer mix and the determinism placement that decided each one's approach. The placement column is the hook the Determinism-Fit Map (`determinism-fit-map`) carries in full.

| Capability ID | Capability (outcome name) | Determinism placement | Performer mix | Autonomy | Accountability owner |
|---|---|---|---|---|---|
| `CAP-001` | Categorise and route a ticket | deterministic | rules engine + human (no-match) | n/a | Head of Support (Liisa Aalto) |
| `CAP-002` | Set ticket priority (SLA) | mostly deterministic | rules engine + human (edge) | n/a | Head of Support |
| `CAP-003` | Draft a first response / KB answer | probabilistic | agent (suggests) + human (sends) | `L1` | Support Team Lead (Mikko Räsänen) |
| `CAP-004` | Flag a churn / dissatisfaction risk | probabilistic, low-consequence | agent (flags) + human (reviews) | `L3` | Customer Success Lead (Noora Salmi) |
| `CAP-005` | Decide a refund / credit | deterministic policy + exceptions | rules engine + human-alone (out-of-policy) | n/a | Billing Lead (Petri Kallio) |
| `CAP-006` | Detect a stale knowledge-base article | hybrid | rules (age) + agent-assisted review | `L0` | Knowledge Lead (Sanna Virta) |

**Read the placement column.** Four of six capabilities are placed `deterministic`/`mostly-deterministic`/`hybrid` and resolve to a rules engine plus a human — *not* an agent. Only `CAP-003` and `CAP-004` are genuinely probabilistic and become agent actors (→ `agent-catalog`). That is the architecture decision the mandate would have skipped.
