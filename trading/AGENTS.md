# AGENTS.md

This file provides guidance to AI coding assistants (Codex, Claude Code, and others) when working with code in this repository.

This vault is maintained interchangeably by **Claude Code** and **Codex**, chosen per session. This file (`AGENTS.md`) is the **single canonical operating manual** for both. `CLAUDE.md` is a redirect stub that points Claude Code here. Operate from `AGENTS.md` alone.

## Keeping the manuals in sync

`AGENTS.md` is the canonical source. `CLAUDE.md` is a stub — it contains only a pointer to this file. **All conventions, workflows, and rules live here only.** Whenever you update `AGENTS.md`, also update the `stub last confirmed` date in `CLAUDE.md`.

## What this repository is

This is not a software project. It is an LLM-maintained stock-trading **knowledge vault** built on Andrej Karpathy's LLM Wiki pattern (see `llm-wiki.md`): compile knowledge from raw sources into a persistent, interlinked markdown wiki that compounds over time. There is no build, test, or lint toolchain — all "operations" are content edits to markdown files. The vault is also an Obsidian vault (`.obsidian/`).

## Core roles and layers

- The user curates sources, asks questions, reviews outputs, and decides what matters.
- You (the LLM) maintain the wiki layer: summarizing, cross-linking, updating indexes, flagging contradictions, and appending the log.
- **`raw/`** — source-of-truth layer. Immutable. Do not modify, rename, or delete raw source files unless the user explicitly asks.
- **`wiki/`** — the generated knowledge layer. Edit freely to keep knowledge current and coherent.
- Always update `wiki/index.md` and `wiki/log.md` after changes.
- Write in clear, plain language. When uncertain how to categorize something, ask the user.
- **Never read or use `backup/`.** It is just backup — never use it for any processing or as guidance. (It contains a stale `CLAUDE.md` from an unrelated Japan-trip vault that prescribes `[[wiki-links]]`; ignore it entirely.)

A single ingested source typically touches 10–15 wiki pages (source note + entity/concept/strategy/indicator/setup pages + indexes + log). That is normal. `wiki/index.md` is the entry point — **read it first** for any query or ingest. `wiki/log.md` is append-only and reverse-chronological.

## Financial research posture

- This vault is for trading research and education, not personalized financial advice.
- Separate facts, interpretations, hypotheses, and trade ideas.
- Every market-sensitive statement must include an as-of date or source date.
- Never claim something is current, latest, today, or now without checking a current source.
- Record uncertainty with `low`/`medium`/`high` confidence in frontmatter and on key claims.
- Distinguish backtested results, paper-traded observations, and live-trading outcomes.
- Strategy pages must include invalidation criteria, risk controls, regime assumptions, and failure modes.

## Directory contract

```text
raw/                 Source-of-truth layer (immutable).
  inbox/             New unprocessed sources.
  articles/          Web clips, essays, newsletters, blog posts.
  books/             Book excerpts and reading notes.
  filings/           SEC filings, annual reports, investor presentations.
  reports/           Broker, fund, macro, sector, thematic reports.
  transcripts/       Earnings calls, interviews, podcasts, webinars.
  data/              CSV/XLSX/JSON/parquet datasets and exports.
  charts/            Screenshots, chart studies, visual references.
  trade-journal/     Immutable trade log exports or screenshots.
  assets/            Images and attachments referenced by raw sources.

wiki/                Generated knowledge layer (edit freely).
  index.md           Content catalog. Read this first for queries.
  log.md             Append-only chronological history.
  overview.md        High-level map of the vault.
  glossary.md        Trading vocabulary and short definitions.
  source-notes/      One page per ingested source.
  entities/          Companies, people, institutions, exchanges.
  concepts/          Market structure, risk, indicators, psychology, etc.
  strategies/        Strategy hypotheses and evidence.
  indicators/        Technical/fundamental/quantitative indicators.
  setups/            Concrete trade setup checklists.
  sectors/           Sector and industry pages.
  instruments/       Stocks, ETFs, options, futures, bonds, crypto, etc.
  comparisons/       Side-by-side analyses.
  syntheses/         Higher-level answers and evolving theses.
  questions/         Open research questions and investigation trails.
  watchlist.md       Living swing-trade monitoring dashboard. Read when asked "which stocks to check today/this week?"
  trade-journal/     LLM-written analysis sessions and trade records.
    analysis/        Pre-trade chart analysis sessions. One page per day. Month subfolders: YYYY-MM/.
    trades/          Actual trade records: annual ledgers `all-trades-YYYY.md` plus monthly narrative pages `YYYY-MM/<stock-code>.md`.
  _templates/        Page templates to copy when creating new pages.
```

