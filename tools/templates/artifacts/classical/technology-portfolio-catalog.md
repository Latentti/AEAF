---
artifact: technology-portfolio-catalog
title: Technology Portfolio Catalog
type: catalog
phase: 5
domain: [T]
status: stub
owner: "TBD"
version: 0.1
links: [model-portfolio, guardrail-policy-catalog, application-portfolio-catalog]
---

# Technology Portfolio Catalog

**Classical artifact; changed for the Agentic Enterprise.** Now includes **inference platforms, model gateways, vector stores, and agent/orchestration runtimes** as first-class technology components — the AI platform. The model gateway is also where several runtime guardrails are enforced. (→ Book 1 Table 21.1; Book 1 §14.)

## Template — one technology component per row

| Field | What to record |
|---|---|
| **Tech ID** | `TC-nnn`. |
| **Component** | The platform/service. |
| **Category** *(extended)* | compute / data / network / **inference / model-gateway / vector-store / agent-runtime / eval-pipeline / guardrail-enforcement**. |
| **Role in the AI platform** *(new)* | what agentic function it provides. |
| **Enforces guardrails** *(new, if applicable)* | `G-n` enforced here (→ `guardrail-policy-catalog`). |
| **Radar status** | Adopt / Trial / Assess / Hold *(supporting view, not a 10th core artifact)*. |
| **Owner** | Platform owner. |

## Filled rows

<!-- example -->

| Tech ID | Component | Category | Role in the AI platform | Enforces guardrails | Radar | Owner |
|---|---|---|---|---|---|---|
| `TC-001` | *(model gateway)* | model-gateway | routes inference; PII egress filter | `G-3` | Adopt | Platform/security |
| `TC-002` | *(vector store)* | vector-store | hosts knowledge corpora indexes | — | Adopt | EA / Platform |
| `TC-003` | *(eval pipeline)* | eval-pipeline | runs eval suites pre-merge & online | — | Trial | Runtime assurance |

**Watch.** The LLMOps substrate — where evals run, where guardrails are enforced, where decision trails are captured — is now an architecture concern recorded here, not an implementation detail.
