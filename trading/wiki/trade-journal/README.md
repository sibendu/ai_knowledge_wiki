---
type: index
status: seed
created: 2026-06-13
updated: 2026-06-13
tags: [trade-journal]
sources: []
confidence: low
---

# Trade Journal

LLM-written analysis sessions, trade records, and lessons. Two distinct subfolders:

## Subfolders

- **`analysis/YYYY-MM/`** — Pre-trade chart analysis sessions. One page per day reviewed, named `YYYY-MM-DD-swing-review.md`. Contains stage diagnoses, trend template checks, R/R scenarios, and verdicts. Links to [watchlist.md](../watchlist.md).
- **`trades/YYYY-MM/`** — Actual trade records. One page per trade, named `YYYY-MM-DD-ticker-direction.md`. Created when a watchlist item is triggered (entry condition met). Uses `wiki/_templates/trade-review.md`.

Both use month-level subfolders (`YYYY-MM/`) for organization.

Do not store the only copy of a raw trade record here; `raw/trade-journal/` holds the immutable source exports.
