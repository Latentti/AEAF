---
artifact: knowledge-corpus-catalog
title: "Knowledge-Corpus Catalog — Parkki Nordic support line"
type: catalog
phase: 3
domain: [D, I]
status: approved
owner: "Support Operations Lead (content); EA / Platform owner (index)"
as_of: 2026-06-03
version: 1.0
links: [agent-catalog, data-entity-catalog, guardrail-policy-catalog]
---

# Knowledge-Corpus Catalog — Parkki Nordic support line

The governed content the agents retrieve from to ground their answers. No customer PII is held in any corpus — the corpora ground *reasoning about policy*, not lookups of a person; customer facts come from the read tools at runtime, not the corpus.

| Corpus ID · name | Sources & data entities | Freshness / refresh cadence | Classification | Embedding · index | Access policy | Retrieving agents | Owner |
|---|---|---|---|---|---|---|---|
| `KC-001` Pricing & Fees | Tariff schedule, service-fee rule, daily-cap rule (from `DE-002` Tariff, `DE-003` Fee Rule) | Reviewed monthly; re-indexed on any tariff change; staleness > 14 days fires `G-7` | Internal; **no PII**; commercially sensitive | EU embedding model; hybrid index | Read-only to `AG-002`, `AG-003` | Billing Lead |
| `KC-002` ANPR & Camera-Parking | How ANPR works, misread causes, retry logic, previous-owner cases (from `DE-004` ANPR Rule) | Reviewed quarterly; re-indexed on process change; staleness > 30 days fires `G-7` | Internal; **no PII** | EU embedding model; hybrid index | Read-only to `AG-002`, `AG-004` | Data Lead |
| `KC-003` Payment & Refund Process | Auto-retry policy, refund policy and caps, account-freeze rules (from `DE-003` Fee Rule, `DE-005` Refund Policy) | Reviewed monthly; re-indexed on policy change; staleness > 14 days fires `G-7` | Internal; **no PII**; regulated (consumer payment) | EU embedding model; hybrid index | Read-only to `AG-003` | Billing Lead |
| `KC-004` Escalation Criteria | Escalation categories and triggers, the human queues, the 24/7 safety line (from `DE-006` Escalation Rule) | Reviewed quarterly; re-indexed on org change | Internal; **no PII** | EU embedding model; hybrid index | Read-only to `AG-001`, `AG-005` | Support Operations Lead |

**Freshness is enforced, not hoped.** Each corpus's staleness threshold is wired to guardrail `G-7`: a corpus that falls behind *stops* the agent that depends on it, rather than letting it answer from stale policy. The catalog and the Guardrail/Policy Catalog agree by construction.
