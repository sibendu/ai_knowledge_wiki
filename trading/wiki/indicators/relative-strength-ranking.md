---
type: indicator
status: active
created: 2026-06-18
updated: 2026-06-18
tags: [relative-strength, ibd, minervini, momentum, market-leadership, sepa]
sources:
  - ../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md
confidence: medium
category: fundamental / cross-sectional momentum
---

# Relative Strength Ranking (IBD RS Rating)

> **Name collision warning:** This is NOT the RSI (Relative Strength Index) momentum oscillator. The IBD RS Ranking compares a stock's 12-month price performance to the broader market. See [RSI](../indicators/rsi.md) for the momentum oscillator.

**Publisher:** Investor's Business Daily (IBD) — proprietary, subscription-required
**Also called:** RS Rating, Relative Strength Rating, RS Ranking
**Used in:** [Trend Template](../concepts/trend-template.md) (criterion 8), [SEPA Strategy](../strategies/sepa-strategy.md)

## Definition

The IBD RS Rating expresses a stock's **12-month price performance relative to all other stocks in the IBD database**, on a scale of 1–99. A rating of 85 means the stock outperformed 85% of all stocks over the past 12 months.

## Construction

The calculation weights recent quarters more heavily than older quarters (the most recent quarter is typically weighted 2×). The result is a percentile rank, not an absolute return figure. The exact proprietary formula is not published by IBD.

## Interpretation

| RS Rating | Interpretation |
|-----------|---------------|
| 90–99 | Elite relative strength — top-decile performer |
| 80–89 | Strong — typical range for emerging leaders |
| 70–79 | Minimum acceptable threshold for SEPA entry |
| 60–69 | Borderline — likely a laggard in its group |
| Below 60 | Weak relative performer — avoid for long setups |

**Minervini's minimum:** RS ≥70 required by the Trend Template. RS in the 80–99 range strongly preferred. Many of the biggest historical winners showed RS ratings in the 90s *before* their largest advances.

## The Lead Indicator Property

True market leaders typically build RS strength *before* the price advance becomes obvious to most investors — they hold up better during market corrections, pull back less than average, and emerge with high RS ratings even while still forming a base. Watching for stocks with high and rising RS while still in a base (i.e., not yet breaking out) is a key practitioner technique for identifying leaders early.

![Pharmacyclics vs. Nasdaq relative strength 2009–2010](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p178_072.png)

*Pharmacyclics (PCYC) outperforming the Nasdaq composite before its 1,500% advance over 33 months — RS strength building ahead of the price move.*

## Leaders vs. Laggards vs. Sector

Leaders emerge first in a new market cycle — before their sector confirms and before laggards recover.

![Leaders vs. sector vs. laggards timing](../../raw/inbox/trade_like_a_stock_market_wizard/assets/stock-trading/fig_p181_073.png)

*Typical sequence: true leaders bottom and begin advancing first, the sector ETF confirms later, and laggards recover last (or not at all).*

## Practical Use Without an IBD Subscription

IBD RS Ranking requires a paid subscription. Reasonable free proxies:
- Calculate the stock's 12-month total return and rank it as a percentile against the S&P 500 or Russell 3000 universe
- Many screening tools (Finviz, Stock Analysis, TradingView) offer 52-week relative performance metrics that approximate the concept
- The key characteristic to replicate: normalise for market performance to measure the stock's *excess* return, not its raw return

## Failure Modes

- Entirely backward-looking (12-month window); a stock can show high RS from a past move while already deteriorating fundamentally
- Does not distinguish between RS built through consistent accumulation vs. one or two gap-up events on earnings
- In a sector rotation, an entire sector can jump from low to high RS quickly; sector-level RS context matters as much as stock-level RS
- A stock in a market crash will show declining RS for months even if it is a future leader — timing the re-entry requires other signals (Stage Analysis, VCP)

## Evidence

- Used as criterion 8 in Minervini's Trend Template across all historical examples in the book (1984–2012)
- Minervini states most of his biggest winners had RS ≥80–90 before their major advances
- Confidence: medium (author's own observation from trading history; no controlled statistical study cited)

## Related Pages

- [RSI (Relative Strength Index)](../indicators/rsi.md) — different indicator, similar name; see disambiguation section
- [Trend Template](../concepts/trend-template.md) — RS Ranking is criterion 8
- [SEPA Strategy](../strategies/sepa-strategy.md)
- [Market Leadership](../concepts/market-leadership.md)
- [Stage Analysis](../concepts/stage-analysis.md)

## Source Notes

- [Trade Like a Stock Market Wizard — Mark Minervini](../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md)
