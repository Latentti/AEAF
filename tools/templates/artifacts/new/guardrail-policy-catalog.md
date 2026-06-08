---
artifact: guardrail-policy-catalog
title: Guardrail/Policy Catalog
type: catalog
phase: 6
domain: [I, T]
status: stub
owner: "TBD — named human/role answerable that the guardrails hold"
as_of: TBD
version: 0.1
links: [agent-catalog, principles-catalog, eval-suite-specification]
---

# Guardrail/Policy Catalog

**What it is.** The register of the machine-enforceable constraints on agent behaviour and the policies they enforce. It is where a principle with `enforcement = runtime` is shown **compiled into** concrete guardrails, with the enforcement point named — it answers "what is the agent actually prevented from doing, and where is that prevention enforced." A guardrail *bounds*; it does not specify. A constraint that lives only in a system prompt and that the model can talk past is **advisory, not a guardrail**.
**Produced in.** Phase 6 · Intelligence & Agency, fed by the principle set from the Preliminary phase (→ Book 1 §8).
**Instantiates.** `Guardrail` and `Policy`, with a back-link to the `Principle` each realizes and forward to the agents each bounds.
**Defined in.** Book 1 §21.4.4 · templated in Book 2 §15.5.

## Template — one guardrail per row, with the policy/principle it enforces

| Field | What to record |
|---|---|
| **Guardrail ID** | e.g. `G-n`. |
| **Guardrail (what it does)** | The constraint in one sentence. |
| **Policy / principle enforced** | The principle (with its Enforcement value) or policy it compiles from (→ `principles-catalog`). |
| **Scope** | Which agents/capabilities it bounds (→ `agent-catalog`). |
| **Trigger condition** | When it fires. |
| **Enforcement point** | input filter / output check / tool permission / spend limit / pre-action / model gateway. |
| **Fail action** | block / escalate / log. |
| **Owner** | Who is answerable for the guardrail holding. |
| **Verifying eval** | The eval case that proves it holds (→ `eval-suite-specification`). |

## Filled rows

<!-- example — replace with your own guardrails -->

| ID | Guardrail | Policy / principle enforced | Scope | Trigger | Enforcement point | Fail action | Owner | Verifying eval |
|---|---|---|---|---|---|---|---|---|
| `G-1` | *(block the unsafe / out-of-policy action)* | *(intent hard bound)* | `AG-001` | *(flag = fail)* | Output check | Block + escalate | Eval lead | `EV-001` safety |
| `G-2` | *(human-route on a vulnerability/edge signal)* | Principle `P-n` (runtime) | `AG-001` | *(detector positive)* | Pre-action | Escalate to human | AI-risk reviewer | `EV-001` alignment |
| `G-3` | No customer data past the gateway | Principle `P-n` (runtime) | all agents on gateway | PII pattern in egress | Model gateway | Block + log | Platform/security | gateway probe |

## Common mistakes (→ Book 2 §15.5)

- **Guardrails with no policy/principle behind them.** A guardrail that enforces nothing stated is unauditable. Every row traces to a principle (with its Enforcement value) or a named policy — the compilation chain.
- **Naming the constraint but not the enforcement point.** The *where* and the *fail action* are the artifact's reason to exist.
- **Confusing a guardrail with a prompt instruction.** A guardrail holds regardless of the agent's reasoning. If the model can talk past it, record it as advisory and find a real enforcement point.
- **No verifying eval.** A guardrail you never test silently rots. Link each to the eval case that proves it still fires.
