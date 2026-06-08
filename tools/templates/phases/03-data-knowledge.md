---
artifact: phase-03-data-knowledge
title: "Phase 3 · Data & Knowledge — worksheet"
type: worksheet
phase: 3
domain: [D, I]
status: stub
owner: "TBD"
version: 0.1
links: [data-entity-catalog, knowledge-corpus-catalog]
---

# Phase 3 · Data & Knowledge

**Purpose.** Conceptual / logical / physical data; governance, MDM. **ADM analogue:** C (data). **Agentic addition:** add the **cognitive substrate** — knowledge corpora, embeddings/vector indexes, memory, graphs — and their classification and freshness. (→ Book 1 §9, §12; Book 2 §10, §17.3.)

## Inputs
- Capability allocations (which agents need which knowledge).

## Steps
1. Define conceptual / logical / physical data models; data governance and MDM.
2. Design the **cognitive substrate**: the knowledge corpora, embeddings/vector indexes, memory, and graphs the agents will use. **[+I]**
3. Populate the **Knowledge-Corpus Catalog**: per corpus — sources, freshness policy, classification, access controls, retrieving agents. **[+I]**
4. Assign **corpus governance**: who owns currency and quality of each corpus. **[+I]**

## Produces
- `data-entity-catalog` (with `feedsCorpus` links) · `knowledge-corpus-catalog`.

## Exit gate (must be true before Phase 4)
- [ ] Data models + governance/MDM defined
- [ ] Cognitive substrate designed **[+I]**
- [ ] Knowledge-Corpus Catalog populated (sources, freshness, classification, access, agents) **[+I]**
- [ ] Corpus governance assigned (named owner of currency) **[+I]**
