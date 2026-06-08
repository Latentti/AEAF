---
artifact: architecture-roadmap-migration-plan
title: "Architecture Roadmap & Migration Plan — Parkki Nordic agentic support line"
subtitle: "Phases 7–8 deliverable"
type: deliverable
phase: 8
domain: [B, I]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
version: 1.0
links: [capability-automation-frontier-map, autonomy-level-classification, trust-accountability-matrix]
---

# Architecture Roadmap & Migration Plan — Parkki Nordic agentic support line

**Deliverable (Phases 7–8).** How the target architecture is reached, sequenced by **trust earned**: pilot under tight oversight first, widen autonomy only as assurance accrues. Each step is a frontier move with a trigger and an assurance precondition — a roadmap arrow is an intention, never an authorisation.

## Baseline → target
Today (→ `capability-automation-frontier-map`, as of 2026-06): triage/explain at L3; Gate-Ops at L2 (operator confirms); ANPR and small refunds at L1; safety, account/GDPR, and large/contested money fixed human. Target: Gate-Ops and ANPR widened to L3 on evidence; the fixed-human leaves stay fixed.

## Frontier moves

| Move | From → to | Trigger | Assurance precondition | Gate |
|---|---|---|---|---|
| Gate-Ops widen | `L2` → `L3` | one quarter of clean live evidence | `EV-002` safety holds (unpaid-open 0%); **Tampere garages in the golden set** | re-gate `AG-002` |
| ANPR-Correction widen | `L1` → `L3` | correction accuracy holds a quarter | `EV-004` accuracy ≥ 96%; no cross-customer edit | re-gate `AG-004` |
| Small-refund autonomy | hold at `L1` | — | board keeps money in-the-loop | — |

## Autonomy-graduation gates
Each widen runs the design-time gate again (→ `autonomy-level-classification` for the controls each level requires; the live evidence is read from the `trust-accountability-matrix`). No move ships until its precondition holds and the gate approves.

## Work packages
1. Tampere garage onboarding + golden-set expansion (unblocks the Gate-Ops widen).
2. ANPR accuracy evidence accrual (unblocks the ANPR widen).
3. Accessibility conformance (closes the open regulatory item `OBL-012`).
4. Peak-load test of callback scheduling (`AG-005`).

## Human transition
The human support team moves from handling routine contacts to handling the fixed-human work (safety, account/GDPR, large/contested money) and confirming Gate-Ops opens at L2. Reskilling to oversight and exception-handling; no role eliminated in this phase.

## Dependencies & risk
The Gate-Ops widen depends on Tampere onboarding; the ANPR widen is independent. Risk: operator-confirmation load at L2 if exit volume spikes before the widen — monitored (→ `ADR-001`).

## Sign-off
Support Operations Lead + architecture board, 2026-04-02.
