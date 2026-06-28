---
type: chart-analysis
status: active
created: 2026-06-28
updated: 2026-06-28
tags: [swing-trading, nse, trend-template, stage-analysis, watchlist]
confidence: medium
sources: ["../../../../analysis1.md", "../../../../data_nse_calculated", "../../../../code/swing_analysis.py"]
---

# NSE Swing Trading Opportunity Scan - 16-Symbol Review

**Analysis date:** 2026-06-28  
**Price data as of:** 2026-06-25  
**Source report:** [analysis1.md](../../../../analysis1.md)  
**Reusable scanner:** [code/swing_analysis.py](../../../../code/swing_analysis.py)  
**Universe:** NIFTYBEES, BANKBEES, MIDCAPETF, HDFCSML250, ICICIBANK, KOTAKBANK, LT, BAJAJHLDNG, GILLETTE, GLAXO, IRFC, ITC, UCOBANK, BANDHANBANK, APOLLOHOSP, EXIDEIND  
**Horizon:** swing trades from a couple of weeks to 1-2 quarters.

This page ingests the generated scan into the durable wiki layer. It is research and education only, not personalized financial advice.

## Method

The scan used 504 trading rows, roughly two years, from `data_nse_calculated/` and combined:

- Stage Analysis.
- Minervini-style 8-point Trend Template.
- 1-month, 3-month, and 6-month momentum.
- 52-week high/low distance.
- 10-day pivot highs/lows.
- ATR14-based entry, stop, and target scenarios.
- 10-day volume versus 50-day volume and 20-day delivery context.

## Ranked Verdicts

| Rank | Symbol | Verdict | Stage | Close | Trend | 1m | 3m | Main monitoring level |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | LT | Strong Setup | Stage 2 markup | 4216.40 | 8/8 | +4.4% | +26.1% | Resistance 4440.00; support 4028.79 |
| 2 | BANDHANBANK | Strong Setup | Stage 2 markup | 201.76 | 8/8 | +0.7% | +36.0% | Resistance 212.48; support 197.66 |
| 3 | MIDCAPETF | Strong Setup | Stage 2 markup | 23.26 | 7/8 | +0.1% | +17.1% | Resistance 23.34; support 22.83 |
| 4 | EXIDEIND | Setup | Stage 1 base / transition | 389.80 | 7/8 | +6.4% | +34.1% | Resistance 409.80; support 366.16 |
| 5 | APOLLOHOSP | Setup | Mixed / transition | 8592.00 | 7/8 | +4.0% | +20.3% | Resistance 8624.00; support 8110.59 |
| 6 | BANKBEES | Setup | Stage 3 topping / repair | 601.92 | 6/8 | +5.8% | +13.2% | Resistance 623.98; support 596.69 |
| 7 | HDFCSML250 | Setup | Stage 1 base / transition | 177.91 | 6/8 | +3.6% | +23.8% | Resistance 180.00; support 170.60 |
| 8 | ICICIBANK | Conditional | Stage 3 topping / repair | 1387.50 | 5/8 | +8.5% | +13.5% | Resistance 1393.10; support 1336.00 |
| 9 | UCOBANK | Avoid | Stage 4 decline | 27.16 | 3/8 | +6.9% | +16.1% | Needs repair above MA150/MA200 |
| 10 | KOTAKBANK | Avoid | Insufficient history | 409.00 | 3/8 | +5.2% | +14.7% | Data discontinuity; post-gap history only |
| 11 | NIFTYBEES | Avoid | Stage 4 decline | 273.43 | 3/8 | +1.0% | +7.2% | Needs reclaim of MA150/MA200 zone |
| 12 | GLAXO | Avoid | Stage 4 decline | 2354.80 | 2/8 | +3.2% | +3.3% | Needs base and MA recovery |
| 13 | BAJAJHLDNG | Avoid | Stage 4 decline | 10599.00 | 1/8 | -1.0% | +15.7% | Needs base and MA200 flattening |
| 14 | GILLETTE | Avoid | Stage 4 decline | 7719.00 | 0/8 | -2.2% | -0.9% | Needs base and MA recovery |
| 15 | ITC | Avoid | Stage 4 decline | 290.00 | 0/8 | -3.9% | -0.2% | Needs base and MA recovery |
| 16 | IRFC | Avoid | Stage 4 decline | 91.77 | 0/8 | -7.6% | +2.6% | Needs base and MA recovery |

