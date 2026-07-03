---
type: chart-analysis
status: active
created: 2026-07-03
updated: 2026-07-03
tags: [swing-trading, etf, vcp, pivotal-point, stage-analysis, trend-template, sepa, livermore, minervini, nse]
sources: [data_nse_calculated]
confidence: medium
---

# ETF Swing Deep Analysis — 23 Symbols (2026-07-03)

**Method:** Stage Analysis + Minervini Trend Template + VCP contraction measurement + Livermore Pivotal Points + SEPA filtering  
**Data as of:** 2026-07-03 | **Lookback:** 1 year (252 bars)  
**Universe:** 22 of 23 NSE ETFs (SBISENSEX.BO missing from data)  
**Posture:** research and education only; not personalized financial advice.

---

## Framework Applied

### Minervini SEPA / VCP
A **Volatility Contraction Pattern** requires:
1. Price range contracting in successive swings (each correction smaller than the prior)
2. Volume contracting during the base formation
3. An identifiable **pivot point** — the high of the last tight consolidation before a breakout
4. At least 2 (ideally 3+) identifiable price contractions

### Livermore Pivotal Points
Key natural pivots are tracked: prior highs, prior lows, reaction points where price reversed. The **pivotal buy point** is the breakout above the last pivot high on expanding volume. The **pivotal stop** sits just below the last pivot low.

### Stage Analysis (Weinstein/Minervini)
- Stage 1: Flat base, MA200 flattening
- Stage 2: Markup, MA50 > MA150 > MA200, price above all MAs
- Stage 3: Topping/distribution, MAs starting to cross down
- Stage 4: Decline, price below all MAs

---

## Ranked Summary

| Rank | Symbol | Rating | Stage | TT | VCP | Livermore Pivot | Close | 52wH dist |
|---:|---|---|---|---:|---|---|---:|---:|
| 1 | **MONQ50** | Strong Setup | Stage 2 | 8/8 | 3-contraction VCP forming | Pivotal High 147.24 | 147.09 | -0.1% |
| 2 | **MIDCAPETF** | Strong Setup | Stage 2 | 7/8 | Vol contracting base | Pivot 23.96, support 22.92 | 23.41 | -2.3% |
| 3 | **JUNIORBEES** | Setup | Stage 1→2 | 6/8 | Tightening range 8.2% | Pivot 798.07 (hit 2026-07-03) | 780.71 | -2.2% |
| 4 | **NEXT50IETF** | Setup | Stage 1→2 | 6/8 | Range 7.8%, vol stabilising | Pivot 78.19 (hit 2026-07-03) | 76.14 | -2.6% |
| 5 | **HDFCSML250** | Setup | Mixed | 7/8 | Vol contracting, range 9.5% | Pivot 183.18 (52w high) | 181.46 | -0.9% |
| 6 | **MOSMALL250** | Setup | Mixed | 7/8 | Range expanding (15.3%), vol elevated | Pivot 19.18 broken, now 19.38 | 18.07 | -6.8% |
| 7 | **MOALPHA50** | Setup | Stage 1→2 | 7/8 | Range 10.9%, very low volume | Pivot 55.97, support 52.19 | 53.09 | -5.1% |
| 8 | **ALPHA** | Setup | Stage 1→2 | 6/8 | Range contracting 8.4% | Pivot 53.60, support 50.23 | 51.36 | -4.2% |
| 9 | **BANKBEES** | Setup | Stage 3 | 6/8 | Range re-expanding (13.2%) | Stage 3 risk; pivot 623.98 | 600.12 | -6.1% |
| 10 | **MON100** | Watchlist | Stage 2 | 7/8 | Tight 8.6%, but -1.9% 1m | Pivot 342.55 (52w high, 2026-06-05) | 332.78 | -2.9% |
| 11 | **MASPTOP50** | Watchlist | Mixed | 6/8 | Range widening (10.0%), below MA50 | Pivot 82.78; pulled back through MA50 | 77.78 | -6.0% |
| 12 | **MAFANG** | Watchlist | Mixed | 6/8 | Range 13%, vol very low | Pivot 208.38; -8.4% pullback | 190.81 | -8.4% |

---

## Tier 1 — Highest-Priority Setups

### 1. MONQ50 — Strong Setup | Stage 2 | TT 8/8 | VCP Active

**As-of:** 2026-07-03 | **Confidence:** high

