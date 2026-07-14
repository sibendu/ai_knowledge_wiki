---
name: analyze
description: "Run the swing-trading scanner on local CSV data and atomically save results into the wiki. Accepts a symbol list and optional --deep flag for VCP/Livermore/SEPA analysis. Creates the analysis page, updates watchlist, index, and log in one pass. Use when the user asks to analyze stocks/ETFs for swing opportunities, scan symbols, or run the scanner."
user-invocable: true
---

# /analyze — Atomic Data-Analysis-to-Wiki Pipeline

## When To Use

Trigger this skill when the user says any of:
- "analyze [symbols] over [period]"
- "scan [symbols] for swing opportunities"
- "run the scanner on [symbols]"
- "identify swing trading opportunities from data"
- "/analyze [symbols]"
- Any request to run `swing_analysis.py` on a symbol list

This is NOT the ingest workflow. Do not create source-notes, entity pages, instrument pages, or syntheses.

## Non-Negotiables

- **Python path:** ALWAYS use `.venv/Scripts/python.exe`. NEVER use `python`, `python3`, or system Python.
- **Script path:** ALWAYS use `code/swing_analysis.py`. NEVER write a new analysis script.
- **Output location:** ONLY `wiki/trade-journal/analysis/YYYY-MM/YYYY-MM-DD-<description>.md`. NEVER write to source-notes, instruments, syntheses, entities, or the project root.
- **Frontmatter type:** `chart-analysis`.
- **Temp file:** Delete the scanner output file after reading it.
- **Wiki updates are mandatory:** analysis page + watchlist + index + log. All four, every time.

## Inputs

Parse from the user message:
- `SYMBOLS` — list of stock/ETF codes (required)
- `DEEP` — whether to use `--deep` flag (use when user mentions VCP, Livermore, SEPA, Minervini, contraction, pivotal points, or "deep analysis")
- `LOOKBACK` — lookback days (default: 504; user may say "1 year" = 252, "2 years" = 504, "6 months" = 126)
- `DESCRIPTION` — short kebab-case slug for the filename (derive from context, e.g. "nse-etf-scan", "midcap-vcp-screen")

## Workflow

### Step 1: Run the scanner

```bash
./.venv/Scripts/python.exe code/swing_analysis.py \
  --data-dir data_nse_calculated \
  --symbols SYMBOL1 SYMBOL2 ... \
  --output _temp_analysis.md \
  --lookback-days {LOOKBACK} \
  {--deep if DEEP}
```

If the data directory doesn't exist at `data_nse_calculated`, check for alternative paths the user may have used previously (e.g. a path they specify in their message). Ask if ambiguous.

### Step 2: Read the output

Read `_temp_analysis.md` (or whatever output path was used).

### Step 3: Create the analysis page

Write to: `wiki/trade-journal/analysis/YYYY-MM/YYYY-MM-DD-{DESCRIPTION}.md`

Create the month subdirectory if needed. Use this frontmatter:

```yaml
---
type: chart-analysis
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [swing-scan, data-analysis]
symbols: [SYMBOL1, SYMBOL2, ...]
method: standard  # or "deep-vcp-livermore" if --deep was used
confidence: medium
---
```

The body is the scanner output, optionally with a brief summary table at top for quick reference.

### Step 4: Update watchlist

Read `wiki/watchlist.md`. For each symbol rated Setup or Strong Setup (or VCP Setup / Strong VCP Setup in deep mode):
- Add a new row if not present
- Update the existing row if the symbol is already there (update verdict, price, date, check-back)

For symbols rated Avoid, mark them as such if they were previously on the watchlist.

### Step 5: Update index

Read `wiki/index.md`. Add a link to the new analysis page under "Recent Analysis Sessions" (or the appropriate section). Keep the list in reverse-chronological order.

### Step 6: Update log

Append to `wiki/log.md` (reverse-chronological, at the top after the heading):

```markdown
## [YYYY-MM-DD] chart-analysis | SYMBOL1, SYMBOL2, ... (truncate if >6 symbols)

- Scanner: `code/swing_analysis.py` {--deep if used}
- Symbols: {count} analyzed
- Setups found: {list of Setup/Strong Setup symbols}
- Analysis page: `wiki/trade-journal/analysis/YYYY-MM/YYYY-MM-DD-{DESCRIPTION}.md`
- Watchlist updated: yes
```

### Step 7: Clean up

Delete the temporary output file (`_temp_analysis.md`).

### Step 8: Report

Tell the user:
- How many symbols were analyzed
- Which symbols rated Setup or better
- Link to the analysis page
- Any symbols with missing data files

## Edge Cases

- If the user says "don't update the wiki" or "just show me results" — run steps 1-2 only, display the output, skip steps 3-7.
- If the user provides a custom data directory path, use it instead of the default.
- If `--deep` produces errors for a symbol (insufficient data), still include it in results with the error noted.
