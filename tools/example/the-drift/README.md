# The Drift — just-do-it vs AEAF-governed

The comparison that makes the case. The same agentic support line exists in two versions: the just-do-it proof-of-concept ("the drift") and the AEAF-governed service in `../customer-support/`. They are indistinguishable in a demo and entirely different in production.

## Contents

- **`the-drift.md`** — the comparison document (renders to PDF): the two architectures side by side, the PoC reverse-mapped into AEAF to expose what is missing, a coverage chart, the collapse dynamic, the EU-legal axis, and the thesis. This is the piece to read and to hand to a board.
- **`gap-register.md`** — the structured `aeaf-retrofit` Stage-3 output: 20 gaps, each with its production risk, the AEAF artifact/gate that closes it, and a severity (legal / operational / quality).

## The argument in one line

A just-do-it agentic service that touches money, personal data, and a physical action is a **collapsing PoC, not a business** — and in the EU it may be unlawful to operate. Controlled, systematic enterprise architecture is what turns it into something you can run, defend to a board, and answer to a regulator — and agents now make that architecture cheap enough to sustain.

## PDF

A pre-rendered **`the-drift.pdf`** is included in this folder. The source is plain
Markdown with Mermaid diagrams and a Vega-Lite chart, so it re-renders with any
Markdown→PDF toolchain that supports them.