#### Stage and Trend Template
All 8/8 Trend Template criteria pass:
- Price > MA50 (147.09 > 137.19) ✓
- Price > MA150 (147.09 > 112.87) ✓
- Price > MA200 (147.09 > 108.98) ✓
- MA50 > MA150 (137.19 > 112.87) ✓
- MA150 > MA200 (112.87 > 108.98) ✓
- ≥25% above 52w low (72.97 × 1.25 = 91.21 — current 147 is far above) ✓
- Within 25% of 52w high (147.24 × 0.75 = 110.43 — current 147 is within) ✓
- 1-month momentum positive (+1.5%) ✓

MA200 monthly slope: **+6.6%** — very strong, consistent Stage 2.

#### VCP Analysis (Minervini)
Price range contractions measured over 20-bar windows in the last 100 bars:
- Window 1 (Feb 04 – Mar 04): **9.3%** range
- Window 2 (Mar 05 – Apr 06): **20.3%** (April tariff shock — range widened)
- Window 3 (Apr 07 – May 06): **17.8%** (recovery)
- Window 4 (May 07 – Jun 04): **12.2%** (contracting)
- Window 5 (Jun 05 – Jul 03): **7.3%** ← tightest window — VCP terminal contraction

**VCP verdict:** The last 20 bars show a textbook terminal tightening. After the April tariff-shock expansion (20%), range has successively contracted: 17.8% → 12.2% → 7.3%. This is a 3-contraction VCP.

#### Volume Analysis
- 10d/50d volume ratio: **1.26x** (elevated, above 1.0)
- Volume in the last tight phase (Jun 22 – Jul 03): daily volumes 16K–167K, with a high-volume expansion spike on 2026-07-02 (166K) when price hit the new high 147.24
- Delivery: +97% — very high institutional participation

**Volume verdict:** Volume contracted during the June 12–22 base period, then expanded sharply on Jul 02 when price hit the 52w high. This is the VCP signature: quiet base → volume surge on breakout attempt.

#### Livermore Pivotal Points
Key recent pivots (from scanner):
- H 2026-02-23 @ 101.89 → L 2026-03-20 @ 92.01 ← base pivot low
- H 2026-06-08 @ 147.03 ← **prior pivot high** (first attempt at new high)
- L 2026-06-12 @ 137.28 ← **pivot low / stop anchor**
- H 2026-07-02 @ **147.24** ← new 52w high — **current pivotal breakout level**

**Livermore interpretation:** The Jul 02 print of 147.24 is the first new 52-week high in the current rally. Livermore's principle: a new price high that clears a "line of resistance" (prior 147.03 high) on expanding volume is a **pivotal buy signal**. Price has broken above the prior high but not held above on strong close — 147.09 vs 147.24 high. Needs a sustained hold above 147.24.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R | Notes |
|---|---|---|---|---|---|
| Pullback to pivot low | 145.10 | 142.61 | 150.08 | **2.0:1** | Best risk-adjusted entry; wait for test of 142-145 zone |
| Breakout continuation | 148.00 | 145.10 | 154.00 | **2.0:1** | Enter on daily close above 147.24 with volume >1.5x avg |
| Avoid current price | 147.09 | 137.28 | 151 | 0.4:1 | Stop is too far; risk/reward does not work |

**Pivot target:** The next natural Livermore pivot target after 147.24 is a measured move projection: prior base (92–147 range = 55 pts) → target area **175–185** on a 6-month view, or minimum **154–158** (1×ATR extensions above breakout).

**Invalidation:** Close below 137.28 (the Jun 12 pivot low) on expanding volume — confirms Stage 2 is broken, exit.

---

### 2. MIDCAPETF — Strong Setup | Stage 2 | TT 7/8 | Volume Contracting

**As-of:** 2026-07-03 | **Confidence:** high | *Existing position opened 2026-07-01 @ 23.32*

#### Stage and Trend Template
7/8 criteria pass (misses: ≥25% above 52w low — 19.60 × 1.25 = 24.5; current 23.41 < 24.5).
MA200 monthly slope: **+0.7%** — gently rising Stage 2.

#### VCP Analysis
- Window 1 (Feb 04 – Mar 04): 9.2%
- Window 2 (Mar 05 – Apr 06): 11.7%
- Window 3 (Apr 07 – May 06): 14.7% (tariff shock)
- Window 4 (May 07 – Jun 04): 8.4% (contracting)
- Window 5 (Jun 05 – Jul 03): **8.1%** ← tightest → mild VCP

