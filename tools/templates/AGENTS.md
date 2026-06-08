# AGENTS.md — AEAF templates (agents.md standard)

Instructions for any coding/authoring agent working with the AEAF template set. This mirrors `CLAUDE.md`; if the two ever diverge, `CLAUDE.md` is canonical.

## What this is

AEAF (Agentic Enterprise Architecture Framework) is the agentic-age successor to TOGAF. These templates are the fill-in form of its artifacts; the AEAF books are the definition (Book 1 §21, Book 2 §15). Each artifact is one Markdown file: a YAML frontmatter header plus a Markdown body. An agent's role is the upkeep — drafting rows, resolving cross-references, re-verifying on change — so a human keeps only the intent, the accountability, and the gate approval.

## Order of operations

1. Read `conventions.md` (frontmatter schema, ID scheme, status lifecycle, diagram/colour/lexicon rules).
2. Read the specific artifact template in `artifacts/` and keep its column set.
3. Use `llms.txt` to locate the right template.
4. Fill frontmatter first, then the body. Mark unknowns `TBD`, never delete a field. Mark sample rows `<!-- example -->`.

## Hard rules (never break)

- **Accountability is a named human/role, never an agent.** An agent is only ever Responsible (`R`), never Accountable (`A`). One accountability owner per capability.
- **Never drop a cross-reference link, an autonomy level, or the accountability owner.** Everything else is tailorable.
- **A guardrail bounds at a named enforcement point; it does not merely advise.** A constraint the model can talk past is advisory, not a guardrail.
- **Eval thresholds are fixed before results are seen.**
- **A gate checklist box names its evidence**, not an intention.
- **Resolve every ID.** A dangling reference is the next thing to fix.

## Style (binding)

Locked AEAF lexicon (`agent actor`, `guardrail`, `eval`, `intent`, oversight modes `in-/on-/out-of-the-loop`); the anti-AI-slop ban list; Mermaid-only diagrams with the indigo (machine) / amber (human) colour convention; Vega-Lite for quantitative charts; tables for sets of ≥3. TOGAF is independent of AEAF — no claim of lineage or endorsement. Full rules: the AEAF Style Guide (in the published AEAF books).
