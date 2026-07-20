---
type: chart-analysis
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [swing-scan, data-analysis, deep-vcp-livermore, one-year-outlook]
symbols: [LT]
method: deep-vcp-livermore
confidence: medium
---

# 2026-07-20 LT Deep 1-Year Legendary-Investor Scan

**Data as of:** 2026-07-14  
**Lookback:** 252 trading rows, roughly 1 year  
**Requested outlook period:** 1 year  
**Verdict:** Watchlist / wait for repair

## Summary

| Symbol | Rating | Deep Rating | Stage | Close | Trend Template | VCP | Livermore | 1-Year Posture |
|---|---|---|---|---:|---:|---|---|---|
| LT | Watchlist | Early Stage / Watch | Stage 1 base / transition | 3848.70 | 3/8 | Yes, 3 contractions | Neutral | Watch only until price reclaims key moving averages and confirms strength above resistance |

The scanner finds a possible VCP trace in LT, but the broader legendary-investor framework is not aligned yet. Stage Analysis says the stock is in a Stage 1 base / transition rather than a confirmed Stage 2 advance. The Minervini-style Trend Template is only 3/8, with price below MA50, MA150, and MA200. Livermore is neutral, not giving a clear pivotal-point continuation signal. SEPA extension is also weak because LT is below MA10/MA20 and MA50 is not rising over 5 days.

For a 1-year outlook, LT belongs on the watchlist rather than in an active buy zone. The constructive path is base repair, reclaim of the major moving averages, and then a high-quality breakout above the 4128-4272 resistance/pivot zone. A close below 3847 with expanding volume would weaken the base and argue against fresh swing exposure.

# NSE Swing Trading Opportunity Scan

**Generated:** 2026-07-20
**Price data as of:** 2026-07-14
**Lookback:** last 252 trading rows, roughly 1.0 years.
**Horizon:** short-term swing trades from a couple of weeks to 1-2 quarters.
**Posture:** research and education only; not personalized financial advice.

## Method

The scan combines Stage Analysis, a Minervini-style 8-point Trend Template, 1/3/6-month momentum, 52-week distance, recent pivots, ATR-based risk levels, and volume/delivery context. Ratings are mechanical research labels, not trade instructions.

**Deep mode enabled:** also evaluates VCP (Volatility Contraction Pattern), Livermore pivotal points, and extended SEPA criteria per symbol.

## Ranked Summary

| Rank | Symbol | Rating | Deep Rating | Stage | Close | 52wH dist | Trend | 1m | 3m | VCP | Livermore |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | LT | **Watchlist** | Early Stage / Watch | Stage 1 base / transition | 3848.70 | -13.3% | 3/8 | -5.0% | -2.7% | Yes | neutral |

## Actionable Watchlist

- No symbols met the mechanical setup threshold.

## Per-Symbol Analysis

### LT - Watchlist

- **As-of:** 2026-07-14; **confidence:** low.
- **Rows used:** 252 after data-quality filtering.
- **Stage:** Stage 1 base / transition.
- **Trend Template:** 3/8.
- **Momentum:** 1m -5.0%, 3m -2.7%, 6m -7.4%.
- **Moving averages:** MA50 4015.03, MA150 3981.00, MA200 3955.59, MA200 1m slope +1.4%.
- **Key levels:** support 3847.00, resistance 4128.00, 52w high 4440.00, 52w low 3288.10, ATR14 76.54.
- **Participation:** 10d volume vs 50d volume 0.96x; 20d avg delivery +54.7%.

**Recent pivots:**
- L 2026-01-23 @ 3720.10, H 2026-02-24 @ 4440.00, L 2026-03-23 @ 3288.10, H 2026-04-16 @ 4149.00, L 2026-05-12 @ 3847.00, H 2026-05-29 @ 4128.00, L 2026-06-11 @ 3854.40, H 2026-06-25 @ 4272.30

**Scenarios:**
- Current-price attempt: entry 3848.70, stop 3733.90, target 4128.00, R:R 2.4:1
- Pullback attempt: entry 3847.00, stop 3732.20, target 4128.00, R:R 2.4:1
- Breakout attempt: entry 4140.38, stop 3847.00, target 4331.72, R:R 0.7:1

**Invalidation / risk controls:**
- Avoid fresh swing exposure if price closes below 3847.00 with expanding volume, or if the broader index ETF cohort breaks below its MA50/MA150 area.
- Treat ATR stops as research levels; actual position sizing should cap loss per trade before entry.

**Trend checks:**
- price > MA50: no
- price > MA150: no
- price > MA200: no
- MA50 > MA150: yes
- MA150 > MA200: yes
- >=25% above 52w low: no
- within 25% of 52w high: yes
- 1m momentum positive: no

**Deep Analysis (VCP / Livermore / SEPA):**

- **Deep Rating:** Early Stage / Watch
- **VCP Detected:** Yes (3 contractions, tight=True, volume dryup=0.96x)
  - Pivot line (breakout trigger): 4272.30 (2026-06-25)
  - Swing 3: depth 7.5%, ratio 0.69 (2025-11-27 high 4140.00 / 2025-11-07 low 3831.10)
  - Swing 4: depth 4.0%, ratio 0.53 (2025-12-12 high 4114.00 / 2025-12-09 low 3949.10)
  - Swing 8: depth 3.9%, ratio 0.19 (2026-05-04 high 4139.50 / 2026-04-23 low 3978.50)
- **Livermore Signal:** neutral (correction from 50d high: -9.9%, 20d range: +11.2%)
- **SEPA Extended:** above MA10=no, above MA20=no, MA50 rising 5d=no (-0.4%), MA150 rising 20d=yes (+0.3%)

## Reuse Notes

Reusable script: `code/swing_analysis.py`.

Example command:

```powershell
.venv\Scripts\python.exe code\swing_analysis.py --data-dir data_nse_calculated --symbols NIFTYBEES BANKBEES MIDCAPETF HDFCSML250 ICICIBANK KOTAKBANK LT BAJAJHLDNG GILLETTE GLAXO IRFC ITC UCOBANK BANDHANBANK APOLLOHOSP EXIDEIND --output analysis1.md
```
