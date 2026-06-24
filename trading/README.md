# AI Trading Knowledge Wiki

This repository is a stock-trading knowledge vault built around the LLM wiki pattern described in [llm-wiki.md](llm-wiki.md).

The vault has three layers:

- `raw/` stores immutable source material: articles, filings, reports, datasets, transcripts, charts, and trade-journal exports.
- `wiki/` stores the LLM-maintained knowledge base: source notes, company pages, concepts, strategies, comparisons, syntheses, and trading lessons.
- `AGENTS.md` is the schema and operating manual for future LLM sessions.

## How To Use

1. Add one source at a time to the relevant folder under `raw/`.
2. Ask the LLM to ingest that source.
3. Review the generated source note and updated wiki pages.
4. Ask questions against the wiki; useful answers should be saved back into `wiki/syntheses/` or another appropriate wiki folder.
5. Periodically ask for a lint pass to find contradictions, stale claims, orphan pages, and missing source coverage.

This vault is for research and education. Treat all trading-related conclusions as hypotheses unless they are supported by cited evidence, dated market context, and risk analysis.

## Sample Instruction

/preprocessed-pdf-wiki-ingest Ingest `raw/inbox/<folder>/` into this trading wiki. 
First produce the Proposed Ingest Plan and wait for my confirmation before creating or updating any wiki files. 
Preserve all raw image/asset links appropriately.

