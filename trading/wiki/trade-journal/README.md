---
type: index
status: seed
created: 2026-06-13
updated: 2026-07-03
tags: [trade-journal]
sources: []
confidence: low
---

# Trade Journal

LLM-written analysis sessions, trade records, and lessons.

## Subfolders

- **`analysis/YYYY-MM/`** - Pre-trade chart analysis sessions. One page per day reviewed, named `YYYY-MM-DD-swing-review.md`. Contains stage diagnoses, trend template checks, R/R scenarios, and verdicts. Links to [watchlist.md](../watchlist.md).
- **`trades/all-trades-YYYY.md`** - Compact annual actual-trade ledger. Each row records position, stock code, direction, quantity, buy/sell details, P&L, and remarks.
- **`trades/YYYY-MM/<stock-code>.md`** - Monthly narrative detail pages linked from the annual ledger's `stock_code` column. These hold planned thesis, actual execution notes, rule adherence, and lessons. Uses `wiki/_templates/trade-review.md`.

Analysis sessions and trade narratives use month-level subfolders (`YYYY-MM/`) for organization.

Do not store the only copy of a raw trade record here; `raw/trade-journal/` holds the immutable source exports.
