# Counterexample to Conjecture 2.1 of *Generalizing OOOOOOB*

This repository contains a computational counterexample for Version B of Conjecture 2.1 in *Generalizing OOOOOOB*.

## Counterexample

Consider

\[
P=(5,5,5,5,5,5,5,6,6,6,6,6)=(5^7,6^5).
\]

For `k = 12`,

\[
m=\lceil k/3\rceil=4.
\]

Every pile has more than four tokens and exactly seven piles are odd, so the conjecture classifies `P` as losing.

However, the legal move

\[
(5^7,6^5)\longrightarrow(4^7,5^5)=Q
\]

gives

\[
g(P)=2,\qquad g(Q)=0.
\]

Therefore `P` is winning, contradicting the conjectured classification.

## Verification

```bash
python verify_counterexample.py
```

The exhaustive computation evaluates 17,640 canonical states.

## Files

- [`COUNTEREXAMPLE.md`](COUNTEREXAMPLE.md): mathematical explanation.
- [`verify_counterexample.py`](verify_counterexample.py): exact verifier.

Original paper: [arXiv:2605.23213](https://arxiv.org/abs/2605.23213)