Volume blocks (20-day): 2.30M → 2.88M → 4.21M → 6.52M (older). Recent = lowest → **volume contracting** (confirmed True). Classic VCP setup: shrinking range + shrinking volume.

#### Livermore Pivotal Points
- H 2026-01-08 @ 23.61 ← first pivot high
- L 2026-04-02 @ **19.60** ← major pivot low (52w low on tariff shock)
- H 2026-05-29 @ **23.96** ← new 52w high — current resistance
- L 2026-06-04 @ **22.11** ← recent pivot low

The 23.96 pivot (May 29) is the **pivotal buy point** — a close and hold above it on volume signals the next leg.

#### Trade Scenarios (for additional sizing)
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Hold existing + add on pullback | 22.92 (MA50) | 22.20 | 24.50 | **2.1:1** |
| Breakout above 23.96 | 24.00 | 22.92 | 25.50 | **1.4:1** |

**Existing position:** Entry 23.32, stop 22.60, target 24.40. At current 23.41, the position is just above water (+0.4%). MA50 at 22.92 is the natural add-on level if a pullback occurs.

**Invalidation:** Close below 22.11 (Jun 04 pivot low).

---

## Tier 2 — Solid Setups Requiring Patience

### 3. JUNIORBEES — Setup | Stage 1→2 | TT 6/8 | Tightening Base

**As-of:** 2026-07-03 | **Confidence:** medium

#### Key Data
- Close: 780.71 | 52wH: 798.07 | 52wL: 632.34 | ATR14: 12.51
- MA50: 762.86 | MA150: 740.69 | MA200: 741.20 (MA150 ≈ MA200 — early transition)
- Vol 10d/50d: 1.04x; Vol blocks shrinking (True)
- Momentum: 1m +3.6%, 3m +16.6%, 6m +5.7%

#### VCP / Range Contraction
- Window 1: 6.8% | Window 2: 15.9% (tariff shock) | Window 3: 15.9% | Window 4: 7.2% | Window 5: **8.2%**
Contraction pattern: 15.9% → 7.2% → 8.2% — last two windows are tight. Volume declining across 80d→60d→40d blocks.

#### Livermore Pivotal Points
- L 2026-04-01 @ **632.34** ← major pivot low
- H 2026-05-07 @ 777.30
- L 2026-05-18 @ 728.65
- H 2026-05-29 @ **780.89** ← prior pivot high / resistance
- L 2026-06-11 @ **737.56** ← recent pivot low
- H 2026-07-03 @ **798.07** ← new 52w high made TODAY

**Pivotal signal:** Today (Jul 03) JUNIORBEES made a new 52-week high of 798.07 — a Livermore pivotal breakout. However, the close is only 780.71 (sold off from high), so this is a **reversal bar** (high vs close divergence). Requires confirmation on next session.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to MA50 | 765 | 748 | 803 | **2.2:1** |
| Retest of today's breakout | 786 | 770 | 815 | **1.8:1** |
| Breakout continuation | 799 | 778 | 835 | **1.7:1** |

**Invalidation:** Close below 737.56 (Jun 11 pivot low).

---

### 4. NEXT50IETF — Setup | Stage 1→2 | TT 6/8 | Tracking Same Index as JUNIORBEES

**As-of:** 2026-07-03 | **Confidence:** medium

*(Tracks Nifty Next 50 — same index as JUNIORBEES; treat these as one position decision.)*

- Close: 76.14 | 52wH: 78.19 (hit today) | 52wL: 62.60 | ATR14: 1.35
- Vol blocks: 20d=1.39M > 40d=0.95M — vol NOT contracting (recent spike from June 18 event: 6.84M volume)
- Price windows: 9.3% → 16.3% → 15.3% → 8.9% → **8.6%** — tightening last 2 windows

**Pivotal signal:** New 52w high 78.19 made today (Jul 03), same as JUNIORBEES. Same reversal-bar risk — high at 78.19, close only 76.14.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to MA50 | 74.52 | 72.50 | 78.57 | **2.0:1** |
| Hold above 76.54 | 76.54 | 74.52 | 80.27 | **1.9:1** |

