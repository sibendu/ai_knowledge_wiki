---
type: chart-analysis
status: active
created: 2026-07-03
updated: 2026-07-03
tags: [swing-trading, etf, scan, stage-analysis, trend-template, nse]
sources: [data_nse_calculated]
confidence: medium
---

# ETF Swing Scan — 23 Symbols (2026-07-03)

**Scanner:** `code/swing_analysis.py`
**Data as of:** 2026-07-03
**Lookback:** 504 trading rows (~2 years)
**Universe:** 23 NSE ETFs (SBISENSEX.BO not in data; 22 symbols scanned)
**Posture:** research and education only; not personalized financial advice.

---

## Summary Table

| Rank | Symbol | Rating | Stage | TT | Close | 52wH dist | 1m | 3m |
|---:|---|---|---|---:|---:|---:|---:|---:|
| 1 | MONQ50 | **Strong Setup** | Stage 2 markup | 8/8 | 147.09 | -0.1% | +1.5% | +40.7% |
| 2 | MIDCAPETF | **Strong Setup** | Stage 2 markup | 7/8 | 23.41 | -2.3% | +3.2% | +15.4% |
| 3 | HDFCSML250 | **Setup** | Mixed / transition | 7/8 | 181.46 | -0.9% | +6.4% | +21.7% |
| 4 | MOSMALL250 | **Setup** | Mixed / transition | 7/8 | 18.07 | -6.8% | +6.0% | +21.4% |
| 5 | MOALPHA50 | **Setup** | Stage 1 base / transition | 7/8 | 53.09 | -5.1% | +2.2% | +16.5% |
| 6 | BANKBEES | **Setup** | Stage 3 topping / repair | 6/8 | 600.12 | -6.1% | +7.2% | +12.5% |
| 7 | JUNIORBEES | **Setup** | Stage 1 base / transition | 6/8 | 780.71 | -2.2% | +3.6% | +16.6% |
| 8 | NEXT50IETF | **Setup** | Stage 1 base / transition | 6/8 | 76.14 | -2.6% | +3.3% | +16.1% |
| 9 | ALPHA | **Setup** | Stage 1 base / transition | 6/8 | 51.36 | -4.2% | +2.9% | +16.5% |
| 10 | ICICIB22 | **Conditional** | Stage 1 base / transition | 5/8 | 118.77 | -9.3% | +0.3% | +1.8% |
| 11 | MON100 | **Watchlist** | Stage 2 markup | 7/8 | 332.78 | -2.9% | -1.9% | +39.5% |
| 12 | MASPTOP50 | **Watchlist** | Mixed / transition | 6/8 | 77.78 | -6.0% | -5.6% | +15.4% |
| 13 | MAFANG | **Watchlist** | Mixed / transition | 6/8 | 190.81 | -8.4% | -8.4% | +27.4% |
| 14 | SETFGOLD | **Watchlist** | Stage 3 topping / repair | 5/8 | 124.17 | -19.3% | -5.7% | -2.5% |
| 15 | HDFCGOLD | **Watchlist** | Stage 3 topping / repair | 5/8 | 124.29 | -18.4% | -5.8% | -2.4% |
| 16 | SBISILVER | **Watchlist** | Stage 3 topping / repair | 4/8 | 226.63 | -37.4% | -10.3% | -1.4% |
| 17 | HDFCMOMENT | **Watchlist** | Stage 1 base / transition | 3/8 | 30.82 | -7.3% | +1.1% | +8.5% |
| 18 | CPSEETF | **Watchlist** | Stage 1 base / transition | 3/8 | 97.42 | -13.0% | -3.2% | -4.0% |
| 19 | MOMENTUM | **Watchlist** | Stage 1 base / transition | 2/8 | 30.88 | -6.4% | +2.6% | +9.0% |
| 20 | NIFTYBEES | **Avoid** | Stage 4 decline | 3/8 | 275.91 | -8.7% | +3.9% | +7.2% |
| 21 | NIFTYIETF | **Avoid** | Stage 4 decline | 3/8 | 274.47 | -16.4% | +3.9% | +7.2% |
| 22 | MAHKTECH | **Avoid** | Stage 4 decline | 0/8 | 21.75 | -38.9% | -10.1% | -6.2% |