## Actionable Monitoring

### Strong Setups

- **LT:** Stage 2 markup and 8/8 Trend Template. Prefer pullback near 4119-4029 or breakout above 4440 with volume. Current-price attempt had weaker R:R than the pullback scenario.
- **BANDHANBANK:** Stage 2 markup and 8/8 Trend Template. Local data file is `BANDHANBNK.csv`. Watch support near 197.66 and breakout trigger above 212.48.
- **MIDCAPETF:** Stage 2 markup and 7/8 Trend Template. Watch support near 22.83 and breakout above 23.34; liquidity/volume confirmation matters because recent volume was below the 50-day average.

### Setups / Conditional

- **EXIDEIND:** Base/transition with 7/8 Trend Template. Prefer pullback near 376.78-366.16 or breakout above 409.80 only with confirmation.
- **APOLLOHOSP:** Mixed transition with strong momentum and price near 52-week high. Current R:R is weak; pullback near 8429-8111 is cleaner than chasing.
- **BANKBEES:** Upgraded from earlier conditional monitoring to Setup, but stage remains repair/topping. Watch 596.69 support and 623.98 breakout.
- **HDFCSML250:** Stage 1 base/transition with improving trend. Watch support near 170.60 and breakout above 180.00.
- **ICICIBANK:** Conditional. Momentum is strong, but MA stack is not fully aligned. Watch breakout above 1393.10 and support near 1336.00.

## Avoid / Review Later

- **NIFTYBEES:** Downgraded from earlier conditional monitoring to Avoid because the scanner classified it as Stage 4 decline with only 3/8 Trend Template alignment as of 2026-06-25. Re-evaluate after it reclaims MA150/MA200 or forms a cleaner base.
- **BAJAJHLDNG:** Existing watchlist row should be softened to Avoid / long check-back; trend remains Stage 4 with 1/8 Trend Template.
- **UCOBANK, GLAXO, GILLETTE, ITC, IRFC:** Not added as active swing candidates. Watch only after base-building and moving-average repair.
- **KOTAKBANK:** Avoid for this scan because the local file has an unadjusted price discontinuity on 2026-01-14. The scanner used only 109 post-gap bars, so long moving-average confidence is low.

## Data Notes

- `BANDHANBANK` was resolved to the local file `BANDHANBNK.csv`.
- KOTAKBANK had a large price discontinuity: 2026-01-13 close 2132.60 to 2026-01-14 close 421.00, a -80.3% move. The scan treated this as unadjusted data and used post-gap bars only.
- All market-sensitive claims are as of the dataset date, 2026-06-25.

## Watchlist Updates

Updated [watchlist](../../../watchlist.md) entries from this ingest:

- Added LT, BANDHANBANK, MIDCAPETF, EXIDEIND, APOLLOHOSP, HDFCSML250, and ICICIBANK.
- Updated BANKBEES from conditional/recovering to Setup/Stage 3 repair.
- Downgraded NIFTYBEES from Conditional to Avoid.
- Downgraded BAJAJHLDNG from Watchlist to Avoid.

## Related Pages

- [Stage Analysis](../../../concepts/stage-analysis.md)
- [Trend Template](../../../concepts/trend-template.md)
- [Moving Averages](../../../indicators/moving-averages.md)
- [Average True Range](../../../indicators/average-true-range.md)
- [Volume Analysis](../../../concepts/volume-analysis.md)
