# AEAF — Agentic Enterprise Architecture Framework

An enterprise-architecture framework for the human–agent enterprise. AEAF reworks the discipline of enterprise architecture for a world in which **AI agents are first-class actors** — executing work, consuming the architecture at runtime, and being governed as participants rather than tools.

The standing critique of classical EA frameworks is that they are too heavy to sustain — catalogs maintained by hand go stale, and a stale architecture stops being trusted. AEAF answers that on two fronts: its **content** is shaped for agentic systems (autonomy, guardrails, evals, accountability), and its **tooling** makes the artifacts cheap to produce and keep current, because agents do the upkeep that used to defeat adoption.

> **TOGAF® is a registered trademark of The Open Group.** AEAF is independent and original work; it is neither derived from, a profile of, nor endorsed by The Open Group. Where AEAF draws a parallel to TOGAF, it is a migration aid for existing practices, not a claim of lineage.

## What's here

### 📚 `books/` — the framework, as published PDFs
- **AEAF — The Framework** (Book 1): what the agentic enterprise is and how to architect it — the meta-model, the five domains (BDAT **+ I**ntelligence & Agency), the method (Preliminary + 10 phases), the nine new artifacts, the dual governance loop.
- **AEAF in Practice** (Book 2): how to adopt and run it — tailoring, playbooks, the artifact templates, checklists and gates.
- **AEAF At a Glance**: the one-page summary.

### 🛠️ `tools/` — the framework, made executable
- **`tools/templates/`** — every AEAF artifact as a Markdown file with YAML frontmatter: the 9 new artifacts, the 10 changed classical artifacts, supporting views (Regulatory Obligations Register, Determinism-Fit Map), deliverables (Vision, Architecture Definition Document, Roadmap…), phase worksheets, decisions, and gate checklists. Diff-able, human-editable, agent-writable, PDF-renderable.
- **`tools/skills/`** — broadly-usable skills (skills standard) that make AEAF light enough to execute: `aeaf-author`, `aeaf-allocate`, `aeaf-guardrails`, `aeaf-evals`, `aeaf-govern`, `aeaf-maturity`, plus two end-to-end workflows — `aeaf-retrofit` (lift an existing service to AEAF level) and `aeaf-greenfield`.
- **`tools/validate/`** — a deterministic, no-LLM linter (`aeaf_validate.py`) that checks an AEAF repository for integrity: every cross-reference resolves, accountability is never an agent, oversight matches autonomy, every runtime principle compiles to a guardrail. Run it in CI.
- **`tools/example/`** — two fully-worked, machine-validated examples, each carried through the AEAF phases:
  - **`customer-support/`** — a fictional parking operator's **agentic support line** (EU-compliant, every ID resolving): *agentic done right, with governance*. Its **`the-drift/`** companion contrasts a just-do-it PoC with the AEAF-governed version — why controlled architecture is the difference between a collapsing demo and a business.
  - **`automation-portfolio/`** — a fictional SaaS vendor placing six capabilities on the **determinism spectrum**: *where AI belongs* — rules where the answer is specifiable, an LLM only where the value is genuinely probabilistic (the right answer is sometimes **less** AI, placed deliberately). Its `the-default-trap.md` contrasts LLM-by-default with determinism-fit allocation.

## Quick start

```sh
# Validate an AEAF artifact repository (no dependencies, Python 3 stdlib only)
python3 tools/validate/aeaf_validate.py tools/example/customer-support --report
```

The artifacts are plain Markdown + YAML frontmatter, so they render to PDF with any
Markdown→PDF toolchain that supports Mermaid and Vega-Lite. Pre-rendered example PDFs
are included under `tools/example/`.

Start reading at `tools/templates/00-processing-model.md` (why Markdown + frontmatter), then `tools/templates/conventions.md`, then a worked example's walkthrough — `tools/example/customer-support/walkthrough.md` (agentic done right) or `tools/example/automation-portfolio/walkthrough.md` (where AI belongs).

## Licensing

This repository is **dual-licensed**:

| Part | License |
|---|---|
| **The books** (`books/`) | **CC BY-NC-ND 4.0** — read and share with attribution; no commercial use, no derivatives. See `LICENSE-books`. |
| **The tools** (`tools/`) | **Apache-2.0** — use, modify, and build on freely, including commercially. See `LICENSE-tools`. |

See `NOTICE` for trademark and attribution details.

---

*AEAF is created and maintained by [Latentti](https://github.com/Latentti).*
