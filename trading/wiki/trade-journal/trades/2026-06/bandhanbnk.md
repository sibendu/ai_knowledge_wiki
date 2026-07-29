---
type: trade-review
status: active
created: 2026-07-03
updated: 2026-07-29
tags: [trade-review, swing-trading, nse, bandhanbnk, bandhanbank, closed-loss]
sources:
  - ../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md
confidence: medium
trade_date: 2026-06-30
tickers: [BANDHANBNK]
strategy: swing-trade
position_status: closed
direction: long
---

# BANDHANBNK Trade Narrative

This page records narrative details for the BANDHANBNK trade opened in June 2026 and closed on 2026-07-22. The related watchlist/analysis label is BANDHANBANK; the local data file used by the scan was BANDHANBNK.

## Raw Trade Reference

- **Instrument:** BANDHANBNK, stock, NSE.
- **Direction:** Long.
- **Entry date:** 2026-06-30.
- **Quantity:** 250 shares.
- **Entry price:** 202.24.
- **Gross entry value:** 50,560.00, excluding brokerage, taxes, slippage, and other charges.
- **Exit date:** 2026-07-22.
- **Exit price:** 189.00.
- **Gross exit value:** 47,250.00, excluding brokerage, taxes, slippage, and other charges.
- **Gross P&L:** -3,310.00 before costs.
- **Position status:** Closed-loss as of 2026-07-22.

## Planned Thesis

The entry follows the 2026-06-28 NSE swing scan, which classified BANDHANBANK/BANDHANBNK as a **Strong Setup** using data as of 2026-06-25. The scan showed Stage 2 markup, 8/8 Trend Template alignment, support near 197.66, and resistance near 212.48.

## Trade Plan

The target, stop loss, and R:R were supplied with the trade record on 2026-07-03, then the realized stop was recorded at 189.00 on 2026-07-29 from the user's sell note:

| Field | Value |
|---|---:|
| Target | 222 |
| Stop loss | 189 |
| R:R | 1.5:1 |

These values are close to the scan's current-price scenario: entry 201.76, stop 189.61, target 222.00, R:R 1.7:1.

## Actual Execution

| Field | Value |
|---|---:|
| Entry date | 2026-06-30 |
| Quantity | 250 |
| Entry price | 202.24 |
| Gross entry value | 50,560.00 |
| Target | 222 |
| Stop loss | 189 |
| R:R | 1.5:1 |
| Risk per share | 13.24 |
| Total planned risk | 3,310.00 |
| Exit date | 2026-07-22 |
| Exit price | 189.00 |
| Gross exit value | 47,250.00 |
| Gross P&L | -3,310.00 |

## Outcome

Closed at stop on 2026-07-22. The position rose to roughly 220, nearly reaching the 222 target, then reversed sharply and hit the 189 stop. After the stop, price continued down toward roughly 167, so the stop prevented a larger drawdown even though the trade first came very close to target.

## What Worked

- Entry aligned with a pre-existing Strong Setup.
- Trade plan values were recorded alongside the entry.
- The stop was honored after the sharp reversal, limiting the loss to the planned risk area.

## What Failed

- The trade nearly reached target but was not exited or de-risked around 220.
- A sharp reversal converted a near target-hit into a full stop-loss exit.
- The reversal suggests that profit-protection rules may be needed when price reaches a high percentage of target.

## Rule Adherence

- **Setup alignment:** High, based on the 2026-06-28 NSE scan.
- **Risk definition:** Medium; stop and target are recorded.
- **Execution status:** Closed at the recorded stop on 2026-07-22.
- **Exit discipline:** Mixed; the stop was respected, but there was no partial exit, trailing stop, or profit-protection adjustment after price reached roughly 220 against a 222 target.

## Lessons

- When a swing trade reaches roughly 90-95% of target, consider a predefined profit-protection rule: partial booking, stop raised toward breakeven/profit, or a trailing stop below the prior day's low.
- Near-target reversals are psychologically difficult because the setup was almost right; record them separately from poor entries.
- The original stop did its job after reversal, but the bigger improvement is protecting open profit before the stop becomes relevant.

## Updates To Strategy / Setup Pages

- No strategy page changes yet.

## Related

- [2026-06-28 NSE swing scan](../../analysis/2026-06/2026-06-28-nse-swing-scan-analysis1.md)
- [All Trades 2026](../all-trades-2026.md)
- [Watchlist](../../../watchlist.md)
