---
artifact: application-portfolio-catalog
title: "Application Portfolio Catalog — Parkki Nordic support line"
type: catalog
phase: 4
domain: [A]
status: approved
owner: "EA / Platform owner (Joonas Mäkinen)"
version: 1.0
links: [agent-catalog, technology-portfolio-catalog]
---

# Application Portfolio Catalog — Parkki Nordic support line

The applications, with the agents each hosts. The application is the runtime; the agents are modelled separately in the Agent Catalog.

| App ID | Name | Purpose | Hosts agents | Integration points | TIME | Owner |
|---|---|---|---|---|---|---|
| `APP-001` | Support Agent Runtime | Hosts and orchestrates the support agents; calls the tool webhooks | `AG-001`, `AG-002`, `AG-003`, `AG-004`, `AG-005` | tool webhooks; model gateway; voice front-end | Invest | EA / Platform owner |
| `APP-002` | Voice front-end | Telephony + speech I/O for the caller | — | SIP/WebRTC; STT/TTS; `APP-001` | Invest | EA / Platform owner |
| `APP-003` | Parkki core platform | System of record for sessions, payments, accounts, gates | — | tool APIs consumed by `APP-001` | Tolerate | Platform owner |

*A model swap is a Model Portfolio change, a new tool is an Agent Catalog change, and re-platforming `APP-001` is an application change — three different changes, three owners, never collapsed into "we changed the AI."*
