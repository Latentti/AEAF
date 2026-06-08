---
artifact: actor-role-matrix
title: "Actor/Role Matrix — Parkki Nordic support line"
type: matrix
phase: 2
domain: [B]
status: approved
owner: "Head of Customer Support (Antti Salo)"
version: 1.0
links: [organization-actor-catalog, role-catalog, autonomy-level-classification]
---

# Actor/Role Matrix — Parkki Nordic support line

Which actor holds which role, and — for an agent actor — at what autonomy level. The cells reconcile with the Autonomy-Level Classification (the assignment) and the Human-Agent RACI (the accountability split).

| Actor \ Role | `ROLE-001` Triager | `ROLE-002` Gate resolver | `ROLE-003` Billing explainer | `ROLE-004` Refund ≤ €50 | `ROLE-005` Refund > €50 | `ROLE-006` ANPR corrector | `ROLE-007` Account/GDPR | `ROLE-008` Safety | `ROLE-009` Escalation router |
|---|---|---|---|---|---|---|---|---|---|
| `ACT-001` Support operator (human) | ✓ (confirm) | ✓ (confirms opens) | — | — | — | — | — | ✓ | ✓ (confirm) |
| `ACT-002` Billing operator (human) | — | — | ✓ | ✓ (approves) | ✓ | — | — | — | — |
| `ACT-003` Data operator (human) | — | — | — | — | — | ✓ (approves) | ✓ | — | — |
| `ACT-004` Safety responder (human) | — | — | — | — | — | — | — | ✓ | — |
| `ACT-005` Triage Agent | ✓ (`L3`) | — | — | — | — | — | — | — | — |
| `ACT-006` Gate-Ops Agent | — | ✓ (`L2`) | — | — | — | — | — | — | — |
| `ACT-007` Billing-Dispute Agent | — | — | ✓ (`L3`) | ✓ (`L1`) | — | — | — | — | — |
| `ACT-008` ANPR-Correction Agent | — | — | — | — | — | ✓ (`L1`) | — | — | — |
| `ACT-009` Escalation-Router Agent | — | — | — | — | — | — | — | — | ✓ (`L3`) |

*The human-only roles (`ROLE-005` refund > €50, `ROLE-007` account/GDPR, `ROLE-008` safety) carry no agent ✓ — the frontier the agents cannot cross. Where an agent holds a role, the autonomy level shown matches its assignment in `autonomy-level-classification`; if the two ever disagree, that is a defect to reconcile.*
