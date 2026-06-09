---
artifact: autonomy-level-classification
title: "Autonomy-Level Classification — Parkki Nordic support line"
type: map
phase: P
domain: [I]
status: approved
owner: "Architecture board"
as_of: 2026-06-03
version: 1.0
links: [agent-catalog, human-agent-raci, eval-suite-specification, trust-accountability-matrix]
---

# Autonomy-Level Classification — Parkki Nordic support line

## Part A — the scale (canonical L0–L4, Book 1 §4)

Parkki Nordic uses the canonical scale unchanged. Controls are cumulative; the board caps the support line at **L3** (no out-of-the-loop action, because every case touches money or a physical gate).

| Level | Name | What the agent does | Required controls (cumulative) | Oversight | Gating evidence |
|---|---|---|---|---|---|
| `L0` | Assistive | Drafts/retrieves; no action | Disclosure; source attribution | In-the-loop | none beyond build |
| `L1` | Recommend | Proposes an action; human executes | Confidence surfaced; approve/reject; audit log | In-the-loop | golden-set evals pass + shadow run within threshold |
| `L2` | Execute-with-approval | Stages an action; executes after explicit human sign-off | Pre-execution preview; reversible staging; per-action veto | In-the-loop | L0–L1 controls live; staging proven |
| `L3` | Act-and-report | Executes within bounds without per-case approval; reports every action | Runtime guardrails; rate/spend limits; full action log; reversibility; escalation; ≥ 20% sampled review | On-the-loop | one quarter of L1/L2 evidence holds; assurance case approved |
| `L4` | Autonomous-within-bounds | Acts with no human in the path | Hard guardrails + veto; continuous evals; drift detection; incident response | Out-of-the-loop | **not authorised** — board caps the support line at L3 |

## Part B — assignment

*The scale above is set in the **Preliminary** phase; the per-capability assignment below is produced in **Phases 2 & 6** (allocation and agent design). The eval references in this part are therefore Phase-6 assurance, co-located here by design — not Preliminary outputs.*

| Capability / agent | Assigned level | Effective from | Assurance that justifies it |
|---|---|---|---|
| Triage & route (`AG-001`, `CAP-001`) | `L3` | 2026-03 | Routing accuracy ≥ 98% + correct safety routing ≥ 99.5% (`EV-001`) |
| Resolve gate/exit (`AG-002`, `CAP-002`) | `L2` (→ L3 target) | 2026-04 | Staging proven; `G-1` holds in `EV-002`; L3 awaits one quarter of live evidence (→ `ADR-001`) |
| Explain a charge (`AG-003`, `CAP-003`) | `L3` | 2026-03 | Explanation quality ≥ 95% (`EV-003`) |
| Issue refund ≤ €50 (`AG-003`, `CAP-007`) | `L1` | 2026-03 | Recommend-only; human approves each (`G-2`) |
| Correct ANPR misread (`AG-004`, `CAP-004`) | `L1` (→ L3 target) | 2026-04 | Correction accuracy under review; L3 awaits a quarter of evidence |
| Escalate & callback (`AG-005`, `CAP-008`) | `L3` | 2026-03 | Routing accuracy ≥ 98% (`EV-005`); actions reversible |

**Why Gate-Ops is L2, not L3, at go-live.** Opening a physical gate is consequential and the payment-verification guardrail `G-1` had no live evidence yet, so the board started it in-the-loop — an operator confirms each open — and set L3 as the target once a quarter of evidence holds. The reasoning is recorded in `ADR-001`.
