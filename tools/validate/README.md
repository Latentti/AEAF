# aeaf-validate

A deterministic integrity linter for an AEAF artifact repository. **No LLM, no network, Python 3 stdlib only** — so it runs anywhere with no install.

## Why this exists

AEAF's whole premise is that agents collapse the upkeep cost that defeated classical EA. But agent-maintained upkeep is only *cheap* if its correctness is *automatically verifiable* — otherwise every change re-introduces the trust problem. This tool is that verifier: the deterministic third leg alongside the templates (the form) and the skills (the agent-guided judgment). It runs the integrity rules the AEAF books state in prose, so a human can trust an agent-maintained repository at machine speed.

It answers the checklists' core question — *is this complete enough, or coherent enough, to proceed?* — for the **mechanical** subset, leaving the **judgment** subset to the `aeaf-govern` review. That split mirrors the books: mechanical completeness vs architecture review.

## Usage

```sh
# Check a repository (default: current dir). Exit 1 if any ERROR.
python3 aeaf_validate.py path/to/repo

# Markdown coherence report (for a PR comment or a doc)
python3 aeaf_validate.py path/to/repo --report

# Treat warnings as failing too
python3 aeaf_validate.py path/to/repo --strict

# Apply only safe whitespace normalisation (no value changes)
python3 aeaf_validate.py path/to/repo --fix
```

Point it at a filled engagement repository (e.g. `tools/example/customer-support/`) or at the template set itself (`tools/templates/`). The semantic checks engage on well-formed artifact tables and no-op on template field-lists and placeholder rows.

## What it checks

The full rule catalog with severities and the book reference for each rule is in **`rules.md`**. In short: frontmatter schema and enums (R01–R06), cross-reference resolution / the dangling-reference rule (R10), and the semantic-consistency rules that matter most — **accountability is never an agent** (R20), oversight↔autonomy consistency (R21), runtime-principle→guardrail (R22), and guardrail→enforcement-point/fail-action/eval (R23).

## Pre-commit hook

```sh
# .git/hooks/pre-commit
#!/bin/sh
python3 tools/validate/aeaf_validate.py . || {
  echo "AEAF integrity check failed — see output above."; exit 1; }
```

## CI

```yaml
# e.g. GitHub Actions
- name: AEAF integrity
  run: python3 tools/validate/aeaf_validate.py . --report
```

The non-zero exit on any ERROR makes it a real gate, not advice. It is the cheapest quality control in the toolset: *show me that every reference resolves and no agent is accountable* — answered in milliseconds, on every change.
