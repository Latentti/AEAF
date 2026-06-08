---
name: aeaf-guardrails
description: Compile principles into runtime guardrails and build the Guardrail/Policy Catalog (Phase 6). Use when the user needs to turn architecture principles or policies into machine-enforceable constraints on agent behaviour — e.g. "what guardrails does this agent need", "compile our PII principle into a guardrail", "build the guardrail catalog". Produces the Guardrail/Policy Catalog with each guardrail traced to a principle, a named enforcement point, a fail action, and a verifying eval.
---

# AEAF Guardrails

Turn what the enterprise believes into what the agent is actually prevented from doing. Compile each runtime-enforced principle into concrete guardrails, with the enforcement point named.

## When to use
- Phase 6, designing the constraints that bound an agent.
- After a principle with `enforcement = runtime` is added or changed.

## Inputs you need
- The Principles Catalog, with each principle's Enforcement attribute (advisory / design-time / runtime).
- The agent's intent and hard bounds (from the Requirements & Intent Catalog).
- The technology platform — the enforcement points available (model gateway, tool-permission layer, output check).

## Procedure (the compilation chain: principle → policy → guardrail → enforcement point)
1. **Take each runtime-enforced principle and each hard bound the intent declares** (spend limits, prohibited actions, data boundaries).
2. **Express it as a machine-enforceable policy** — a rule stated so it can be enforced automatically, not only read.
3. **Define the guardrail** that enforces it: the constraint in one sentence, its trigger condition, its **enforcement point** (input filter / output check / tool permission / spend limit / pre-action / model gateway), and its **fail action** (block / escalate / log).
4. **Set fail-closed where consequence demands** — default-on-failure is block where harm is irreversible; fail-open only for low-consequence reversible actions, documented as a choice.
5. **Pair each guardrail with a verifying eval** — the eval case that proves it still fires (hand to `aeaf-evals`).
6. **Name an owner** answerable for the guardrail holding.

## Templates it drives
- `tools/templates/artifacts/new/guardrail-policy-catalog.md`
- reads `tools/templates/artifacts/classical/principles-catalog.md`

## Quality bar
- **A guardrail bounds; it does not specify.** It constrains what the agent may do, not what it should do.
- **If it lives only in a system prompt and the model can talk past it, it is advisory, not a guardrail.** Find a real enforcement point or record it as advisory.
- **Every guardrail traces to a principle or a named policy** — a guardrail enforcing nothing stated is unauditable.
- **Tool permissions are least-privilege** — only the tools the capability needs, narrowest scope.
- **No guardrail without a verifying eval** — one you never test silently rots.

## Hand off to
- `aeaf-evals` for the verifying eval cases; `aeaf-govern` — guardrails deployed at named enforcement points are gate row 1.
