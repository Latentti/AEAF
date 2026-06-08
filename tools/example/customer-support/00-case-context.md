---
artifact: case-context
title: "Parkki Nordic Oy — agentic support line: case context"
type: reference
status: approved
version: 1.0
links: []
---

# Parkki Nordic Oy — case context

**In brief.** This is a worked AEAF example: a fictional Nordic parking operator, **Parkki Nordic Oy**, runs an **agentic customer-support line** and brings it under AEAF. The case is deliberately concrete so a reader can see what "an agentic service designed on real enterprise-architecture principles" actually means — every artifact in this folder is filled for this one engagement, and the IDs cross-reference so you can trace one agent across the whole set. The implementation seed is a real proof-of-concept (a voice support agent on a model + telephony + tool webhooks); the company, the people, the figures, and the expanded agent fleet are invented for the example.

> **Fictional.** Parkki Nordic Oy, its staff, its figures, and its agents are invented for this worked example. Any resemblance to a real operator is coincidental. This folder is the **target-state, AEAF-governed** version of the service; the just-do-it version it is compared against is `tools/example/the-drift/` (Pass 4).

## The company

Parkki Nordic Oy operates camera-recognition (ANPR) parking in Finnish city-centre garages — Kamppi and Kluuvi in Helsinki, expanding to Tampere and Turku. Drivers register a plate and a payment card; cameras recognise the plate on entry and exit; the visit is billed automatically (hourly rate + a service fee, with a daily cap). There is no ticket and no barrier-button — which is exactly why support matters: when the camera misreads a plate, when a payment is pending, or when the exit gate will not open, the driver is stuck and calls.

## The decision

Support volume tripled as the garage estate grew. Parkki Nordic decided to put an **agentic voice line** in front of the human support team: agents resolve the routine, reversible cases in minutes (stuck at the gate with a paid session, "why was I charged €18", a camera misread), and hand the sensitive, contested, or irreversible cases to humans. The board's condition was explicit: this is a **production service running real money and a physical gate**, so it must be governed — quality, safety, and continuity provable — not a demo. That condition is why AEAF is applied.

## The blended workforce (the agent fleet)

Five agent actors sit alongside the human support team. The full register is the Agent Catalog (`artifacts/new/agent-catalog.md`); in brief:

| Agent | Purpose | Go-live autonomy |
|---|---|---|
| `AG-001` Triage Agent | Understand the contact, verify identity, route to the right specialist or human. | L3 (on-the-loop) |
| `AG-002` Gate-Ops Agent | Resolve a stuck-at-exit case: verify a paid session, open the gate. | **L2** (execute-with-approval) → L3 target |
| `AG-003` Billing-Dispute Agent | Explain a charge; initiate an in-policy refund or escalate. | L1 / L3 (explain) |
| `AG-004` ANPR-Correction Agent | Correct a camera misread / wrong plate association within bounds. | L1 → L3 target |
| `AG-005` Escalation-Router Agent | Hand a bounded/low-confidence case to the right human queue with context; schedule a callback. | L3 |

## What stays human (on purpose)

Two kinds of work never move to an agent, by board decision and by principle — they are first-class decisions in the frontier map, not gaps:

- **Safety / emergency** — a caller trapped in a garage, an accident, a medical situation. The agent routes to a human and the 24/7 line; it never tries to resolve. (Principle `P-2`.)
- **Account / GDPR and large or contested money** — close an account, delete data, a large or disputed refund. These are human-decided. (Principles `P-4`, `P-7`.)

## The tool surface

The agents act through nine tools, each with a permission and a reversibility class (detailed per agent in the Agent Catalog): read tools — `get_parking_session`, `get_payment_history`, `get_anpr_event`, `account_lookup`, `knowledge_search`; write tools — `open_gate` (gated, reversible), `refund_initiate` (gated, money), `schedule_callback` (reversible), `escalate_to_human` (creates a human ticket).

## How to read this folder

Start with `walkthrough.md` — it runs the AEAF Method phase by phase for this case, so you see *how* the artifacts were produced and *why* each decision was made. Then read the artifacts themselves under `artifacts/`, the decisions under `decisions/`, and the filled gate in `checklists/`. Everything is cross-linked by ID; `aeaf-validate` confirms the set is coherent (see the README).