## Naming and linking

- Lowercase kebab-case filenames: `risk-management.md`, `aapl.md`, `2026-06-13-source-title.md`.
- ISO dates: `YYYY-MM-DD`. Source notes start with the ingest date: `wiki/source-notes/YYYY-MM-DD-short-title.md`.
- Company entity pages use the primary ticker when practical: `wiki/entities/companies/aapl.md`.
- **Use relative Markdown links for internal links**, e.g. `[Risk Management](../concepts/risk-management.md)` — not Obsidian `[[wiki-links]]`. Use standard external links for web URLs and raw-source references.

## Standard frontmatter

Every wiki page begins with YAML frontmatter:

```yaml
---
type: concept
status: seed
created: 2026-06-13
updated: 2026-06-13
tags: []
sources: []
confidence: low
---
```

- `type` values: `index`, `log`, `source-note`, `company`, `person`, `institution`, `concept`, `strategy`, `indicator`, `setup`, `sector`, `instrument`, `comparison`, `synthesis`, `question`, `trade-review`, `chart-analysis`, `watchlist`, `lint-report`.
- `status` values: `seed` (scaffold), `active` (useful and sourced), `needs-review` (uncertainty/contradictions/missing citations), `stale` (likely outdated, needs current verification).
- Copy from `wiki/_templates/` when creating a new page of a given type.

## Ingest workflow

When the user asks to ingest a source:

1. Read `wiki/index.md`, `wiki/log.md`, and any obviously relevant wiki pages.
2. Read the raw source without altering it.
3. Create a source note under `wiki/source-notes/` using `wiki/_templates/source-note.md`.
4. Extract trading-relevant facts, claims, dates, tickers, catalysts, risks, strategy ideas, and contradictions.
5. Update relevant entity, concept, strategy, sector, instrument, or setup pages.
6. Add backlinks from updated pages to the source note.
7. Update `wiki/index.md`.
8. Append a `wiki/log.md` entry with heading: `## [YYYY-MM-DD] ingest | Source Title`
9. Tell the user what changed and what deserves review.

## Query workflow

When the user asks a question:

1. Read `wiki/index.md` first.
2. Search or inspect relevant wiki pages.
3. Use raw sources only to verify a wiki page or when the user asks for source-level detail.
4. Answer with citations to wiki pages and source notes.
5. If the answer is reusable, save it under `wiki/syntheses/`, `wiki/comparisons/`, or another appropriate folder.
6. Append a `query` entry to `wiki/log.md` when a new durable page is created or the query materially changes the wiki.

## Lint workflow

When asked to lint or health-check the vault:

- Look for unsupported claims, stale market facts, contradictions, duplicate pages, orphan pages, missing backlinks, missing tickers, missing dates, and missing source notes.
- Identify strategy pages lacking risk controls, invalidation criteria, evidence, or failure modes.
- Identify company pages that mix old and current data without as-of dates.
- Recommend new sources or questions that would improve the wiki.
- Save durable lint results under `wiki/syntheses/` or `wiki/questions/` when useful.
- Append a `lint` entry to `wiki/log.md`.

## Log entry headings

Append entries in reverse chronological order, using search-friendly headings:

```markdown
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question Summary
## [YYYY-MM-DD] lint | Scope
## [YYYY-MM-DD] maintenance | Change Summary
## [YYYY-MM-DD] chart-analysis | Tickers Reviewed
```

## Chart analysis workflow

