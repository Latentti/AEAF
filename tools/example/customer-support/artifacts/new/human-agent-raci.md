---
artifact: human-agent-raci
title: "Human-Agent RACI — Parkki Nordic support line"
type: matrix
phase: 2
domain: [B, I]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
accountable: "Head of Customer Support (Antti Salo)"
as_of: 2026-06-03
version: 1.0
links: [autonomy-level-classification, trust-accountability-matrix, capability-automation-frontier-map, agent-catalog]
---

# Human-Agent RACI — Parkki Nordic support line

The responsibility/accountability split per capability, with the decision-authority band. In every row the **A is a human**; the agent is **R** only where the work is routine and reversible.

| Capability / decision | Agent | Support operator (human) | Accountability owner | AI-risk reviewer | Decision-authority band | Escalation target |
|---|---|---|---|---|---|---|
| Triage & route (`CAP-001`) | **R** `AG-001` (L3, on-loop) | C | **A** Support Operations Lead | I | agent-alone | operator on low confidence |
| Open gate for paid session (`CAP-002`) | **R** `AG-002` (L2, in-loop) | A?→C (confirms each open) | **A** Support Operations Lead | I | agent-proposes-human-approves → agent-alone (target, sampled) | operator |
| Explain a charge (`CAP-003`) | **R** `AG-003` (L3, on-loop) | C | **A** Billing Lead | I | agent-alone | operator on dispute |
| Refund ≤ €50 in policy (`CAP-007`) | **R** `AG-003` (L1) | **A**?→C (approves each) | **A** Billing Lead | I | agent-proposes-human-approves | Billing operator |
| Refund > €50 / contested (`CAP-007`) | I (drafts only) | **R** | **A** Billing Lead | C | **human-alone** (principle `P-4`) | Billing supervisor |
| Correct ANPR misread (`CAP-004`) | **R** `AG-004` (L1) | C | **A** Data Lead | I | agent-proposes-human-approves | Data operator |
| Account / GDPR request (`CAP-005`) | I (routes only) | **R** | **A** Data Lead | C | **human-alone** | Data Lead |
| Safety / emergency (`CAP-006`) | I (routes only) | **R** | **A** Support Operations Lead | C | **human-alone** (principle `P-2`) | 24/7 line + supervisor |
| Escalate & callback (`CAP-008`) | **R** `AG-005` (L3, on-loop) | C | **A** Support Operations Lead | I | agent-alone | named human queue |
| Raise an agent's autonomy level | I | I | C | **R** (recommends) | governance gate decides | architecture gate |

*The two human-alone rows for safety and account/GDPR are the frontier the board pre-decided the agents cannot cross. The refund row splits at the decision level: ≤ €50 in-policy is agent-proposes-human-approves; > €50 or contested is human-alone.*
