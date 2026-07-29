# Counterexample to Conjecture 2.1

This note records a computational counterexample for Version B of *Generalizing OOOOOOB*.

## Conjectured classification

For `k = 12`, let

\[
m=\left\lceil\frac{12}{3}\right\rceil=4.
\]

The conjecture classifies positions with seven odd piles as losing when every pile has more than four tokens.

## Counterexample

Take

\[
P=(5^7,6^5)=(5,5,5,5,5,5,5,6,6,6,6,6).
\]

All twelve piles have more than four tokens and exactly seven piles are odd, so the conjecture predicts that `P` is losing.

The legal all-piles move gives

\[
P=(5^7,6^5)\longrightarrow Q=(4^7,5^5).
\]

Exact Sprague–Grundy computation gives

\[
g(P)=2,\qquad g(Q)=0.
\]

Therefore `P` is winning and `Q` is losing. Hence `P` contradicts the conjectured classification.

## Verification

Run:

```bash
python verify_counterexample.py
```

The verifier checks the legal move, both Grundy values, and 17,640 canonical states.

Original paper: [arXiv:2605.23213](https://arxiv.org/abs/2605.23213)
