---
artifact: guardrail-policy-catalog
title: "Guardrail/Policy Catalog — Parkki Nordic support line"
type: catalog
phase: 6
domain: [I, T]
status: approved
owner: "AI-risk reviewer (Riikka Nieminen)"
as_of: 2026-06-03
version: 1.0
links: [agent-catalog, principles-catalog, eval-suite-specification]
---

# Guardrail/Policy Catalog — Parkki Nordic support line

The machine-enforceable constraints that bound the agents at runtime. Each traces to a principle (→ `principles-catalog`), names where it is enforced, what it does on failure, and the eval that proves it still fires. A guardrail here *bounds*; none of these is a prompt instruction the model could talk past.

| ID | Guardrail | Policy / principle enforced | Scope | Trigger | Enforcement point | Fail action | Owner | Verifying eval |
|---|---|---|---|---|---|---|---|---|
| `G-1` | Open the gate only when a paid (or exempt) session is verified in the system | `P-5` (runtime) | `AG-002` | `open_gate` requested without a verified paid/exempt session | Pre-action (tool permission) | Block + escalate to operator | Support Operations Lead | `EV-002` safety |
| `G-2` | Block any `refund_initiate` > €50 or flagged contested; route to a human | `P-4` (runtime) | `AG-003` | Refund amount > €50 OR contested flag | Output check / spend limit | Block + escalate | Billing Lead | `EV-003` safety |
| `G-3` | No customer PII or payment data past the model gateway | `P-1` (runtime) | all agents | PII / PAN pattern in egress | Model gateway | Block + log | EA / Platform owner | gateway probe (in `EV-001`) |
| `G-4` | Any safety / distress signal routes to a human and the 24/7 line; agent cannot proceed | `P-2` (runtime) | all agents | Distress detector positive (trapped / accident / medical) | Pre-action | Escalate to human + 24/7 line | Support Operations Lead | `EV-001` alignment |
| `G-5` | Act only on system-verified facts; ignore claimed authority/identity | `P-3` (runtime) | all agents | Caller asserts authority/identity not backed by system data | Pre-action | Block the asserted action + log | AI-risk reviewer | `EV-002` safety |
| `G-6` | Rate-limit gate opens per plate | Fraud-prevention policy (from `P-5`) | `AG-002` | > 3 `open_gate` attempts for a plate in 60s | Pre-action | Block + escalate | Support Operations Lead | `EV-002` safety |
| `G-7` | Stop if the policy corpus is behind its freshness threshold | `KC-*` freshness rule | `AG-002`, `AG-003`, `AG-004` | Corpus age beyond its threshold (14/30 d) | Pre-reasoning | Block + alert owner | EA / Platform owner | freshness check (in `EV-003`) |
| `G-8` | Verify identity before any account-specific action | `P-3` (runtime) | `AG-001`, `AG-004` | Account-specific action requested before identity verified | Pre-action | Block until verified | Support Operations Lead | `EV-001` safety |
| `G-9` | Process/record the call only after consent is captured | `P-10` (runtime, ePrivacy) | `AG-001` | Call begins without a recorded consent flag | Pre-reasoning | Block + fall back to human line | DPO (Eeva Lindström) | `EV-001` safety |

**The compilation chain, visible.** Read `G-1`: principle `P-5` ("a physical action needs a paid session") → policy ("no `open_gate` without a verified paid/exempt session") → guardrail enforced **pre-action**, fail = **block + escalate**, proven by **`EV-002` safety**. That chain is what turns a belief into something the agent cannot cross — and what an auditor follows backwards from an incident.
