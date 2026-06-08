---
name: aeaf-allocate
description: Run an AEAF capability-allocation and automation-frontier workshop (Phase 2). Use when the user needs to decide which capabilities are performed by humans, agents, or hybrid teams, at what autonomy level and oversight mode, and who is accountable — e.g. "allocate these support capabilities", "map our automation frontier", "build the Human-Agent RACI". Produces the Business Capability Catalog (performer mix), Human-Agent RACI / Decision-Authority Matrix, Autonomy-Level assignment, and Capability Automation-Frontier Map.
---

# AEAF Allocate

Facilitate the central AEAF design act: capability allocation. Decide *which kind* of actor performs each capability, how autonomously, under what oversight, and who is accountable.

## When to use
- Phase 2 of a method pass, greenfield or retrofit.
- Whenever the frontier moves — a capability is being re-allocated from human to agent (or back).

## Inputs you need
- The capability model (outcome-named, actor-agnostic capabilities). If none exists, build it first — capabilities name *what*, never *who*.
- The autonomy scale (canonical L0–L4) and the accountability model from the Preliminary phase.
- The consequence/risk envelope from Vision (how far autonomy may go).

## Procedure
1. **Decompose to the decision level.** A capability is not uniform — "offer a standard arrangement" and "approve a write-off" have opposite allocations. Decompose until each row has one allocation.
2. **Allocate each leaf** — human / agent / hybrid team. State the *reason* it goes to an agent (tied to the value stream), not "because we can".
3. **Set the autonomy level** per leaf against the canonical scale, matched to **consequence and reversibility** — suggest-only/in-the-loop for high-consequence/irreversible; higher autonomy only where bounded and recoverable.
4. **Choose the oversight mode** (in/on/out-of-the-loop) and the **escalation path** (trigger → target → fallback).
5. **Name exactly one accountability owner** per capability — a named human/role, never an agent.
6. **Mark the leaves that stay human on purpose** as first-class decisions, not gaps.

## Templates it drives
- `tools/templates/artifacts/classical/business-capability-catalog.md` (performer mix + autonomy)
- `tools/templates/artifacts/new/human-agent-raci.md` (R/A split + decision-authority band)
- `tools/templates/artifacts/new/autonomy-level-classification.md` (Part B assignment)
- `tools/templates/artifacts/new/capability-automation-frontier-map.md` (the derived view)
- worksheet: `tools/templates/phases/02-business-capability.md`

## Quality bar
- **A is always a human.** If a RACI cell tempts you to mark the agent A, you have not named the human who answers.
- **Record the decision-authority band**, not just "agent is R" (agent-alone / agent-proposes-human-approves / human-alone).
- **The frontier map is derived**, not authored — it is a view over the allocations; stamp its `as_of`.

## Hand off to
- `aeaf-author` to write the underlying catalogs; Phase 6 (`aeaf-guardrails`, `aeaf-evals`) to design the agents the allocation calls for.
