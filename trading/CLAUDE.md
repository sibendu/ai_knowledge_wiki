# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This vault is maintained interchangeably by **Claude Code** and **Codex**, chosen per session. This file (`CLAUDE.md`) is the operating manual for Claude Code sessions; `AGENTS.md` is the equivalent for Codex. Operate from this file alone; do not depend on reading `AGENTS.md`.

## Keeping the two manuals in sync

`CLAUDE.md` and `AGENTS.md` are parallel copies of the same operating manual. **Whenever you change a shared convention in one, mirror it in the other in the same session.** Parts that must stay identical:

- Directory contract (the `raw/` and `wiki/` structure)
- Naming and linking rules (kebab-case, ISO dates, relative Markdown links)
- Frontmatter schema (`type`/`status` values and fields)
- Ingest / Query / Lint workflows and log-heading formats
- Financial research posture and the page quality bar

Tool-specific phrasing (which assistant the file addresses) may differ; the conventions and workflows above must not.

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
  trade-journal/     LLM-written trade reviews and lesson summaries.
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

- `type` values: `index`, `log`, `source-note`, `company`, `person`, `institution`, `concept`, `strategy`, `indicator`, `setup`, `sector`, `instrument`, `comparison`, `synthesis`, `question`, `trade-review`, `lint-report`.
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
```

## Page quality bar

Good wiki pages are concise, sourced, dated, and linked. They make future answers cheaper by compiling knowledge once instead of rediscovering it from raw files. Prefer a clear synthesis with citations over long copied excerpts.
