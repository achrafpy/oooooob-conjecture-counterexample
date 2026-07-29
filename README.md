# Counterexample to Conjecture 2.1 of *Generalizing OOOOOOB*

This repository contains an exact computational counterexample to Conjecture 2.1 for Version B of *Generalizing OOOOOOB*.

## Result

Consider the position

\[
P=(5^7,6^5)=(5,5,5,5,5,5,5,6,6,6,6,6).
\]

For \(k=12\),

\[
m=\left\lceil\frac{k}{3}\right\rceil=4.
\]

Every pile contains more than four tokens, and exactly seven piles are odd. Under Conjecture 2.1, this places \(P\) among the losing positions.

The legal all-piles move gives

\[
P=(5^7,6^5)\longrightarrow Q=(4^7,5^5).
\]

Exact Sprague–Grundy computation yields

\[
g(P)=2,\qquad g(Q)=0.
\]

Therefore \(P\) is winning, while \(Q\) is losing. This contradicts the conjectured classification.

## Verification

Run the independent verifier with Python 3.9 or later:

```bash
python verify_counterexample.py
```

The computation checks the legal move, both Grundy values, and exactly \(17{,}640\) canonical states.

## Repository contents

- [`COUNTEREXAMPLE.md`](COUNTEREXAMPLE.md): mathematical statement and verification.
- [`verify_counterexample.py`](verify_counterexample.py): exact recursive verifier.

## Reference

A. Danai, P. Ellis and T. Aek Thanatipanonda, *Generalizing OOOOOOB*, [arXiv:2605.23213v1](https://arxiv.org/abs/2605.23213).
