---
artifact: knowledge-corpus-catalog
title: Knowledge-Corpus Catalog
type: catalog
phase: 3
domain: [D, I]
status: stub
owner: "TBD — named owner of corpus currency and accuracy"
as_of: TBD
version: 0.1
links: [agent-catalog, data-entity-catalog, guardrail-policy-catalog]
---

# Knowledge-Corpus Catalog

**What it is.** The register of every governed body of content an agent retrieves from to ground its reasoning — its sources, freshness, classification, and access controls — so that what an agent *knows*, and how current and trustworthy that knowledge is, is governed rather than assumed. The raw document is a Data Entity; the embedded, access-controlled, agent-retrievable corpus is the new object — link them, do not conflate them.
**Produced in.** Phase 3 · Data & Knowledge.
**Instantiates.** `Knowledge Corpus`, with a back-link to the `Data Entity`(ies) it is curated from and forward to the agents that retrieve from it.
**Defined in.** Book 1 §21.4.3 · templated in Book 2 §15.4.

## Template — one corpus per row

| Field | What to record |
|---|---|
| **Corpus ID · name** | e.g. `KC-nnn`. |
| **Sources & data entities** | The documents/data and the Data Entity entries they derive from (→ `data-entity-catalog`). |
| **Freshness / refresh cadence** | How current it is and how/when it is refreshed; the staleness threshold. |
| **Classification** | Sensitivity and regulatory class; the PII stance (explicitly). |
| **Embedding model · index type** | The embedding model and vector index. |
| **Access policy** | Who and which agents may retrieve; retrieval logging. |
| **Retrieving agents** | Agent IDs that draw on it (→ `agent-catalog`). |
| **Owner** | Named owner of the corpus's currency and accuracy (separate from who runs the index). |

## Filled row

<!-- example — replace with your own corpora -->

| Field | Value |
|---|---|
| **Corpus ID · name** | `KC-001` *(corpus name)* |
| **Sources & data entities** | *(documents · derives from `DE-nnn` Data Entities)* |
| **Freshness / refresh cadence** | Reviewed monthly; re-indexed on source change; staleness > 30 days triggers guardrail `G-n` |
| **Classification** | Internal-confidential; **no customer PII held in the corpus**; *(regulatory class)* |
| **Embedding model · index type** | *(EU-hosted embedding model; hybrid keyword + dense)* |
| **Access policy** | Read-only to `AG-001`; no write path; retrieval logged for the assurance case |
| **Retrieving agents** | `AG-001` |
| **Owner** | *(named owner — content currency)*; EA *(index/freshness)* |

## Common mistakes (→ Book 2 §15.4)

- **No freshness field, or one nobody enforces.** Tie staleness to a guardrail so a stale corpus *stops* the agent — the catalog and the Guardrail/Policy Catalog must agree.
- **Letting customer PII leak into the corpus.** The corpus grounds reasoning; it is not a place to stash personal data. Record the PII stance explicitly.
- **No owner for currency.** Name who is answerable for the *content* being right and current, separate from who runs the index.
- **Cataloguing the data entity instead of the curated corpus.** Link them; do not conflate.