**Note:** JUNIORBEES is preferred over NEXT50IETF (higher volume, deeper history). Don't hold both unless the exposure is intentional diversification.  
**Invalidation:** Close below 72.03 (Jun 11 pivot low).

---

### 5. HDFCSML250 — Setup | Mixed / Transition | TT 7/8 | Tightest Range in Series

**As-of:** 2026-07-03 | **Confidence:** high

- Close: 181.46 | 52wH: 183.18 | 52wL: 142.70 | ATR14: 2.73
- MA50: 172.13 | MA150: 164.27 | MA200: 166.30 (MA150 < MA200 — "mixed", not pure Stage 2)
- Vol contracting: True (1.70M → 2.07M → 2.75M — shrinking toward recent)
- Momentum: 1m +6.4%, 3m +21.7%, 6m +9.2%

#### VCP Analysis
Windows: 9.0% → 11.2% → 16.7% → 9.7% → **9.5%** — contracting last 2; tight at the 52w high level.

Last 20 bars show a 10-day consolidation (Jun 08–17) between 167–177, then a steady grind higher to 181.46. The 20-day range has been shrinking from 9.7% to 9.5% as price approaches the prior high 183.18. **This is a VCP approaching the pivot.**

#### Livermore Pivotal Points
- L 2026-03-23 @ 142.70 ← major low (52w low)
- H 2026-05-07 @ 180.00
- L 2026-05-18 @ 164.01
- H 2026-05-29 @ 173.40
- L 2026-06-11 @ **166.96** ← recent pivot low
- H 2026-05-07 (ATH in data) @ **183.18** ← pivotal resistance / buy pivot

**Pivot play:** 183.18 is both the 52w high and the pivotal buy point. A close above it on volume ≥1.5x avg triggers the entry.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to MA50 | 178.19 | 174.10 | 186.37 | **2.0:1** |
| Breakout above 183.18 | 183.50 | 178.19 | 190.55 | **1.3:1** |

**Invalidation:** Close below 166.96 (Jun 11 pivot low).

---

### 6. MOSMALL250 — Setup | Mixed | TT 7/8 | Elevated Range, High Volume

**As-of:** 2026-07-03 | **Confidence:** high

- Close: 18.07 | 52wH: 19.38 | 52wL: 14.22 | ATR14: 0.37
- MA50: 17.16 | MA150: 16.38 | MA200: 16.58 | Vol 10d/50d: 1.37x
- Vol NOT contracting (20d=2.68M > 40d=1.69M) — volume expanding, not VCP-like
- Range last window: 15.3% — NOT contracting (Jun 15 spike to 19.18 expanded range)

#### Livermore Analysis
- L 2026-03-30 @ **14.22** ← 52w low (tariff shock)
- H 2026-02-06 @ 19.38 ← prior high (was resistance)
- H 2026-06-15 @ **19.18** ← tested prior high zone
- L 2026-06-09 @ **16.63** ← recent pivot low / stop anchor

On Jun 15, MOSMALL250 briefly touched 19.18 — a test of the prior high area. The subsequent pullback to 17.62 and recovery to 18.07 is a normal reaction pullback from a near-pivotal-high test. Not a VCP — more a Livermore "secondary reaction" after the initial breakout.

**Livermore framework:** Price is in the "natural reaction" phase after testing the old high zone. The bullish case: hold the 17.16 MA50 zone as support, then next attempt at 19.18–19.38 resistance. If 19.38 clears with volume, that is the real pivotal breakout.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to MA50 | 17.62 | 17.06 | 19.18 | **2.8:1** |
| Current price | 18.07 | 17.16 | 19.18 | 1.2:1 |
| Pivot breakout | 19.40 | 17.62 | 21.00 | **0.9:1** |

**Best entry:** Pullback to 17.62–17.16 MA50 zone offers outstanding R:R. Avoid chasing at current levels.  
**Invalidation:** Close below 16.63 (Jun 09 pivot low).

---

### 7. MOALPHA50 — Setup | Stage 1→2 | TT 7/8 | Very Tight, Low Volume

**As-of:** 2026-07-03 | **Confidence:** high

- Close: 53.09 | 52wH: 55.97 | 52wL: 42.10 | ATR14: 0.91
- MA50: 52.19 | MA150: 50.34 | MA200: 50.54 | Vol 10d/50d: 1.96x
- Range windows: 9.2% → 17.8% → 16.6% → 6.8% → **10.9%**

