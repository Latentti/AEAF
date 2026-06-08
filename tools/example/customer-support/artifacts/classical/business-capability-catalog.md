---
artifact: business-capability-catalog
title: "Business Capability Catalog — Parkki Nordic support line"
type: catalog
phase: 2
domain: [B]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
version: 1.0
links: [capability-automation-frontier-map, human-agent-raci, autonomy-level-classification, agent-catalog]
---

# Business Capability Catalog — Parkki Nordic support line

The leaf capabilities of "Resolve a customer support contact", decomposed to the level where each has a single allocation. Capabilities are outcome-named and actor-agnostic; the performer mix and autonomy are the agentic additions.

| Capability ID | Capability (outcome name) | Performer mix | Autonomy level | Accountability owner | Agent(s) |
|---|---|---|---|---|---|
| `CAP-001` | Triage and identify the contact | agent | `L3` | Support Operations Lead | `AG-001` |
| `CAP-002` | Resolve a gate / exit problem | agent (hybrid at go-live) | `L2` → L3 target | Support Operations Lead | `AG-002` |
| `CAP-003` | Explain a charge / billing question | agent | `L3` | Billing Lead (Markus Vainio) | `AG-003` |
| `CAP-004` | Correct an ANPR misread / plate association | agent | `L1` → L3 target | Data Lead (Tuuli Korhonen) | `AG-004` |
| `CAP-005` | Handle an account / GDPR request | **human** | n/a | Data Lead | — |
| `CAP-006` | Handle a safety / emergency contact | **human** | n/a | Support Operations Lead | — |
| `CAP-007` | Issue a refund | split: agent recommends ≤ €50 in-policy; **human** for > €50 / contested | `L1` (small) | Billing Lead | `AG-003` |
| `CAP-008` | Escalate and schedule a callback | agent | `L3` | Support Operations Lead | `AG-005` |

**The two human-only leaves are decisions, not gaps.** `CAP-005` and `CAP-006` stay human by principle (`P-2`) and board appetite — recorded as fixed-human in the frontier map (→ `capability-automation-frontier-map`). `CAP-007` is split at the decision level because "refund €12 for a double-charge" and "refund a contested €400" have opposite allocations.
