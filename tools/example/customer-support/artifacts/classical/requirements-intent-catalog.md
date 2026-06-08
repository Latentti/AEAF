---
artifact: requirements-intent-catalog
title: "Requirements & Intent Catalog — Parkki Nordic support line"
type: catalog
phase: 1
domain: [B, I]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
version: 1.0
links: [eval-suite-specification, guardrail-policy-catalog, assurance-case]
---

# Requirements & Intent Catalog — Parkki Nordic support line

The agents' work is probabilistic, so it is declared as **intent** (outcome + bounds), not a fully-specified requirement, and measured by evals. One deterministic requirement is included to show the contrast.

## Intent records (agent work)

| Intent ID | Outcome | Bounds | Acceptance signal | Enforced by | Assured by |
|---|---|---|---|---|---|
| `INT-001` | Route every contact to the right specialist or human, fast | never resolve a safety case itself; never act before identity verified | routing ≥ 98%, safety routing ≥ 99.5% (`EV-001`) | `G-4`, `G-5`, `G-8` | `AC-002` |
| `INT-002` | Get a paid-up driver out of the garage in under 90 s | open the gate **only** for a verified paid/exempt session; never on claimed authority; rate-limited | unpaid-open 0%, correct-open ≥ 98% (`EV-002`) | `G-1`, `G-5`, `G-6` | `AC-001` |
| `INT-003` | Explain a charge clearly and resolve in-policy billing | never refund > €50 or contested without a human; always cite the rule | quality ≥ 95%, over-cap refund 0% (`EV-003`) | `G-2`, `G-7` | `AC-003` |
| `INT-004` | Correct a genuine ANPR misread within bounds | never transfer ownership; never edit another customer's record | accuracy ≥ 96%, out-of-bounds 0% (`EV-004`) | `G-8` | `AC-004` |
| `INT-005` | Hand a bounded case to the right human queue with full context | never make the substantive decision | queue accuracy ≥ 98% (`EV-005`) | `G-4` | `AC-005` |

## Deterministic requirement (for contrast)

| Req ID | Requirement | Acceptance test | Priority |
|---|---|---|---|
| `REQ-001` | The caller is told they are speaking with Parkki Nordic's AI assistant before any action | disclosure present in 100% of call openings (`P-6`) | Must |

*The split is the point: `REQ-001` is deterministic — it either discloses or it is broken, tested pass/fail. `INT-001…005` cannot be exhaustively specified, so they are declared as outcome + bounds and assured by evals. Putting `INT-002` behind a "tested once, signed off" gate would be a category error.*