#### VCP Analysis
The 6.8% window (May 07 – Jun 04) is the tightest — a clear VCP contraction. The Jun 22 spike to 55.97 (new 52w high on 122K volume — 20x average!) was a pivotal breakout attempt. Since then, price has quietly consolidated between 53.09–53.95 for 8 sessions with very low volume (2K–14K/day). This post-spike consolidation at elevated levels is a **tight VCP handle** — typical Minervini cup-with-handle.

#### Livermore Pivotal Points
- L 2026-03-30 @ **42.10** ← 52w low / pivot base
- H 2026-05-29 @ 54.00 ← first push to new territory
- L 2026-06-11 @ **50.49** ← reaction low
- H 2026-06-22 @ **55.97** ← new 52w high — pivotal high
- Current price 53.09 is ~5% below the pivot high

**Signal:** The Jun 22 spike to 55.97 on massive volume was a **Livermore pivotal breakout** — the first new 52w high in this ETF's history at current prices. The stock is now "resting" in a tight handle. Entry on pullback to MA50 (52.19) or on a close back above 54.00 are both valid.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Tight handle — pullback to MA50 | 52.19 | 50.82 | 55.97 | **2.8:1** |
| Entry near current | 53.09 | 51.72 | 55.38 | **1.7:1** |
| Breakout above 55.97 | 56.20 | 52.19 | 59.50 | **0.8:1** |

**Note:** Very low daily volume (thousands, not millions) — liquidity risk. Position size accordingly.  
**Invalidation:** Close below 50.49 (Jun 11 pivot low).

---

### 8. ALPHA — Setup | Stage 1→2 | TT 6/8 | Range Contracting

**As-of:** 2026-07-03 | **Confidence:** medium

- Close: 51.36 | 52wH: 53.60 | 52wL: 42.00 | ATR14: 0.98
- MA50: 50.23 | MA150: 48.38 | MA200: 48.53 (MA150 < MA200 — transitional)
- Vol: 20d slightly < 40d (contracting: True); 10d/50d = 0.82x
- Range windows: 15.9% → 13.7% → 14.5% → 9.0% → **8.4%** ← tight contraction

#### VCP and Pivot Analysis
Price range has contracted consistently from ~16% to 8.4% — a clear multi-contraction VCP. Current price is between the MA50 (50.23) and the 52w high (53.60). The last 20 bars show a well-ordered consolidation between 48.58–53.60.

Key pivots:
- L 2026-03-30 @ **42.00** ← 52w low
- H 2026-03-04 @ 53.60 ← prior 52w high
- L 2026-06-11 @ **48.58** ← recent pivot low
- H 2026-06-22 @ **52.59** ← most recent pivot high
- The 52.59 high is below the 53.60 prior high — **lower high** forming — needs clearing 53.60

**Livermore:** Until 53.60 is cleared, ALPHA is "testing its old high." The VCP base (8.4% current range) is tight enough to suggest accumulation. A close above 53.60 on volume ≥1.5x avg would be the pivotal signal.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to MA50 | 50.23 | 48.77 | 53.60 | **2.3:1** |
| Current price | 51.36 | 49.89 | 53.81 | 1.7:1 |
| Breakout | 53.75 | 50.23 | 57.00 | **0.8:1** |

**Invalidation:** Close below 48.58 (Jun 11 pivot low).

---

### 9. BANKBEES — Setup (with Stage 3 caveat) | TT 6/8 | Range Re-Expanding

**As-of:** 2026-07-03 | **Confidence:** medium

- Close: 600.12 | 52wH: 638.99 | 52wL: 515.98 | ATR14: 10.08
- MA50: 574.36 | **MA50 < MA150 (591.87)** ← Stage 3 structure warning
- Vol contracting: True (20d=1.17M < 40d=1.33M)
- Range windows: 6.0% → 18.6% → 10.5% → 6.6% → **13.1%** ← range RE-EXPANDING

**Stage 3 warning:** The MA50 is below the MA150 — this is a structural Stage 3 pattern. The 6-month momentum is -1.2%. The Jul 03 data shows the 20-day range has re-expanded to 13.1% (from a low of 6.6%), suggesting distribution rather than base-building.

