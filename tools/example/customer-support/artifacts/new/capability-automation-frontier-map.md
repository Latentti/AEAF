---
artifact: capability-automation-frontier-map
title: "Capability Automation-Frontier Map — Parkki Nordic support line"
type: map
phase: 2
domain: [B, I]
status: runtime
owner: "Support Operations Lead (Henna Laaksonen)"
as_of: 2026-06-03
version: 1.0
links: [business-capability-catalog, human-agent-raci, autonomy-level-classification, trust-accountability-matrix]
---

# Capability Automation-Frontier Map — Parkki Nordic support line

The boundary between human-performed and agent-performed work across the support capability, and where it is moving — a view over the allocations, as of **2026-06-03**.

| Capability leaf | As-of performer | Current autonomy | Projected next | Assurance precondition for the move | Trend |
|---|---|---|---|---|---|
| Triage & route (`CAP-001`) | Agent | `L3` | hold at L3 | — | → stable |
| Resolve gate/exit (`CAP-002`) | Agent (operator confirms) | `L2` | L3 | one quarter of live evidence; `G-1` holds; Tampere in golden set | → toward agent |
| Explain a charge (`CAP-003`) | Agent | `L3` | hold at L3 | — | → stable |
| Correct ANPR misread (`CAP-004`) | Agent | `L1` | L3 | correction accuracy holds a quarter | → toward agent |
| Refund ≤ €50 in policy (`CAP-007`) | Agent (human approves) | `L1` | hold at L1 | board keeps money in-the-loop | ⏸ held |
| Refund > €50 / contested (`CAP-007`) | **Human** | n/a | **stays human** | none — principle `P-4` | ⏹ fixed human |
| Account / GDPR (`CAP-005`) | **Human** | n/a | **stays human** | none — board appetite | ⏹ fixed human |
| Safety / emergency (`CAP-006`) | **Human** | n/a | **stays human** | none — principle `P-2` | ⏹ fixed human |

```mermaid
flowchart LR
    classDef human fill:#F59E0B,stroke:#B45309,color:#1a1a1a;
    classDef agent fill:#4F46E5,stroke:#3730A3,color:#ffffff;
    classDef hybrid fill:#4F46E5,stroke:#B45309,stroke-width:3px,color:#ffffff;

    subgraph CAP["Resolve a customer support contact — as of 2026-06"]
        tri["Triage & route<br/>L3"]:::agent
        gate["Resolve gate/exit<br/>L2 (operator confirms)"]:::hybrid
        bill["Explain a charge<br/>L3"]:::agent
        anpr["Correct ANPR misread<br/>L1"]:::agent
        rsmall["Refund ≤ €50<br/>L1 (human approves)"]:::hybrid
        rbig["Refund > €50 / contested<br/>human-only (P-4)"]:::human
        acct["Account / GDPR<br/>human-only"]:::human
        safe["Safety / emergency<br/>human-only (P-2)"]:::human
    end
    gate -. "move on a quarter of live evidence + Tampere golden set" .-> gate
    anpr -. "move on accuracy holding a quarter" .-> anpr
    %% INDIGO = agent-performed; AMBER = human-performed; split = hybrid; the line between is the frontier
```

*Figure — the support-line frontier. Indigo leaves are agent-performed, amber leaves are human-performed, split nodes are hybrid (agent acts, human confirms). The three amber leaves are fixed human by board appetite and principle — first-class decisions, not gaps. The dotted self-loops are intended, gated moves: Gate-Ops L2→L3 and ANPR L1→L3, each firing only when its assurance precondition holds. This map is derived from the allocations and the Trust & Accountability Matrix — it is not authored by hand.*
