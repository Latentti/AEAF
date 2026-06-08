---
artifact: regulatory-obligations-register
title: Regulatory Obligations Register
type: catalog
phase: P
domain: [B, I]
status: stub
owner: "TBD — DPO / compliance owner"
as_of: TBD
version: 0.1
links: [principles-catalog, guardrail-policy-catalog, requirements-intent-catalog, trust-accountability-matrix, agentic-adr]
---

# Regulatory Obligations Register

**Supporting view — not a tenth core artifact.** AEAF defines exactly nine core artifacts; this is a *supporting governance view* in the same sense as the Technology Radar (→ Book 1 §21.6). It does not instantiate a new meta-model entity — it **maps** an external obligation onto the principles, guardrails, and controls that already realise it, so an auditor or a DPO can read, in one place, "which law applies, what realises it, and what is the evidence." If a regulation needs a *new* enforced rule, that rule is added as a principle (with `Enforcement`) and a guardrail in the core artifacts; this register only traces it.

**What it is.** One row per obligation. Each obligation names the regulation and article, what it requires here, what in the architecture realises it, the evidence, and the named owner. Established in the Preliminary phase from the regulatory exposure characterised there; refreshed when the law or the system changes.

> **Not legal advice.** This register is an engineering-traceability artifact. The classification of obligations (especially an EU AI Act risk tier) must be confirmed with counsel / the DPO; record that confirmation as the evidence.

## Template — one obligation per row

| Field | What to record |
|---|---|
| **Obligation ID** | e.g. `OBL-nnn`. |
| **Regulation · article** | The instrument and the specific article/provision. |
| **Obligation (plain)** | What it requires, in one sentence, for this service. |
| **Applies to** | The capability/agent it bears on (→ `agent-catalog`, capability IDs). |
| **Realised by** | The principle / guardrail / control / allocation that satisfies it (→ `principles-catalog`, `guardrail-policy-catalog`). |
| **Evidence** | The record that proves it is satisfied (DPIA, classification ADR, DPA, log, gate row). |
| **Owner** | The named human answerable (often the DPO / compliance owner). |
| **Status** | met / partial / open. |

## Filled row

<!-- example — replace with your own obligations -->

| Obligation ID | Regulation · article | Obligation (plain) | Applies to | Realised by | Evidence | Owner | Status |
|---|---|---|---|---|---|---|---|
| `OBL-001` | GDPR Art 22 | A significant decision is not made by the agent alone; a human can intervene | `CAP-007` refund, `CAP-005` account | human-alone allocation + `P-n` + guardrail `G-n` | RACI; autonomy assignment | DPO | met |

## Common mistakes

- **Treating it as the place the rule is *enforced*.** It is not — it *maps* to the principle and guardrail that enforce the rule. A register row with no `Realised by` link is an obligation nobody actually meets.
- **Asserting a risk classification without evidence.** An AI Act tier or a "no DPIA needed" call is a documented decision (an ADR + counsel sign-off), not a checkbox.
- **Letting it drift from the law.** Stamp `as_of`; re-check when the regulation or the system changes (a new tool, a new model, a new jurisdiction).
