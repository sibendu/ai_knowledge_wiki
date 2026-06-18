---
type: concept
status: active
created: 2026-06-18
updated: 2026-06-18
tags: [stage-analysis, trend, market-cycle, stock-lifecycle, weinstein, minervini]
sources:
  - ../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md
confidence: medium
---

# Stage Analysis

**Origin:** Stan Weinstein, *Secrets for Profiting in Bull and Bear Markets* (1988); refined and applied by Mark Minervini in [SEPA Strategy](../strategies/sepa-strategy.md)
**Also known as:** Four-stage model, stock price maturation cycle

## Definition

Stage Analysis divides a stock's price history into four sequential phases based on price trend, moving average direction, and volume behaviour. Every stock cycles through these stages repeatedly over its lifetime. The stages are descriptions of where a stock currently sits in its price cycle — not predictions.

**The practical rule: buy Stage 2 only. Never initiate in Stage 1, 3, or 4.**

## The Four Stages

### Stage 1 — Neglect (Consolidation)

Sideways movement. The stock oscillates around its 200-day MA with no sustained directional trend. Volume is low and undistinguished. Institutional interest is absent or declining. This phase can last months to years.

**Characteristics:**
- Price flat, trending neither up nor down
- 200-day MA flat or barely moving
- Low volume; no persistent buying or selling pressure
- Earnings often uncertain or recovering from a Stage 4 decline

**Action:** Do not buy. Wait for Stage 2 confirmation.

---

### Stage 2 — Advancing (Accumulation)

The stock is in a confirmed uptrend — higher highs and higher lows in a staircase pattern. This is where superperformers produce their largest gains.

**Characteristics:**
- Price above 150-day and 200-day MAs
- 200-day MA trending upward
- 50-day MA above both 150-day and 200-day MAs
- Higher volume on up days/weeks; lighter volume on pullbacks
- Price ≥30% above 52-week low; within 25% of 52-week high
- IBD RS Ranking ≥70

Minervini's empirical observation from historical study (not a controlled study): 99% of the largest superperformers were above their 200-day MA before their biggest advances, and 96% were above their 50-day MA. Confidence: medium (selection and survivorship bias possible).

**Action:** The only stage where new longs should be opened. Entries made from [VCP](../setups/volatility-contraction-pattern.md) or base breakouts within Stage 2.

#### Base Count within Stage 2

As a stock advances through Stage 2 it typically forms a series of consolidation bases before resuming higher. Tracking the base count provides perspective on how mature the advance is:

| Base | Interpretation | Action |
|------|---------------|--------|
| 1–2 | Early Stage 2. Institutional awareness limited. Highest probability of a large subsequent move. | Best entry opportunities |
| 3 | Trend becoming more widely known; reward/risk ratio narrows. | Still tradable, use smaller size |
| 4–5 | Late Stage 2. Trend visible to everyone. Failure rates rise sharply. | Avoid or use minimal size |

After a significant market correction that forces a **base reset** (the stock's base count restarts because the overall market correction was severe enough), earlier-base dynamics can recur even for previously extended stocks.

---

### Stage 3 — Topping (Distribution)

The stock is still near highs but behaviour becomes erratic. Smart money is selling into strength. Stage 3 is frequently misread as a pause in an ongoing uptrend.

**Characteristics:**
- Price volatile and choppy; may still make new highs but with increasing reversals
- 200-day MA flattening or beginning to roll over
- Price may undercut the 200-day MA and fail to reclaim it convincingly
- Volume on down days begins to exceed volume on up days
- Earnings still growing but growth rate often decelerating
- Large single-day or single-week price breaks on above-average volume

The single most important Stage 3 exit signal: **the largest daily decline since the Stage 2 advance began, on the highest volume since the advance began.** This is a near-definitive sign of institutional distribution.

**Action:** Sell existing positions or tighten stops aggressively. Do not initiate new longs.

![Amgen Stage 3 topping 1993](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p88_017.png)

*Amgen Stage 3 (1993): erratic price action, increased volatility, 200-day MA flattening.*

---

### Stage 4 — Declining (Capitulation)

Full downtrend. Lower lows and lower highs. The 200-day MA is in a confirmed downtrend. Volume on down days is heavy; volume on rallies is light.

**Characteristics:**
- Price well below declining 200-day MA
- 50-day MA below 150-day and 200-day MAs
- "Dead cat bounces" — brief rallies that fail to establish a new uptrend
- Earnings decelerating or turning negative
- Extended decline until price exhaustion leads back to Stage 1

**Action:** Do not buy. Short selling may be considered by experienced traders, but is outside the SEPA long-only framework.

---

## Visual: Amgen Full Cycle (1989–1997)

The Amgen (AMGN) sequence is the book's primary teaching example for all four stages:

![Amgen Stage 1 consolidation 1987–1989](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p82_013.png)

*Stage 1: Horizontal, low-volatility consolidation around the 200-day MA.*

![Amgen Stage 1 to Stage 2 transition](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p84_014.png)

*Transition: Price begins to trend above moving averages with increasing volume.*

![Amgen Stage 2 uptrend](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p86_016.png)

*Stage 2: Confirmed uptrend — staircase pattern above all MAs.*

![Amgen Stage 4 decline](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p90_018.png)

*Stage 4: Lower lows and lower highs, price well below the declining 200-day MA.*

![Amgen full 4-stage cycle 1989–1997](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p91_019.png)

*Full annotated cycle: all four stages from 1989 to 1997.*

---

## Industry / Sector Stage Analysis

Stage analysis applies at the sector and industry level as well. As firms in a new industry proliferate (Stage 2), competition eventually compresses margins, the weakest fail, and survivors consolidate — the sector enters Stage 3 and 4. The number of manufacturers in the U.S. automobile and television industries illustrates this over decades.

![U.S. industry firm counts 1890–1990](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p129_044_vec.png)

*Number of firms in U.S. auto and TV industries — secular growth then consolidation.*

---

## Key Distinction: Stage Analysis vs. MA Crossovers

Stage Analysis uses moving averages diagnostically (to confirm which stage a stock is in), not as mechanically triggered buy/sell signals. A stock crossing above its 200-day MA is a stage transition *candidate*, not automatically a buy signal. The full [Trend Template](../concepts/trend-template.md) criteria must be met.

## Why It Matters for Trading

- Keeps traders out of the majority of the price distribution (Stages 1, 3, 4)
- Concentrates exposure in the phase with the highest historical reward/risk
- Provides an objective framework for distinguishing a healthy pullback (normal reaction within Stage 2) from the beginning of Stage 3

## Common Mistakes

- Buying Stage 1 because it looks "cheap" — Stage 1 can persist for years
- Misreading early Stage 3 volatility as a buying opportunity within Stage 2
- Ignoring the base count and buying late-Stage 2 situations as aggressively as early ones
- Using moving average crossovers alone without checking the full configuration

## Related Pages

- [Trend Template](../concepts/trend-template.md) — 8-criterion filter for Stage 2 confirmation
- [SEPA Strategy](../strategies/sepa-strategy.md) — uses Stage Analysis as its primary filter
- [Volatility Contraction Pattern](../setups/volatility-contraction-pattern.md) — entry method within Stage 2
- [Market Leadership](../concepts/market-leadership.md) — leaders enter Stage 2 before their sector
- [Support and Resistance](../concepts/support-resistance.md) — 200-day MA as dynamic support in Stage 2

## Source Notes

- [Trade Like a Stock Market Wizard — Mark Minervini](../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md)
- Stan Weinstein's original four-stage model: *Secrets for Profiting in Bull and Bear Markets* (1988) — not yet ingested in this wiki
