# A counterexample to Conjecture 2.1

This note records an exact computational counterexample to Conjecture 2.1 for Version B of *Generalizing OOOOOOB*.

## Statement under consideration

Let \(k\geq 3\) denote the number of piles and define

\[
m=\left\lceil\frac{k}{3}\right\rceil.
\]

For \(k\equiv 0\pmod 4\), the conjecture classifies a position as losing, under the stated lower bound on pile sizes, when the number of odd piles belongs to

\[
0,2,4,\ldots,\frac{k}{2}-2,\frac{k}{2}+1,\frac{k}{2}+3,\ldots,k-1.
\]

For \(k=12\), this set is

\[
\{0,2,4,7,9,11\}.
\]

## Counterexample

Consider

\[
P=(5^7,6^5)=(5,5,5,5,5,5,5,6,6,6,6,6).
\]

Here \(k=12\) and

\[
m=\left\lceil\frac{12}{3}\right\rceil=4.
\]

Every pile contains more than four tokens, and exactly seven piles are odd. The conjecture therefore classifies \(P\) as a losing position.

In Version B, removing one token from every pile is a legal move. Applied to \(P\), it gives

\[
P=(5^7,6^5)\longrightarrow Q=(4^7,5^5).
\]

The exact Sprague–Grundy computation yields

\[
g(P)=2,\qquad g(Q)=0.
\]

Thus \(Q\) is a losing position and \(P\) is a winning position. Consequently, \(P\) does not satisfy the outcome classification asserted by Conjecture 2.1.

## Computational verification

The accompanying program computes the Sprague–Grundy function recursively on canonical positions. It verifies that

\[
g(P)=2,\qquad g(Q)=0,\qquad Q\in\operatorname{Opt}(P),
\]

and evaluates exactly \(17{,}640\) canonical states.

Run:

```bash
python verify_counterexample.py
```

## Reference

A. Danai, P. Ellis and T. Aek Thanatipanonda, *Generalizing OOOOOOB*, arXiv:2605.23213v1.