---

## Actionable Setups

### MONQ50 — Strong Setup (high confidence)

- **Stage:** Stage 2 markup. **TT:** 8/8. MA50 137.19 < MA150 112.87; all MA slope positive.
- **Momentum:** 1m +1.5%, 3m +40.7%, 6m +48.0%. Within 0.1% of 52-week high (147.24).
- **Key levels:** support 137.28 (recent swing low 2026-06-12), resistance/52w high 147.24, ATR14 1.66.
- **Volume:** 1.26x recent vs 50d average; delivery +97.0%.
- **Scenarios:**
  - Pullback: entry 145.10, stop 142.61, target 150.08 → **R:R 2.0:1**
  - Breakout: entry 148.56, stop 145.10, target 154.54 → R:R 1.7:1
  - Current price: entry 147.09, stop 137.28 → R:R only 0.4:1 (wide stop; avoid current-price entry)
- **Invalidation:** close below 137.28 on expanding volume.
- **Check-back:** 2026-07-17

### MIDCAPETF — Strong Setup (high confidence) [position already open]

- **Stage:** Stage 2 markup. **TT:** 7/8 (misses: ≥25% above 52w low). MA50 22.92 rising.
- **Momentum:** 1m +3.2%, 3m +15.4%. 52w high 23.96 (-2.3% away).
- **Key levels:** support 22.92 (MA50), resistance 23.61 / 52w high 23.96, ATR14 0.48.
- **Volume:** 0.89x (soft); delivery +71.1%.
- **Scenarios:**
  - Pullback: entry 22.92, stop 22.20, target 24.28 → **R:R 1.9:1**
  - Breakout: entry 23.68, stop 22.92, target 24.88 → R:R 1.6:1
- **Note:** Existing position opened 2026-07-01 at 23.32. Stop is 22.60, target 24.40. Fresh entries at pullback to MA50 zone.
- **Invalidation:** close below 22.92 on expanding volume.
- **Check-back:** 2026-07-17

### HDFCSML250 — Setup (high confidence)

- **Stage:** Mixed / transition. **TT:** 7/8 (misses: MA150 > MA200). 52w high 183.18.
- **Momentum:** 1m +6.4%, 3m +21.7%, 6m +9.2%.
- **Key levels:** support 172.13 (MA50), resistance 183.18 (52w high), ATR14 2.73.
- **Volume:** 0.89x; delivery +66.3%.
- **Scenarios:**
  - Pullback: entry 178.19, stop 174.10, target 186.37 → **R:R 2.0:1**
  - Breakout: entry 183.73, stop 178.19, target 190.55 → R:R 1.2:1
- **Note:** Also flagged in 2026-06-28 scan. Stage upgraded to mixed/transition with improving MA alignment.
- **Invalidation:** close below 172.13 on expanding volume.
- **Check-back:** 2026-07-17

### MOSMALL250 — Setup (high confidence)

- **Stage:** Mixed / transition. **TT:** 7/8 (misses: MA150 > MA200).
- **Momentum:** 1m +6.0%, 3m +21.4%. 52w high 19.38 (-6.8% away).
- **Key levels:** support 17.16 (MA50), resistance 19.18 (recent swing high), ATR14 0.37.
- **Volume:** 1.37x (elevated); delivery +67.9%.
- **Scenarios:**
  - Pullback: entry 17.62, stop 17.06, target 19.18 → **R:R 2.8:1**
  - Current price: entry 18.07, stop 17.16, target 19.18 → R:R 1.2:1
- **Invalidation:** close below 17.16 on expanding volume.
- **Check-back:** 2026-07-17

### MOALPHA50 — Setup (high confidence)

- **Stage:** Stage 1 base / transition (242 rows of data — shorter history). **TT:** 7/8.
- **Momentum:** 1m +2.2%, 3m +16.5%, 6m +5.6%. 52w high 55.97 (-5.1% away).
- **Key levels:** support 52.19 (MA50), resistance 54.00 (recent pivot), ATR14 0.91.
- **Volume:** 1.96x (strong participation); delivery +64.7%.
- **Scenarios:**
  - Pullback: entry 52.19, stop 50.82, target 54.74 → **R:R 1.9:1**
  - Current price: entry 53.09, stop 51.72, target 55.38 → R:R 1.7:1
