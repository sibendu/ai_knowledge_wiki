#!/usr/bin/env python
"""
Reusable NSE swing-trading scanner for local OHLCV CSV files.

The script intentionally uses only Python's standard library so it can run in
the repository virtual environment without reinstalling dependencies.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Iterable


TRADING_DAYS_PER_YEAR = 252
SYMBOL_ALIASES = {
    "BANDHANBANK": "BANDHANBNK",
}
PRICE_GAP_WARNING_THRESHOLD = 35.0


@dataclass
class Bar:
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    delivery_percent: float | None = None


@dataclass
class Pivot:
    kind: str
    date: datetime
    price: float


def parse_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_bars(csv_path: Path) -> list[Bar]:
    bars: list[Bar] = []
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            date = datetime.strptime(row["datetime"], "%d-%m-%Y %H:%M")
            delivery = parse_float(row.get("delivery_percent"))
            bars.append(
                Bar(
                    date=date,
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row["total_volume"]),
                    delivery_percent=delivery,
                )
            )
    return sorted(bars, key=lambda bar: bar.date)


def find_large_price_gaps(bars: list[Bar], threshold_pct: float = PRICE_GAP_WARNING_THRESHOLD) -> list[dict]:
    gaps: list[dict] = []
    for previous, current in zip(bars, bars[1:]):
        change = pct_change(previous.close, current.close)
        if abs(change) >= threshold_pct:
            gaps.append(
                {
                    "from_date": previous.date.date().isoformat(),
                    "to_date": current.date.date().isoformat(),
                    "from_close": previous.close,
                    "to_close": current.close,
                    "change_pct": change,
                }
            )
    return gaps


def sma(values: list[float], period: int) -> float | None:
    if len(values) < period:
        return None
    return mean(values[-period:])


def pct_change(start: float, end: float) -> float:
    if start == 0:
        return 0.0
    return (end / start - 1.0) * 100.0


def rolling_atr(bars: list[Bar], period: int = 14) -> float | None:
    if len(bars) < period + 1:
        return None
    true_ranges: list[float] = []
    for index in range(1, len(bars)):
        current = bars[index]
        previous = bars[index - 1]
        true_ranges.append(
            max(
                current.high - current.low,
                abs(current.high - previous.close),
                abs(current.low - previous.close),
            )
        )
    return mean(true_ranges[-period:])


def find_pivots(bars: list[Bar], window: int = 10) -> list[Pivot]:
    pivots: list[Pivot] = []
    if len(bars) < (window * 2) + 1:
        return pivots
    for index in range(window, len(bars) - window):
        left_right = bars[index - window : index + window + 1]
        bar = bars[index]
        if bar.high == max(item.high for item in left_right):
            pivots.append(Pivot("H", bar.date, bar.high))
        if bar.low == min(item.low for item in left_right):
            pivots.append(Pivot("L", bar.date, bar.low))
    return compress_pivots(pivots)


def compress_pivots(pivots: list[Pivot]) -> list[Pivot]:
    compressed: list[Pivot] = []
    for pivot in sorted(pivots, key=lambda item: item.date):
        if not compressed or compressed[-1].kind != pivot.kind:
            compressed.append(pivot)
            continue
        previous = compressed[-1]
        if pivot.kind == "H" and pivot.price > previous.price:
            compressed[-1] = pivot
        elif pivot.kind == "L" and pivot.price < previous.price:
            compressed[-1] = pivot
    return compressed


def trend_template(
    close: float,
    ma50: float | None,
    ma150: float | None,
    ma200: float | None,
    high_52w: float,
    low_52w: float,
    momentum_1m: float,
) -> tuple[int, list[str]]:
    checks = [
        ("price > MA50", ma50 is not None and close > ma50),
        ("price > MA150", ma150 is not None and close > ma150),
        ("price > MA200", ma200 is not None and close > ma200),
        ("MA50 > MA150", ma50 is not None and ma150 is not None and ma50 > ma150),
        ("MA150 > MA200", ma150 is not None and ma200 is not None and ma150 > ma200),
        (">=25% above 52w low", close >= low_52w * 1.25),
        ("within 25% of 52w high", close >= high_52w * 0.75),
        ("1m momentum positive", momentum_1m > 0),
    ]
    return sum(1 for _, passed in checks if passed), [
        f"{name}: {'yes' if passed else 'no'}" for name, passed in checks
    ]


def ma_slope(values: list[float], period: int, days: int) -> float | None:
    if len(values) < period + days:
        return None
    current = sma(values, period)
    previous = sma(values[:-days], period)
    if current is None or previous is None:
        return None
    return pct_change(previous, current)


def classify_stage(
    close: float,
    ma50: float | None,
    ma150: float | None,
    ma200: float | None,
    ma200_slope_1m: float | None,
    momentum_3m: float,
) -> str:
    if ma50 is None or ma150 is None or ma200 is None or ma200_slope_1m is None:
        return "Insufficient history"
    near_ma200 = abs(close / ma200 - 1.0) <= 0.08
    if close > ma50 > ma150 > ma200 and ma200_slope_1m > 0:
        return "Stage 2 markup"
    if close < ma200 and ma200_slope_1m < 0:
        return "Stage 4 decline"
    if close > ma200 and (ma50 < ma150 or momentum_3m < 0):
        return "Stage 3 topping / repair"
    if near_ma200 and abs(ma200_slope_1m) < 1.5:
        return "Stage 1 base / transition"
    return "Mixed / transition"


def fmt_price(value: float | None) -> str:
    if value is None or math.isnan(value):
        return "n/a"
    return f"{value:.2f}"


def fmt_pct(value: float | None) -> str:
    if value is None or math.isnan(value):
        return "n/a"
    return f"{value:+.1f}%"


def reward_risk(entry: float, stop: float, target: float) -> float | None:
    risk = entry - stop
    reward = target - entry
    if risk <= 0 or reward <= 0:
        return None
    return reward / risk


def detect_vcp(bars: list[Bar], min_contractions: int = 2) -> dict:
    """Detect Volatility Contraction Pattern (Mark Minervini).

    Looks for successive pivot-high/low contractions where each swing
    is shallower than the previous, with volume declining into the apex.
    """
    empty_vcp = {
        "detected": False,
        "contraction_count": 0,
        "contractions": [],
        "volume_dryup_ratio": None,
        "last_contraction_depth_pct": None,
        "tight_pattern": False,
        "pivot_line": None,
        "pivot_line_date": None,
    }

    if len(bars) < 60:
        return {**empty_vcp, "reason": "Insufficient bars for VCP detection"}

    pivots = find_pivots(bars, window=5)
    if len(pivots) < 4:
        return {**empty_vcp, "reason": "Too few pivots"}

    contractions: list[dict] = []
    highs = [p for p in pivots if p.kind == "H"]
    lows = [p for p in pivots if p.kind == "L"]

    for i in range(1, min(len(highs), len(lows))):
        if i >= len(highs) or i >= len(lows):
            break
        prev_range = highs[i - 1].price - lows[i - 1].price
        curr_range = highs[i].price - lows[i].price
        if prev_range > 0:
            depth_pct = (curr_range / highs[i].price) * 100
            contraction_ratio = curr_range / prev_range
            contractions.append({
                "swing": i,
                "depth_pct": round(depth_pct, 1),
                "contraction_ratio": round(contraction_ratio, 2),
                "high": highs[i].price,
                "low": lows[i].price,
                "high_date": highs[i].date.date().isoformat(),
                "low_date": lows[i].date.date().isoformat(),
            })

    valid_contractions = [c for c in contractions if c["contraction_ratio"] < 0.85]

    volumes = [bar.volume for bar in bars]
    vol_50 = sma(volumes, 50)
    vol_10 = sma(volumes, 10)
    volume_dryup = None
    if vol_50 and vol_10 and vol_50 > 0:
        volume_dryup = round(vol_10 / vol_50, 2)

    detected = len(valid_contractions) >= min_contractions
    last_depth = valid_contractions[-1]["depth_pct"] if valid_contractions else None
    tight = last_depth is not None and last_depth < 15

    return {
        "detected": detected,
        "contraction_count": len(valid_contractions),
        "contractions": valid_contractions[-4:],
        "volume_dryup_ratio": volume_dryup,
        "last_contraction_depth_pct": last_depth,
        "tight_pattern": tight,
        "pivot_line": highs[-1].price if highs else None,
        "pivot_line_date": highs[-1].date.date().isoformat() if highs else None,
    }


def detect_livermore_pivots(bars: list[Bar]) -> dict:
    """Detect Jesse Livermore pivotal points.

    Identifies breakouts from consolidation (continuation pivots) and
    new highs after meaningful corrections (reversal pivots).
    """
    empty_livermore = {
        "pivotal_points": [],
        "current_signal": "neutral",
        "correction_from_50d_high_pct": 0.0,
        "range_20d_pct": 0.0,
        "volume_expanding": False,
        "high_50d": 0.0,
        "low_20d": 0.0,
    }
    if len(bars) < 60:
        return empty_livermore

    closes = [bar.close for bar in bars]
    highs_list = [bar.high for bar in bars]
    lows_list = [bar.low for bar in bars]

    high_20 = max(highs_list[-20:])
    high_50 = max(highs_list[-50:]) if len(bars) >= 50 else max(highs_list)
    low_20 = min(lows_list[-20:])
    latest = bars[-1]

    correction_from_high = pct_change(high_50, latest.close)
    range_20d = pct_change(low_20, high_20)

    pivotal_points: list[dict] = []

    if latest.close >= high_20 * 0.98 and range_20d < 15:
        pivotal_points.append({
            "type": "continuation",
            "description": "Price near 20-day high after tight consolidation",
            "trigger_price": round(high_20, 2),
            "consolidation_range_pct": round(range_20d, 1),
        })

    if correction_from_high < -15 and latest.close > low_20 * 1.05:
        pivotal_points.append({
            "type": "reversal",
            "description": "Meaningful correction with signs of recovery",
            "correction_depth_pct": round(correction_from_high, 1),
            "recovery_from_low_pct": round(pct_change(low_20, latest.close), 1),
        })

    recent_bars_20 = bars[-20:]
    vol_expansion = False
    if len(bars) >= 50:
        avg_vol_50 = mean([b.volume for b in bars[-50:]])
        avg_vol_5 = mean([b.volume for b in bars[-5:]])
        if avg_vol_50 > 0 and avg_vol_5 / avg_vol_50 > 1.3:
            vol_expansion = True

    if latest.high >= high_50 and vol_expansion:
        pivotal_points.append({
            "type": "breakout",
            "description": "New high with volume expansion",
            "breakout_level": round(high_50, 2),
            "volume_expansion": True,
        })

    if pivotal_points:
        signal = "bullish"
    elif correction_from_high < -25:
        signal = "bearish"
    else:
        signal = "neutral"

    return {
        "pivotal_points": pivotal_points,
        "current_signal": signal,
        "correction_from_50d_high_pct": round(correction_from_high, 1),
        "range_20d_pct": round(range_20d, 1),
        "volume_expanding": vol_expansion,
        "high_50d": round(high_50, 2),
        "low_20d": round(low_20, 2),
    }


def compute_deep_metrics(bars: list[Bar], result: dict) -> dict:
    """Compute VCP, Livermore, and extended SEPA metrics for a symbol."""
    vcp = detect_vcp(bars)
    livermore = detect_livermore_pivots(bars)

    closes = [bar.close for bar in bars]
    ma10 = sma(closes, 10)
    ma20 = sma(closes, 20)
    latest = bars[-1]

    ma50_slope_5d = ma_slope(closes, 50, 5)
    ma150_slope_20d = ma_slope(closes, 150, 20)

    sepa_extended = {
        "ma10": ma10,
        "ma20": ma20,
        "price_above_ma10": ma10 is not None and latest.close > ma10,
        "price_above_ma20": ma20 is not None and latest.close > ma20,
        "ma50_rising_5d": ma50_slope_5d is not None and ma50_slope_5d > 0,
        "ma150_rising_20d": ma150_slope_20d is not None and ma150_slope_20d > 0,
        "ma50_slope_5d_pct": ma50_slope_5d,
        "ma150_slope_20d_pct": ma150_slope_20d,
    }

    deep_rating = compute_deep_rating(result, vcp, livermore, sepa_extended)

    return {
        "vcp": vcp,
        "livermore": livermore,
        "sepa_extended": sepa_extended,
        "deep_rating": deep_rating,
    }


def compute_deep_rating(result: dict, vcp: dict, livermore: dict, sepa: dict) -> str:
    """Synthesize VCP + Livermore + SEPA into an actionable rating."""
    score = 0

    if result.get("trend_score", 0) >= 7:
        score += 3
    elif result.get("trend_score", 0) >= 5:
        score += 1

    if vcp.get("detected"):
        score += 2
        if vcp.get("tight_pattern"):
            score += 1
        if vcp.get("volume_dryup_ratio") is not None and vcp["volume_dryup_ratio"] < 0.7:
            score += 1

    if livermore.get("current_signal") == "bullish":
        score += 2
        if any(p["type"] == "breakout" for p in livermore.get("pivotal_points", [])):
            score += 1

    if sepa.get("price_above_ma10") and sepa.get("price_above_ma20"):
        score += 1
    if sepa.get("ma50_rising_5d") and sepa.get("ma150_rising_20d"):
        score += 1

    if score >= 9:
        return "Strong VCP Setup"
    if score >= 7:
        return "VCP Setup"
    if score >= 5:
        return "Developing Pattern"
    if score >= 3:
        return "Early Stage / Watch"
    return "No Pattern"


def rating_from_metrics(score: int, stage: str, momentum_1m: float, momentum_3m: float, near_high_pct: float) -> str:
    if score >= 7 and "Stage 2" in stage and momentum_1m > 0 and near_high_pct >= -12:
        return "Strong Setup"
    if score >= 6 and momentum_1m > 0 and momentum_3m > 0:
        return "Setup"
    if score >= 5 and momentum_1m > 0:
        return "Conditional"
    if score >= 4 or "base" in stage.lower():
        return "Watchlist"
    return "Avoid"


def analyze_symbol(symbol: str, data_dir: Path, lookback_days: int, deep: bool = False) -> dict:
    requested_symbol = symbol
    data_symbol = SYMBOL_ALIASES.get(symbol, symbol)
    csv_path = data_dir / f"{data_symbol}.csv"
    if not csv_path.exists():
        return {"symbol": requested_symbol, "error": f"Missing file: {csv_path}"}

    bars = read_bars(csv_path)
    if not bars:
        return {"symbol": requested_symbol, "error": "No bars found"}

    bars = bars[-lookback_days:]
    warnings: list[str] = []
    if requested_symbol != data_symbol:
        warnings.append(f"Used local file symbol {data_symbol} for requested symbol {requested_symbol}.")

    large_gaps = find_large_price_gaps(bars)
    if large_gaps:
        latest_gap = large_gaps[-1]
        warnings.append(
            "Large price discontinuity detected "
            f"({latest_gap['from_date']} close {fmt_price(latest_gap['from_close'])} -> "
            f"{latest_gap['to_date']} close {fmt_price(latest_gap['to_close'])}, "
            f"{fmt_pct(latest_gap['change_pct'])}). "
            "Metrics use only post-gap bars because the file appears unadjusted."
        )
        gap_date = datetime.fromisoformat(latest_gap["to_date"])
        bars = [bar for bar in bars if bar.date >= gap_date]

    closes = [bar.close for bar in bars]
    volumes = [bar.volume for bar in bars]
    latest = bars[-1]
    last_date = latest.date.date().isoformat()

    one_month_ago = closes[-22] if len(closes) >= 22 else closes[0]
    three_months_ago = closes[-63] if len(closes) >= 63 else closes[0]
    six_months_ago = closes[-126] if len(closes) >= 126 else closes[0]

    recent_252 = bars[-TRADING_DAYS_PER_YEAR:] if len(bars) >= TRADING_DAYS_PER_YEAR else bars
    high_52w = max(bar.high for bar in recent_252)
    low_52w = min(bar.low for bar in recent_252)
    atr14 = rolling_atr(bars, 14)
    avg_volume_50 = sma(volumes, 50)
    recent_volume_10 = sma(volumes, 10)
    delivery_values = [bar.delivery_percent for bar in bars[-20:] if bar.delivery_percent is not None]

    ma50 = sma(closes, 50)
    ma150 = sma(closes, 150)
    ma200 = sma(closes, 200)
    ma200_slope = ma_slope(closes, 200, 22)
    momentum_1m = pct_change(one_month_ago, latest.close)
    momentum_3m = pct_change(three_months_ago, latest.close)
    momentum_6m = pct_change(six_months_ago, latest.close)
    trend_score, trend_checks = trend_template(
        latest.close, ma50, ma150, ma200, high_52w, low_52w, momentum_1m
    )
    stage = classify_stage(latest.close, ma50, ma150, ma200, ma200_slope, momentum_3m)

    pivots = find_pivots(bars, window=10)
    recent_pivots = pivots[-8:]
    pivot_lows = [pivot.price for pivot in pivots if pivot.kind == "L"]
    pivot_highs = [pivot.price for pivot in pivots if pivot.kind == "H"]

    support_candidates = [price for price in pivot_lows[-4:] if price < latest.close]
    if ma50 and ma50 < latest.close:
        support_candidates.append(ma50)
    if ma150 and ma150 < latest.close:
        support_candidates.append(ma150)
    support = max(support_candidates) if support_candidates else low_52w

    resistance_candidates = [price for price in pivot_highs[-4:] if price > latest.close]
    if high_52w > latest.close:
        resistance_candidates.append(high_52w)
    resistance = min(resistance_candidates) if resistance_candidates else high_52w

    atr = atr14 or latest.close * 0.03
    current_stop = min(support, latest.close - 1.5 * atr)
    current_target = max(resistance, latest.close + 2.5 * atr)
    breakout_entry = max(resistance * 1.003, latest.close * 1.01)
    breakout_stop = max(latest.close - 1.2 * atr, support)
    breakout_target = breakout_entry + max(2.5 * atr, (resistance - support) * 0.6)
    pullback_entry = max(support, latest.close - 1.2 * atr)
    pullback_stop = pullback_entry - 1.5 * atr
    pullback_target = max(resistance, latest.close + 1.8 * atr)

    near_high_pct = pct_change(high_52w, latest.close)
    from_low_pct = pct_change(low_52w, latest.close)
    rating = rating_from_metrics(trend_score, stage, momentum_1m, momentum_3m, near_high_pct)
    volume_ratio = None
    if avg_volume_50 and recent_volume_10:
        volume_ratio = recent_volume_10 / avg_volume_50

    base_result = {
        "symbol": requested_symbol,
        "data_symbol": data_symbol,
        "warnings": warnings,
        "bars_used": len(bars),
        "last_date": last_date,
        "close": latest.close,
        "ma50": ma50,
        "ma150": ma150,
        "ma200": ma200,
        "ma200_slope_1m": ma200_slope,
        "high_52w": high_52w,
        "low_52w": low_52w,
        "near_high_pct": near_high_pct,
        "from_low_pct": from_low_pct,
        "momentum_1m": momentum_1m,
        "momentum_3m": momentum_3m,
        "momentum_6m": momentum_6m,
        "trend_score": trend_score,
        "trend_checks": trend_checks,
        "stage": stage,
        "rating": rating,
        "atr14": atr14,
        "support": support,
        "resistance": resistance,
        "volume_ratio": volume_ratio,
        "delivery_20d": mean(delivery_values) if delivery_values else None,
        "pivots": recent_pivots,
        "scenarios": {
            "current": {
                "entry": latest.close,
                "stop": current_stop,
                "target": current_target,
                "rr": reward_risk(latest.close, current_stop, current_target),
            },
            "pullback": {
                "entry": pullback_entry,
                "stop": pullback_stop,
                "target": pullback_target,
                "rr": reward_risk(pullback_entry, pullback_stop, pullback_target),
            },
            "breakout": {
                "entry": breakout_entry,
                "stop": breakout_stop,
                "target": breakout_target,
                "rr": reward_risk(breakout_entry, breakout_stop, breakout_target),
            },
        },
    }

    if deep:
        base_result["deep"] = compute_deep_metrics(bars, base_result)

    return base_result


def sort_key(result: dict) -> tuple[int, float, float]:
    rating_rank = {
        "Strong Setup": 5,
        "Setup": 4,
        "Conditional": 3,
        "Watchlist": 2,
        "Avoid": 1,
    }
    return (
        rating_rank.get(result.get("rating", ""), 0),
        result.get("trend_score", 0),
        result.get("momentum_1m", -999),
    )


def claim_confidence(result: dict) -> str:
    score = result["trend_score"]
    if score >= 7:
        return "high"
    if score >= 5:
        return "medium"
    return "low"


def scenario_line(name: str, scenario: dict) -> str:
    rr = scenario["rr"]
    rr_text = "n/a" if rr is None else f"{rr:.1f}:1"
    return (
        f"- {name}: entry {fmt_price(scenario['entry'])}, stop {fmt_price(scenario['stop'])}, "
        f"target {fmt_price(scenario['target'])}, R:R {rr_text}"
    )


def render_deep_section(result: dict) -> list[str]:
    """Render VCP/Livermore/SEPA deep analysis for one symbol."""
    deep = result.get("deep")
    if not deep:
        return []

    lines: list[str] = ["", "**Deep Analysis (VCP / Livermore / SEPA):**", ""]
    lines.append(f"- **Deep Rating:** {deep['deep_rating']}")

    vcp = deep["vcp"]
    if vcp["detected"]:
        lines.append(f"- **VCP Detected:** Yes ({vcp['contraction_count']} contractions, "
                     f"tight={vcp['tight_pattern']}, volume dryup={vcp['volume_dryup_ratio']}x)")
        if vcp.get("pivot_line"):
            lines.append(f"  - Pivot line (breakout trigger): {fmt_price(vcp['pivot_line'])} ({vcp['pivot_line_date']})")
        for c in vcp.get("contractions", []):
            lines.append(f"  - Swing {c['swing']}: depth {c['depth_pct']}%, ratio {c['contraction_ratio']} "
                         f"({c['high_date']} high {fmt_price(c['high'])} / {c['low_date']} low {fmt_price(c['low'])})")
    else:
        lines.append(f"- **VCP Detected:** No ({vcp.get('reason', 'contraction criteria not met')})")

    liv = deep["livermore"]
    lines.append(f"- **Livermore Signal:** {liv['current_signal']} "
                 f"(correction from 50d high: {fmt_pct(liv['correction_from_50d_high_pct'])}, "
                 f"20d range: {fmt_pct(liv['range_20d_pct'])})")
    for pp in liv.get("pivotal_points", []):
        lines.append(f"  - {pp['type'].title()}: {pp['description']}")

    sepa = deep["sepa_extended"]
    above_ma10 = "yes" if sepa["price_above_ma10"] else "no"
    above_ma20 = "yes" if sepa["price_above_ma20"] else "no"
    ma50_rising = "yes" if sepa["ma50_rising_5d"] else "no"
    ma150_rising = "yes" if sepa["ma150_rising_20d"] else "no"
    lines.append(f"- **SEPA Extended:** above MA10={above_ma10}, above MA20={above_ma20}, "
                 f"MA50 rising 5d={ma50_rising} ({fmt_pct(sepa['ma50_slope_5d_pct'])}), "
                 f"MA150 rising 20d={ma150_rising} ({fmt_pct(sepa['ma150_slope_20d_pct'])})")

    return lines


def render_markdown(results: list[dict], lookback_days: int) -> str:
    valid = [result for result in results if "error" not in result]
    errors = [result for result in results if "error" in result]
    valid.sort(key=sort_key, reverse=True)
    as_of_dates = sorted({result["last_date"] for result in valid})
    as_of_text = as_of_dates[-1] if as_of_dates else "n/a"

    lines: list[str] = [
        "# NSE Swing Trading Opportunity Scan",
        "",
        f"**Generated:** {datetime.now().date().isoformat()}",
        f"**Price data as of:** {as_of_text}",
        f"**Lookback:** last {lookback_days} trading rows, roughly {lookback_days / TRADING_DAYS_PER_YEAR:.1f} years.",
        "**Horizon:** short-term swing trades from a couple of weeks to 1-2 quarters.",
        "**Posture:** research and education only; not personalized financial advice.",
        "",
        "## Method",
        "",
        "The scan combines Stage Analysis, a Minervini-style 8-point Trend Template, 1/3/6-month momentum, 52-week distance, recent pivots, ATR-based risk levels, and volume/delivery context. Ratings are mechanical research labels, not trade instructions.",
        "",
    ]

    has_deep = any(result.get("deep") for result in valid)
    if has_deep:
        lines.append("**Deep mode enabled:** also evaluates VCP (Volatility Contraction Pattern), "
                     "Livermore pivotal points, and extended SEPA criteria per symbol.")
        lines.append("")

    lines.extend([
        "## Ranked Summary",
        "",
    ])

    if has_deep:
        lines.append("| Rank | Symbol | Rating | Deep Rating | Stage | Close | 52wH dist | Trend | 1m | 3m | VCP | Livermore |")
        lines.append("|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|")
    else:
        lines.append("| Rank | Symbol | Rating | Stage | Bars | Close | 52wH dist | 52wL dist | Trend | 1m | 3m | Volume |")
        lines.append("|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")

    for rank, result in enumerate(valid, start=1):
        volume = result["volume_ratio"]
        volume_text = "n/a" if volume is None else f"{volume:.2f}x"
        if has_deep:
            deep = result.get("deep", {})
            deep_rating = deep.get("deep_rating", "n/a") if deep else "n/a"
            vcp_flag = "Yes" if deep and deep.get("vcp", {}).get("detected") else "No"
            liv_signal = deep.get("livermore", {}).get("current_signal", "n/a") if deep else "n/a"
            lines.append(
                f"| {rank} | {result['symbol']} | **{result['rating']}** | {deep_rating} | {result['stage']} | "
                f"{fmt_price(result['close'])} | {fmt_pct(result['near_high_pct'])} | {result['trend_score']}/8 | "
                f"{fmt_pct(result['momentum_1m'])} | {fmt_pct(result['momentum_3m'])} | {vcp_flag} | {liv_signal} |"
            )
        else:
            lines.append(
                f"| {rank} | {result['symbol']} | **{result['rating']}** | {result['stage']} | {result['bars_used']} | "
                f"{fmt_price(result['close'])} | {fmt_pct(result['near_high_pct'])} | "
                f"{fmt_pct(result['from_low_pct'])} | {result['trend_score']}/8 | "
                f"{fmt_pct(result['momentum_1m'])} | {fmt_pct(result['momentum_3m'])} | {volume_text} |"
            )

    if errors:
        lines.extend(["", "## Missing / Unreadable Symbols", ""])
        for error in errors:
            lines.append(f"- {error['symbol']}: {error['error']}")

    lines.extend(["", "## Actionable Watchlist", ""])
    for result in valid:
        if result["rating"] in {"Strong Setup", "Setup", "Conditional"}:
            confidence = claim_confidence(result)
            lines.append(
                f"- **{result['symbol']} ({result['rating']}, {confidence} confidence):** "
                f"watch {fmt_price(result['resistance'])} resistance and {fmt_price(result['support'])} support. "
                f"Preferred plan: breakout only if price clears resistance with volume, or pullback if support holds."
            )
    if not any(result["rating"] in {"Strong Setup", "Setup", "Conditional"} for result in valid):
        lines.append("- No symbols met the mechanical setup threshold.")

    lines.extend(["", "## Per-Symbol Analysis", ""])
    for result in valid:
        confidence = claim_confidence(result)
        volume_participation = "n/a" if result["volume_ratio"] is None else f"{result['volume_ratio']:.2f}x"
        lines.extend(
            [
                f"### {result['symbol']} - {result['rating']}",
                "",
                f"- **As-of:** {result['last_date']}; **confidence:** {confidence}.",
                f"- **Rows used:** {result['bars_used']} after data-quality filtering.",
                f"- **Stage:** {result['stage']}.",
                f"- **Trend Template:** {result['trend_score']}/8.",
                f"- **Momentum:** 1m {fmt_pct(result['momentum_1m'])}, 3m {fmt_pct(result['momentum_3m'])}, 6m {fmt_pct(result['momentum_6m'])}.",
                f"- **Moving averages:** MA50 {fmt_price(result['ma50'])}, MA150 {fmt_price(result['ma150'])}, MA200 {fmt_price(result['ma200'])}, MA200 1m slope {fmt_pct(result['ma200_slope_1m'])}.",
                f"- **Key levels:** support {fmt_price(result['support'])}, resistance {fmt_price(result['resistance'])}, 52w high {fmt_price(result['high_52w'])}, 52w low {fmt_price(result['low_52w'])}, ATR14 {fmt_price(result['atr14'])}.",
                f"- **Participation:** 10d volume vs 50d volume {volume_participation}; 20d avg delivery {fmt_pct(result['delivery_20d'])}.",
            ]
        )
        if result["warnings"]:
            lines.append("- **Data notes:** " + " ".join(result["warnings"]))
        lines.extend(["", "**Recent pivots:**"])
        if result["pivots"]:
            pivot_text = ", ".join(
                f"{pivot.kind} {pivot.date.date().isoformat()} @ {fmt_price(pivot.price)}"
                for pivot in result["pivots"]
            )
            lines.append(f"- {pivot_text}")
        else:
            lines.append("- Not enough clean pivots in the lookback window.")
        lines.extend(
            [
                "",
                "**Scenarios:**",
                scenario_line("Current-price attempt", result["scenarios"]["current"]),
                scenario_line("Pullback attempt", result["scenarios"]["pullback"]),
                scenario_line("Breakout attempt", result["scenarios"]["breakout"]),
                "",
                "**Invalidation / risk controls:**",
                f"- Avoid fresh swing exposure if price closes below {fmt_price(result['support'])} with expanding volume, or if the broader index ETF cohort breaks below its MA50/MA150 area.",
                "- Treat ATR stops as research levels; actual position sizing should cap loss per trade before entry.",
                "",
                "**Trend checks:**",
            ]
        )
        for check in result["trend_checks"]:
            lines.append(f"- {check}")
        lines.extend(render_deep_section(result))
        lines.append("")

    lines.extend(
        [
            "## Reuse Notes",
            "",
            "Reusable script: `code/swing_analysis.py`.",
            "",
            "Example command:",
            "",
            "```powershell",
            ".venv\\Scripts\\python.exe code\\swing_analysis.py --data-dir data_nse_calculated --symbols NIFTYBEES BANKBEES MIDCAPETF HDFCSML250 ICICIBANK KOTAKBANK LT BAJAJHLDNG GILLETTE GLAXO IRFC ITC UCOBANK BANDHANBANK APOLLOHOSP EXIDEIND --output analysis1.md",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a reusable NSE swing-trading scan.")
    parser.add_argument("--data-dir", default="data_nse_calculated", type=Path)
    parser.add_argument("--symbols", nargs="+", required=True)
    parser.add_argument("--output", default="analysis1.md", type=Path)
    parser.add_argument("--lookback-days", default=504, type=int)
    parser.add_argument("--deep", action="store_true",
                        help="Enable VCP, Livermore pivotal-point, and extended SEPA analysis")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = [
        analyze_symbol(symbol.upper(), args.data_dir, args.lookback_days, deep=args.deep)
        for symbol in args.symbols
    ]
    markdown = render_markdown(results, args.lookback_days)
    args.output.write_text(markdown, encoding="utf-8")
    mode = " (deep mode)" if args.deep else ""
    print(f"Wrote {args.output} for {len(results)} symbols{mode}")


if __name__ == "__main__":
    main()
