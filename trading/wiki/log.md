---
type: log
status: active
created: 2026-06-13
updated: 2026-06-19
tags: [log]
sources: []
confidence: high
---

# Vault Log

Append entries in reverse chronological order. Use headings that are easy to search:

```markdown
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question Summary
## [YYYY-MM-DD] lint | Scope
## [YYYY-MM-DD] maintenance | Change Summary
```

## [2026-06-19] ingest | Reminiscences of a Stock Operator — Edwin LeFevre (Jesse Livermore)

Source folder: `raw/inbox/Reminiscences_Of_Stock_Operator/`
(Single Markdown file, 263 pages, 0 images extracted.)

Created:
- `wiki/source-notes/2026-06-19-reminiscences-of-a-stock-operator.md`
- `wiki/concepts/line-of-least-resistance.md`
- `wiki/concepts/tape-reading.md`
- `wiki/concepts/market-manipulation.md` (historical-reference page, pre-SEC mechanics)
- `wiki/concepts/stock-group-behavior.md`

Updated:
- `wiki/entities/people/jesse-livermore.md` — added career arc from Reminiscences (bucket-shop origins, repeated ruin/recovery, May 9 1901 tape-lag lesson, 1906–07 first million, Percy Thomas disaster, later distribution campaigns); second source backlink
- `wiki/strategies/pivotal-point-trading.md` — pivotal point as line-of-least-resistance break, buy-on-rising-scale, probe-then-pyramid, don't-force-the-move, sit-tight
- `wiki/syntheses/livermore-trading-principles.md` — added Reminiscences principles (sitting tight / Old Turkey, big-swing money, probe, sell-loser-keep-winner, hope/fear reversal, stand aside)
- `wiki/concepts/trading-psychology.md` — hope/fear reversal, Percy Thomas (magnetic personality), Dan Williamson (gratitude vs. judgment), the semisucker, tips as "hope cocktails"
- `wiki/concepts/risk-management.md` — exploratory/probe sizing, always-sell-loser-keep-winner, the "sleeping point", don't-make-the-market-pay-a-bill
- `wiki/concepts/market-structure.md` — pre-SEC historical notes (bucket shops, tape lag, pools/corners, own market impact)
- `wiki/concepts/market-leadership.md` — group-divergence signal cross-link to new Stock Group Behavior page
- `wiki/concepts/README.md`, `wiki/source-notes/README.md`, `wiki/index.md` — catalog the new pages and source note (source-notes README also backfilled two prior sources)

Mapped:
- New concepts: Line of Least Resistance, Tape Reading, Stock Group Behavior, Market Manipulation (historical)
- Embedded principle: Sitting Tight / Old Turkey (in Livermore Trading Principles synthesis, per decision not to create a standalone page)
- Existing concepts reinforced: risk management (probe sizing), trading psychology (hope/fear, magnetic-personality risk), market leadership (divergence), pivotal-point trading

Linked assets:
- None — the source folder contains no images/assets (images_extracted: 0).

Needs review:
- "Larry Livingston" is a pseudonym; book is a lightly fictionalised account of Jesse Livermore. Treated as Livermore throughout, with disclaimers on the entity and source-note pages.
- All market mechanics are pre-SEC; manipulation page scoped as historical reference, not current-market advice.
- Probe/line-of-least-resistance methods are 1923 anecdote, not modern backtests — follow-up questions logged in the source note.
- Complements (does not contradict) the 1940 *How to Trade in Stocks* source already in the vault.

## [2026-06-18] ingest | Trade Like a Stock Market Wizard — Mark Minervini

Source folder: `raw/inbox/trade_like_a_stock_market_wizard/`

Created:
- `wiki/source-notes/2026-06-18-trade-like-a-stock-market-wizard.md`
- `wiki/entities/people/mark-minervini.md`
- `wiki/strategies/sepa-strategy.md`
- `wiki/concepts/stage-analysis.md`
- `wiki/concepts/trend-template.md`
- `wiki/setups/volatility-contraction-pattern.md`
- `wiki/indicators/relative-strength-ranking.md`
- `wiki/concepts/earnings-acceleration.md`
- `wiki/concepts/earnings-quality.md`

Updated:
- `wiki/concepts/risk-management.md` — Minervini stop-loss rules, win/loss ratio, batting average math, difficult-market protocol
- `wiki/concepts/position-sizing.md` — pilot buys, pyramid-up-only rule, never-average-down, losing-streak scaling
- `wiki/concepts/trading-psychology.md` — ego vs. money, commitment vs. interest, paper trading limitation
- `wiki/concepts/market-leadership.md` — leaders emerge first, RS-based leadership, industry group rotation
- `wiki/strategies/pivotal-point-trading.md` — pivot point terminology disambiguation (Livermore vs. Minervini)
- `wiki/indicators/rsi.md` — RSI oscillator vs. IBD RS Ranking disambiguation table
- `wiki/concepts/support-resistance.md` — moving averages as dynamic support in Stage 2
- `wiki/concepts/trading-edge.md` — SEPA probability convergence, outcome asymmetry, individual investor structural advantage
- `wiki/setups/breakout-after-normal-reaction.md` — VCP as formalisation of the same supply-exhaustion logic

