---
type: trade-review
status: active
created: 2026-07-03
updated: 2026-07-20
tags: [trade-review, swing-trading, nse, lt, closed-loss]
sources:
  - ../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md
confidence: medium
trade_date: 2026-07-01
tickers: [LT]
strategy: swing-trade
position_status: closed
direction: long
---

# LT Trade Narrative

This page records the narrative details for LT trades opened in July 2026. The annual ledger is the compact source for trade rows; this page keeps the setup context, execution notes, and review material.

## Raw Trade Reference

- **Instrument:** LT, stock, NSE.
- **Direction:** Long.
- **Entry date:** 2026-07-01.
- **Quantity:** 12 shares.
- **Entry price:** 4097.8.
- **Gross entry value:** 49,173.60, excluding brokerage, taxes, slippage, and other charges.
- **Exit date:** 2026-07-07.
- **Exit price:** 3998.00.
- **Gross exit value:** 47,976.00, excluding brokerage, taxes, slippage, and other charges.
- **Position status:** Closed at stop loss on 2026-07-07.

## Planned Thesis

The entry follows the 2026-06-28 NSE swing scan, which classified LT as a **Strong Setup** using data as of 2026-06-25:

- Stage: Stage 2 markup.
- Trend Template: 8/8.
- Key monitoring levels from the scan: support near 4028.79 and resistance near 4440.00.
- Preferred entry from the scan: pullback near 4119-4029 or breakout above 4440 with volume confirmation.

The 4097.8 entry sits inside the preferred pullback zone from that scan.

## Trade Plan

The target, stop loss, and R:R were supplied with the trade record on 2026-07-03:

| Field | Value |
|---|---:|
| Target | 4440 |
| Stop loss | 3998 |
| R:R | 2.6:1 |

These values align with the 2026-06-28 scan's LT pullback scenario: analysis entry 4119.57, target 4440.00, stop 3998.53, R:R 2.6:1.

## Actual Execution

| Field | Value |
|---|---:|
| Entry date | 2026-07-01 |
| Quantity | 12 |
| Entry price | 4097.8 |
| Gross entry value | 49,173.60 |
| Target | 4440 |
| Stop loss | 3998 |
| R:R | 2.6:1 |
| Risk per share | 99.80 |
| Total planned risk | 1,197.60 |

## Outcome

The position was sold on 2026-07-07 at 3998.00, matching the planned stop loss. Gross sell value was 47,976.00, creating a gross loss of 1,197.60 before brokerage, taxes, slippage, and other charges.

| Field | Value |
|---|---:|
| Exit date | 2026-07-07 |
| Exit price | 3998.00 |
| Gross exit value | 47,976.00 |
| Gross profit / loss | -1,197.60 |
| Outcome | Closed-Loss |

## What Worked

- Entry aligned with a pre-existing watchlist setup rather than an unplanned trade.
- Entry price was within the pullback area identified before the trade.
- Stop discipline was followed; the position was exited when the planned stop was hit.

## What Failed

- The entry was documented after execution rather than as a pre-entry order plan.
- The stock had already been falling continuously for 2-3 days when the buy was placed. The fall continued after entry and hit the stop loss within a few days.
- In hindsight, the better execution would have been to wait for a reversal signal before buying, rather than buying during an active short-term slide.

## Rule Adherence

- **Setup alignment:** High, based on the 2026-06-28 scan.
- **Risk definition:** Medium; target and stop loss are recorded and align with the prior analysis, but were documented after execution.
- **Execution status:** Closed at the planned stop on 2026-07-07.

## Lessons

- Future entry records should include target, stop loss, R:R, invalidation condition, and whether the trade is full size or pilot size. If target/stop/R:R are omitted, derive them from the matching analysis scenario and record that derivation here.
- For pullback entries, do not treat a falling price inside the desired zone as sufficient by itself. Prefer evidence that selling pressure has paused or reversed, such as a reclaim, reversal candle, support hold, or higher low.

## Updates To Strategy / Setup Pages

- No strategy page changes yet. This trade weakens the pullback-entry process when it is used without a reversal signal or support confirmation.

## Related

- [2026-06-28 NSE swing scan](../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md)
- [All Trades 2026](../all-trades-2026.md)
- [Watchlist](../../../watchlist.md)
