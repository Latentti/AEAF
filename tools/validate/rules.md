# aeaf-validate — rule catalog

Every rule the linter enforces, its severity, and the AEAF source that requires it. The point of the tool: turn the integrity rules the books state in prose into a deterministic check, so "is this set coherent / safe to proceed?" is answered by one command, not a manual read. No LLM, no network.

**Severities.** `ERROR` fails the run (exit 1). `WARN` is a smell (exit 0, unless `--strict`). `INFO` is informational (placeholders, recognised skill files).

## Structural rules (per file)

| Rule | Severity | What it checks | Source |
|---|---|---|---|
| **R01** | INFO / WARN | An artifact carries frontmatter. Recognised docs (`README.md`, `CLAUDE.md`, `AGENTS.md`, `rules.md`) → INFO; any other frontmatter-less `.md` → WARN (treated as documentation, not a forgotten artifact; `--strict` makes it fail). | conventions.md §1 |
| **R02** | ERROR / WARN | Required fields present: `artifact`, `title`, `type`, `status`, `version` (ERROR if missing). `owner` set (WARN; TBD → INFO) — not required on `reference`/`checklist` types. | conventions.md §1 |
| **R03** | ERROR | `type`, `status`, `phase`, `domain` hold valid enum values. | conventions.md §1, §3; Style Guide §3 |
| **R04** | ERROR / WARN | A living view (`status: runtime`) carries an `as_of` date in `YYYY-MM-DD` form. | conventions.md §3; Book 2 §15.9 |
| **R05** | WARN | Filename matches the `artifact` slug (tolerant of numeric-order `NN-` and `phase-` prefixes). | conventions.md §1 |
| **R06** | ERROR / WARN | A `SKILL.md` carries the skills-standard `name` + `description`, and `name` matches its folder. | skills standard |

## Cross-reference & integrity rules (repo-wide)

| Rule | Severity | What it checks | Source |
|---|---|---|---|
| **R10** | ERROR | Every `links:` target resolves to a known artifact slug in the repo — no dangling references. | Book 2 §15.11 (the dangling-reference rule) |

## Semantic-consistency rules (best-effort over parsed tables)

These engage on well-formed artifact tables (a filled engagement repo); they no-op on vertical template field-lists and on placeholder rows (`*(…)*`, `TBD`, `—`, `<!-- example -->`).

| Rule | Severity | What it checks | Source |
|---|---|---|---|
| **R20** | ERROR | Accountability is never an agent: an `accountable:` field or an Agent/RACI accountability cell is not an `AG-` id, and a RACI `A` does not sit in an agent column. | Book 1 §6.4 / §4; Book 2 §15.6 (the absolute rule) |
| **R21** | WARN | Oversight mode is consistent with autonomy level (L0–L2 ↔ in-the-loop, L3 ↔ on-the-loop, L4 ↔ out-of-the-loop) when a row states a single level + a single mode. | Book 1 Table 4.8 |
| **R22** | WARN | A principle marked `runtime` (Enforcement) references a compiled guardrail (`G-n`). | Book 1 §8, §4.6.1; Book 2 §15.5 |
| **R23** | WARN | A guardrail row names an enforcement point, a fail action, and a verifying eval (`EV-n`). | Book 2 §15.5 |

## What the linter deliberately does NOT do

- It does not judge whether an autonomy level is *wise* for the consequence, whether an allocation is *sound*, or whether an eval threshold is *right*. Those are judgment calls — they belong to the human and to the `aeaf-govern` / `aeaf-allocate` skills (the architecture-review checklist), not to a deterministic linter. The split mirrors the books' own: mechanical completeness (this tool) vs architecture review (judgment).
- It does not auto-fill values. `--fix` applies only safe whitespace normalisation (trailing whitespace, final newline); everything else is reported, not changed.
