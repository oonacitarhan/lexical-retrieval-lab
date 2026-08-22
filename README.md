# Lexical Retrieval Lab

Build a BM25 passage index, save and reload a corpus, and evaluate ranked retrieval with reciprocal rank.

**Python** · Reusable core · CLI examples · Regression checks · Reproducible benchmark

> **Provenance:** created with AI assistance on **2026-11-01**.
> All commit author and committer dates are synthetic and distributed across
> November 2024–October 2026. They do not establish work on those dates.

## Quick start

```sh
python3 -m lexrank examples/corpus.json "quantum photons"
python3 -m lexrank examples/corpus.json --evaluate examples/queries.json
```

## Repository map

- `lexrank/core.py` — algorithm primitives.
- `lexrank/features.py` — experiment and analysis APIs.
- `lexrank/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload; machine-dependent measurements.

## How it works

The index stores term counts, document frequencies, and lengths. BM25 scores use length normalization and positive inverse document frequency. Separate corpus utilities handle chunking and JSON persistence; evaluation computes MRR and recall from explicit relevance judgments.

## Verification

```sh
sh scripts/check.sh
```

Eight Python test groups exercise reference cases, invalid inputs, and relevant invariants.
The complete local run is in [docs/verification.txt](docs/verification.txt).
The [checks workflow](.github/workflows/check.yml) executes the same source checks.

## Boundaries

ASCII tokenization and exact lexical matching do not capture semantic similarity. This is a retrieval baseline, not a generative RAG system; it never calls an LLM or fabricates answer text.

See [architecture](docs/architecture.md), [usage](docs/usage.md),
[release notes](CHANGELOG.md), and [provenance](PROVENANCE.json).

## License

MIT — [LICENSE](LICENSE).
