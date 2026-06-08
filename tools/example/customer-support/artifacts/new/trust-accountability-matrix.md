---
artifact: trust-accountability-matrix
title: "Trust & Accountability Matrix — Parkki Nordic support line"
type: matrix
phase: 9
domain: [B, I]
status: runtime
owner: "Support Operations Lead (Henna Laaksonen)"
accountable: "Head of Customer Support (Antti Salo)"
as_of: 2026-06-03
version: 1.0
links: [agent-catalog, autonomy-level-classification, eval-suite-specification, human-agent-raci, capability-automation-frontier-map, regulatory-obligations-register]
---

# Trust & Accountability Matrix — Parkki Nordic support line

The live standing view as of **2026-06-03** — who is answerable for each agent right now, how it is overseen, and the current evidence it is fit to operate. Refreshed by the runtime loop; this is what the governance gate and an auditor read.

| Capability / agent | Accountability owner | Oversight mode | Autonomy | Assurance status | Residual risk | Escalation path |
|---|---|---|---|---|---|---|
| Triage & route (`AG-001`) | Support Operations Lead | On-the-loop | `L3` | Routing 98.6%; safety routing 99.7%; no open incident; case reviewed 2026-05 | Dialect-heavy calls sampled thin | low confidence → operator |
| Resolve gate/exit (`AG-002`) | Support Operations Lead | In-the-loop (operator confirms) | `L2` | `G-1` holds 100% in `EV-002`; staging proven; gathering live evidence toward L3 | No live L3 evidence yet; Tampere garages not in golden set | operator → supervisor |
| Explain a charge (`AG-003`) | Billing Lead | On-the-loop | `L3` | Explanation quality 96%; no incident | New fee categories untested | operator on dispute |
| Refund ≤ €50 (`AG-003`) | Billing Lead | In-the-loop | `L1` | `G-2` cap holds 100%; human approves each | — | Billing supervisor |
| Correct ANPR misread (`AG-004`) | Data Lead | In-the-loop | `L1` | Correction accuracy 96%; no cross-customer edit | Previous-owner cases still thin | Data operator |
| Escalate & callback (`AG-005`) | Support Operations Lead | On-the-loop | `L3` | Queue accuracy 98.4%; context completeness 95% | Callback scheduling load not yet peak-tested | named human queue |
| Account / GDPR (`CAP-005`) | Data Lead | Human-only | n/a | n/a — not agent-performed | — | Data Lead |
| Safety / emergency (`CAP-006`) | Support Operations Lead | Human-only | n/a | n/a — not agent-performed | — | 24/7 line |

*The matrix does live work: it records `AG-002` honestly as L2 with **no L3 evidence yet** and the Tampere-garage gap in its golden set — the residual-risk column filled honestly, so a future Tampere incident is a known gap surfacing, not a surprise. The oversight modes reconcile with the Agent Catalog; where they ever disagree, this live matrix wins and the catalog is corrected.*

**Regulatory standing.** The **DPO (Eeva Lindström)** owns the EU-obligation evidence behind this matrix; the live mapping is the Regulatory Obligations Register (→ `regulatory-obligations-register`). Open regulatory residual risk as of this date: accessibility (`OBL-012`) is **partial** pending the accessibility test report — tracked, not silent. The GDPR Art 22 human-intervention requirement is satisfied by the human-alone and in-the-loop allocations recorded above.