- **Invalidation:** close below 52.19 on expanding volume.
- **Check-back:** 2026-07-17

### BANKBEES — Setup (medium confidence) [previously flagged]

- **Stage:** Stage 3 topping / repair (caution: MA50 < MA150). **TT:** 6/8.
- **Momentum:** 1m +7.2%, 3m +12.5%. 52w high 638.99 (-6.1% away).
- **Key levels:** support 596.69, resistance 623.98, ATR14 10.08.
- **Volume:** 0.81x; delivery +56.2%.
- **Scenarios:**
  - Pullback: entry 596.69, stop 581.57, target 623.98 → **R:R 1.8:1**
  - Current price: entry 600.12, stop 585.00, target 625.32 → R:R 1.7:1
- **Note:** Stage 3 tag is a risk flag; strong volume on a breakout above 623.98 would upgrade confidence.
- **Invalidation:** close below 596.69 on expanding volume.
- **Check-back:** 2026-07-17

### JUNIORBEES — Setup (medium confidence)

- **Stage:** Stage 1 base / transition. **TT:** 6/8.
- **Momentum:** 1m +3.6%, 3m +16.6%. 52w high 798.07 (-2.2% away).
- **Key levels:** support 762.86 (MA50), resistance 780.89 (recent swing high), 52w high 798.07, ATR14 12.51.
- **Scenarios:**
  - Pullback: entry 765.70, stop 746.94, target 803.23 → **R:R 2.0:1**
  - Breakout: entry 788.52, stop 765.70, target 819.79 → R:R 1.4:1
- **Invalidation:** close below 762.86 on expanding volume.
- **Check-back:** 2026-07-17

### NEXT50IETF — Setup (medium confidence)

- **Stage:** Stage 1 base / transition. **TT:** 6/8. Closely tracks JUNIORBEES/Nifty Next 50.
- **Momentum:** 1m +3.3%, 3m +16.1%. 52w high 78.19 (-2.6% away).
- **Key levels:** support 74.51 (MA50), resistance 76.54, 52w high 78.19, ATR14 1.35.
- **Scenarios:**
  - Pullback: entry 74.52, stop 72.50, target 78.57 → **R:R 2.0:1**
  - Breakout: entry 76.90, stop 74.52, target 80.27 → R:R 1.4:1
- **Note:** Very similar structure to JUNIORBEES; avoid holding both unless diversification by fund house is intentional.
- **Invalidation:** close below 74.51 on expanding volume.
- **Check-back:** 2026-07-17

### ALPHA — Setup (medium confidence)

- **Stage:** Stage 1 base / transition. **TT:** 6/8.
- **Momentum:** 1m +2.9%, 3m +16.5%. 52w high 53.60 (-4.2% away).
- **Key levels:** support 50.23 (MA50), resistance 52.59 (recent pivot), 52w high 53.60, ATR14 0.98.
- **Scenarios:**
  - Pullback: entry 50.23, stop 48.77, target 53.12 → **R:R 2.0:1**
  - Current price: entry 51.36, stop 49.89, target 53.81 → R:R 1.7:1
- **Invalidation:** close below 50.23 on expanding volume.
- **Check-back:** 2026-07-17

---

## Conditional Setup

### ICICIB22 — Conditional (medium confidence)

- **Stage:** Stage 1 base / transition. **TT:** 5/8 — price is below MA50 and MA150 (below both short-term MAs).
- **Momentum:** 1m +0.3%, 3m +1.8% — flat. 52w high 131.00 (-9.3% away).
- **Key levels:** support 116.14 (recent swing low), resistance 123.24, ATR14 1.95.
- **Condition:** Enter only on a close above MA50 (121.00) or reclaim of MA150 (119.99) on volume ≥1.5x.
- **Scenarios:**
  - Pullback: entry 116.43, stop 113.50, target 123.24 → **R:R 2.3:1** (if support holds)
  - Current price: entry 118.77, stop 115.84, target 123.65 → R:R 1.7:1
