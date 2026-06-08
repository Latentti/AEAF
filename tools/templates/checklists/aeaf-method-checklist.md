---
artifact: aeaf-method-checklist
title: AEAF Method Checklist (Preliminary → Phase 10)
type: checklist
phase: all
domain: [B, D, A, T, I]
status: approved
version: 1.0
links: []
---

# AEAF Method Checklist

**What it is.** A deliverable-**completeness** checklist, organized by phase: each phase's list confirms it produced what the next phase needs. The agentic rows — which did not exist in a classical ADM checklist — are marked **[+I]**; they are mandatory wherever an agent actor is in scope and may be dropped only where the scope contains no agents. Run by the phase lead with the architect at the close of each phase. (→ Book 2 §17.3.)

**The three binding rules.** A checked box **points to evidence** (names the artifact/test/record that makes it true). An **owner answers each row**. **Weight matches consequence** — a reversible in-the-loop copilot clears a light subset; a money-moving out-of-the-loop agent clears every row.

## Preliminary
- [ ] Architecture capability stood up; agentic roles assigned (agent owner, runtime assurance owner, AI-risk) **[+I]**
- [ ] Principles established, each with an Enforcement attribute **[+I]**
- [ ] Repository + agentic artifact set provisioned **[+I]**
- [ ] Agentic operating context + risk appetite characterized **[+I]**
- [ ] Autonomy-Level Classification scheme adopted **[+I]**
- [ ] Accountability model defined (named human per capability; never an agent) **[+I]**

## Phase 1 — Vision
- [ ] Drivers, stakeholders, scope, target value documented; vision approved
- [ ] Human–agent ambition stated **[+I]**
- [ ] Consequence/risk envelope for autonomy stated **[+I]**
- [ ] Stakeholder concerns captured, incl. affected people **[+I]**

## Phase 2 — Business & Capability
- [ ] Capability model mapped; capabilities outcome-first, actor-agnostic
- [ ] Capability allocation recorded per in-scope capability **[+I]**
- [ ] Capability Automation-Frontier Map produced **[+I]**
- [ ] Roles carry a performer-type **[+I]**
- [ ] Each agent/hybrid capability has a named accountability owner **[+I]**

## Phase 3 — Data & Knowledge
- [ ] Data models + governance/MDM defined
- [ ] Cognitive substrate designed **[+I]**
- [ ] Knowledge-Corpus Catalog populated **[+I]**
- [ ] Corpus governance assigned (named owner of currency) **[+I]**

## Phase 4 — Application
- [ ] Application portfolio, integration, services documented
- [ ] Non-determinism designed for (bounded outputs, fallback, handoff, idempotency, observability) **[+I]**
- [ ] Each agent-touched flow has a defined behaviour on model fail / low confidence **[+I]**

## Phase 5 — Technology
- [ ] Infrastructure, platforms, security documented
- [ ] AI platform specified (inference, gateway, vector store, agent runtime) **[+I]**
- [ ] LLMOps substrate specified (evals, guardrail enforcement, decision-trail capture) **[+I]**

## Phase 6 — Intelligence & Agency
- [ ] Agent Catalog populated **[+I]**
- [ ] Model Portfolio populated **[+I]**
- [ ] Orchestration designed **[+I]**
- [ ] Guardrail/Policy Catalog populated; runtime principles compiled to guardrails **[+I]**
- [ ] Eval-Suite Specification produced per capability (thresholds fixed before results) **[+I]**
- [ ] Autonomy level assigned per capability, with required controls **[+I]**
- [ ] Oversight mode chosen per capability, with escalation path **[+I]**

## Phase 7 — Opportunities & Solutions
- [ ] Work packages, transition architectures, value increments defined
- [ ] Sequenced by trust earned (pilot tight, widen on assurance) **[+I]**

## Phase 8 — Migration Planning
- [ ] Sequencing, dependencies, risk, business case documented
- [ ] Frontier moves planned (each with trigger + assurance precondition) **[+I]**
- [ ] Human transition planned (reskilling, role change) **[+I]**

## Phase 9 — Implementation Governance
- [ ] Architecture compliance review completed
- [ ] Design-time gate cleared per agent; agentic architecture contract signed **[+I]**
- [ ] Handoff to the runtime loop confirmed **[+I]**

## Phase 10 — Change & Runtime Assurance
- [ ] Runtime loop operating (guardrails enforced; evals + drift monitored) **[+I]**
- [ ] Re-gating triggers wired **[+I]**
- [ ] Runtime evidence captured (decision trails, veto logs, eval/drift, incidents) **[+I]**
- [ ] Trust & Accountability Matrix current **[+I]**
