# CLAUDE.md — Agent instructions for the AEAF templates

You are filling in or maintaining an AEAF artifact. AEAF (the Agentic Enterprise Architecture Framework) is the agentic-age successor to TOGAF. These templates are the form; the AEAF books are the definition. Your job is the upkeep that defeated classical EA: draft catalog rows, resolve cross-references, and re-verify artifacts when something changes — so the human keeps only the intent, the accountability, and the approval.

## Before you write

1. **Read `conventions.md`.** It fixes the frontmatter schema, the ID prefixes, the status lifecycle, and the binding diagram/colour/lexicon rules. Do not invent your own.
2. **Read the artifact's own template** in `artifacts/` — its column set is faithful to Book 1 §21 / Book 2 §15. Keep the columns; the books win over your judgement on what a column should be.
3. **Find the right template fast** via `llms.txt` (the machine index).

## How to fill an artifact

- **Frontmatter first.** Set `artifact`, `phase`, `domain`, `status`, `owner`, `version`, and `links`. Stamp `as_of` (a date) on any living view (status `runtime`). If you cannot answer a field, write `TBD` — never delete the field.
- **Use stable IDs** from the §2 scheme (`AG-`, `M-`, `KC-`, `G-`, `EV-`, `P-`, …). Never reuse an ID after retirement.
- **Resolve every link.** When you write `M-002` in an Agent Catalog row, confirm `M-002` exists in the Model Portfolio. A reference that does not resolve is a dangling reference — flag it; it is the next thing to fix.
- **One claim per cell.** If a cell stacks three ideas, it belongs as its own rows or a sub-table.
- **Mark example rows** clearly with `<!-- example -->` so a reader never mistakes a sample for real data.

## The rules you must never break

1. **Accountability is always a named human or role — never an agent.** If a cell tempts you to mark an agent `A` (Accountable) in a RACI, stop: you have not yet named the human who answers for it. An agent is only ever `R` (Responsible). One accountability owner per capability.
2. **Never drop a cross-reference link, an autonomy level, or the accountability owner.** Everything else is tailorable; these three are not (→ Book 2 §15.1).
3. **A guardrail bounds; it does not advise.** If a constraint lives only in a system prompt and the model can talk past it, it is not a guardrail — record it as advisory and find a real enforcement point.
4. **Thresholds are set before results are seen.** A threshold chosen after looking at the score is rationalisation, not assurance.
5. **A gate checklist box points to evidence**, naming the artifact/test/record that makes it true — not an intention to produce one.

## Style (binding, from the AEAF Style Guide)

- **Locked lexicon.** Use AEAF terms exactly: `agent actor`, `guardrail`, `eval`, `intent`, `capability allocation`, `blended workforce`, oversight modes `in-/on-/out-of-the-loop`. Never "bot", "digital worker", "the AI", "the LLM" in formal text.
- **Anti-AI-slop ban list applies.** No "leverage", "robust", "seamless", "game-changer", "unlock", "navigate the complexities", hollow tricolons, or throat-clearing openers. Name the actor, state the bound, delete the adjective.
- **Diagrams are Mermaid only**, with the binding indigo (machine/agent) / amber (human judgment) colour convention from `conventions.md`. Quantitative charts are Vega-Lite. Sets of ≥3 items go in a table.
- **TOGAF** is a registered trademark of The Open Group; AEAF is independent and original, not a derivative or profile, not endorsed by The Open Group. Phase-to-ADM parallels are a migration aid only.

## When you finish an artifact

- Confirm every `links` target resolves.
- Confirm no `A` sits on an agent.
- Confirm the frontmatter `status` and `as_of` are right.
- For a living view, note that it is refreshed by the runtime loop, not filed once.
