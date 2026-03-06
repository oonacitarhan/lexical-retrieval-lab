# Architecture

The index stores term counts, document frequencies, and lengths. BM25 scores use length normalization and positive inverse document frequency. Separate corpus utilities handle chunking and JSON persistence; evaluation computes MRR and recall from explicit relevance judgments.

## Data flow

- `lexrank/core.py` — algorithm primitives.
- `lexrank/features.py` — experiment and analysis APIs.
- `lexrank/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## Limits

ASCII tokenization and exact lexical matching do not capture semantic similarity. This is a retrieval baseline, not a generative RAG system; it never calls an LLM or fabricates answer text.
