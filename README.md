# Lexical Retrieval Lab

> **Synthetic-history demo.** Created on **2026-11-01** with AI assistance.
> Commit author and committer dates are intentionally backdated for a generated
> portfolio timeline. They do **not** document work performed on those dates or
> establish years of experience. This is a new educational project.

Inspectable BM25 document retrieval with ranked passages and source attribution.

**Language:** Python · **Scope:** small, inspectable educational prototype.

## Run and verify

Requires Python 3.10+; standard library only.

```sh
python3 retrieve.py
```

The command runs the demonstration and built-in checks. Check failures produce
a nonzero exit code. Verified locally on 2026-11-01.

## Design and limits

The implementation lives in [retrieve.py](retrieve.py) so the complete
algorithm can be read in one sitting. Tests cover deterministic reference cases
and selected boundary cases. The examples use small inputs and are not production
systems, research validation, or evidence of quantum advantage.

## Provenance

The code and documentation were generated together on 2026-11-01. Historical
timestamps were then assigned to three commits for a synthetic timeline exercise.
No original repository history was rewritten. No third-party project was copied
or presented as original work. Algorithm names describe standard methods.

## License

MIT. See [LICENSE](LICENSE).
