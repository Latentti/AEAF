---
artifact: actor-role-matrix
title: Actor/Role Matrix
type: matrix
phase: 2
domain: [B]
status: stub
owner: "TBD"
version: 0.1
links: [organization-actor-catalog, role-catalog, autonomy-level-classification]
---

# Actor/Role Matrix

**Classical artifact; changed for the Agentic Enterprise.** Cells may now record an **agent** holding a role, with a link to the **autonomy level** at which it holds it. (→ Book 1 Table 21.1.)

## Template — actor rows × role columns

Each cell records whether the actor holds the role, and — for an agent actor — the autonomy level.

| Actor \ Role | `ROLE-001` | `ROLE-002` | … |
|---|---|---|---|
<!-- example -->
| `ACT-001` *(human)* | ✓ | ✓ | |
| `ACT-002` *(agent `AG-001`)* | ✓ (`L3`) | — | |
| `ACT-003` *(hybrid team)* | ✓ (`L1`) | ✓ (human) | |

**Watch.** An agent holding a role at an autonomy level must reconcile with the Autonomy-Level Classification (the assignment) and the Human-Agent RACI (the accountability split). If the matrix says `L3` and the classification says `L1`, one is wrong.
