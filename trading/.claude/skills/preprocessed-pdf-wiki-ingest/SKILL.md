---
name: preprocessed-pdf-wiki-ingest
description: Ingest preprocessed PDF/document folders from a trading research vault into an interlinked markdown wiki. Use when the user has Markdown extracted from PDFs, books, reports, articles, or transcripts under raw/inbox document folders with linked image assets and generated image descriptions, and wants the source mapped into existing wiki concepts/entities/strategies/indicators/setups or new pages with user confirmation before durable edits.
---

# Preprocessed PDF Wiki Ingest

## Overview

Use this skill to ingest a preprocessed source folder into a stock-trading knowledge wiki while preserving raw assets and asking for confirmation before wiki edits. The expected repository shape is a raw source layer under `raw/` and a generated knowledge layer under `wiki/`.

## Non-Negotiables

- Do not modify, move, rename, copy, or rewrite anything under `raw/`.
- Never inspect or use any backup folder.
- Read the repository operating manual first: `AGENTS.md` for Codex, or `CLAUDE.md` for Claude Code when that is the active assistant manual.
- Read `wiki/index.md` before answering or planning.
- Read `wiki/log.md` before appending to it.
- Update `wiki/index.md` and append `wiki/log.md` after approved wiki changes.
- Use lowercase kebab-case filenames and ISO dates.
- Use relative Markdown links for internal wiki links and raw asset links.
- Every wiki page must begin with YAML frontmatter.
- Every market-sensitive claim must include a source date, as-of date, or explicit uncertainty note.
- Separate facts, interpretations, hypotheses, and trade ideas.
- Treat generated image descriptions as secondary annotations, not primary evidence when the visual is ambiguous.
- This vault is for trading research and education, not personalized financial advice.

## Confirmation Gate

Before creating or updating wiki files, produce an ingest plan and wait for explicit user approval.

Ask for clarification before editing when:

- A new concept, term, setup, strategy, indicator, sector, instrument, or entity should be created but its category is unclear.
- A term overlaps with an existing wiki page and the merge-versus-new-page decision is ambiguous.
- A ticker, company, author, source title, or source date cannot be identified confidently.
- The source contradicts existing wiki pages.
- The source appears stale, promotional, low quality, or missing important context.
- A chart/image is important but its meaning is unclear from the generated description.
- A strategy idea lacks enough detail to classify as a strategy, setup, indicator, or hypothesis.
- Current market verification outside the repository is required.

## Workflow

### 1. Read Existing Wiki Context

Read:

- `wiki/index.md`
- `wiki/log.md`
- `wiki/overview.md` if present
- `wiki/glossary.md` if present
- Relevant pages found by searching source title, author, tickers, companies, sectors, instruments, strategies, setups, indicators, and major terms.

Prefer updating existing pages over creating duplicates.

### 2. Read The Raw Source Folder

Read all Markdown files in `raw/inbox/<document_name>/`. Inspect linked image references and generated image descriptions.

Extract:

- Source title, author/publisher, source date, and ingest date.
- Tickers, companies, people, institutions, sectors, instruments, indicators, setups, and strategies.
- Catalysts, risks, macro claims, market structure claims, trading psychology claims, statistical claims, and backtest claims.
- Important charts, tables, diagrams, figures, and generated image descriptions.
- Contradictions with existing wiki content.
- Uncertainty, missing context, and items needing human review.

### 3. Produce The Ingest Plan And Stop

Before editing wiki files, show:

- Proposed source-note filename.
- Existing pages to update and why.
- New pages to create and why they are reusable knowledge.
- Concepts/entities/strategies/indicators/setups mapped from the source.
- Terms needing confirmation or categorization.
- Important raw images/assets to link and where they will be referenced.
- Contradictions, stale claims, low-confidence claims, and unclear source metadata.

Use this structure:

