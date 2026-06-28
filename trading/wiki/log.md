---
type: log
status: active
created: 2026-06-13
updated: 2026-06-28
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

## [2026-06-28] ingest | analysis1.md NSE swing scan

- Ingested root report `analysis1.md` into `wiki/trade-journal/analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md`.
- Preserved the 16-symbol scan summary, method, ranked verdicts, actionable monitoring levels, avoid/review-later notes, and data-quality flags.
- Updated `wiki/watchlist.md`: added LT, BANDHANBANK, MIDCAPETF, EXIDEIND, APOLLOHOSP, HDFCSML250, and ICICIBANK; updated BANKBEES; downgraded NIFTYBEES and BAJAJHLDNG based on the 2026-06-25 dataset.
- Updated `wiki/index.md` to point to the durable wiki analysis page.

## [2026-06-28] query | NSE swing scan reusable script

- Created `code/swing_analysis.py`, a dependency-light reusable scanner for local `data_nse_calculated/*.csv` files.
- Generated `analysis1.md` for NIFTYBEES, BANKBEES, MIDCAPETF, HDFCSML250, ICICIBANK, KOTAKBANK, LT, BAJAJHLDNG, GILLETTE, GLAXO, IRFC, ITC, UCOBANK, BANDHANBANK, APOLLOHOSP, and EXIDEIND.
- Analysis uses Stage Analysis, Trend Template, 1/3/6-month momentum, 52-week distance, pivots, ATR-based scenario levels, and volume/delivery context.
- Data notes: `BANDHANBANK` resolved to local file `BANDHANBNK.csv`; KOTAKBANK had a large unadjusted price discontinuity on 2026-01-14, so the scanner used post-gap bars for metrics.

## [2026-06-28] chart-analysis | Historical Price Data - 6.5 Year Stock Analysis

**Swing Trading Opportunity from Historical Data** — Unknown ticker (data.csv), 2020-01-23 to 2026-04-07 (1540 bars).

**Summary:**
- **Current**: 831 (as of 2026-04-07)
- **52w High**: 1009 (+21.5%)
- **52w Low**: 202 (311% above low)
- **Stage**: Stage 2/3 transition (risky consolidation)
- **Trend Template**: 3/8 (not ready)
- **Verdict**: WATCHLIST / CONDITIONAL

**Key Finding:** Stock shows strong 6-year bull trend but **weak current technicals** (volume decline, stage 3 topping, low delivery %). 

**Swing Setup Options:**
1. **Bullish Entry**: Break above 877–885 + volume confirmation → target 920–950 (+11-14%)
2. **Value Entry**: Pullback to 760–775 (support) + recovery break → target 850–890
3. **Avoid**: Until volume increases or institutional holding (delivery %) recovers to >50%

**Created:** `wiki/trade-journal/analysis/2026-06/2026-06-28-swing-trade-data-analysis.md` — full technical analysis, price structure, scenarios, Trend Template assessment, entry/stop framework, invalidation criteria.

**Watchlist Status**: Added with conditional alerts (break 877, break 750, delivery >50%).

---

## [2026-06-28] chart-analysis | AXISBANK, NAM-INDIA, SBIN, COLPAL, HINDUNILVR, RELIANCE, HDFCAMC, HDFCBANK

**Livermore Pivotal Points & Swing Opportunities** — 8-stock institutional review (1-year horizon).

**Tier 1 (Strong Setup):**
- **AXISBANK** (8/8 TT): Base 1042 → ATH 1418 (Feb) → correction to 1150 → V-recovery at 1391 (re-pivot signal). Current 1377, 2.9% from ATH. Perfect Stage 2 uptrend structure. Entry: breakout >1420 or pullback 1290–1320. Target 1520–1580. Stop 1220. R:R 2:1–3:1.
- **NAM-INDIA** (8/8 TT): Textbook four-test base (780–800 zone held 4×). Feb breakout >1000 = pivotal point. ATH 1194. Current 1139 (4.6% from high). Entry: current 1100–1140 or ATH breakout >1195. Target 1280–1380. Stop 1038. R:R 1.5:1–2:1.

**Tier 2 (Conditional):**
- **SBIN** (7/8 TT): +57% run to ATH 1235 (Feb), then lower high/lower low pattern; in repair mode. Entry trigger: weekly close >1121 (Apr pivot). Target 1180–1235. Stop 975. R:R 1.5:1–2:1.
- **COLPAL** (0/8 TT): Stage 4 decline from ATH 2504 → climactic low 1782 → +25% bounce → consolidation. Entry trigger: weekly close >2090 (MA cluster) = Stage reversal signal. Speculative, counter-trend.

**Tier 3 (Avoid):**
- **HINDUNILVR, RELIANCE**: Stage 4, lower highs/lows in progress. No entry; monitor for reversal.
- **HDFCAMC, HDFCBANK**: ~50–53% structural price breaks (likely corporate events Dec 2025 & Sep 2025). Data distortion; no analysis until 12+ mo post-event history.

**Watchlist updated** with 4 new active stocks + entry conditions + check-back dates.

**Created:** `wiki/trade-journal/analysis/2026-06/2026-06-28-pivotal-points-swing-opportunities.md` — full analysis with pivotal sequences, Livermore interpretation, TT verification, key levels, entry signals, risk notes.

---

## [2026-06-25] maintenance | Trade journal restructure + watchlist setup

