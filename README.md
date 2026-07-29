# Exact counterexample to Conjecture 2.1 of *Generalizing OOOOOOB*

**Author of the counterexample:** Achraf El Angoudi El Haddadi  
**Verification date:** 27 July 2026  
**Original paper:** [Danai, Ellis and Aek Thanatipanonda, arXiv:2605.23213v1](https://arxiv.org/abs/2605.23213)

## Result

Conjecture 2.1 for Version B is false.

Consider the 12-pile position

\[
P=(5,5,5,5,5,5,5,6,6,6,6,6)=(5^7,6^5).
\]

For `k = 12`, the conjecture uses

\[
m=\lceil k/3\rceil=4.
\]

Every pile of `P` has more than four tokens, and exactly seven piles are odd. Since `k ≡ 0 (mod 4)`, Conjecture 2.1 classifies seven odd piles as a losing configuration.

However, the legal all-piles move

\[
(5^7,6^5)\longrightarrow(4^7,5^5)=Q
\]

leads to a losing position. Exact Sprague–Grundy computation gives

\[
g(P)=2,\qquad g(Q)=0.
\]

Therefore `P` is a winning position, contradicting the conjecture.

## Reproduce the verification

```bash
python verify_counterexample.py
```

Expected output:

```text
P = (5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6)
Q = (4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5)
g(P) = 2
g(Q) = 0
Q is a legal option of P: True
VERIFIED: counterexample to Conjecture 2.1
```

The exhaustive computation evaluates 17,640 canonical states.

## Repository contents

- [`COUNTEREXAMPLE.md`](COUNTEREXAMPLE.md): full mathematical explanation.
- [`verify_counterexample.py`](verify_counterexample.py): independent exact verifier.
- [`CITATION.cff`](CITATION.cff): citation metadata.
- Original article: [arXiv abstract](https://arxiv.org/abs/2605.23213) · [PDF](https://arxiv.org/pdf/2605.23213)

## Priority statement

I did not find a public antecedent of this exact counterexample after a broad search conducted on 27 July 2026. This does not rule out private discoveries, unindexed sources, or earlier material not found in that search.

## Citation

```bibtex
@misc{el_angoudi_2026_oooooob,
  author = {Achraf El Angoudi El Haddadi},
  title = {Exact counterexample to Conjecture 2.1 of Generalizing OOOOOOB},
  year = {2026},
  url = {https://github.com/achrafpy/oooooob-conjecture-counterexample}
}
```
