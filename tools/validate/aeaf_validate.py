#!/usr/bin/env python3
"""
aeaf-validate — a deterministic integrity linter for an AEAF artifact repository.

No LLM, no network, stdlib only. It operationalizes the integrity rules the AEAF
books state in prose (Book 1 §21.5, §4; Book 2 §15.1, §15.9, §15.11, §17.1) so
that "is this set coherent / safe to proceed?" is a one-command machine check
rather than a manual read. Run it on a filled engagement repository or on the
template set itself.

Usage:
    python3 aeaf_validate.py [PATH]            # check (default); exit 1 if any ERROR
    python3 aeaf_validate.py [PATH] --report   # write a Markdown coherence report to stdout
    python3 aeaf_validate.py [PATH] --strict   # treat WARN as failing too
    python3 aeaf_validate.py [PATH] --fix       # apply only safe whitespace normalisation

PATH defaults to the current directory. The rule catalog with severities and the
book reference for each rule is in rules.md next to this script.
"""
import sys, os, re, glob

# ---- enums (from conventions.md / the style guide) --------------------------
TYPES   = {"catalog","matrix","map","spec","diagram","worksheet","decision","checklist","reference","deliverable"}
STATUS  = {"stub","baseline","target","approved","runtime","retired"}
PHASES  = {"P","1","2","3","4","5","6","7","8","9","10","all","TBD","none"}
DOMAINS = set("BDATI")
GUIDANCE = {"README.md","CLAUDE.md","AGENTS.md","rules.md"}   # docs; frontmatter not expected
ID_RE   = re.compile(r"\b(AG|M|KC|G|EV|P|CAP|ACT|ROLE|APP|DE|TC|INT|AC|ADR|CON)-[0-9]+\b")
AGENT_ID_RE = re.compile(r"\bAG-[0-9]+\b")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLACEHOLDER = ("*(", "TBD", "…", "...", "<!--", "(named", "(agent", "(capability",
               "(one sentence", "(leaf", "(routine", "(assess", "(decide", "(sensitive",
               "(intent", "(corpus", "(documents", "(host", "(human", "(team")

# autonomy <-> default oversight mode (Book 1 Table 4.8)
OVERSIGHT_FOR = {"L0":"in","L1":"in","L2":"in","L3":"on","L4":"out"}


def is_placeholder(cell: str) -> bool:
    c = cell.strip().lower()
    if not c or c == "—" or c == "-":
        return True
    return any(p.lower() in cell.lower() for p in PLACEHOLDER)


# ---- minimal frontmatter parser (inline scalars + inline lists only) --------
def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    raw, body = parts[1], parts[2]
    fm = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()] if inner else []
        else:
            fm[key] = val.strip('"').strip("'")
    return fm, body


# ---- markdown table parser --------------------------------------------------
def parse_tables(body):
    """Return list of tables; each is (headers:list[str], rows:list[dict])."""
    tables, block = [], []
    for line in body.splitlines():
        if line.lstrip().startswith("|"):
            block.append(line.strip())
        else:
            if len(block) >= 2:
                tables.append(block)
            block = []
    if len(block) >= 2:
        tables.append(block)

    out = []
    for blk in tables:
        cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
        headers = [h.lower() for h in cells(blk[0])]
        if not re.match(r"^[\s:\-\|]+$", blk[1].replace("|", "")):  # 2nd row must be separator
            continue
        rows = []
        for r in blk[2:]:
            vals = cells(r)
            if len(vals) != len(headers):
                continue
            rows.append(dict(zip(headers, vals)))
        out.append((headers, rows))
    return out


def col(headers, *needles):
    """Return the header key whose text contains all needles (lowercase), else None."""
    for h in headers:
        if all(n in h for n in needles):
            return h
    return None


# ---- load repository --------------------------------------------------------
class Rec:
    __slots__ = ("path", "rel", "fm", "body")
    def __init__(self, path, rel, fm, body):
        self.path, self.rel, self.fm, self.body = path, rel, fm, body


