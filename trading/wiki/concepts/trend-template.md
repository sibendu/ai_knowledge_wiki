---
type: concept
status: active
created: 2026-06-18
updated: 2026-06-18
tags: [minervini, trend, moving-averages, sepa, screen, filter, stage-analysis]
sources:
  - ../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md
confidence: medium
---

# Trend Template

**Creator:** Mark Minervini
**Used in:** [SEPA Strategy](../strategies/sepa-strategy.md)
**Purpose:** Objective, all-or-nothing filter that confirms a stock is in a Stage 2 uptrend before any fundamental or chart-pattern analysis is done

## Definition

The Trend Template is a set of **eight criteria that must all be satisfied simultaneously** for a stock to be considered for purchase under the SEPA framework. If any single criterion fails, the stock is excluded — no exceptions. A different analyst might define different criteria for trend confirmation; this is Minervini's specific formulation, not a universal standard.

The template operationalises [Stage Analysis](../concepts/stage-analysis.md): passing all eight criteria is functionally equivalent to confirming Stage 2.

## The Eight Criteria

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | Current price above both the 150-day (30-week) and 200-day (40-week) MAs | Confirms price is above the two primary trend lines |
| 2 | 150-day MA above 200-day MA | Shorter-term trend faster than longer-term — upward slope confirmed |
| 3 | 200-day MA trending upward for at least 1 month (preferably 4–5 months) | Eliminates stocks just turning up after a deep Stage 4 decline |
| 4 | 50-day MA above both 150-day and 200-day MAs | Near-term trend strongest of the three — full MA stack aligned |
| 5 | Current price above 50-day MA | Price above all three MAs |
| 6 | Price at least 30% above its 52-week low | Eliminates stocks that have barely bounced; most superperformers are 100%+ above their low before emerging |
| 7 | Price within 25% of its 52-week high (closer the better) | Ensures the stock is near the top of its recent range, not recovering from deep damage |
| 8 | IBD Relative Strength Ranking ≥70 (preferably 80–99) | Confirms the stock outperforms the broad market on a 12-month basis |

## Moving Average Configuration ("MA Stack")

The fully aligned template requires:

```
Price > 50-day MA > 150-day MA > 200-day MA (trending up)
```

This is sometimes called an "upward MA stack" or "bullish MA alignment." Criteria 1–5 collectively enforce this configuration.

## Application Notes

- **Apply the template first**, before any chart pattern or fundamental analysis. It is a pre-filter, not a buy signal.
- Stocks near the boundary of criterion 6 or 7 deserve extra scrutiny — they may be early Stage 2 or still emerging from Stage 1.
- In strong bull markets, criterion 7 (within 25% of 52-week high) may be briefly violated during healthy consolidations within an ongoing Stage 2. Context matters.
- The template is designed for individual stock selection, not for timing the overall market index.

## Why All Eight vs. a Subset

A stock above its 200-day MA but below its 50-day MA, or near its 52-week low despite being "above its MAs," does not carry the same risk/reward profile as one passing all eight. The template is a probabilistic filter: the universe of stocks passing all eight criteria contains a disproportionate share of future superperformers, relative to any partial-criteria subset. Minervini's claim is not that every passing stock will advance, but that the best risk/reward opportunities cluster in this universe.

## Limitations

- **Backward-looking:** Confirms a trend already in progress. By definition, the entry is not at the absolute bottom.
- **Bear markets:** In a broad bear market, most stocks fail criteria 1–5 simultaneously, leaving a very thin qualifying universe. This is by design — SEPA calls for moving to cash in such environments.
- **IBD subscription required:** IBD RS Ranking (criterion 8) requires a paid Investor's Business Daily subscription. A proxy (12-month price return percentile vs. the S&P 500 or Russell 3000 universe) can approximate it. See [Relative Strength Ranking](../indicators/relative-strength-ranking.md).

## Why It Matters for Trading

The template acts as a mechanical gate that removes emotion from the initial stock selection step. By enforcing all eight criteria before any further analysis, it prevents the common mistake of buying fundamentally attractive stocks that are still in Stage 1, Stage 3, or early Stage 4. The filter does not guarantee a winning trade — it ensures the analyst is working within the correct phase of the price cycle.

## Related Pages

- [Stage Analysis](../concepts/stage-analysis.md) — conceptual framework the template operationalises
- [SEPA Strategy](../strategies/sepa-strategy.md) — overall framework the template gates
- [Relative Strength Ranking](../indicators/relative-strength-ranking.md) — criterion 8 in detail
- [Support and Resistance](../concepts/support-resistance.md) — MAs as dynamic support in Stage 2
- [Mark Minervini](../entities/people/mark-minervini.md)

## Source Notes

- [Trade Like a Stock Market Wizard — Mark Minervini](../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md)
