---
artifact: phase-10-change-runtime-assurance
title: "Phase 10 · Change & Runtime Assurance — worksheet"
type: worksheet
phase: 10
domain: [I]
status: stub
owner: "TBD — runtime assurance owner"
version: 0.1
links: [trust-accountability-matrix, eval-suite-specification, guardrail-policy-catalog, assurance-case]
---

# Phase 10 · Change & Runtime Assurance

**Purpose.** Monitor, assess impact, evolve; trigger new cycles. **ADM analogue:** H (transformed). **Agentic addition:** owns the **continuous runtime loop** — enforcement, drift/eval monitoring, incident response, bounded adaptation, escalation. Material change triggers a new design-time cycle. (→ Book 1 §9, §20; Book 2 §14, §17.6.)

## The runtime loop (continuous)
Enforce guardrails → monitor evals & drift → detect/contain incidents → adapt within bounds or escalate → repeat. The loop keeps an agent within its approved bounds; it **cannot widen them**. Widening routes back to the gate (`checklists/re-gating-trigger.md`).

## Steps
1. Operate the **runtime loop**: guardrails enforced at decision points; evals and drift monitored continuously. **[+I]**
2. Wire the **re-gating triggers**: material change, widened autonomy, failed assurance case. **[+I]**
3. Capture **runtime evidence**: decision trails, guardrail-veto logs, eval/drift records, assurance-case history, incident records. **[+I]**
4. Keep the **Trust & Accountability Matrix current** (refresh `as_of`): each capability → owner, oversight mode, live assurance. **[+I]**
5. On a fired trigger: return the affected agent's lifecycle state to **Proposed**; only the changed slice re-enters the cycle.

## Produces
- Living `trust-accountability-matrix` · refreshed `assurance-case` · runtime evidence store · re-gating decisions.

## Exit gate (continuous — the loop never stops while anything operates)
- [ ] Runtime loop operating (guardrails enforced; evals + drift monitored) **[+I]**
- [ ] Re-gating triggers wired (material change / widened autonomy / failed assurance) **[+I]**
- [ ] Runtime evidence captured (decision trails, veto logs, eval/drift, incidents) **[+I]**
- [ ] Trust & Accountability Matrix current **[+I]**
