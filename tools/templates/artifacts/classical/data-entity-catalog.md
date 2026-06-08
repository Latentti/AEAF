---
artifact: data-entity-catalog
title: Data Entity Catalog
type: catalog
phase: 3
domain: [D]
status: stub
owner: "TBD"
version: 0.1
links: [knowledge-corpus-catalog]
---

# Data Entity Catalog

**Classical artifact; changed for the Agentic Enterprise.** A data entity that is **curated into a knowledge corpus** gains a `feedsCorpus` link to the Knowledge-Corpus Catalog. The raw data entity and the embedded, access-controlled corpus are distinct objects — link them, do not conflate them. (→ Book 1 Table 21.1.)

## Template — one data entity per row

| Field | What to record |
|---|---|
| **Entity ID** | `DE-nnn`. |
| **Entity name** | The data entity. |
| **Classification** | Sensitivity / regulatory class; PII flag. |
| **System of record** | Where it is mastered. |
| **Feeds corpus** *(new)* | `KC-nnn` it is curated into (→ `knowledge-corpus-catalog`). |
| **Owner** | Data owner. |

## Filled rows

<!-- example -->

| Entity ID | Entity name | Classification | System of record | Feeds corpus | Owner |
|---|---|---|---|---|---|
| `DE-001` | *(policy document)* | internal-confidential, no PII | *(doc store)* | `KC-001` | *(named owner)* |
| `DE-002` | *(customer record)* | PII / regulated | *(core system)* | — (not curated into a corpus) | *(named owner)* |

**Watch.** A data entity with PII generally does **not** feed a knowledge corpus — the corpus grounds reasoning, it is not a place to stash personal data. If it must, the corpus's classification and access policy carry the control.
