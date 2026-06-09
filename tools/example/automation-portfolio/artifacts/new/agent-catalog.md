---
artifact: agent-catalog
title: "Agent Catalog — Aava automation portfolio"
type: catalog
phase: 6
domain: [I]
status: approved
owner: "Support Team Lead (Mikko Räsänen)"
as_of: 2026-06-08
version: 1.0
links: [model-portfolio, guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, human-agent-raci]
---

# Agent Catalog — Aava automation portfolio

**Two agents, not six.** Only the capabilities the Determinism-Fit Map placed `probabilistic` become agent actors. The other four capabilities are served by a rules engine and humans, and so have no row here — which is exactly the point: the Agent Catalog lists agents *where an agent is the right component*, not everywhere AI was imagined.

| Agent ID | Name | Purpose / objective (incl. what it does NOT do) | Capability | Model | Tools / actions | Guardrails | Autonomy | Oversight | Eval | Accountability owner | Lifecycle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `AG-001` | KB-Draft Agent | Draft a first-response answer grounded in the knowledge base for a human to edit and send. Does **not** send to the customer and does **not** state policy not found in the cited article. | `CAP-003` | `M-001` | `knowledge_search` (read) · draft (suggest-only) | `G-1`, `G-2`, `G-3` | `L1` | In-the-loop (human edits & sends) | `EV-001` | Support Team Lead (Mikko Räsänen) | operating |
| `AG-002` | Churn-Flag Agent | Flag accounts showing dissatisfaction or churn risk for a human to review. Does **not** contact the customer or take any account action. | `CAP-004` | `M-002` | `read_ticket_history` (read) · flag (write, reversible) | `G-1` | `L3` | On-the-loop (human reviews flags) | `EV-002` | Customer Success Lead (Noora Salmi) | operating |

**Why these two and only these two.** `AG-001` generates natural language (no single correct output) and `AG-002` judges sentiment (not specifiable) — both genuinely probabilistic, both kept suggest/flag-only so a human owns the consequential step. Routing, priority, and refund were placed `deterministic` and are rules, not agents; they appear in the Determinism-Fit Map and the requirements catalog, not here.
