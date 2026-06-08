# AEAF Skills

The human-facing tools that make AEAF light enough to actually execute. The standing critique of TOGAF was execution cost; these skills are where that cost is removed. Each is a `SKILL.md` (skills standard — YAML frontmatter `name` + `description`, then the procedure) that drives the Pass-1 templates in `tools/templates/` and points back to the AEAF books for the theory.

## The set

**Six act-based skills** — each performs one practitioner *act* across the phases that need it:

| Skill | The act | Drives |
|---|---|---|
| `aeaf-author` | Fill / maintain any artifact | every template |
| `aeaf-allocate` | Capability-allocation + automation-frontier workshop (Phase 2) | Capability Catalog · Human-Agent RACI · Autonomy assignment · Frontier Map |
| `aeaf-guardrails` | Compile principles → runtime guardrails (Phase 6) | Guardrail/Policy Catalog |
| `aeaf-evals` | Build the eval suite + thresholds (Phase 6) | Eval-Suite Specification |
| `aeaf-govern` | Pre-gate review · design-time gate · runtime loop · re-gating · **audit** (Phases 9–10) | Contract · Assurance Case · Trust & Accountability Matrix · checklists |
| `aeaf-maturity` | Maturity assessment + entry point (Book 2 §5–§6) | maturity assessment + MVP scope |

**Two workflow skills** — each runs an end-to-end journey through the acts:

| Skill | Journey |
|---|---|
| `aeaf-retrofit` | **Brownfield** — lift an already-implemented service to AEAF level: scan → reverse-map (baseline) → gap-analyse vs the gates → target-state + migration backlog. |
| `aeaf-greenfield` | **Greenfield** — design a new agentic service from Vision through the design-time gate, before it is built. |

## Why this shape (and what was folded in)

The acts, not the phases, are the unit — one skill per phase (~11) would repeat the same filling and gating logic over and over. Two workflow candidates were **folded into `aeaf-govern`** rather than built as separate skills, to avoid sprawl:
- **Audit** (independent read-only assessment of a live agentic system against the gates) → `aeaf-govern` mode 5.
- **Runtime-loop setup** (drift monitors, incident response, evidence) → `aeaf-govern` mode 3.

`aeaf-retrofit` is the requested brownfield workflow and the engine behind the worked example (`tools/example/customer-support/`) and the just-do-it-vs-AEAF comparison (`tools/example/the-drift/`).

## How they compose

`aeaf-maturity` sets the entry point → `aeaf-greenfield` or `aeaf-retrofit` runs the journey → each calls `aeaf-allocate`, `aeaf-guardrails`, `aeaf-evals`, `aeaf-govern` at the right phase → all of them call `aeaf-author` to write the artifacts. Every skill obeys the three rules: accountability is a named human; links are never dropped; a guardrail bounds at an enforcement point.
