---
name: aeaf-author
description: Fill in or update any AEAF artifact (the nine new artifacts and the changed classical artifacts) from its template. Use when the user wants to author, populate, or maintain an AEAF catalog, matrix, map, or worksheet — e.g. "create the Agent Catalog", "fill the Guardrail/Policy Catalog", "update the Trust & Accountability Matrix". Drives the templates in tools/templates/, keeps frontmatter and IDs correct, resolves cross-references, and enforces the three rules (accountability is a named human; links are never dropped; a guardrail bounds at an enforcement point).
---

# AEAF Author

Fill and maintain AEAF artifacts. This is the upkeep that defeated classical EA — drafting catalog rows, resolving cross-references, re-verifying on change — done by an agent so the human keeps only the intent, the accountability, and the approval.

## When to use
- The user wants a specific artifact created, populated, or updated.
- A change elsewhere (a new agent, a model swap, a corpus refresh) means an artifact must be re-derived.

## Before you write
1. Read `tools/templates/conventions.md` — frontmatter schema, ID scheme, status lifecycle, diagram/colour rules. Do not invent your own.
2. Open the artifact's template in `tools/templates/artifacts/new/` or `tools/templates/artifacts/classical/`. Keep its column set — the books (Book 1 §21, Book 2 §15) win over your judgement on what a column should be.
3. Use `tools/templates/llms.txt` to find the right template fast.

## Procedure
1. **Identify the artifact** from the need or the phase (the phase worksheets in `tools/templates/phases/` say which artifacts each phase produces).
2. **Fill frontmatter first** — `artifact`, `phase`, `domain`, `status`, `owner`, `version`, `links`; stamp `as_of` on any living view (status `runtime`). Unknown → `TBD`, never delete the field.
3. **Fill rows with stable IDs** from the §2 scheme (`AG-`, `M-`, `KC-`, `G-`, `EV-`, `P-`, …). One claim per cell.
4. **Resolve every link.** When you write `M-002`, confirm it exists in the Model Portfolio. Mark sample rows `<!-- example -->`.
5. **Run the dangling-reference check** — every ID referenced resolves somewhere. A dangle is the next thing to fix.

## Quality bar (enforce on every artifact)
- **Accountability is a named human/role — never an agent.** An agent is only ever Responsible (`R`), never Accountable (`A`).
- **Never drop a cross-reference link, an autonomy level, or the accountability owner.** Everything else is tailorable.
- **A guardrail bounds at a named enforcement point** with a fail action — not a prompt instruction the model can talk past.
- **Eval thresholds are fixed before results are seen.**
- **Style:** locked AEAF lexicon; the anti-AI-slop ban list; Mermaid-only with indigo (machine) / amber (human) colours; tables for sets of ≥3.

## Hand off to
- `aeaf-allocate` for the Phase 2 allocation set, `aeaf-guardrails` for the Guardrail/Policy Catalog, `aeaf-evals` for the Eval-Suite Specification, `aeaf-govern` for the gate artifacts. This skill is the general filler; those are the specialised acts.