```markdown
## Proposed Ingest Plan

Source folder: `raw/inbox/<document_name>/`
Proposed source note: `wiki/source-notes/YYYY-MM-DD-<document-name>.md`

Existing pages to update:
- `wiki/concepts/example.md` - reason

New pages to create:
- `wiki/concepts/new-term.md` - why this should be reusable

Concepts and terms needing confirmation:
- `<term>` - proposed category and ambiguity

Important images/assets to link:
- `raw/inbox/<document_name>/assets/figure-01.png` - target page and reason

Contradictions or uncertainty:
- Existing page says X; this source says Y.

Please confirm whether to proceed and clarify the ambiguous items.
```

Wait for explicit approval before durable wiki edits.

### 4. Create The Source Note After Approval

Create one source note under `wiki/source-notes/YYYY-MM-DD-<document-name>.md`. Use `wiki/_templates/source-note.md` if available.

Include frontmatter like:

```yaml
---
type: source-note
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources:
  - raw/inbox/<document_name>/
confidence: low
---
```

The note should include source metadata, summary, trading-relevant facts, interpretations, hypotheses, trade ideas, images/figures, extracted terms, mapped wiki pages, contradictions, uncertainty, and review items.

From `wiki/source-notes/`, raw asset links usually look like:

```markdown
![Short figure description](../../raw/inbox/<document_name>/assets/figure-01.png)
```

When an image has a generated description, include:

```markdown
### Figure: Short Title

![Short alt text](../../raw/inbox/<document_name>/assets/figure-01.png)

Generated description: <description>

Use in wiki:
- Supports [Concept Name](../concepts/concept-name.md).
- Confidence: low/medium/high.
```

### 5. Update Existing Pages

For each relevant page:

- Preserve existing structure and tone.
- Add durable knowledge only.
- Add backlinks to the source note.
- Include source date or as-of date for market-sensitive claims.
- Link important raw images/assets where they materially improve the page.
- Mark contradictions or uncertainty clearly.
- Mark stale claims as stale instead of deleting them unless the user approved deletion.

Example:

```markdown
## Notes From <Source Title>

As of <source date>, <claim or finding>. Source: [Source Note](../source-notes/YYYY-MM-DD-document-name.md).

Related figure:

![Short figure description](../../raw/inbox/<document_name>/assets/figure-01.png)
```

Adjust relative paths by page depth. From `wiki/entities/companies/page.md`, a raw asset path usually starts with `../../../raw/`.

### 6. Create Approved New Pages

Create new pages only for reusable knowledge that future queries will likely need. Use the appropriate folder:

- `wiki/concepts/`
- `wiki/strategies/`
- `wiki/indicators/`
- `wiki/setups/`
- `wiki/sectors/`
- `wiki/instruments/`
- `wiki/entities/companies/`
- `wiki/entities/people/`
- `wiki/entities/institutions/`
- `wiki/syntheses/`
- `wiki/questions/`

Use frontmatter like:

```yaml
---
type: concept
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources:
  - ../source-notes/YYYY-MM-DD-document-name.md
confidence: low
---
```

For strategy pages, always include thesis, setup conditions, regime assumptions, invalidation criteria, risk controls, failure modes, evidence level, related indicators, related instruments, and source links.

### 7. Update Index And Log

Update `wiki/index.md` with the new source note, new pages, and materially updated pages.

Append to `wiki/log.md` using:

```markdown
## [YYYY-MM-DD] ingest | <Source Title>

Source folder: `raw/inbox/<document_name>/`

Created:
- `wiki/source-notes/YYYY-MM-DD-document-name.md`

Updated:
- `wiki/concepts/example.md`

Mapped:
- Existing concept: risk management
- New concept: example concept

Linked assets:
- `raw/inbox/<document_name>/assets/figure-01.png`

Needs review:
- Source date could not be verified.
```

### 8. Final Response

Report source note created, pages created, pages updated, existing concepts mapped, new concepts added, images/assets linked, contradictions found, and items needing review. Keep it concise and audit-friendly.
