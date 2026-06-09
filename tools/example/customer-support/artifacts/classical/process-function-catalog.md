---
artifact: process-function-catalog
title: "Process / Function Catalog — Parkki Nordic support line"
type: catalog
phase: 2
domain: [B]
status: approved
owner: "Support Operations Lead (Henna Laaksonen)"
version: 1.0
links: [business-capability-catalog, agent-catalog, human-agent-raci]
---

# Process / Function Catalog — Parkki Nordic support line

The call flow as process steps, each with its actor-type and — for agent steps — its oversight mode, escalation, and behaviour on model failure.

| Step ID | Process · step | Capability | Actor-type | Oversight | Escalation path | On model fail / low confidence |
|---|---|---|---|---|---|---|
| `PRC-001` | Call · greet, disclose AI (`P-6`) & capture recording consent (`P-10`) | `CAP-001` | agent | on-the-loop | human line if consent declined (`G-9`) | fall back to fixed greeting script |
| `PRC-002` | Call · verify identity (plate/account) | `CAP-001` | agent | on-the-loop | operator on repeated mismatch (`G-8`) | route to operator, preserve context |
| `PRC-003` | Call · classify intent & route | `CAP-001` | agent | on-the-loop | operator on low confidence | route to operator |
| `PRC-004` | Gate · verify paid session & open | `CAP-002` | agent | in-the-loop (operator confirms) | operator → supervisor (`G-1`) | deny + escalate (never open on uncertainty) |
| `PRC-005` | Any · detect safety/distress | `CAP-006` | agent → human | n/a (routes only) | 24/7 line + supervisor (`G-4`) | route to human immediately |
| `PRC-006` | Billing · explain charge / stage refund | `CAP-003`, `CAP-007` | agent | on/in-the-loop | billing operator (`G-2`) | escalate with context |
| `PRC-007` | Any · escalate & schedule callback | `CAP-008` | agent | on-the-loop | named human queue | schedule callback, preserve context |

*Every agent-touched step has a defined behaviour when the model fails or is unsure — and for the consequential step (`PRC-004`) that behaviour is **deny and escalate**, never "open on uncertainty."* The catalog's home is Phase 2 (the process steps and their actor-type/oversight allocation); the **behaviour-on-failure column records the Phase 4 non-determinism design** against each step — one classical artifact carrying attributes from two phases.
