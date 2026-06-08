---
artifact: data-entity-catalog
title: "Data Entity Catalog — Parkki Nordic support line"
type: catalog
phase: 3
domain: [D]
status: approved
owner: "Data Lead (Tuuli Korhonen)"
version: 1.0
links: [knowledge-corpus-catalog]
---

# Data Entity Catalog — Parkki Nordic support line

Data entities, with the `feedsCorpus` link where one is curated into a knowledge corpus. Note that the PII and transactional entities feed **no** corpus — they are read live by the tools, never embedded.

| Entity ID | Entity name | Classification | System of record | Feeds corpus | Owner |
|---|---|---|---|---|---|
| `DE-001` | Customer Account | **PII** / regulated | `APP-003` core | — (read live, never embedded) | Data Lead |
| `DE-002` | Tariff schedule | internal, commercially sensitive | `APP-003` core | `KC-001` | Billing Lead |
| `DE-003` | Fee & service-charge rule | internal | policy store | `KC-001`, `KC-003` | Billing Lead |
| `DE-004` | ANPR rule & event model | internal | `APP-003` core | `KC-002` | Data Lead |
| `DE-005` | Refund policy | internal, regulated | policy store | `KC-003` | Billing Lead |
| `DE-006` | Escalation rule | internal | policy store | `KC-004` | Support Operations Lead |
| `DE-007` | Parking Session | transactional (links to PII) | `APP-003` core | — (read live) | Platform owner |
| `DE-008` | Payment Transaction | **PII / PAN** / regulated | `APP-003` core | — (read live) | Billing Lead |

*The rule made visible: policy documents (`DE-002…006`) are curated into corpora the agents reason over; customer, session, and payment data (`DE-001`, `DE-007`, `DE-008`) are **not** — they are fetched live by the read tools and never enter a corpus. This is what keeps PII out of the embeddings, the stance principle `P-1` and guardrail `G-3` enforce.*