When the user submits a chart image for swing-trade assessment:

1. Identify the instrument (ticker, type: stock/ETF/index ETF, exchange).
2. Apply [Stage Analysis](wiki/concepts/stage-analysis.md): determine which of the four stages the instrument is in.
3. Run a Trend Template check: evaluate all 8 criteria against the visible chart structure.
4. Identify key price levels: prior high, resistance zones, current price, support zones, crash low.
5. Calculate risk/reward for at least two entry scenarios (current price, pullback, breakout).
6. Deliver a verdict: Strong Avoid / Watchlist / Conditional / Setup / Strong Setup.
7. After the session, create (or append to today's) analysis page: `wiki/trade-journal/analysis/YYYY-MM/YYYY-MM-DD-swing-review.md`.
8. Update `wiki/watchlist.md`: add/update rows for each instrument; set check-back dates.
9. Append a `chart-analysis` entry to `wiki/log.md`.

Log heading format for chart analysis:
```markdown
## [YYYY-MM-DD] chart-analysis | Tickers Reviewed
```

## Data analysis workflow

When the user asks to analyze local historical data files (CSV price data, backtests, scanner output) to identify swing trading opportunities:

**This is NOT an ingest workflow.** Do not create source-notes, instrument pages, syntheses, or any files outside `wiki/trade-journal/analysis/`.

The swing analysis script already exists at `code/swing_analysis.py`. The virtual environment is at `.venv/`. Do **not** rewrite or recreate the script.

1. Run the scanner:
   ```bash
   ./.venv/Scripts/python.exe code/swing_analysis.py \
     --data-dir data_nse_calculated \
     --symbols SYM1 SYM2 ... \
     --output <temp>.md \
     --lookback-days 504
   ```

2. Read the generated output file.

3. Create **one analysis session page** at:
   `wiki/trade-journal/analysis/YYYY-MM/YYYY-MM-DD-<short-description>.md`
   Use `type: chart-analysis` frontmatter. Keep it self-contained: summary table, per-symbol findings, actionable setups with entry/stop/target, and check-back dates.

4. Update `wiki/watchlist.md`: add new Setup/Strong Setup candidates; update verdicts for symbols already on the watchlist.

5. Update `wiki/index.md` with a link to the new analysis page under "Recent Analysis Sessions".

6. Append to `wiki/log.md`:
   ```markdown
   ## [YYYY-MM-DD] chart-analysis | Tickers Reviewed
   ```

7. Delete the temporary output file generated in step 1.

**Trigger phrases that mean "run this workflow"** (not the ingest workflow):
- "analyze [symbols] over [period]"
- "scan [symbols] for swing opportunities"
- "run the scanner on [symbols]"
- "ingest the analysis" (when the context is a data/scanner analysis session)
- "identify swing trading opportunities from data"

## Trade recording workflow

When the user records an actual trade:

1. Update the annual ledger: `wiki/trade-journal/trades/all-trades-YYYY.md`.
2. The annual ledger should only contain this table: position (OPEN/CLOSED), stock_code, direction, quantity, buy_date, buy_price, total_cost, target, stop_loss, R:R, sell_date, sell_price, total_sell_value, profit (loss). Do not add a Remarks column.
3. Target, stop_loss, and R:R may be supplied by the user when recording the trade. If omitted, populate them from the corresponding analysis record; if the actual entry differs from the analysis entry, recalculate R:R from the actual buy price and the analysis-derived target/stop.
4. Link the `stock_code` cell to the monthly narrative page: `wiki/trade-journal/trades/YYYY-MM/<stock-code>.md`.
5. Use the monthly narrative page for planned thesis, actual execution, source scenario for target/stop/R:R, rule adherence, outcome, and lessons.
6. Update `wiki/watchlist.md`, `wiki/index.md`, and `wiki/log.md`.

## Page quality bar

Good wiki pages are concise, sourced, dated, and linked. They make future answers cheaper by compiling knowledge once instead of rediscovering it from raw files. Prefer a clear synthesis with citations over long copied excerpts.
