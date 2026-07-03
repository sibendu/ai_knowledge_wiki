---
type: trade-review
status: active
created: 2026-07-03
updated: 2026-07-03
tags: [trade-review, swing-trading, nse, lt, open-position]
sources:
  - ../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md
confidence: medium
trade_date: 2026-07-01
tickers: [LT]
strategy: swing-trade
position_status: open
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
- **Position status:** Open as of 2026-07-03.

## Planned Thesis

The entry follows the 2026-06-28 NSE swing scan, which classified LT as a **Strong Setup** using data as of 2026-06-25:

- Stage: Stage 2 markup.
- Trend Template: 8/8.
- Key monitoring levels from the scan: support near 4028.79 and resistance near 4440.00.
- Preferred entry from the scan: pullback near 4119-4029 or breakout above 4440 with volume confirmation.

The 4097.8 entry sits inside the preferred pullback zone from that scan.

## Analysis-Derived Plan

The trade entry did not specify target, stop loss, or R:R separately. Because the buy price sits in the pullback zone from the 2026-06-28 scan, the ledger uses the scan's LT pullback scenario:

| Source scenario | Analysis entry | Actual entry | Target | Stop loss | R:R used in ledger |
|---|---:|---:|---:|---:|---:|
| Pullback attempt | 4119.57 | 4097.8 | 4440.00 | 3998.53 | 3.4:1 |

The scan-listed pullback R:R was 2.6:1 using an analysis entry of 4119.57. The ledger R:R is recalculated from the actual buy price: `(4440.00 - 4097.8) / (4097.8 - 3998.53)`, approximately 3.4:1.

## Actual Execution

| Field | Value |
|---|---:|
| Entry date | 2026-07-01 |
| Quantity | 12 |
| Entry price | 4097.8 |
| Gross entry value | 49,173.60 |
| Target | 4440.00 |
| Stop loss | 3998.53 |
| R:R | 3.4:1 |
| Risk per share | 99.27 |
| Total planned risk | 1,191.24 |

## Outcome

Open. Exit, P&L, and post-trade review are not yet recorded in [all-trades-2026](../all-trades-2026.md).

## What Worked

- Entry aligned with a pre-existing watchlist setup rather than an unplanned trade.
- Entry price was within the pullback area identified before the trade.

## What Failed

- Target, stop loss, and R:R were not provided with the entry record; they were derived from the corresponding 2026-06-28 analysis scenario.

## Rule Adherence

- **Setup alignment:** High, based on the 2026-06-28 scan.
- **Risk definition:** Medium; target and stop loss are analysis-derived, not explicitly supplied at order entry.
- **Execution completeness:** Partial; entry is recorded, but actual exit remains open.

## Lessons

- Future entry records should include target, stop loss, R:R, invalidation condition, and whether the trade is full size or pilot size. If target/stop/R:R are omitted, derive them from the matching analysis scenario and record that derivation here.

## Updates To Strategy / Setup Pages

- No strategy page changes yet. Review after exit to determine whether the LT trade supports or weakens the pullback-entry process.

## Related

- [2026-06-28 NSE swing scan](../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md)
- [All Trades 2026](../all-trades-2026.md)
- [Watchlist](../../../watchlist.md)
