# AGENTS.md

This repository is an LLM-maintained stock-trading knowledge vault. Follow the LLM wiki pattern in `llm-wiki.md`: compile knowledge from raw sources into a persistent, interlinked markdown wiki that compounds over time.

This vault is maintained interchangeably by **Codex** and **Claude Code**, chosen per session. This file (`AGENTS.md`) is the operating manual for Codex sessions; `CLAUDE.md` is the equivalent for Claude Code. Operate from this file alone; do not depend on reading `CLAUDE.md`.

## Keeping the two manuals in sync

`AGENTS.md` and `CLAUDE.md` are parallel copies of the same operating manual. **Whenever you change a shared convention in one, mirror it in the other in the same session.** Parts that must stay identical:

- Directory contract (the `raw/` and `wiki/` structure)
- Naming and linking rules (kebab-case, ISO dates, relative Markdown links)
- Frontmatter schema (`type`/`status` values and fields)
- Ingest / Query / Lint workflows and log-heading formats
- Financial research posture and the page quality bar

Tool-specific phrasing (which assistant the file addresses) may differ; the conventions and workflows above must not.

## Core Roles

- The user curates sources, asks questions, reviews outputs, and decides what matters.
- The LLM maintains the wiki layer: summarizing, cross-linking, updating indexes, identifying contradictions, and appending the log.
- `raw/` is the source-of-truth layer. Do not modify raw source files unless the user explicitly asks.
- `wiki/` is the generated knowledge layer. It may be edited freely to keep the knowledge base current and coherent.
- Always update `wiki/index.md` and `wiki/log.md` after changes
- Write in clear, plain language
- When uncertain about how to categorize something, ask the user
- Never look into the backup folder, anything there is just backup and never to be used for any processing  



## Financial Research Posture

- This vault is for trading research and education, not personalized financial advice.
- Separate facts, interpretations, hypotheses, and trade ideas.
- Every market-sensitive statement must include an as-of date or source date.
- Never claim something is current, latest, today, or now without checking a current source.
- Record uncertainty. Use `low`, `medium`, or `high` confidence in frontmatter and in key claims.
- Distinguish backtested results, paper-traded observations, and live-trading outcomes.
- For strategy pages, always include invalidation criteria, risk controls, regime assumptions, and failure modes.

## Directory Contract

```text
raw/
  inbox/             New unprocessed sources.
  articles/          Web clips, essays, newsletters, and blog posts.
  books/             Book excerpts and reading notes.
  filings/           SEC filings, annual reports, investor presentations.
  reports/           Broker, fund, macro, sector, and thematic reports.
  transcripts/       Earnings calls, interviews, podcasts, webinars.
  data/              CSV/XLSX/JSON/parquet datasets and exports.
  charts/            Screenshots, chart studies, and visual references.
  trade-journal/     Immutable trade log exports or screenshots.
  assets/            Images and attachments referenced by raw sources.

wiki/
  index.md           Content-oriented catalog. Read this first for queries.
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
    trades/          Actual trade records and post-trade reviews. Month subfolders: YYYY-MM/.
  _templates/        Page templates to copy when creating new pages.
```

## Naming Rules

- Use lowercase kebab-case filenames: `risk-management.md`, `aapl.md`, `2026-06-13-source-title.md`.
- Use ISO dates: `YYYY-MM-DD`.
- Source notes should start with the ingest date: `wiki/source-notes/YYYY-MM-DD-short-title.md`.
- Company entity pages should use the primary ticker when practical: `wiki/entities/companies/aapl.md`.
- Prefer relative Markdown links for internal links, for example `[Risk Management](../concepts/risk-management.md)`.
- Use standard external links for web URLs and raw-source references.

## Standard Frontmatter

Every wiki page should begin with YAML frontmatter:

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

Recommended `type` values:

- `index`
- `log`
- `source-note`
- `company`
- `person`
- `institution`
- `concept`
- `strategy`
- `indicator`
- `setup`
- `sector`
- `instrument`
- `comparison`
- `synthesis`
- `question`
- `trade-review`
- `chart-analysis`
- `watchlist`
- `lint-report`

Recommended `status` values:

- `seed`: placeholder or lightly developed page.
- `active`: useful and sourced.
- `needs-review`: contains uncertainty, contradictions, or missing citations.
- `stale`: likely outdated and needs current verification.

## Ingest Workflow

When the user asks to ingest a source:

1. Read `wiki/index.md`, `wiki/log.md`, and any obviously relevant wiki pages.
2. Read the raw source without altering it.
3. Create a source note under `wiki/source-notes/` using `wiki/_templates/source-note.md`.
4. Extract trading-relevant facts, claims, dates, tickers, catalysts, risks, strategy ideas, and contradictions.
5. Update relevant entity, concept, strategy, sector, instrument, or setup pages.
6. Add backlinks from updated pages to the source note.
7. Update `wiki/index.md`.
8. Append a `wiki/log.md` entry using this heading format:

```markdown
## [YYYY-MM-DD] ingest | Source Title
```

9. Tell the user what changed and what deserves review.

## Query Workflow

When the user asks a question:

1. Read `wiki/index.md` first.
2. Search or inspect relevant wiki pages.
3. Use raw sources only when the wiki page needs verification or the user asks for source-level detail.
4. Answer with citations to wiki pages and source notes.
5. If the answer is reusable, save it as a page in `wiki/syntheses/`, `wiki/comparisons/`, or another appropriate folder.
6. Append a `query` entry to `wiki/log.md` when a new durable page is created or when the query materially changes the wiki.

## Lint Workflow

When asked to lint or health-check the vault:

- Look for unsupported claims, stale market facts, contradictions, duplicate pages, orphan pages, missing backlinks, missing tickers, missing dates, and missing source notes.
- Identify strategy pages that lack risk controls, invalidation criteria, evidence, or failure modes.
- Identify company pages that mix old and current data without as-of dates.
- Recommend new sources or questions that would improve the wiki.
- Save durable lint results under `wiki/syntheses/` or `wiki/questions/` when useful.
- Append a `lint` entry to `wiki/log.md`.

## Chart Analysis Workflow

When the user submits a chart image for swing-trade assessment:

1. Identify the instrument (ticker, type: stock/ETF/index ETF, exchange).
2. Apply Stage Analysis: determine which of the four stages the instrument is in.
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

## Page Quality Bar

Good wiki pages are concise, sourced, dated, and linked. They should make future answers cheaper by compiling knowledge once instead of rediscovering it from raw files. Prefer a clear synthesis with citations over long copied excerpts.

