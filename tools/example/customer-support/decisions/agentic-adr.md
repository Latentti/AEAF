---
artifact: agentic-adr
title: "ADR-001 — Gate-Ops Agent goes live at L2, not L3"
type: decision
phase: 6
domain: [I]
status: approved
owner: "Architecture board"
version: 1.0
links: [autonomy-level-classification, guardrail-policy-catalog, eval-suite-specification]
---

# ADR-001 — Gate-Ops Agent goes live at L2, not L3

| Field | Entry |
|---|---|
| **ID** | `ADR-001` |
| **Date** | 2026-03-18 |
| **Status** | accepted |
| **Decision owner** | Architecture board (Support Operations Lead recommending) |

## Context
`AG-002` opens a physical exit gate — a consequential, real-world action. The payment-verification guardrail `G-1` is sound by design (fail-closed, pre-action), but at go-live it had **no live evidence**: the golden set covered Kamppi and Kluuvi, not the new Tampere garages, and there was no production track record of `G-1` holding under real traffic. The component sits at the probabilistic end for *recognising the situation* and the deterministic end for *the gate check* — so the gate check can be tested, but the agent's judgement around it must be evaluated and earned.

## Decision
`AG-002` goes live at **L2 (execute-with-approval)** — it stages the gate-open and a support operator confirms each one — rather than L3 (act-and-report). L3 is the target, reached only after one quarter of live evidence shows `G-1` holds and the Tampere garages are represented in the golden set.

## Agentic dimensions
| Dimension | Entry |
|---|---|
| **Autonomy level** | `L2` at go-live; `L3` target (→ `autonomy-level-classification`). |
| **Guardrails** | `G-1` (paid-session), `G-5` (no claimed authority), `G-6` (rate limit) (→ `guardrail-policy-catalog`). |
| **Eval / assurance** | `EV-002` safety must hold (unpaid-open 0%) for a quarter (→ `eval-suite-specification`, `AC-001`). |
| **Accountability owner** | Support Operations Lead — never an agent. |
| **Oversight mode** | In-the-loop at L2; on-the-loop at L3 target. |

## Consequences
Slower per case at go-live (an operator confirms each open), accepted as the cost of starting conservative on a physical action with no live evidence. Easier to defend to the board and to earn L3 honestly. Residual risk: operator-confirmation load if exit volume spikes — monitored; if it bites before L3 evidence accrues, the board revisits. Review date: 2026-Q3.
