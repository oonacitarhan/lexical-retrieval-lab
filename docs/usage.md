# Usage

Run from the repository root with Python 3.10 or newer. No runtime dependencies are required.

```sh
python3 -m lexrank examples/corpus.json "quantum photons"
python3 -m lexrank examples/corpus.json --evaluate examples/queries.json
```

The CLI prints JSON so results can be archived or consumed by another tool. Use `--help` for options.
