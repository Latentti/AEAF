# Worked example — Aava Software Oy AI automation portfolio

A second AEAF worked example, alongside `../customer-support/`. Where that one shows *agentic done right with governance*, this one shows the **prior decision the AI rush skips**: where a capability sits on the determinism spectrum, and **whether it should use an LLM at all**.

A fictional B2B SaaS vendor, **Aava Software Oy**, gets a board "AI efficiency mandate" and — instead of putting an LLM on everything — places each of six capabilities deliberately: rules where the answer is specifiable, an LLM only where the value is genuinely probabilistic, a human where the consequence demands it. Two of six become agents. That ratio is the lesson.

> Seeded from a real, widely-shared practitioner account (an LLM ticket-classifier replaced by a rules engine — accuracy 92%→99%, cost $180/mo→$0, and the team's trust restored because the logic was traceable). Aava and its staff are fictional.

## How to read it

1. **`00-case-context.md`** — the company, the mandate, the trap, the portfolio.
2. **`walkthrough.md`** — the AEAF method run, vision-first (Phase 1 → 2 → 4 → 9). Start here for the *why*.
3. **`deliverables/architecture-vision.md`** — the centerpiece: determinism-fit + explainability as the governing principles.
4. **`artifacts/supporting/determinism-fit-map.md`** — the signature artifact: six capabilities placed on the spectrum.
5. **`artifacts/classical/requirements-intent-catalog.md`** — the contrast: routing as a tested *requirement*, KB-drafting as an evaluated *intent*.
6. **`artifacts/new/`** — a *light* agent catalog: only the two genuinely-probabilistic capabilities became agents.
7. **`the-default-trap.md`** — the inverse-drift comparison: LLM-by-default vs AEAF determinism-fit allocation (renders to PDF).

## The argument in one line

Not everything needs an LLM. The architecture decision — *where on the determinism spectrum does this capability sit?* — is what tells you whether to reach for rules + a test or an LLM + an eval. Skip it and you ship a black box the team routes around; make it, and you ship a portfolio the team trusts. AEAF's right answer is sometimes **less AI, placed deliberately**.

## Validate it

```sh
python3 ../../validate/aeaf_validate.py . --report
```
Passes with zero errors — every cross-reference resolves, accountability is always a human, and the agent set covers only the capabilities the determinism-fit map placed `probabilistic`.