**Livermore analysis:** Pivots show:
- H 2026-02-19 @ **638.99** ← 52w high
- L 2026-04-02 @ **515.98** ← 52w low (tariff shock)
- H 2026-05-26 @ 573.99 ← lower high
- Recent: consolidating 595–628 zone

The series of lower highs (638 → 592 → 574 → 628) is **mixed** — not a clean ascending pivot series. The Jun 30 bar shows H=627.90 followed by close at 596.37 — a reversal bar suggesting supply still present.

**Verdict:** The Setup rating is valid but the Stage 3 classification and re-expanding range reduce conviction. Best play is a pullback entry at the 596.69 support, not a chase at current levels.

#### Trade Scenarios
| Scenario | Entry | Stop | Target | R:R |
|---|---|---|---|---|
| Pullback to support | 596.69 | 581.57 | 623.98 | **1.8:1** |
| Breakout above 623.98 with vol | 625 | 596.69 | 651 | **0.9:1** |

**Invalidation:** Close below 515.98 (52w low). Caution alert below 586.

---

## Tier 3 — Watchlist

### 10. MON100 (Nasdaq 100 Proxy) — Watchlist | Stage 2 | TT 7/8

- Close 332.78 | 52wH 342.55 (-2.9%) | MA50 323.02 | Vol contracting: False (20d > 40d)
- Strong Stage 2: MA200 slope +5.8%, 3m +39.5%, 6m +44.4%
- **Issue:** 1m momentum -1.9% — pullback from Jun 05 high (342.55). Range last window 8.6% — tight.
- Livermore pivot: 342.55 (Jun 05 high) is the buy pivot. Current 332.78 is ~3% below it.
- **Watch for:** Recovery of 1m momentum (need to see daily closes pushing back above 335–336) and a return to test 342.55 on volume.
- Entry trigger: close above 335 + volume ≥1.2x avg. Stop: 323.02 (MA50). Target: 360+.

### 11. MASPTOP50 (S&P 500 Top 50 proxy) — Watchlist | Mixed | TT 6/8

- Close 77.78 | 52wH 82.78 (-6.0%) | Below MA50 (79.31) — critical weakness
- Range last window 10.0% (widening from 5.2% low in May — range re-expanding)
- The 82.78 high (May 22) was a big up-day. Since then price has pulled back to 75.75 (Jun 30) and partially recovered.
- **Issue:** Currently below MA50 (79.31). Livermore rule: price below MA50 during a pullback is a structural weakness signal — do not buy until MA50 is reclaimed.
- Watch: Close above MA50 (79.31) with volume ≥1.2x is the re-entry trigger. Support: 76.51.

### 12. MAFANG (Hang Seng Tech proxy) — Watchlist | Mixed | TT 6/8

- Close 190.81 | 52wH 208.38 (-8.4%) | Below MA50 (191.16) — just below
- Volume very low (0.61x); range 13% (elevated)
- Hard pullback from Jun 03 high (208.38): -8.4% in 1 month
- Jul 03 close 190.81 is just below MA50 (191.16) — needs to reclaim
- Livermore: The 208.38 high was the pivotal point. Current price is in "natural reaction" territory. Support at MA150 (173.10) is 9% lower.
- Watch: Reclaim of MA50 (191.16) + stabilisation above 192 is the condition to upgrade to Setup.

---

## Avoids

| Symbol | Stage | TT | Reason |
|---|---|---:|---|
| NIFTYBEES | Stage 4 | 3/8 | -8.7% from 52w high; MA200 slope -0.4%; broad Nifty 50 in structural decline |
| NIFTYIETF | Stage 4 | 3/8 | Mirror of NIFTYBEES; -16.4% from 52w high 328.24 |
| MAHKTECH | Stage 4 | 0/8 | All 8 criteria fail; -38.9% from 52w high; every MA declining |
| CPSEETF | Weak Stage 1 | 3/8 | Below all 3 MAs; 1m -3.2%; PSU basket underperforming |
| MOMENTUM | Weak Stage 1 | 2/8 | Only 2/8 TT criteria; MA structure deteriorating |
| HDFCMOMENT | Weak Stage 1 | 3/8 | Below MA150/MA200; 6m -1.3% |
| SETFGOLD | Stage 3 | 5/8 | -19.3% from Jan 2026 high 153.95; gold correcting |
| HDFCGOLD | Stage 3 | 5/8 | Mirror of SETFGOLD; -18.4% from 52w high 152.30 |
| SBISILVER | Stage 3 | 4/8 | -37.4% from 52w high 362.00; very high volatility; no base |
| ICICIB22 | Stage 1 base | 5/8 | Below MA50 and MA150; flat 1m/3m momentum; conditional only |

