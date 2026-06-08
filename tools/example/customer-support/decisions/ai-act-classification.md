---
artifact: ai-act-classification
title: "ADR-002 — EU AI Act risk classification of the support line"
type: decision
phase: P
domain: [I]
status: approved
owner: "DPO (Eeva Lindström), with external counsel"
version: 1.0
links: [principles-catalog, regulatory-obligations-register, requirements-intent-catalog]
---

# ADR-002 — EU AI Act risk classification of the support line

| Field | Entry |
|---|---|
| **ID** | `ADR-002` |
| **Date** | 2026-03-25 |
| **Status** | accepted (confirmed with external counsel 2026-03-24) |
| **Decision owner** | DPO (Eeva Lindström) |

## Context
The EU AI Act (Regulation 2024/1689) requires every AI system to be classified by risk, and the classification drives the obligations that follow. The Parkki Nordic support line is an AI system that interacts with the public, processes personal data, and assists decisions on money and a physical gate. Its tier had to be decided and recorded, not assumed.

## Decision
The support line is classified **limited-risk** under the AI Act, carrying the **Art 50 transparency obligation** (the caller must be told they are interacting with an AI). It is assessed as **not high-risk**: it is not an Annex III use case — it does not evaluate creditworthiness, determine access to essential services or benefits, or perform biometric categorisation; refunds are small and reversible, the gate action is operational and bounded by a human-confirmed guardrail, and the significant decisions are reserved to humans. This assessment was confirmed with external counsel.

## Agentic dimensions
| Dimension | Entry |
|---|---|
| **Transparency (Art 50)** | Realised by principle `P-6` and requirement `REQ-001` — disclosure at call start. |
| **Human oversight** | The autonomy model keeps significant decisions human (`P-8`, GDPR Art 22) — see the RACI and autonomy assignment. |
| **Accountability owner** | DPO for the classification; capability owners for operation — never an agent. |

## Consequences
The limited-risk tier means transparency and good-practice obligations rather than the full high-risk conformity regime — a materially lighter load, justified by the bounded use case. **Re-classification triggers** are recorded: if the agents are later given a high-risk capability (e.g. assessing eligibility for a benefit or a credit decision), the tier must be re-assessed before that capability ships. Review date: 2026-Q4, or on any material capability change. The full obligation mapping is the Regulatory Obligations Register (→ `regulatory-obligations-register`).

> Not legal advice — this records a decision taken with counsel; the citation is the evidence, and the classification is revisited on material change.
