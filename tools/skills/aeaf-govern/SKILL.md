---
name: aeaf-govern
description: Run AEAF governance — the design-time gate, the pre-gate review, the architecture contract, the assurance case, the Trust & Accountability Matrix, the runtime assurance loop, and re-gating decisions (Phases 9–10). Also runs an independent read-only AEAF audit of an existing agentic system against the gates. Use when the user needs to review, gate, sign off, audit, or operate the governance of an agent — e.g. "gate this agent", "review before the board", "audit our agent against AEAF", "set up the runtime loop", "should this change re-open the gate". Folds the audit and runtime-loop acts into one governance skill.
---

# AEAF Govern

Operate the dual governance loop: the deliberate design-time gate, and the continuous runtime assurance loop. The binding rule throughout — **a checked box points to evidence, not an intention.**

## Modes

### 1. Pre-gate review (Phase 6 output, before the board)
Run the **agentic architecture review** (`tools/templates/checklists/agentic-architecture-review.md`) as an independent reviewer not on the design team. A fail on any row sends the design back; the gate is not convened until every row passes or there is a documented, reviewer-accepted exception.

### 2. Design-time gate (Phase 9)
Run the **design-time gate checklist** (`tools/templates/checklists/design-time-gate.md`) per agent. Clear each applicable row **with its evidence reference** (a box with no evidence does not count). Produce and sign the **agentic architecture contract** (`tools/templates/decisions/architecture-contract.md`) — the record of what the agent was permitted to be. Move the lifecycle state Gated → Operating only on full clearance. Match gate weight to consequence.

### 3. Runtime assurance loop (Phase 10)
Stand up and operate the loop: enforce guardrails → monitor evals & drift → detect/contain incidents → adapt within bounds or escalate. Keep the **Trust & Accountability Matrix** (`tools/templates/artifacts/new/trust-accountability-matrix.md`) current (refresh `as_of`) and the **assurance case** (`tools/templates/decisions/assurance-case.md`) reviewed and dated. Capture runtime evidence: decision trails, guardrail-veto logs, eval/drift records, incidents.

### 4. Re-gating decision
Run the **re-gating trigger checklist** (`tools/templates/checklists/re-gating-trigger.md`) when something changes. Apply the boundary test: can the loop's bounded adaptation return the agent to its contracted behaviour? Yes → loop handles it. No → the gate re-opens (lifecycle → Proposed; only the changed slice re-enters).

### 5. Audit (read-only assessment)
Assess an existing agentic system against the gates without changing it. Score each gate row against the live evidence, produce a scorecard of pass / gap / unknown, and name the artifact each gap needs. This is the assessment half of `aeaf-retrofit`, usable standalone.

## Quality bar
- **A box points to evidence** — name the artifact/test/record. The standing question: *show me the artifact that makes this true.*
- **Accountability is one named human** per capability; never an agent.
- **The Trust & Accountability Matrix is a living view**, not a sign-off filed once — a stale one asserts a fitness the evidence no longer supports.
- **Three re-gating triggers only** — material change, widened autonomy, failed assurance case. Neither escalate a transient dip to a full cycle, nor treat a broken assurance case as a dip.

## Hand off to
- `aeaf-author` to write the contract / matrix / assurance case; `aeaf-evals` when assurance evidence is the gap.
