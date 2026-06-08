---
artifact: architecture-definition-document
title: Architecture Definition Document (BDAT+I)
type: deliverable
phase: 6
domain: [B, D, A, T, I]
status: stub
owner: "TBD — lead architect"
version: 0.1
links: [business-capability-catalog, data-entity-catalog, knowledge-corpus-catalog, application-portfolio-catalog, technology-portfolio-catalog, agent-catalog, model-portfolio, guardrail-policy-catalog, autonomy-level-classification, human-agent-raci, trust-accountability-matrix, capability-automation-frontier-map]
---

# Architecture Definition Document (BDAT+I)

**Deliverable — the headline one.** The ADD is the single document an architecture review or a board reads to understand the whole target architecture. In AEAF it spans the five domains — **B**usiness, **D**ata, **A**pplication, **T**echnology, **+ I**ntelligence & Agency — by *assembling* the domain artifacts with a synthesis per layer. It does not re-author the artifacts; it composes them into one reviewable whole.

## Structure (one section per domain, each assembling its artifacts)

| Domain | Assembles | Synthesis to write |
|---|---|---|
| **Business** | `business-capability-catalog`, `human-agent-raci`, `capability-automation-frontier-map`, `organization-actor-catalog`, `role-catalog` | The capability model, who/what performs each, the frontier and its trajectory. |
| **Data** | `data-entity-catalog`, `knowledge-corpus-catalog` | The data + the cognitive substrate; what is governed, what is kept out of corpora. |
| **Application** | `application-portfolio-catalog`, `process-function-catalog` | The services, the runtimes, the non-determinism design. |
| **Technology** | `technology-portfolio-catalog`, `model-portfolio` | The AI platform and its enforcement points. |
| **Intelligence & Agency (+I)** | `agent-catalog`, `guardrail-policy-catalog`, `eval-suite-specification`, `autonomy-level-classification`, `trust-accountability-matrix` | The agents, their guardrails, their evals, their autonomy, who is accountable. |

## Front matter to write
- **Architecture overview** — one diagram of the whole (Mermaid), one paragraph per domain.
- **Key decisions** — the significant ADRs (→ `decisions/`).
- **Gaps & roadmap pointer** — what is target vs baseline (→ the Roadmap deliverable).

**Assembled from** every BDAT+I artifact. The ADD is the composition; trace any claim in it back to the artifact that holds the detail.
