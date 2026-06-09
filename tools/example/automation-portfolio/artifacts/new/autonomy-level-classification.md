---
artifact: autonomy-level-classification
title: "Autonomy-Level Classification — Aava automation portfolio"
type: map
phase: P
domain: [I]
status: approved
owner: "Architecture board"
as_of: 2026-06-08
version: 1.0
links: [agent-catalog, human-agent-raci, eval-suite-specification]
---

# Autonomy-Level Classification — Aava automation portfolio

## Part A — the scale (canonical L0–L4, Book 1 §4)

Aava uses the canonical scale. Autonomy applies **only to agent actors** — the rules-based capabilities (`CAP-001/002/005`) are not on this scale at all, because a deterministic rule engine has no autonomy to grade; it executes a specified rule and is verified by test.

| Level | Name | What the agent does | Oversight |
|---|---|---|---|
| `L0` | Assistive | Suggests/retrieves; no action | In-the-loop |
| `L1` | Recommend | Proposes; a human executes | In-the-loop |
| `L2` | Execute-with-approval | Stages; human signs off | In-the-loop |
| `L3` | Act-and-report | Executes within bounds; reports; human monitors | On-the-loop |
| `L4` | Autonomous-within-bounds | No human in the path | Out-of-the-loop |

## Part B — assignment (agents only)

| Capability / agent | Assigned level | Effective from | Assurance |
|---|---|---|---|
| KB-answer draft (`AG-001`, `CAP-003`) | `L1` | 2026-05 | `EV-001`; draft suggest-only, human sends (`G-3`) |
| Churn flag (`AG-002`, `CAP-004`) | `L3` | 2026-05 | `EV-002`; flag-only, reversible, human reviews each |
| KB-staleness review note (`CAP-006`) | `L0` | 2026-05 | LLM suggests a note only; the staleness trigger is a rule, not an agent |

**The deterministic capabilities are absent on purpose.** Routing, priority, and refund (`CAP-001/002/005`) carry no autonomy level because they are not agents. Looking for their row here is the tell that someone tried to make a rule engine into an agent.
