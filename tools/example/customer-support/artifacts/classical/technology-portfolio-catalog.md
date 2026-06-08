---
artifact: technology-portfolio-catalog
title: "Technology Portfolio Catalog — Parkki Nordic support line"
type: catalog
phase: 5
domain: [T]
status: approved
owner: "EA / Platform owner (Joonas Mäkinen)"
version: 1.0
links: [model-portfolio, guardrail-policy-catalog, application-portfolio-catalog]
---

# Technology Portfolio Catalog — Parkki Nordic support line

The AI platform components, including the enforcement points where runtime guardrails live.

| Tech ID | Component | Category | Role in the AI platform | Enforces guardrails | Radar | Owner |
|---|---|---|---|---|---|---|
| `TC-001` | Model gateway (EU) | model-gateway | Routes inference for all agents; PII/PAN egress filter | `G-3` | Adopt | EA / Platform owner |
| `TC-002` | Vector store (EU) | vector-store | Hosts the `KC-*` corpus indexes | — | Adopt | EA / Platform owner |
| `TC-003` | Eval pipeline | eval-pipeline | Runs `EV-*` pre-merge, pre-prod, and online | — | Adopt | Runtime assurance owner |
| `TC-004` | Finnish STT | inference | Speech-to-text for the caller | — | Adopt | EA / Platform owner |
| `TC-005` | TTS voice | inference | Text-to-speech reply | — | Adopt | EA / Platform owner |
| `TC-006` | Telephony (SIP/WebRTC) | network | Carries the voice call | — | Adopt | Platform owner |
| `TC-007` | Agent orchestration runtime | agent-runtime | Runs the agent loop; pre-action guardrail hooks | `G-1`, `G-4`, `G-5`, `G-6`, `G-7`, `G-8` | Adopt | EA / Platform owner |
| `TC-008` | Decision-trail / audit store (WORM) | data | Append-only log of reasoning, tool calls, guardrail vetoes | — | Adopt | Runtime assurance owner |

*The orchestration runtime (`TC-007`) and the model gateway (`TC-001`) are the two enforcement points where the runtime guardrails actually fire — the Guardrail/Policy Catalog's "enforcement point" column resolves to these components. The WORM audit store (`TC-008`) is where the runtime evidence the assurance case relies on is captured.*