Established new structure for chart analysis and trade tracking:
- Created `wiki/watchlist.md` — living swing-trade monitoring dashboard
- Created `wiki/trade-journal/analysis/` — pre-trade chart analysis sessions, month subfolders
- Created `wiki/trade-journal/trades/` — actual trade records, month subfolders
- Added `chart-analysis` and `watchlist` page types to CLAUDE.md / AGENTS.md
- Added chart-analysis workflow to both manuals
- Updated `wiki/index.md` with new Active Monitoring and Recent Analysis sections
- Ingested first analysis session: `wiki/trade-journal/analysis/2026-06/2026-06-25-swing-review.md`

## [2026-06-25] chart-analysis | Bajaj Holdings, BANKBEES, NIFTYBEES, HUL

Daily swing-trade assessment of 4 NSE instruments (2-week to 3-month horizon).

- **Bajaj Holdings (~10,599):** Stage 4 → early Stage 1. Capitulation flush visible. No setup yet. Watchlist — check back 2026-07-23.
- **BANKBEES (~601.92):** Event-driven crash, 67% recovered. At resistance. Conditional — pullback to 570–580 (3:1) or breakout >610 (2.3:1). Check back 2026-07-09.
- **NIFTYBEES (272.60):** Event-driven crash, 46% recovered. At resistance. Conditional — pullback to 265–267 (3:1) or breakout >280 (2:1). Check back 2026-07-09.
- **HUL (2,174.20):** Structural Stage 4, fails all 8 Trend Template criteria, 21% below 200-day MA. Strong Avoid. Check back 2026-09-25.

Source: `wiki/trade-journal/analysis/2026-06/2026-06-25-swing-review.md` | Watchlist: `wiki/watchlist.md`

## [2026-06-24] ingest | Technical Analysis For Dummies — Barbara Rockefeller (4th Ed, 2020)

Source folder: `raw/inbox/Technical_Analysis_For_Dummies/`
(536 pages, 104 images extracted)

Created:
- `wiki/source-notes/2026-06-24-technical-analysis-for-dummies.md`
- `wiki/entities/people/barbara-rockefeller.md`
- `wiki/indicators/moving-averages.md`
- `wiki/indicators/macd.md`
- `wiki/indicators/bollinger-bands.md`
- `wiki/indicators/average-true-range.md`
- `wiki/indicators/stochastic-oscillator.md`
- `wiki/indicators/ta4d-pivot-points.md`
- `wiki/concepts/dow-theory.md`
- `wiki/concepts/price-bars.md`
- `wiki/concepts/candlestick-charting.md`
- `wiki/concepts/chart-patterns.md`
- `wiki/concepts/trendlines-channels.md`
- `wiki/concepts/volume-analysis.md`
- `wiki/concepts/ichimoku.md`
- `wiki/concepts/point-and-figure.md`

Updated:
- `wiki/concepts/support-resistance.md` — breakout authentication rules
- `wiki/concepts/market-structure.md` — auction model, crowd dynamics
- `wiki/concepts/risk-management.md` — 5-step plan, stop taxonomy, recovery table
- `wiki/concepts/trading-psychology.md` — loss denial, guru trap, business mindset
- `wiki/concepts/trading-edge.md` — expectancy, confirmation principle, backtesting
- `wiki/indicators/rsi.md` — stochastic comparison, multi-indicator context
- `wiki/setups/ascending-triangle-breakout.md` — breakout confirmation rules
- `wiki/concepts/stage-analysis.md` — Wyckoff historical antecedent section
- `wiki/strategies/pivotal-point-trading.md` — disambiguation notice
- `wiki/glossary.md` — 10 new entries

Mapped:
- New indicator methodology: Moving Averages (SMA/EMA/ribbon/crossover), MACD (12/26/9), Bollinger Bands (squeeze/walk), ATR (true range/stop sizing), Stochastic (%K/%D/divergence), TA4D Pivot Points (PP formula, R1-R3/S1-S3)
- New concepts: Dow Theory (foundational TA), Price Bars (OHLC/special bars/gaps), Candlestick Charting (doji/hammer/engulfing), Chart Patterns (triangles/H&S/double tops/measured moves), Trendlines & Channels (regression/breakout authentication/orderliness), Volume Analysis (OBV/divergence/spikes), Ichimoku (Hosoda five-component system), Point & Figure (X/O/projections)
- Wyckoff model embedded in stage-analysis as historical antecedent of Weinstein/Minervini Stage Analysis
- Pivot-point disambiguation resolved: Livermore "Pivotal Point" (strategy) vs TA4D "Pivot Points" (formula indicator)

Linked assets (key images):
- fig_p201_029.png (candlestick anatomy), fig_p203_030.png (doji types), fig_p205_031.png (shaven bars), fig_p276_056.png (false breakout), fig_p280_057.png (orderly vs disorderly), fig_p285_059.png (pivot formulas), fig_p312_065.png (MA crossover), fig_p315_066.png (three MA), fig_p316_067.png (MA ribbon), fig_p319_068.png (MACD C/D), fig_p320_069.png (MACD indicator), fig_p321_070.png (MACD histogram), fig_p344_075.png (bullish divergence), fig_p358_080.png (Bollinger), fig_p360_081.png (ATR bands), fig_p379_085.png (P&F patterns), fig_p383_086.png (P&F vertical projection), fig_p410_092.png (Wyckoff model), fig_p433_096_vec.png (Ichimoku terms), fig_p446_105_vec.png (Ichimoku comparison)

Needs review:
- All market performance statistics (S&P returns, timer performance, JP Morgan quant AUM) are as of 2020 or earlier — marked stale
- Elliott Wave, Gann, Hurst cycles given introductory treatment only — deeper sources not yet ingested
- Barbara Rockefeller entity page is seed status (limited biographical detail)

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
