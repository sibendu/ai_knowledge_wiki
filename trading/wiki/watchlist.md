---
type: watchlist
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [watchlist, swing-trading, monitoring]
confidence: medium
---

# Watchlist — Swing Trade Monitoring

Living dashboard for instruments under active monitoring. Updated after each chart analysis session.

**Query:** Read this file when asked "which stocks should I check today / this week?" — filter Active rows where `Check-back` ≤ today's date.

---

## Active

| Instrument | Type | Flagged | Stage at Flag | Verdict | Entry Condition | Check-back | Analysis |
|-----------|------|---------|--------------|---------|----------------|-----------|----------|
| Bajaj Finance Investments & Holding (~10,599) | Stock (NSE) | 2026-06-25 | Stage 4 → early Stage 1 | Watchlist | Base builds 5–10 weeks; 200-day MA flattens; VCP forms | 2026-07-23 | [2026-06-25](trade-journal/analysis/2026-06/2026-06-25-swing-review.md) |
| BANKBEES (~601.92) | ETF (NSE) | 2026-06-25 | Stage 4 → recovering | Conditional | Pullback to 570–580 (3:1 R/R) OR close >610 on vol >normal (2.3:1 R/R) | 2026-07-09 | [2026-06-25](trade-journal/analysis/2026-06/2026-06-25-swing-review.md) |
| NIFTYBEES | Index ETF (NSE) | 2026-06-25 | Stage 4 → early Stage 1 | Conditional | Pullback to 265–267 (3:1 R/R) OR close >280 on vol >6–7M (2:1 R/R) | 2026-07-09 | [2026-06-25](trade-journal/analysis/2026-06/2026-06-25-swing-review.md) |
| HUL | Stock (NSE) | 2026-06-25 | Stage 4 confirmed | Strong Avoid | Re-evaluate only after 200-day MA flattens and earnings show re-acceleration | 2026-09-25 | [2026-06-25](trade-journal/analysis/2026-06/2026-06-25-swing-review.md) |

---

## Closed

| Instrument | Flagged | Closed | Outcome | Notes |
|-----------|---------|--------|---------|-------|
| — | — | — | — | — |

---

## Status Key

| Status | Meaning |
|--------|---------|
| Watchlist | Avoid now; revisit on check-back date to see if base is forming |
| Conditional | Valid recovery thesis; better entry levels identified — wait for trigger |
| Strong Avoid | Stage 4 structural decline; no setup exists; long check-back date |
| Triggered | Entry condition met; position opened — move to trades journal |
| Closed-Win | Position closed profitably |
| Closed-Loss | Position closed at stop |
| Closed-NoTrade | Watched and passed — did not meet entry criteria by expiry |

---

## Workflow

- **After chart analysis session:** add new rows to Active; update any existing rows whose stage or verdict changed.
- **When check-back fires:** re-run chart analysis, update stage/verdict/check-back, or close the row.
- **When entry triggered:** change status to Triggered; create a trade record under `wiki/trade-journal/trades/YYYY-MM/`.
- **When position closes:** move row to Closed with outcome.
