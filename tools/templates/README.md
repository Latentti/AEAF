# AEAF Templates

The fill-in form of the Agentic Enterprise Architecture Framework. Classical enterprise architecture kept its catalogs in spreadsheets and paid for it in upkeep — the standing critique of TOGAF is an execution-cost critique, not a content critique. These templates put the same sound content in a format the **blended workforce** can both maintain: Markdown + YAML frontmatter, diff-able in git, writable by an agent, readable by a human, renderable to branded PDF.

This is the form you fill in. The *definition* of each artifact is the AEAF books: Book 1 §21 (the artifact catalog) and Book 2 §15 (the worked examples).

## Where to start

1. Read **`00-processing-model.md`** — the decision (Markdown + frontmatter) and why it answers the TOGAF-is-too-heavy critique.
2. Read **`conventions.md`** — the frontmatter schema, the ID scheme, the status lifecycle, and the binding diagram/colour/lexicon rules. Everything else assumes it.
3. Pick your **phase worksheet** in `phases/` (Preliminary → Phase 10). Each worksheet lists its inputs, its steps, the artifacts it produces, and its exit-gate checklist.
4. Fill the **artifact templates** the phase produces, from `artifacts/`.

## Folder map

| Path | What's in it |
|---|---|
| `00-processing-model.md` | The format decision and its rationale. |
| `conventions.md` | Frontmatter schema · ID prefixes · status lifecycle · diagram/colour/lexicon rules · the tailoring rule. |
| `README.md` · `CLAUDE.md` · `AGENTS.md` · `llms.txt` | Guidance: human orientation (this file), agent instructions, and the machine index. |
| `artifacts/new/` | The **9 new AEAF artifacts** — the agentic core (Agent Catalog, Model Portfolio, Knowledge-Corpus Catalog, Guardrail/Policy Catalog, Human-Agent RACI, Autonomy-Level Classification, Eval-Suite Specification, Trust & Accountability Matrix, Capability Automation-Frontier Map). |
| `artifacts/classical/` | The **10 classical EA artifacts that change** in the Agentic Enterprise (additive changes per Book 1 Table 21.1). |
| `artifacts/supporting/` | **Supporting governance views** — not core artifacts (the Technology Radar precedent, Book 1 §21.6). The **Regulatory Obligations Register** (GDPR / EU AI Act / ePrivacy / sector obligation mapping) and the **Determinism-Fit Map** (placing each capability on the determinism spectrum — whether to use an LLM at all). |
| `deliverables/` | **Deliverables** — packaged, signed work products that *assemble* artifacts (Statement of Architecture Work, Architecture Vision, Architecture Definition Document BDAT+I, Requirements & Intent Specification, Roadmap & Migration Plan). AEAF folds most deliverables into artifacts; these are the few document-shaped ones, kept thin and linking out. The Agentic Architecture Contract and Assurance Case (in `decisions/`) are also deliverables. |
| `phases/` | **Preliminary + Phases 1–10** worksheets — purpose, inputs, steps, outputs, exit gate. |
| `decisions/` | Agentic ADR · Architecture Contract · Assurance Case. |
| `checklists/` | The four AEAF gate instruments (method completeness, pre-gate review, design-time gate, re-gating trigger) per Book 2 §17. |

## The artifact set is a web, not a pile

The nine new artifacts interlock through shared IDs, with the **Agent Catalog as the hub** — an agent's row links to its model, knowledge corpora, guardrails, autonomy level, eval suite, and accountability owner. The test that your set is coherent: pick one agent ID and trace it across all nine artifacts. If every ID resolves, the meta-model's traceability chains hold. If an ID dangles, that dangle is the next thing to fix (→ Book 2 §15.11).

## The three rules you never break

1. **Accountability is always a named human.** An agent may be *Responsible* for execution; it is never *Accountable*. Never put an `A` on an agent.
2. **Never drop the cross-reference links.** The links are what make nine lists into one architecture.
3. **A checked gate box points to evidence**, not to an intention. "Guardrails defined" is theatre; "Guardrail/Policy Catalog v2.1, three runtime guardrails live, veto log writing" is a check.

## Rendering to PDF

Artifacts and worked examples render through the same Futify-branded pipeline as the AEAF books (`futify-doc-generator`, or the repo's own `build/` pipeline). Mermaid diagrams and Vega-Lite charts render in place; Finnish characters are preserved.
