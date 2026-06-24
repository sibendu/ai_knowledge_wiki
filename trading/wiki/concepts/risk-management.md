---
type: concept
status: active
created: 2026-06-13
updated: 2026-06-24
tags: [risk, drawdown, exposure, livermore, stop-loss, trade-management]
sources:
  - ../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md
  - ../source-notes/2026-06-19-reminiscences-of-a-stock-operator.md
  - ../source-notes/2026-06-24-technical-analysis-for-dummies.md
confidence: medium
---

# Risk Management

Risk management is the discipline of keeping losses small enough that future valid opportunities can still be taken.

## Livermore Notes

In [How to Trade in Stocks](../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md), Livermore emphasizes capital preservation more than prediction. His risk-management rules include:

- Do not average down.
- Treat a margin call as evidence that the position is wrong.
- Risk only a limited amount of capital on any one venture.
- Decide the acceptable loss before making the commitment.
- Avoid overtrading, especially when broker incentives encourage activity.
- Take some realized profits out of the trading account after successful campaigns.

## Practical Translation

- Every setup needs pre-defined invalidation.
- Every strategy should specify maximum loss per trade and per campaign.
- Losing trades should reduce or end exposure, not invite larger exposure.
- Profit withdrawal is partly psychological: it turns account marks into real capital and reduces the urge to keep pressing.

## Questions To Build Out

- What is the maximum acceptable loss per trade, day, week, and strategy?
- How should risk limits change across market regimes?
- What evidence supports each risk rule?

## Source Notes

- [How to Trade in Stocks - Jesse L. Livermore](../source-notes/2026-06-13-how-to-trade-in-stocks-jesse-livermore.md)

## Notes From Trade Like a Stock Market Wizard (Minervini, 2013)

As of publication date 2013. Source: [Trade Like a Stock Market Wizard](../source-notes/2026-06-18-trade-like-a-stock-market-wizard.md).

### Stop-Loss Rules

- Hard maximum: 10% below purchase price — the most important rule, never violated
- Ideal stop: ≤50% of expected average gain (e.g., if average winning trade is 15%, maximum stop is 7.5%)
- Stop location is determined and written down **before** entry — executing after the fact leads to rationalisation and larger losses
- When triggered: execute without hesitation; take the next bid if the stock gaps through the stop
- Raise stop to breakeven once the position is up 3× the initial risk amount
- When up 2–3× initial risk, begin looking for exit opportunities (not automatically selling, but watching closely)

### Win/Loss Ratio and Expectancy Math

Minervini frames risk management mathematically around **batting average** (win rate) and **win/loss ratio** (average gain ÷ average loss):

| Batting average | Viable win/loss ratio | Notes |
|-----------------|----------------------|-------|
| 30% | Not viable at any practical ratio | Negative expectancy regardless |
| 40% | Minimum ~2:1 | 20% average gain / 10% average loss |
| 50% | Optimal ~2:1 | Can use up to 48%/24% at 50% win rate |
| Any | Never let loss exceed average gain | The cardinal rule |

At a 3:1 win/loss ratio, profitable results are achievable with only 40% winning trades. The practical implication: **cutting losses quickly and letting winners run** is the mechanical key to positive expectancy, even with a sub-50% win rate.

### Managing Difficult Markets

- Reduce position size (e.g., from 5,000 to 2,000 or 1,000 shares)
- Tighten stops: if normally 7–8%, cut to 5–6%
- Take smaller profits: if normally 15–20% target, exit at 10–12%
- Exit all margin positions immediately during confirmed market deterioration
- Scale back gradually until results improve; then restore size incrementally
- **Do not increase size to recoup losses** — this accelerates the drawdown

## Five-Step Trading Plan (TA4D, 2020)

Source: [TA4D](../source-notes/2026-06-24-technical-analysis-for-dummies.md), Chapter 5.

1. **Determine whether a trend exists** — trend-following indicators are unreliable without a trend; no trend = no trade
2. **Establish entry rules** — entry timing matters as much as security selection; getting in at the right price sets the ceiling on ultimate profit
3. **Manage money at risk by scaling** — add to winning positions, reduce losers; the most profitable futures managers cite this as most important
4. **Establish exit rules — set stops and targets** — paramount for anyone moving from buy-and-hold thinking; you must know your stop before entering
5. **Establish a reentry rule** — after being stopped out in an ongoing macro trend, reentry rules are different from fresh entries; already-trending security has different context

## Stop-Loss Types (TA4D, 2020)

Source: [TA4D](../source-notes/2026-06-24-technical-analysis-for-dummies.md), Chapter 5.

| Stop Type | Description | Verdict |
|-----------|-------------|---------|
| Mental stop | "I'll sell in my head when it hits X" | Avoid — proven self-delusion; almost never executed properly |
| Hard stop | Order placed with broker at entry | Mandatory minimum |
| Trailing stop | Moves in direction of trade; locks in gains | Good for trend following |
| Parabolic SAR | Accelerates and tightens as trend matures | Good for exits in maturing moves |
| ATR-based stop | Entry ± (ATR × multiplier); adapts to volatility | Best practice for stop sizing |

## Recovery Table

A 50% loss requires a 100% gain to recover. (source: TA4D 2020)

| Loss | Gain Needed to Recover |
|------|----------------------|
| 10% | 11.1% |
| 20% | 25.0% |
| 30% | 42.9% |
| 40% | 66.7% |
| 50% | 100.0% |
| 75% | 300.0% |

See [Average True Range](../indicators/average-true-range.md) for ATR-based stop construction.

Related pages: [Position Sizing](../concepts/position-sizing.md), [SEPA Strategy](../strategies/sepa-strategy.md), [Stage Analysis](../concepts/stage-analysis.md)

## Notes From Reminiscences of a Stock Operator (LeFevre, 1923)

Source: [Reminiscences of a Stock Operator](../source-notes/2026-06-19-reminiscences-of-a-stock-operator.md). These 1923-narrative observations predate and motivate the explicit rules in Livermore's 1940 book.

### Probe Before Committing (Exploratory Sizing)

Never put on the full line at once. Commit roughly **one-fifth** of the intended position as an exploratory bet; add only if it shows a profit. "If that does not show him a profit he must not increase his holdings because he has obviously begun wrong." The small probe losses are a cheap, deliberate cost of confirming the timing — Livermore would "chip out fifty or sixty thousand dollars in these feeling-out plays" and earn it back quickly once the real move started. This is the structural reason the method has **positive expectancy**: the big bet is only down when you are winning, and losses are confined to small exploratory bets.

### Always Sell the Loser, Keep the Winner

"Always sell what shows you a loss and keep what shows you a profit." The book's most painful illustration: under Percy Thomas's influence, Livermore sold his *profitable* wheat (forgoing ~$8M) and held — even added to — his *losing* cotton, eventually accumulating 440,000 bales before being nearly wiped out. **Averaging a losing game** is named "among the greatest of all speculative blunders."

### The "Sleeping Point" (Size to Your Composure)

Dickson G. Watts's anecdote, quoted approvingly: a man who could not sleep for worrying about his cotton was advised to "sell down to the sleeping point." Position size should be small enough that the trader can think and act clearly; an oversized position corrupts judgment.

### Don't Make the Market Pay a Bill

Trying to force the market to produce a specific sum by a specific date ("making the stock market pay for an overcoat") converts speculation into pure gambling — it forces an immediate-profit demand that removes patience and the line-of-least-resistance discipline. Livermore calls this resolve "the busiest and most persistent" of Wall Street hoodoos.
