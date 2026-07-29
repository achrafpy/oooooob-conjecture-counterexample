# Counterexample to Conjecture 2.1

## 1. Version B of the game

A position is a finite collection of nonempty piles. A legal move is either:

1. remove one token from exactly one pile (`unioption`), or
2. remove one token from every nonempty pile (`alloption`).

The player making the last move wins. For a finite impartial game, a position is losing exactly when its Sprague–Grundy value is zero.

## 2. Relevant statement of Conjecture 2.1

Let `k ≥ 3` be the number of piles and

\[
m=\left\lceil\frac{k}{3}\right\rceil.
\]

The conjecture claims that when every pile contains more than `m` tokens, the outcome depends only on the number of odd piles. For `k ≡ 0 (mod 4)`, the conjectured losing counts are

\[
0,2,4,\ldots,\frac{k}{2}-2,\frac{k}{2}+1,\frac{k}{2}+3,\ldots,k-1.
\]

For `k=12`, this list is

\[
0,2,4,7,9,11.
\]

## 3. Exact counterexample

Take

\[
P=(5^7,6^5)=(5,5,5,5,5,5,5,6,6,6,6,6).
\]

Here:

- `k=12`;
- `m=⌈12/3⌉=4`;
- every pile has size 5 or 6, hence every pile is larger than 4;
- exactly seven piles are odd.

Thus the conjecture classifies `P` as a losing position.

## 4. Winning move

The legal alloption removes one token from all twelve piles:

\[
P=(5^7,6^5)\longrightarrow Q=(4^7,5^5).
\]

Exact recursive computation gives

\[
g(P)=2,\qquad g(Q)=0.
\]

Therefore `Q` is losing and `P` is winning. This directly contradicts Conjecture 2.1.

## 5. Local Grundy certificate

The distinct options from `P` have Grundy values:

| Move | Result | Grundy value |
|---|---|---:|
| Remove one from a pile of size 5 | `(4,5^6,6^5)` | 1 |
| Remove one from a pile of size 6 | `(5^8,6^4)` | 1 |
| Remove one from all piles | `(4^7,5^5)=Q` | 0 |

Hence

\[
g(P)=\operatorname{mex}\{0,1\}=2.
\]

The distinct options from `Q` have values:

| Move | Result | Grundy value |
|---|---|---:|
| Remove one from a pile of size 4 | `(3,4^6,5^5)` | 2 |
| Remove one from a pile of size 5 | `(4^8,5^4)` | 2 |
| Remove one from all piles | `(3^7,4^5)` | 1 |

Thus

\[
g(Q)=\operatorname{mex}\{1,2\}=0.
\]

## 6. Exact computational verification

The program [`verify_counterexample.py`](verify_counterexample.py):

- stores positions canonically as sorted tuples;
- generates every legal unioption and the alloption;
- recursively computes Grundy values using memoization;
- verifies `g(P)=2`, `g(Q)=0`, and that `Q` is a legal option of `P`;
- evaluates exactly 17,640 canonical states.

Run:

```bash
python verify_counterexample.py
```

## 7. Formal conclusion

**Proposition.** In Version B of *Generalizing OOOOOOB*, the position

\[
(5^7,6^5)
\]

is a counterexample to Conjecture 2.1.

**Proof.** The position satisfies all hypotheses of the conjecture for `k=12` and has seven odd piles, a count the conjecture classifies as losing. Nevertheless, the legal alloption reaches `(4^7,5^5)`, whose Grundy value is zero, while the initial position has Grundy value two. Therefore the initial position is winning, not losing. ∎

## 8. Source and authorship

Original conjecture:

- Alon Danai, Paul Ellis and Thotsaporn Aek Thanatipanonda, *Generalizing OOOOOOB*, arXiv:2605.23213v1, 22 May 2026.

Counterexample presented by:

- **Achraf El Angoudi El Haddadi**, verified 27 July 2026.

Priority is stated cautiously: no public antecedent of this exact counterexample was found in the search conducted on that date, but private or unindexed prior discoveries cannot be excluded.
