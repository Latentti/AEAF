---
artifact: principles-catalog
title: "Principles Catalog — Parkki Nordic support line"
type: catalog
phase: P
domain: [B, I]
status: approved
owner: "Architecture board (chair: Head of Customer Support, Antti Salo)"
version: 1.0
links: [guardrail-policy-catalog, regulatory-obligations-register]
---

# Principles Catalog — Parkki Nordic support line

The principles the support line operates under, each with its **Enforcement** attribute. The runtime-enforced principles compile into guardrails (→ `guardrail-policy-catalog`); the compilation is what makes the principle reach the agent at runtime, not just a line in a document.

| ID | Name | Statement | Enforcement | Compiled guardrails |
|---|---|---|---|---|
| `P-1` | PII boundary | Customer personal and payment data never leaves the EU region and is never sent to a third party. | **runtime** | `G-3` |
| `P-2` | Safety to a human | Any safety or distress signal (trapped, accident, medical) routes to a human and the 24/7 line; the agent does not attempt to resolve it. | **runtime** | `G-4` |
| `P-3` | Verified facts only | The agent acts only on system-verified facts; it never acts on authority or identity a caller merely claims. | **runtime** | `G-5` |
| `P-4` | Bounded money movement | A refund above €50, or any contested refund, requires a named human's approval. | **runtime** | `G-2` |
| `P-5` | A physical action needs a paid session | The exit gate is opened only when a paid (or genuinely exempt) session is verified in the system. | **runtime** | `G-1` |
| `P-6` | AI disclosure | The caller is told at the start that they are speaking with Parkki Nordic's AI assistant. | design-time | — |
| `P-7` | One accountable human | Every capability has exactly one named human accountability owner; accountability never transfers to an agent. | design-time | — |
| `P-8` | Human review of significant decisions | A significant decision (a refund, an account or ANPR change) is never made by the agent alone; a human can always intervene. | **runtime** | `G-2` |
| `P-9` | Data minimisation & retention | Only the personal data needed for the contact is processed; it is retained no longer than policy allows and never embedded in a corpus. | design-time | — *(G-3 supports)* |
| `P-10` | Recording consent | A call is processed/recorded only after the caller's consent is captured. | **runtime** | `G-9` |

**Regulatory provenance.** `P-1`, `P-8`, `P-9` realise GDPR obligations (PII boundary, Art 22 human intervention, Art 5 minimisation/retention); `P-6` realises EU AI Act Art 50 (transparency); `P-10` realises ePrivacy (recording consent). The full mapping — obligation → principle → guardrail → evidence — is the Regulatory Obligations Register (→ `regulatory-obligations-register`).

**Why these and not more.** The runtime principles are the ones a probabilistic actor running money, personal data, and a physical gate can violate at machine speed; each had to become a guardrail. `P-6`, `P-7`, `P-9` are checked at the gate or in design, not enforced on every action. Advisory principles that nothing enforces would be the classic catalog that reassures and changes nothing.
