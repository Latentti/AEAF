---
artifact: re-gating-trigger
title: Re-Gating Trigger Checklist (in the runtime loop)
type: checklist
phase: 10
domain: [I]
status: approved
version: 1.0
links: [design-time-gate, architecture-contract, trust-accountability-matrix]
---

# Re-Gating Trigger Checklist

**What it is.** What the **runtime assurance owner** runs continuously in the Phase 10 loop when something changes, to decide: does the loop handle this, or does the gate re-open? The runtime loop keeps an agent within its approved bounds; it **cannot widen them**. There are exactly **three triggers** — keep the set small and the boundary sharp. (→ Book 2 §17.6; Book 1 §20.)

| Trigger | Re-gate when | Stays in the loop when |
|---|---|---|
| **Material change** | The agent gains a new capability, swaps model, takes on a new tool/integration, or its corpus changes substantially — the operating agent is no longer the gated agent. | A configuration tweak or corpus refresh inside the approved scope. |
| **Widened autonomy** | A request to move up the autonomy scale, or to relax oversight (on-the-loop → out-of-the-loop). | The agent operates at its granted level; no widening requested. |
| **Failed assurance case** | A dimension falls below threshold and stays there, drift makes the eval set unrepresentative, or the review date passes without re-argument. | A transient dip the loop corrects within bounds (retry, fallback, re-ground). |

- [ ] The change classified against the three triggers above
- [ ] **The boundary test applied** — can the loop's bounded adaptation return the agent to its contracted behaviour? Yes → loop handles it. No → the gate re-opens.
- [ ] On re-gate: the affected agent's lifecycle state returned to **Proposed**; only the changed slice re-enters the cycle, not the whole enterprise
- [ ] On re-gate: a new design-time cycle runs the gate checklist and produces an updated agentic architecture contract before the agent returns to **Operating**
- [ ] Neither failure mode committed — a transient dip was *not* escalated to a full cycle; a broken assurance case was *not* treated as a dip