Mapped:
- New strategy: SEPA (Specific Entry Point Analysis)
- New concepts: Stage Analysis (four-stage lifecycle), Trend Template (8-criterion filter), Earnings Acceleration, Earnings Quality
- New sub-concepts embedded: Code 33 (in Earnings Quality), Post-Earnings Drift (in Earnings Quality), Base Count (in Stage Analysis)
- New setup: Volatility Contraction Pattern (VCP)
- New indicator: Relative Strength Ranking (IBD RS Rating — distinct from RSI oscillator)
- New entity: Mark Minervini

Linked assets (15 key images from 160 total):
- Amgen stage 1–4 sequence: fig_p82_013, fig_p84_014, fig_p86_016, fig_p88_017, fig_p90_018, fig_p91_019
- Leaders/laggards/sector timing: fig_p181_073
- Amazon early bottoming: fig_p182_074
- Pharmacyclics RS strength: fig_p178_072
- Code 33 table: fig_p173_070
- Monster Beverage Code 33: fig_p174_071
- Apple turnaround timeline: fig_p121_042_vec
- Industry firm counts: fig_p129_044_vec
- VCP examples: fig_p208_086_vec, fig_p212_087_vec
- Inventory red flag: fig_p172_069

Needs review:
- Stan Weinstein's stage analysis (*Secrets for Profiting in Bull and Bear Markets*, 1988) cited as foundational source — not yet ingested
- 220% avg/year figure (1994–2000) covers dot-com bull market; regime vs. system attribution unknown
- IBD RS Ranking requires paid subscription; free proxy documented in wiki page
- 145 of 160 images catalogued in source note only; 15 linked to specific wiki pages

## [2026-06-14] maintenance | Import chart assets from Technical Analysis Masterclass sample

- Copied `fig_p1_001_vec.png`, `fig_p2_002_vec.png`, `fig_p3_003_vec.png` from `raw/inbox/sample_market_notes/assets/sample/` → `wiki/assets/charts/`.
- Embedded each image (with full AI-generated chart description and key observations) in its primary wiki page:
  - fig_p1 → `wiki/setups/ascending-triangle-breakout.md` (Examples section)
  - fig_p2 → `wiki/concepts/support-resistance.md` (Role Reversal section)
  - fig_p3 → `wiki/indicators/rsi.md` (Interpretation section, after bearish divergence)
- Added Chart Assets table to `wiki/source-notes/2026-06-14-technical-analysis-masterclass-sample.md`.

## [2026-06-14] ingest | Technical Analysis Masterclass – Sample

- Ingested `raw/inbox/sample_market_notes/notes/sample.md` (3-page excerpt + 3 chart images, BTC/USD examples).
- Source covers: ascending triangle breakouts with volume/RSI confirmation, support/resistance role reversal, and RSI bearish divergence.
- Created source note `wiki/source-notes/2026-06-14-technical-analysis-masterclass-sample.md`.
- Created `wiki/indicators/rsi.md` — RSI definition, construction, overbought/oversold levels, divergence types, failure modes.
- Created `wiki/concepts/support-resistance.md` — S/R definition, role reversal mechanism, practical signals, common mistakes.
- Created `wiki/setups/ascending-triangle-breakout.md` — full checklist setup with entry variants, measured-move target, invalidation, and failure modes.
- Updated `wiki/indicators/README.md`, `wiki/concepts/README.md`, `wiki/setups/README.md`, and `wiki/index.md`.

**Review note:** All three pages are sourced from a single introductory-level sample; confidence is medium. Follow-up questions added to source note: RSI divergence predictive power (crypto vs. equities), measured-move reliability, and role reversal consistency across timeframes.

## [2026-06-13] ingest | How to Trade in Stocks - Jesse L. Livermore

- Ingested `raw/books/How-to-Trade-in-Stocks-Jesse-Livermore.pdf`.
- Added a source note, a Jesse Livermore entity page, a pivotal-point strategy page, a Market Key indicator page, a breakout-after-normal-reaction setup, a market-leadership concept, and a synthesis of Livermore trading principles.
- Updated risk management, position sizing, trading edge, trading psychology, market structure, source notes, category indexes, and the main wiki index.

## [2026-06-13] maintenance | Initial vault scaffold

- Created the raw-source layer, wiki layer, templates, index, log, and Codex schema.
- Seeded trading-specific categories for companies, concepts, strategies, indicators, setups, sectors, instruments, syntheses, comparisons, questions, and trade reviews.
