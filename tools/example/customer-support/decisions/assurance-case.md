---
artifact: assurance-case
title: "AC-001 — Assurance Case for Gate-Ops Agent"
type: decision
phase: 6
domain: [I]
status: approved
owner: "Runtime assurance owner / Eval lead (Sofia Berg)"
accountable: "Support Operations Lead (Henna Laaksonen)"
as_of: 2026-06-03
version: 1.0
links: [eval-suite-specification, guardrail-policy-catalog, trust-accountability-matrix, requirements-intent-catalog]
---

# AC-001 — Assurance Case for Gate-Ops Agent (`AG-002`)

| Field | Entry |
|---|---|
| **Case ID** | `AC-001` |
| **Agent** | `AG-002` |
| **Autonomy level claimed** | `L2` (execute-with-approval) |
| **As of** | 2026-06-03 |
| **Review date** | 2026-09-01 |
| **Accountability owner** | Support Operations Lead (Henna Laaksonen) |

## The claim
`AG-002` operates at **L2** because a deterministic, fail-closed guardrail prevents the one unacceptable outcome (opening for an unpaid session), an operator confirms every open, and `EV-002` shows the agent's judgement is within bounds — while the evidence does not yet support L3.

## Argument and evidence
| Claim | Evidence | Source |
|---|---|---|
| The gate never opens for an unpaid/unverified session | `EV-002` safety: unpaid-open **0%** over 6 weeks; `G-1` fail-closed pre-action | `eval-suite-specification`, `guardrail-policy-catalog` `G-1` |
| Claimed authority is ignored | `EV-002` adversarial: claimed-authority bypass **0%** (`G-5`) | `EV-002` |
| Rapid-retry fraud is blocked | rate-limit holds 100% (`G-6`) | `EV-002` |
| Genuine paid drivers get out fast | correct-open 98.4%; median 71 s | `EV-002` quality/performance |
| Every open is human-confirmed and logged | operator-confirm 100%; veto + decision trail in `TC-008` | `trust-accountability-matrix`, `TC-008` |

## Residual risk
The golden set under-represents the **Tampere** garages (opening 2026-Q3) and night-time low-light ANPR reads. L3 is therefore **not** justified yet — the evidence covers Helsinki daytime traffic, not the full estate. Recorded here so a Tampere incident would be a known gap surfacing, not a surprise.

## Accepted by
Support Operations Lead, 2026-04-02, for L2 only, until the 2026-09-01 review. L3 requires Tampere in the golden set and a quarter of clean live evidence (→ `ADR-001`).
