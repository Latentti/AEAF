---
artifact: architecture-vision
title: "Architecture Vision — Parkki Nordic agentic support line"
subtitle: "Phase 1 deliverable"
type: deliverable
phase: 1
domain: [B, I]
status: approved
owner: "Head of Customer Support (Antti Salo)"
version: 1.0
links: [requirements-intent-catalog, principles-catalog, capability-automation-frontier-map]
---

# Architecture Vision — Parkki Nordic agentic support line

**Deliverable (Phase 1).** Secures agreement on where the support line is going and how far autonomy may go. Assembled from the intent records, the principles, and the target frontier; signed by the architecture board.

## Problem & drivers
Support volume tripled as the garage estate grew. The aim is to resolve routine, reversible contacts (stuck at a paid gate, "why was I charged", a camera misread) in minutes, while keeping sensitive, contested, and irreversible work with people. The board's condition: this runs real money and a physical gate, so it must be **governable**, not a demo.

## Stakeholders & concerns
Drivers stuck at exit; the human support team (whose work changes); the Billing and Data functions; the DPO (personal/payment data); the board (risk and lawfulness). The people whose roles change are in scope of the Vision, not an afterthought.

## Human–agent ambition (+I)
A blended workforce in front of the human support team: **agents resolve the routine, reversible contacts** (stuck at a paid gate, a charge query, a camera misread), and **humans own the sensitive and the irreversible**. How that work decomposes into specific agents, and at what autonomy, is the Phase 2 allocation and the Phase 6 agent design — not something the Vision fixes here.

## Consequence / risk envelope (+I)
The board caps the support line at **autonomy L3** (no out-of-the-loop action — every case touches money or a gate). Three classes of work are **fixed human**: safety/emergency, account/GDPR, and large or contested money. These are decisions, not gaps.

## Target value
Routine contacts resolved in minutes; the human team freed for the cases that need judgment; quality, safety, and continuity provable to the board and a regulator. The latency, resolution rate, and cost this yields are a technology outcome, designed and measured downstream — not numbers committed at the Vision.

## Headline intent
The agent work is declared as **intent** — outcome + bounds, assured by evals, not a fully-specified script (→ `requirements-intent-catalog`). The specific intent records and their thresholds are elaborated as the capabilities are allocated and the eval suites designed.

## Guiding principles
Principles `P-1…P-10` (→ `principles-catalog`) — five runtime-enforced (PII boundary, safety-to-human, verified-facts-only, bounded money, paid-session-for-gate), plus the GDPR/AI Act/ePrivacy principles. Each runtime principle compiles to a guardrail.

## Target frontier
The intended direction: **agents take the routine and reversible work; the boundary widens only as assurance accrues; and three classes stay human — safety, account/GDPR, and large or contested money.** The per-capability boundary and its trajectory are mapped in Phase 2 (→ `capability-automation-frontier-map`), not pre-drawn here.

## Sign-off
Architecture board (chair: Head of Customer Support), 2026-02-20. Proceed to Phase 2.