def load(root):
    recs = []
    for p in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
        text = open(p, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        recs.append(Rec(p, os.path.relpath(p, root), fm, body))
    return recs


# ---- checks -----------------------------------------------------------------
def run_checks(recs):
    findings = []  # (severity, rule, rel, message)
    def add(sev, rule, rel, msg): findings.append((sev, rule, rel, msg))

    slugs = {}
    for r in recs:
        if r.fm and r.fm.get("artifact"):
            slugs[r.fm["artifact"]] = r.rel

    for r in recs:
        base = os.path.basename(r.path)
        # guidance files: frontmatter intentionally absent
        if r.fm is None:
            if base in GUIDANCE:
                add("INFO", "R01", r.rel, "documentation file (no frontmatter expected)")
            else:
                # a loose .md is treated as documentation, not a forgotten artifact;
                # surfaced as WARN so --strict can catch a genuine omission.
                add("WARN", "R01", r.rel, "no frontmatter — treated as documentation, not an artifact")
            continue

        fm = r.fm

        # SKILL.md uses the skills standard (name + description), not artifact frontmatter
        if base == "SKILL.md":
            for f in ("name", "description"):
                if not fm.get(f):
                    add("ERROR", "R06", r.rel, f"skill missing '{f}'")
            folder = os.path.basename(os.path.dirname(r.path))
            if fm.get("name") and fm["name"] != folder:
                add("WARN", "R06", r.rel, f"skill name '{fm['name']}' != folder '{folder}'")
            else:
                add("INFO", "R06", r.rel, "skill frontmatter ok")
            continue

        # R02 required fields
        for f in ("artifact", "title", "type", "status", "version"):
            if not fm.get(f):
                add("ERROR", "R02", r.rel, f"missing required frontmatter field '{f}'")
        # owner (not required on reusable reference / checklist templates)
        owner = fm.get("owner", "")
        if fm.get("type") not in ("reference", "checklist"):
            if not owner:
                add("WARN", "R02", r.rel, "no 'owner' set")
            elif owner.startswith("TBD"):
                add("INFO", "R02", r.rel, "owner is TBD (placeholder)")

        # R03 enums
        if fm.get("type") and fm["type"] not in TYPES:
            add("ERROR", "R03", r.rel, f"invalid type '{fm['type']}'")
        if fm.get("status") and fm["status"] not in STATUS:
            add("ERROR", "R03", r.rel, f"invalid status '{fm['status']}'")
        if fm.get("phase") and str(fm["phase"]) not in PHASES:
            add("ERROR", "R03", r.rel, f"invalid phase '{fm['phase']}'")
        dom = fm.get("domain", [])
        if isinstance(dom, str):
            dom = [dom]
        for d in dom:
            if d not in DOMAINS and d != "TBD":
                add("ERROR", "R03", r.rel, f"invalid domain '{d}' (expected B/D/A/T/I)")

        # R04 as_of on living views
        if fm.get("status") == "runtime":
            ao = fm.get("as_of", "")
            if not ao:
                add("ERROR", "R04", r.rel, "status 'runtime' but no 'as_of' date")
            elif ao != "TBD" and not DATE_RE.match(ao):
                add("WARN", "R04", r.rel, f"as_of '{ao}' is not YYYY-MM-DD")
            elif ao == "TBD":
                add("INFO", "R04", r.rel, "as_of is TBD (placeholder)")

        # R05 filename matches slug (tolerant of numeric-order and 'phase-' prefixes)
        if fm.get("artifact"):
            stem = base[:-3] if base.endswith(".md") else base
            norm = re.sub(r"^\d+[-_]", "", stem)
            slug = fm["artifact"]
            if slug not in (stem, norm, "phase-" + stem, "phase-" + norm):
                add("WARN", "R05", r.rel, f"filename does not match artifact slug '{slug}'")

        # R10 links resolve
        for tgt in (fm.get("links") or []):
            if tgt in ("TBD",):
                continue
            if tgt not in slugs:
                add("ERROR", "R10", r.rel, f"dangling link target '{tgt}' (no artifact with that slug)")

        # ---- semantic checks over parsed tables ----------------------------
        for headers, rows in parse_tables(r.body):
            _semantic(add, r.rel, headers, rows)

    return findings, slugs


def _semantic(add, rel, headers, rows):
    h_agent = col(headers, "agent id") or col(headers, "agent")
    h_auto  = col(headers, "autonomy")
    h_over  = col(headers, "oversight")
    h_acct  = col(headers, "accountab")
    h_band  = col(headers, "decision-authority") or col(headers, "decision authority")
    h_enf   = col(headers, "enforcement")
    h_gid   = col(headers, "guardrail id") or (col(headers, "guardrail") if col(headers, "enforcement point") else None)
    h_eval  = col(headers, "eval") or col(headers, "verifying eval")
    h_efp   = col(headers, "enforcement point")
    h_fail  = col(headers, "fail action") or col(headers, "fail")

    for row in rows:
        # R20a accountability cell is never an agent id
        if h_acct and h_acct in row and not is_placeholder(row[h_acct]):
            if AGENT_ID_RE.search(row[h_acct]):
                add("ERROR", "R20", rel, f"accountability owner is an agent id ({row[h_acct]}) — must be a named human")

        # R21 oversight mode consistent with autonomy level (agent-catalog rows)
        if h_auto and h_over and h_auto in row and h_over in row:
            av, ov = row[h_auto], row[h_over].lower()
            if not is_placeholder(av) and not is_placeholder(row[h_over]):
                m = re.search(r"\bL[0-4]\b", av)
                if m:
                    want = OVERSIGHT_FOR[m.group(0)]
                    seen = ("out" if "out" in ov else "on" if "on-the-loop" in ov or ov.strip()=="on" else
                            "in" if "in-the-loop" in ov or ov.strip()=="in" else None)
                    # only flag when go-live level is single and oversight is single & mismatched
                    if seen and "→" not in av and "/" not in av and seen != want:
                        add("WARN", "R21", rel,
                            f"{m.group(0)} usually pairs with '{want}-the-loop' oversight, row says '{row[h_over]}'")

        # R22 runtime principle should compile to a guardrail
        if h_enf and h_enf in row and "runtime" in row[h_enf].lower():
            joined = " ".join(row.values())
            if not re.search(r"\bG-[0-9]+\b", joined) and not is_placeholder(joined):
                add("WARN", "R22", rel, "principle marked runtime but no guardrail (G-n) referenced in the row")

        # R23 guardrail row should name an enforcement point, a fail action, and a verifying eval
        if h_gid and h_gid in row and not is_placeholder(row.get(h_gid, "")):
            if h_efp and h_efp in row and is_placeholder(row[h_efp]):
                add("WARN", "R23", rel, f"guardrail {row[h_gid]} has no enforcement point")
            if h_fail and h_fail in row and is_placeholder(row[h_fail]):
                add("WARN", "R23", rel, f"guardrail {row[h_gid]} has no fail action")
            if h_eval and h_eval in row and is_placeholder(row[h_eval]):
                add("WARN", "R23", rel, f"guardrail {row[h_gid]} has no verifying eval (EV-n)")

        # R20b RACI: an 'A' must not sit in an agent column
        if h_band and h_agent and h_agent in row:
            cell = row[h_agent].replace("*", "").strip()
            if cell.upper() in ("A", "R/A", "A/R"):
                add("ERROR", "R20", rel, "RACI places Accountable (A) on the agent column — A must be a named human")


# ---- safe --fix (whitespace only) ------------------------------------------
def safe_fix(recs):
    fixed = 0
    for r in recs:
        text = open(r.path, encoding="utf-8").read()
        new = "\n".join(l.rstrip() for l in text.splitlines())
        if not new.endswith("\n"):
            new += "\n"
        if new != text:
            open(r.path, "w", encoding="utf-8").write(new)
            fixed += 1
    return fixed


# ---- output -----------------------------------------------------------------
def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    opts = {a for a in argv[1:] if a.startswith("--")}
    root = args[0] if args else "."
    if not os.path.isdir(root):
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    recs = load(root)
    if "--fix" in opts:
        n = safe_fix(recs)
        print(f"aeaf-validate --fix: normalised whitespace in {n} file(s)")
        recs = load(root)

    findings, slugs = run_checks(recs)
    errors = [f for f in findings if f[0] == "ERROR"]
    warns  = [f for f in findings if f[0] == "WARN"]
    infos  = [f for f in findings if f[0] == "INFO"]

    if "--report" in opts:
        print(f"# AEAF coherence report\n")
        print(f"- Scanned: **{len(recs)}** files · **{len(slugs)}** artifact slugs")
        print(f"- Result: **{len(errors)} errors · {len(warns)} warnings · {len(infos)} info**\n")
        for label, group in (("Errors", errors), ("Warnings", warns)):
            if group:
                print(f"## {label}\n")
                print("| Rule | File | Message |")
                print("|---|---|---|")
                for sev, rule, rel, msg in group:
                    print(f"| {rule} | `{rel}` | {msg} |")
                print()
        if not errors and not warns:
            print("No errors or warnings. The artifact set is coherent.\n")
    else:
        for sev, rule, rel, msg in errors + warns:
            print(f"{sev:5} {rule}  {rel}: {msg}")
        print(f"\naeaf-validate: {len(errors)} error(s), {len(warns)} warning(s), "
              f"{len(infos)} info — {len(recs)} files, {len(slugs)} slugs")

    fail = bool(errors) or ("--strict" in opts and bool(warns))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
