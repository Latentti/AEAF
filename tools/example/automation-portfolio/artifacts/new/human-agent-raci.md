---
artifact: human-agent-raci
title: "Human-Agent RACI — Aava automation portfolio"
type: matrix
phase: 2
domain: [B, I]
status: approved
owner: "Head of Support (Liisa Aalto)"
accountable: "Head of Support (Liisa Aalto)"
as_of: 2026-06-08
version: 1.0
links: [autonomy-level-classification, agent-catalog, determinism-fit-map]
---

# Human-Agent RACI — Aava automation portfolio

Responsibility/accountability per capability. Note the **performer** column distinguishes the three component types the determinism-fit decision produced: a rules engine (deterministic), an agent (probabilistic), or a human. In every row the **A is a named human** — including for the rules engine, because a deterministic system is no more accountable than an agent.

| Capability | Performer (R) | Human role | Accountability owner (A) | Decision-authority band | Escalation target |
|---|---|---|---|---|---|
| Route a ticket (`CAP-001`) | **R** rules engine | C (picks on no-match) | **A** Head of Support | rules-decide / human-on-no-match | rep dropdown |
| Set priority (`CAP-002`) | **R** rules engine | C (edge cases) | **A** Head of Support | rules-decide / human-on-flag | team lead |
| Draft KB answer (`CAP-003`) | **R** `AG-001` (L1) | **R** edits & sends | **A** Support Team Lead | agent-proposes-human-sends | team lead |
| Flag churn risk (`CAP-004`) | **R** `AG-002` (L3) | C (reviews flags) | **A** Customer Success Lead | agent-flags-human-reviews | CS lead |
| Decide refund (`CAP-005`) — in policy | **R** rules engine | C | **A** Billing Lead | rules-decide | billing |
| Decide refund (`CAP-005`) — out of policy | I | **R** | **A** Billing Lead | **human-alone** (`P-6`) | billing supervisor |
| KB staleness (`CAP-006`) | **R** rules (trigger) + `AG`-assist (note) | **R** reviews | **A** Knowledge Lead | rules-flag / human-reviews | knowledge lead |

*Accountability sits on a human in every row, whether the performer is a rule engine or an agent. The refund capability splits at the decision level: in-policy is rules; out-of-policy is human-alone, never an LLM.*
