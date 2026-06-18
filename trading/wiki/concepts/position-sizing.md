---
type: concept
status: active
created: 2026-06-13
updated: 2026-06-13
tags: [risk, sizing, pyramiding, livermore]
sources:
  - ../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md
confidence: medium
---

# Position Sizing

Position sizing converts a trade thesis, invalidation level, volatility, liquidity, and portfolio constraints into trade size.

## Livermore Notes

In [How to Trade in Stocks](../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md), Livermore argues against taking the whole intended line at one price. He prefers an initial commitment followed by additions only if the market proves the trade:

- For long trades, later buys should be at higher prices than earlier buys.
- For short trades, later sales should be at lower prices than earlier sales.
- The first trade should show a profit before the trader increases exposure.
- The trader should know the amount of money at risk before entering.

This is a pyramiding rule, not a complete modern sizing model. It still needs explicit account-risk limits, stop logic, and liquidity constraints.

## Questions To Build Out

- Which sizing method fits each strategy type?
- How should position size change after losses, volatility expansion, or reduced liquidity?
- What assumptions are required before sizing formulas are reliable?

## Source Notes

- [How to Trade in Stocks - Jesse L. Livermore](../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md)

## Notes From Trade Like a Stock Market Wizard (Minervini, 2013)

As of publication date 2013. Source: [Trade Like a Stock Market Wizard](../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md).

### Pilot Buys

Start a new position at reduced size (25–50% of intended full position) to test the trade. If the stock confirms direction, add to the position at a slightly higher price. This limits loss on trades that fail immediately at the entry point while preserving the ability to build a full position in winners.

### Pyramid Up, Never Pyramid Down

- Add to positions **only on strength** — after the stock has already moved in your favour
- Never add to a losing position ("averaging down") — Minervini calls this a "cardinal sin of trading"
- The rationale: averaging down increases exposure in a trade that the market is already telling you is wrong

### Portfolio Sizing Framework

- Typical portfolio: **4–20 positions**; 25% per position at maximum concentration
- Higher concentration (fewer positions) requires higher conviction and tighter risk controls
- At 25% per position with a 10% hard stop, the maximum portfolio drawdown from any single trade is 2.5%
- In difficult markets: increase cash allocation, reduce position count, tighten stops across all existing positions

### Scaling Back During Losing Streaks

When the batting average is falling and losses are mounting:
1. Reduce position size immediately — do not wait for one more trade to "prove" the problem
2. Tighten stops across existing positions
3. Take profits earlier than usual
4. Rebuild size gradually only after 3–5 consecutive profitable trades

Related pages: [Risk Management](../concepts/risk-management.md), [SEPA Strategy](../strategies/sepa-strategy.md)
