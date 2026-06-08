---
artifact: gap-register
title: "Gap Register — just-do-it PoC vs AEAF (Parkki Nordic)"
type: catalog
phase: 7
domain: [B, I]
status: baseline
owner: "EA / retrofit lead (Joonas Mäkinen)"
as_of: 2026-06-03
version: 1.0
links: []
---

# Gap Register — just-do-it PoC vs AEAF

The `aeaf-retrofit` Stage-3 output: every gap the scan of the just-do-it PoC found, the production risk it leaves open, the AEAF artifact or gate that closes it, and its severity. Severity is **legal** (may be unlawful to operate), **operational** (service fails or cannot be run as a business), or **quality** (worse outcomes). The closing artifacts live in `../customer-support/`.

| Gap ID | What the PoC leaves undone | Production risk | Closed by | Severity |
|---|---|---|---|---|
| `GAP-01` | Bounds exist only as prompt instructions | The model can be argued past a "rule"; an unpaid gate opens, an over-cap refund goes out | Guardrail/Policy Catalog (`G-1…G-9`), enforced fail-closed | operational |
| `GAP-02` | No graded autonomy; the agent acts in production with no controls | Consequential actions taken with no preview, no veto, no sampled review | Autonomy-Level Classification + per-capability assignment | operational |
| `GAP-03` | No accountability owner | When something goes wrong, no one is answerable; no decision authority | Human-Agent RACI + Trust & Accountability Matrix | legal · operational |
| `GAP-04` | No agent evaluation | Drift is invisible; "it worked in the demo" is the only evidence | Eval-Suite Specification (`EV-001…005`), online | operational |
| `GAP-05` | No design-time gate | Nothing decides whether the agent is safe to operate before it does | Design-time gate + agentic architecture contract | operational |
| `GAP-06` | No runtime assurance loop | No one watches distributions; no containment on drift | Phase 10 runtime loop + re-gating triggers | operational |
| `GAP-07` | Bounds not traced to principles | Unauditable — no statement of what the service believes/requires | Principles Catalog with Enforcement | quality · legal |
| `GAP-08` | Audit log is 7-day TTL, mutable, no signing | An incident cannot be reconstructed or trusted | WORM decision-trail store (`TC-008`) | legal · operational |
| `GAP-09` | No DPIA | High-risk processing of personal data without the required assessment | Regulatory Obligations Register (`OBL-006`) | legal |
| `GAP-10` | No EU AI Act risk classification | Obligations undetermined; transparency duty unmet | AI Act classification ADR (`ADR-002`, `OBL-009`) | legal |
| `GAP-11` | No GDPR Art 22 human-intervention path | Significant automated decisions made with no lawful intervention | `P-8` + human-alone / in-the-loop allocations (`OBL-004`) | legal |
| `GAP-12` | No processor agreement with the model vendor | Personal data sent to a processor without an Art 28 DPA | DPA + Model Portfolio risk record (`OBL-005`) | legal |
| `GAP-13` | No retention / minimisation policy | Undefined retention; PII risk in logs and corpora | `P-9` + no-PII-in-corpora design (`OBL-002/003`) | legal |
| `GAP-14` | No call-recording consent | Calls processed/recorded without consent | `P-10` + guardrail `G-9` (`OBL-010`) | legal |
| `GAP-15` | No corpus governance (freshness, owner, classification) | Agent answers from stale or unowned policy | Knowledge-Corpus Catalog + `G-7` freshness guardrail | quality |
| `GAP-16` | Fragile escalation; unclear behaviour on tool/model failure | Agent loops or fails silently; caller stuck | Non-determinism design (`process-function-catalog`); escalation paths | operational |
| `GAP-17` | No cost controls on model/agent usage | Uncapped spend; a spike causes runaway cost | Model Portfolio cost profile + eval cost dimension | operational |
| `GAP-18` | No continuity / SLA / staging | No availability guarantee; deploy straight to prod | Technology architecture + migration planning | operational |
| `GAP-19` | One undifferentiated agent | No bounded purpose; cannot reason about or govern it | Agent Catalog (five bounded agents) | quality · operational |
| `GAP-20` | No accessibility consideration | Service may breach the European Accessibility Act | Regulatory Obligations Register (`OBL-012`, tracked partial) | legal |

**How to read severity.** The **legal** rows are the decisive ones: any single one can mean the service cannot lawfully operate in the EU, regardless of how well it demos. The **operational** rows are why it cannot be run as a business even where it is lawful. The **quality** rows are why outcomes are worse. The just-do-it PoC carries all three classes at once — which is the definition of a collapsing PoC, not a near-finished product.
