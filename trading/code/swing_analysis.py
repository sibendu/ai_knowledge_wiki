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


def analyze_symbol(symbol: str, data_dir: Path, lookback_days: int) -> dict:
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

    return {
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
        "## Ranked Summary",
        "",
        "| Rank | Symbol | Rating | Stage | Bars | Close | 52wH dist | 52wL dist | Trend | 1m | 3m | Volume |",
        "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, result in enumerate(valid, start=1):
        volume = result["volume_ratio"]
        volume_text = "n/a" if volume is None else f"{volume:.2f}x"
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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = [
        analyze_symbol(symbol.upper(), args.data_dir, args.lookback_days)
        for symbol in args.symbols
    ]
    markdown = render_markdown(results, args.lookback_days)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"Wrote {args.output} for {len(results)} symbols")


if __name__ == "__main__":
    main()
