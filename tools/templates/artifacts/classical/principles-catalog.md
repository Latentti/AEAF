---
artifact: principles-catalog
title: Principles Catalog
type: catalog
phase: P
domain: [B, I]
status: stub
owner: "TBD — architecture board"
version: 0.1
links: [guardrail-policy-catalog]
---

# Principles Catalog

**Classical artifact; changed for the Agentic Enterprise.** Every principle gains the **Enforcement** attribute — **advisory** (guidance only), **design-time** (checked at a gate), or **runtime** (enforced continuously on agent behaviour). Runtime principles link to the guardrails that enforce them. This is the dual-audience move: a principle now has a second audience — agents at runtime. (→ Book 1 Table 21.1; Book 1 §8, §4.6.)

## Template — one principle per row

| Field | What to record |
|---|---|
| **Principle ID** | `P-n`. |
| **Name** | Short name. |
| **Statement** | What the enterprise believes/requires. |
| **Rationale** | Why. |
| **Implications** | What it forces a design to do. |
| **Enforcement** *(new)* | advisory / design-time / runtime. |
| **Compiled guardrails** *(new, if runtime)* | `G-n` that enforce it (→ `guardrail-policy-catalog`). |

## Filled rows

<!-- example -->

| ID | Name | Statement | Enforcement | Compiled guardrails |
|---|---|---|---|---|
| `P-1` | *(data boundary)* | Customer PII is never sent to third parties. | **runtime** | `G-3` |
| `P-2` | *(human for sensitive cases)* | A vulnerability signal routes to a human; the agent cannot proceed. | **runtime** | `G-2` |
| `P-3` | *(transparency)* | Agent-produced output is disclosed as AI-generated. | design-time | — |

**Watch.** A runtime-enforced principle that compiles into no guardrail is a belief, not a control. The compilation chain *principle → policy → guardrail → enforcement point* is what makes the principle reach the agent at runtime.
