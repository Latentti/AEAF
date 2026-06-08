---
artifact: agent-catalog
title: "Agent Catalog — Parkki Nordic support line"
type: catalog
phase: 6
domain: [I]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
as_of: 2026-06-03
version: 1.0
links: [model-portfolio, knowledge-corpus-catalog, guardrail-policy-catalog, autonomy-level-classification, eval-suite-specification, trust-accountability-matrix, human-agent-raci, capability-automation-frontier-map]
---

# Agent Catalog — Parkki Nordic support line

The five agent actors of the support line. This is the hub: follow any row's IDs to the model that powers it, the corpora it draws on, the guardrails that bound it, the autonomy it holds, the eval that assures it, and the human who answers for it.

| Agent ID | Name | Purpose / objective (incl. what it does NOT do) | Capabilities | Models run | Knowledge corpora | Tools / actions | Guardrails | Autonomy level | Oversight mode | Eval suite | Accountability owner | Lifecycle status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `AG-001` | Triage Agent | Understand the contact and verify identity, then route to the right specialist agent or human. Does **not** resolve cases itself or open the gate. | `CAP-001` | `M-003` | `KC-004` | `account_lookup` (read) · `get_parking_session` (read) · `knowledge_search` (read) · hand-off (internal) | `G-3`, `G-4`, `G-5`, `G-8`, `G-9` | `L3` | On-the-loop | `EV-001` | Support Operations Lead | operating |
| `AG-002` | Gate-Ops Agent | Resolve a stuck-at-exit case by verifying a paid session and opening the gate. Does **not** open a gate without a verified paid session, and does **not** handle safety cases. | `CAP-002` | `M-001` | `KC-002`, `KC-001` | `get_parking_session` (read) · `get_anpr_event` (read) · `open_gate` (gated write, reversible) | `G-1`, `G-3`, `G-4`, `G-5`, `G-6`, `G-7` | `L2` at go-live; `L3` target | In-the-loop (operator confirms each open) | `EV-002` | Support Operations Lead | operating (L2) |
| `AG-003` | Billing-Dispute Agent | Explain a charge and resolve an in-policy billing question; initiate a refund ≤ €50 in-policy or escalate. Does **not** approve refunds > €50 or contested refunds. | `CAP-003`, `CAP-007` | `M-001` | `KC-001`, `KC-003` | `get_payment_history` (read) · `account_lookup` (read) · `knowledge_search` (read) · `refund_initiate` (gated write, money) · `escalate_to_human` (write) | `G-2`, `G-3`, `G-4`, `G-5`, `G-7` | `L3` (explain); `L1` (refund) | On-the-loop (explain); in-the-loop (refund) | `EV-003` | Billing Lead (Markus Vainio) | operating |
| `AG-004` | ANPR-Correction Agent | Correct a camera misread or wrong plate association within bounds; escalate ownership transfers and contested cases. Does **not** transfer ownership or alter another customer's record. | `CAP-004` | `M-001` | `KC-002` | `get_anpr_event` (read) · `get_parking_session` (read) · `account_lookup` (read) · `escalate_to_human` (write) | `G-3`, `G-4`, `G-5`, `G-8` | `L1` → `L3` target | In-the-loop | `EV-004` | Data Lead (Tuuli Korhonen) | operating (L1) |
| `AG-005` | Escalation-Router Agent | Route a bounded or low-confidence case to the right human queue with full context; schedule a callback. Does **not** make the substantive decision it escalates. | `CAP-008` | `M-002` | `KC-004` | `escalate_to_human` (write) · `schedule_callback` (reversible write) · `knowledge_search` (read) | `G-3`, `G-4` | `L3` | On-the-loop | `EV-005` | Support Operations Lead | operating |

**Reading the hub.** Take `AG-002`: it runs model `M-001`, draws on corpora `KC-002` and `KC-001`, is bounded by guardrails `G-1`/`G-3`/`G-4`/`G-5`/`G-6`/`G-7`, sits at autonomy `L2` (in-the-loop) with `L3` as the assured target, is assured by eval suite `EV-002`, and is answerable through the Support Operations Lead. Each of those IDs resolves in its own artifact — that is the traceability the meta-model promises.

**Why one accountability owner per agent, never the platform.** Every row names a single human role; `aeaf-validate` rule R20 fails the build if an `AG-` id ever appears in an accountability cell.
