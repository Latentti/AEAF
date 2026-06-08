---
artifact: regulatory-obligations-register
title: "Regulatory Obligations Register — Parkki Nordic support line"
type: catalog
phase: P
domain: [B, I]
status: approved
owner: "DPO (Eeva Lindström)"
as_of: 2026-06-03
version: 1.0
links: [principles-catalog, guardrail-policy-catalog, requirements-intent-catalog, trust-accountability-matrix, agentic-adr]
---

# Regulatory Obligations Register — Parkki Nordic support line

**Supporting view — not a tenth core artifact.** This maps each EU obligation onto the principle, guardrail, or allocation that already realises it, so the DPO and an auditor read "which law, what realises it, what is the evidence" in one place. Where a regulation needed a new enforced rule, that rule was added to the core artifacts (a principle + a guardrail); this register only traces it.

| Obligation ID | Regulation · article | Obligation (plain) | Applies to | Realised by | Evidence | Owner | Status |
|---|---|---|---|---|---|---|---|
| `OBL-001` | GDPR Art 6 | A lawful basis exists for processing | all contacts | contract-performance basis; recording consent (`P-10`) | privacy notice; `ADR-002` scope | DPO | met |
| `OBL-002` | GDPR Art 5(1)(c) | Data minimisation — no more personal data than needed | all agents | `P-9`; no PII in corpora (`G-3`, `DE-001`/`DE-007`/`DE-008` not embedded) | `data-entity-catalog`; gateway probe | DPO | met |
| `OBL-003` | GDPR Art 5(1)(e) | Storage limitation — defined retention | audit + transcripts | `P-9`; WORM store `TC-008` with retention policy | retention config; `TC-008` | DPO | met |
| `OBL-004` | **GDPR Art 22** | No solely-automated significant decision; human can intervene | `CAP-007` refund, `CAP-005` account, `CAP-002` gate | `P-8`; human-alone & in-the-loop allocations; `G-2` | `human-agent-raci`; `autonomy-level-classification` | DPO + Billing Lead | met |
| `OBL-005` | GDPR Art 28 | A data-processing agreement with each processor | model vendor (`M-001…003`) | EU-region DPA with the inference provider | signed DPA; `model-portfolio` risk profile | DPO | met |
| `OBL-006` | GDPR Art 35 | A DPIA where processing is high-risk to data subjects | the whole service | DPIA completed before go-live | DPIA v1 (2026-03) | DPO | met |
| `OBL-007` | GDPR Art 15–17 | Access / rectification / erasure on request | `CAP-005` | human-only handling; `AG-004` corrects, never deletes | `human-agent-raci` `CAP-005` row | Data Lead | met |
| `OBL-008` | **EU AI Act Art 50** | Tell the user they are interacting with an AI | all contacts | `P-6`; `REQ-001` disclosure at call start | call-opening logs; `requirements-intent-catalog` | DPO | met |
| `OBL-009` | EU AI Act (classification) | Classify the system's risk tier and record it | the whole service | limited-risk classification | `ADR-002` (counsel-confirmed) | DPO | met |
| `OBL-010` | ePrivacy | Consent before recording/processing the call | `AG-001` | `P-10`; guardrail `G-9` (block until consent) | `guardrail-policy-catalog` `G-9`; `PRC-001` | DPO | met |
| `OBL-011` | PSD2 / consumer protection | Honour consumer refund and dispute rights | `CAP-007` | refund policy `KC-003`; cap + escalation `G-2`; large/contested human-alone | `KC-003`; `human-agent-raci` | Billing Lead | met |
| `OBL-012` | European Accessibility Act | The service is accessible | voice line + UI | accessible-design requirement on `APP-002` | accessibility test report | EA / Platform owner | partial |

**Reading the value.** GDPR Art 22 (`OBL-004`) is the clearest case: AEAF's autonomy model already realises it — the human-alone allocation for large/contested refunds and account actions, plus the in-the-loop gate, *is* the "right to human intervention." No bolt-on was needed; the obligation maps onto structure that exists. The one open item — accessibility (`OBL-012`) — is recorded honestly as **partial**, so it is a tracked obligation, not a silent gap.

> Not legal advice. Each row's classification was confirmed with the DPO / counsel; the citation and the evidence record are what make the row true. Re-checked on any material change to the law or the system (`as_of` 2026-06-03).