- **Invalidation:** close below 116.14 on expanding volume.
- **Check-back:** 2026-07-26

---

## Watchlist (Monitor — Not Actionable Now)

| Symbol | Stage | TT | Note | Check-back |
|---|---|---:|---|---|
| MON100 | Stage 2 markup | 7/8 | Strong 3m/6m momentum but 1m negative (-1.9%); needs 1m momentum to recover | 2026-07-17 |
| MASPTOP50 | Mixed / transition | 6/8 | 1m -5.6% pullback from 52w high; watch for support at MA50 79.31 | 2026-07-17 |
| MAFANG | Mixed / transition | 6/8 | 1m -8.4% pullback from 52w high 208.38; support at MA50/MA150 ~173-191 | 2026-07-17 |
| SETFGOLD | Stage 3 topping | 5/8 | -19.3% from 52w high; gold correcting; monitor weekly closes | 2026-08-07 |
| HDFCGOLD | Stage 3 topping | 5/8 | Mirrors SETFGOLD; -18.4% from 52w high 152.30 | 2026-08-07 |
| SBISILVER | Stage 3 topping | 4/8 | -37.4% from 52w high 362.00; extremely volatile; no setup | 2026-08-07 |
| HDFCMOMENT | Stage 1 base | 3/8 | Only 1 of 3 MA tests pass; below MA150/MA200 | 2026-08-07 |
| CPSEETF | Stage 1 base | 3/8 | Price below all three MAs; 1m -3.2%; needs base repair | 2026-08-07 |
| MOMENTUM | Stage 1 base | 2/8 | Only 2/8 trend criteria met; MA structure deteriorating | 2026-08-07 |

---

## Avoid

| Symbol | Stage | TT | Reason |
|---|---|---:|---|
| NIFTYBEES | Stage 4 decline | 3/8 | Below MA150/MA200; MA200 slope negative; broad market index ETF in structural decline |
| NIFTYIETF | Stage 4 decline | 3/8 | Mirrors NIFTYBEES; -16.4% from 52w high |
| MAHKTECH | Stage 4 decline | 0/8 | All 8 trend criteria fail; -38.9% from 52w high; -14.6% in 6m |

---

## Cross-Scan Observations

1. **Small-cap and mid-cap ETFs dominate setups.** MONQ50, MIDCAPETF, HDFCSML250, MOSMALL250, MOALPHA50, JUNIORBEES, NEXT50IETF all ranked Setup or above. The broad Nifty (NIFTYBEES, NIFTYIETF) remains in Stage 4 — relative strength is clearly in the smaller-cap segments.

2. **US-linked thematic ETFs (MAFANG, MON100, MASPTOP50, MAHKTECH) are mixed.** MON100 (Nasdaq 100 proxy) is Stage 2 with strong 3m/6m gains but 1m negative — pulling back from a recent high. MAFANG pulled back harder (-8.4% 1m). MAHKTECH is a full Stage 4 avoid.

3. **Gold and silver ETFs are in Stage 3 topping/repair.** Both SETFGOLD and HDFCGOLD are ~19% below their January 2026 highs (SETFGOLD hit 153.95, HDFCGOLD hit 152.30 on 2026-01-29). SBISILVER is -37% from its January spike high of 362.00. Not actionable for long swing trades now.

4. **PSU/infrastructure ETF (CPSEETF) remains weak.** Below all MAs. Avoid.

5. **Momentum factor ETFs (HDFCMOMENT, MOMENTUM) are lagging.** Only 2-3/8 trend criteria. Ironic given their factor — they hold stocks that were in momentum, but recent rotation has hurt them.

6. **Duplication risk:** JUNIORBEES and NEXT50IETF track the same index (Nifty Next 50); HDFCSML250 and MOSMALL250 track similar small-cap indices. Treat each pair as one position decision.

---

## Missing Symbol

- **SBISENSEX.BO** — no data file found in `data_nse_calculated/`. Not scanned.
