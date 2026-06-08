---
name: aeaf-retrofit
description: Lift an already-implemented agentic service up to AEAF level (brownfield). Use when a working agent system, PoC, or production service exists and the user wants to bring it under AEAF governance — e.g. "take our support bot to AEAF level", "retrofit this PoC", "what's missing for production governance", "AEAF-ify our existing agents". Scans the implemented service, reverse-maps it into the AEAF artifacts as a baseline, gap-analyses it against the gates, and produces the target-state artifact set plus a sequenced migration backlog. This is the workflow that turns a collapsing PoC into a service that can be run as a business.
---

# AEAF Retrofit (brownfield)

The most common real situation: a team built an agentic service fast — it works in the demo — and now needs the governance that makes it a business, not a PoC. This workflow lifts what exists up to AEAF level without rebuilding it. It is the engine behind the worked example and the just-do-it-vs-AEAF comparison.

## When to use
- An implemented agentic service exists (code, configs, prompts, tools, a model, maybe a knowledge base) and needs to be brought under AEAF.
- The user asks what is missing for production, or wants the existing system mapped to the AEAF artifacts.

## Inputs you need
- Access to the service: its code/configs, the agent's instructions, the tools it calls, the model(s), any knowledge base, and whatever docs exist.
- The consequence profile of what the agent does (reversible? moves money? touches PII? safety-relevant?).

## The four stages

### Stage 1 — Scan (inventory the as-is)
Read the service and inventory what is actually there, as built:
- agents (one per distinct bounded purpose), the model(s) each runs, the tools/actions each can call (with read/write/irreversible-write), any knowledge base it retrieves from;
- whatever bounds exist today (prompt instructions, validation checks, rate limits) — note whether each is a real enforcement point or only a prompt instruction;
- what is **absent** (auth, monitoring, agent evals, escalation robustness, data-retention, accountability owner, cost caps).

### Stage 2 — Reverse-map (baseline artifacts, status `baseline`)
Map the inventory into the AEAF artifacts as the **as-is** state — drive `aeaf-author`:
- Agent Catalog (one row per agent actor, not per service), Model Portfolio, Knowledge-Corpus Catalog, Application Portfolio (the runtime, linked to the agents);
- record today's de-facto autonomy level and oversight mode honestly — a PoC that acts without review is L3/out-of-the-loop *with no controls*, which is the finding, not a label to soften;
- where a bound is only a prompt instruction, record it as **advisory**, not a guardrail.

### Stage 3 — Gap-analyse against the gates
Run `aeaf-govern` in **audit** mode over the baseline: score the AEAF Method checklist, the agentic architecture review, and the design-time gate against the as-is. Produce a **gap register** — every `[+I]` item the service does not yet satisfy — and map each gap to the AEAF artifact/gate that closes it and the risk it leaves open (where it breaks under production load).

### Stage 4 — Target-state + migration backlog
- Produce the **target-state** artifact set (status `target`): the guardrails that compile the principles (`aeaf-guardrails`), the Eval-Suite Specification (`aeaf-evals`), the autonomy assignment matched to consequence, the Human-Agent RACI and Trust & Accountability Matrix with a named owner, the architecture contract.
- Sequence the **migration backlog** by trust earned and consequence (Phase 7–8 discipline): pilot under tight oversight first, widen autonomy only as assurance accrues. Each frontier move carries its trigger and assurance precondition.

## Outputs
- A filled **baseline** artifact set (what the service is today).
- A **gap register** (what is missing, mapped to artifact/gate, with the production risk).
- A **target-state** artifact set + a sequenced migration backlog.

## Quality bar
- **Map honestly.** The retrofit's value is the gap register; softening the baseline ("we sort of have guardrails") hides the risk it exists to surface.
- **A prompt instruction is advisory, not a guardrail.** Record it as found, then specify the real enforcement point in the target state.
- **Name the accountability owner** even if the service has none today — the absence is itself a finding.
- All the per-artifact rules from `aeaf-author` apply.

## Hand off to
- `aeaf-allocate`, `aeaf-guardrails`, `aeaf-evals`, `aeaf-govern` for each stage; `aeaf-maturity` first if the entry point is unclear.
