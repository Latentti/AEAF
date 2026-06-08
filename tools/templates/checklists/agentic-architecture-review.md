---
artifact: agentic-architecture-review
title: Agentic Architecture Review Checklist (before the gate)
type: checklist
phase: 6
domain: [I]
status: approved
version: 1.0
links: [agent-catalog, guardrail-policy-catalog, eval-suite-specification, autonomy-level-classification]
---

# Agentic Architecture Review Checklist

**What it is.** The independent review run over an agent design **after Phase 6 produces it and before the design-time gate** — by a reviewer who is not on the design team. Its job is to catch the design defects the gate would otherwise reject, so the gate spends its time on the governance decision, not on finding holes. A **fail** on any row sends the design back to the team; the gate is not convened until every row passes or the team has a documented, reviewer-accepted exception. (→ Book 2 §17.4.)

Run once the Agent Catalog entry, guardrails, evals, autonomy level, and owner are drafted.

## Allocation & autonomy
- [ ] **Allocation justified** — a stated reason this capability is allocated to an agent rather than a human, tied to the value stream and frontier map (not "because we can")
- [ ] **Autonomy level appropriate to consequence** — matches reversibility and blast radius; higher autonomy only where actions are bounded and recoverable
- [ ] **Autonomy is granted, not assumed** — the controls the level requires are present in the design, not deferred

## Guardrails
- [ ] **Guardrails present for every hard bound** the intent declares (spend limits, prohibited actions, data boundaries)
- [ ] **Fail-closed where consequence demands** — default-on-failure is block where harm is irreversible; fail-open only for low-consequence reversible actions, documented as a choice
- [ ] **Guardrails enforce, not advise** — each runtime principle compiled into a guardrail at a named enforcement point
- [ ] **Tool permissions are least-privilege** — only the tools the capability needs, narrowest scope

## Evaluation & assurance
- [ ] **Eval suite exists** covering normal path, edge cases, known failure modes
- [ ] **Thresholds set and fixed before results are seen**
- [ ] **An assurance case argues the agent clears the thresholds**, states residual risk and review date

## Oversight, accountability & knowledge
- [ ] **Oversight mode is a deliberate choice** tied to consequence/confidence, with an escalation path naming trigger, target, fallback
- [ ] **Accountability owner named** — exactly one human/role, recorded before the agent acts
- [ ] **Knowledge-corpus governance in place** — source, freshness policy, access control, owner per corpus

## Safety & threat coverage
- [ ] **Threat surface considered** — prompt injection, tool misuse, data exfiltration, corpus poisoning addressed with a control or an accepted-risk note
- [ ] **Defense in depth** — controls at more than one layer (input, model, reasoning, output, operations)
- [ ] **Graded kill-switch exists** — scope-reduce, session-kill, roll-back; a precondition of granting autonomy
- [ ] **Decision trail will be captured** — reasoning, tools chosen, guardrail checks
