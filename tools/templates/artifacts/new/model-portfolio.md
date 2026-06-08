---
artifact: model-portfolio
title: Model Portfolio
type: catalog
phase: 5
domain: [T, I]
status: stub
owner: "TBD — named human/role answerable for this portfolio's currency"
as_of: TBD
version: 0.1
links: [agent-catalog, eval-suite-specification, technology-portfolio-catalog]
---

# Model Portfolio

**What it is.** The register of the underlying models in use — their cost, risk, and a TIME-style lifecycle stance — because one model powers many agents and is governed as a portfolio asset in its own right. It answers "which models do we depend on, what do they cost, which are we moving off, and what runs on each." Distinct from the agent: cost, risk, and lifecycle attach to the **model** here; purpose, tools, and guardrails attach to the **agent** in the Agent Catalog.
**Produced in.** Phase 5 · Technology (platform and gateways) and Phase 6 · Intelligence & Agency (the rationalization stance).
**Instantiates.** `Model`, with a back-link to the agents it powers and a link to its eval results.
**Defined in.** Book 1 §21.4.2 · templated in Book 2 §15.3.

## Template — one model per row

| Field | What to record |
|---|---|
| **Model ID** | e.g. `M-nnn`. |
| **Provider · version** | Vendor/host and the exact version/snapshot (pin it). |
| **Modality** | text / vision / audio / multimodal. |
| **Context window** | Effective working context. |
| **Cost profile** | per-call / per-token / hosting basis and unit cost. |
| **Risk profile** | data residency, provenance, dependency/lock-in, known failure modes. |
| **Agents powered** | Agent IDs that run it (→ `agent-catalog`). |
| **Eval summary** | Latest eval pass-rate / standing (→ `eval-suite-specification`). |
| **Lifecycle stance** | **T**olerate / **I**nvest / **M**igrate / **E**liminate, with rationale. |
| **Review date** | Next portfolio review for this model. |

## Filled rows

<!-- example — replace with your own models -->

| Model ID | Provider · version | Modality | Context | Cost profile | Risk profile | Agents powered | Eval summary | Stance | Review |
|---|---|---|---|---|---|---|---|---|---|
| `M-001` | *(host · pinned version)* | Text | 128k | *(per-token unit cost)* | *(residency · dependency · failure modes)* | `AG-001`, `AG-002` | Clears `EV-001` | **Invest** — *(rationale)* | 2026-Q4 |
| `M-002` | *(host · pinned version)* | Text | 200k | *(per-call unit cost)* | *(higher cost; held as fallback)* | none in production | Pilot evals only | **Tolerate** — *(rationale)* | 2026-Q4 |

## Common mistakes (→ Book 2 §15.3)

- **Treating "the LLM" as one line.** A pinned version is a portfolio asset; "our LLM" is not. A silent version bump invalidates the eval evidence behind every agent that runs it.
- **No back-link to agents.** Without "agents powered," you cannot answer "if we retire this model, what breaks?"
- **A stance with no rationale or review date.** The TIME stance must carry *why* and *when re-checked*.
- **Confusing the model with the agent.** Do not duplicate the agent's purpose/tools/guardrails here.