---

## Cross-Scan Synthesis

### Opportunity Hierarchy (by conviction)

**Immediate action possible:**
1. **MONQ50** — best VCP setup in the universe; pullback to 145 zone or breakout above 147.24
2. **MIDCAPETF** — existing position; add on MA50 pullback to 22.92
3. **MOALPHA50** — tight handle below 55.97; excellent R:R on pullback to 52.19

**Wait for pullback before entering:**
4. **JUNIORBEES** — new 52w high today but reversal bar; wait for pullback to 765
5. **NEXT50IETF** — same signal as JUNIORBEES; prefer JUNIORBEES for liquidity
6. **HDFCSML250** — nearing 52w high 183.18; wait for breakout or pullback to 178

**Entry on pullback to MA50 support:**
7. **MOSMALL250** — wait for 17.62–17.16 zone; excellent R:R 2.8:1
8. **ALPHA** — wait for 50.23 MA50 zone; clean VCP base

**Conditional / trigger-dependent:**
9. **BANKBEES** — valid but Stage 3 caution; only on pullback to 596, not at current 600
10. **MON100** — upgrade from Watchlist when 1m momentum recovers and close above 335

### Thematic Read

1. **Small/mid-cap ETFs leading the market.** The Nifty 50 (NIFTYBEES) is in Stage 4, yet MIDCAPETF, HDFCSML250, MOSMALL250, MOALPHA50, JUNIORBEES, NEXT50IETF all rank Setup or better. This is a textbook **sector rotation** — money leaving large-cap into mid/small-cap. Livermore's principle: trade the leaders, not the laggards.

2. **US-linked ETFs in correction.** MON100 (+44% 6m) and MAFANG are pulling back after extraordinary runs. These are healthy pullbacks in Stage 2 uptrends — potential re-entries once momentum stabilises.

3. **Gold and silver are in Stage 3 distribution.** SETFGOLD hit 153.95 on Jan 28, 2026 — and has since pulled back ~19%. The gold trend change is a global macro event. No swing long setups in gold/silver ETFs now.

4. **Infrastructure/PSU (CPSEETF) is lagging.** Below all MAs; no setup. The PSU theme that drove 2024–early 2025 has fully rotated out.

5. **Momentum factor ETFs (HDFCMOMENT, MOMENTUM) are the most ironic underperformers.** These hold the prior momentum leaders — which have been the weakest recently as the market rotates.

### Duplication Risks
- **JUNIORBEES ≈ NEXT50IETF** (both track Nifty Next 50): treat as one position
- **HDFCSML250 ≈ MOSMALL250** (both track small-cap indices): similar setups, stagger or pick one
- **ALPHA ≈ MOALPHA50** (both Alpha factor ETFs): near-identical structure, pick one

---

## Quick Reference Card

| Symbol | Best Entry | Stop | Target | R:R | When |
|---|---|---|---|---|---|
| MONQ50 | 145.10 | 142.61 | 150.08 | 2.0:1 | On pullback to 143–145 |
| MONQ50 (breakout) | 148.00 | 145.10 | 154.00 | 2.0:1 | On daily close >147.24 + vol |
| MIDCAPETF (add) | 22.92 | 22.20 | 24.28 | 1.9:1 | On MA50 pullback |
| MOALPHA50 | 52.19 | 50.82 | 55.97 | 2.8:1 | On pullback to MA50 |
| MOSMALL250 | 17.62 | 17.06 | 19.18 | 2.8:1 | On pullback to MA50 zone |
| JUNIORBEES | 765 | 748 | 803 | 2.2:1 | Wait for pullback from 52w high |
| HDFCSML250 | 178.19 | 174.10 | 186.37 | 2.0:1 | On pullback or above 183.18 |
| ALPHA | 50.23 | 48.77 | 53.60 | 2.3:1 | On MA50 pullback |
| BANKBEES | 596.69 | 581.57 | 623.98 | 1.8:1 | Only on pullback to 596 zone |
| MON100 | 326.77 | 319.26 | 342.55 | 2.1:1 | After 1m momentum recovers |
