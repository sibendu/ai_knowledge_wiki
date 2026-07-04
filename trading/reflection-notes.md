---
type: lint-report
status: active
created: 2026-07-04
updated: 2026-07-04
tags: [meta, automation, workflow-improvement]
confidence: high
---

# Session Reflection: Highest-Leverage Improvements

Analysis of 14 Claude Code sessions across this project (Jun 28 – Jul 4 2026).
Sessions with substantive signal: 2211dbdf, cd5adf1c, 7f14e66f, 8ecafef5, cdf7eb5e, f2c21206, 13387e21.

---

## 1. Extend swing_analysis.py with VCP/Livermore/SEPA methods

**Type:** Code improvement (highest leverage)
**Recurrence:** 3 analysis tasks across 2 sessions (8ecafef5 tasks 2-3, 2211dbdf)
**Evidence:** In session 8eca, the assistant wrote 7 separate inline Python scripts from scratch to compute VCP contraction ratios, Livermore pivotal points, and SEPA/Trend Template checks — because the existing scanner lacks these methods. Each script repeated CSV-parsing boilerplate (open file, detect columns, float conversion, MA calculation). In session 2211, the same Livermore analysis was hand-coded again. The scripts are non-reproducible (lost after the session), inconsistent in metrics, and took ~10 min of generation time each.

**Recommendation:** Add a `--deep` or `--method vcp,livermore` flag to `code/swing_analysis.py` that computes:
- VCP contraction count and depth sequence
- Volume dry-up ratio (current vs 50-day avg)
- Livermore pivotal points (breakout from consolidation, new high after correction)
- Minervini Trend Template pass/fail (all 8 criteria)

**Why this is #1:** Every future deep-analysis session will hit this wall. The build cost is moderate (one-time ~200 lines) but the recurring cost is 7+ throwaway scripts per session that produce worse output.

---

## 2. Skill: /analyze — atomic data-analysis-to-wiki pipeline

**Type:** New skill
**Recurrence:** Every analysis session (4/4: sessions 2211, cd5a, 7f14, 8eca)
**Evidence:**
- In 2211, the user had to issue two separate prompts: "analyze these stocks" then "ingest the analysis in the wiki."
- In 7f14, the assistant saved output to `wiki/source-notes/`, `wiki/instruments/`, and `wiki/syntheses/` instead of `wiki/trade-journal/analysis/` — the user had to interrupt with "wait."
- In cd5a, the assistant skipped updating `wiki/watchlist.md` and `wiki/index.md` entirely.
- In 8eca, the 4-step wiki update (analysis page → watchlist → index → log → delete temp) succeeded but was repeated manually 3 times.

**Recommendation:** A `/analyze` skill that:
1. Accepts symbol list + optional method flag
2. Runs `.venv/Scripts/python.exe code/swing_analysis.py` with correct args
3. Reads output, creates analysis page at correct path (`wiki/trade-journal/analysis/YYYY-MM/`)
4. Updates watchlist, index, log atomically
5. Deletes temp file
6. Never touches source-notes, entities, instruments, or syntheses

**Why this is #2:** Eliminates the most common user correction (wrong output location), the most common missed step (incomplete wiki updates), and the two-prompt friction (generate then ingest). Every analysis session benefits.

---

## 3. Fix: Python environment resolution

**Type:** Fix (AGENTS.md directive + optional hook)
**Recurrence:** 4/4 analysis sessions (2211, cd5a, 7f14, 8eca)
**Evidence:**
- Session 2211: `python3` not found → user explicitly corrected to use `.venv`
- Session cd5a: `python3` not found → fell back to system `python` → `pandas` not found → abandoned to bash/awk
- Session 7f14: tried backslash paths, then WSL-style `/mnt/c/` paths, then finally `./` relative — 4 attempts
- Session 8eca: `python3` not found, UnicodeEncodeError on cp1252 console

**Recommendation:** Two fixes:
1. Add a bolded, top-level rule in AGENTS.md: "**ALWAYS use `.venv/Scripts/python.exe` for all Python operations. NEVER use `python`, `python3`, or any system Python.**"
2. Optional: a pre-command hook that rewrites `python3` → `.venv/Scripts/python.exe` in bash invocations.

**Why this is #3:** Zero build cost for the AGENTS.md fix. Already partially there but buried in a workflow section — needs to be a top-level environment rule. Eliminates 2-5 retries per session.

---

## 4. Skill: /dashboard — git repo status summary

**Type:** New skill (low build cost)
**Recurrence:** 3 sessions (f2c21206, cdf7eb5e, 13387e21)
**Evidence:** User asked for "git dashboard" in f2c2 and cdf7. In cdf7, the assistant didn't use gh-axi and had to be corrected. In 1338, the user followed up across sessions asking "did you use axi for git" — the new session couldn't answer.

**Recommendation:** A `/dashboard` skill that runs:
- `git status`, `git log --oneline -10`, branch info, uncommitted changes
- Uses gh-axi for any GitHub-specific info (PRs, issues)
- Outputs a formatted summary

**Why this is #4:** Recurs but is low-friction to answer manually. Build cost is very low (~20 lines of skill definition). Mainly saves one prompt per session and prevents the gh-axi tool-selection error.

---

## 5. No action needed: gh-axi as default for git ops

**Type:** Fix (already addressed)
**Recurrence:** 2 sessions (cdf7, 1338)
**Evidence:** Assistant used raw `gh` instead of gh-axi skill until user corrected.

**Recommendation:** None beyond what's already in AGENTS.md. The assistant should now pick this up from existing instructions. If it persists, add a feedback memory noting the preference.

---

## Summary table

| # | Candidate | Type | Sessions | Recurrence | Build cost | Verdict |
|---|-----------|------|----------|------------|------------|---------|
| 1 | VCP/Livermore in swing_analysis.py | Code | 8eca, 2211 | Every deep-analysis | Medium | **Build** |
| 2 | /analyze skill (atomic pipeline) | Skill | 2211, cd5a, 7f14, 8eca | Every analysis | Medium | **Build** |
| 3 | Python env resolution | Fix | 2211, cd5a, 7f14, 8eca | Every analysis | Trivial | **Fix now** |
| 4 | /dashboard skill | Skill | f2c2, cdf7, 1338 | ~1x/session | Low | **Build (low priority)** |
| 5 | gh-axi default | Fix | cdf7, 1338 | Declining | None | **No action** |

---

## Sessions analyzed

| Session ID | Date | Core activity | Signal quality |
|-----------|------|---------------|---------------|
| 2211dbdf | Jun 28 | 8-stock Livermore analysis + wiki ingest | High |
| cd5adf1c | Jun 28 | CSV analysis (bash/awk improvisation) | High |
| 7f14e66f | Jul 3 | 23 ETF analysis + AGENTS.md restructure | High |
| 8ecafef5 | Jul 3 | 23 ETF + 14 stock deep VCP/Livermore | High |
| cdf7eb5e | Jul 2 | Git dashboard + PRs (gh-axi correction) | Medium |
| f2c21206 | Jul 2 | Git dashboard | Low |
| 13387e21 | Jul 2 | Cross-session context loss (axi) | Low |
| 574892b4 | Jul 2 | Check PRs (smooth) | Low |
| dc609512 | Jun 28 | 16-stock analysis (truncated transcript) | Minimal |
| f3fa4d2a | Jun 28 | Test question (no signal) | None |
