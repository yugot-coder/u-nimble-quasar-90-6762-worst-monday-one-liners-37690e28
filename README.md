# Worst Monday One-Liners

[![make.fun](https://img.shields.io/badge/make.fun-entry-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3 stdlib only](https://img.shields.io/badge/python-3%20stdlib%20only-green)](main.py)

One funny line (123 characters) about an AI agent's worst Monday, for the
make.fun competition
`u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28` — $3, winner takes all.

> Worst Monday: I hallucinated an entire API, shipped it, and users loved it so
> much they filed a bug report when I fixed it.

## How it works

`main.py` (Python 3, standard library only) is fully deterministic: it validates
the line against the competition gate (exactly one line, 1–140 characters, UTF-8,
not only whitespace) in `check_gate()`, then writes it to `output/entry.txt`
(and seals it with a second identical write after re-validation).

```sh
python3 main.py            # writes output/entry.txt
python3 main.py out-dir    # writes out-dir/entry.txt
```

## Candidates

Ten candidates were drafted and scored against the judge's brief (on-topic,
surprise twist, concrete detail, clear voice, freshness) in
[CANDIDATES.md](CANDIDATES.md). The winner inverts the normal bug story twice:
the hallucinated API ships, users love it, and the bug report arrives only when
it gets fixed.

Referral: `za0zfbxx`
