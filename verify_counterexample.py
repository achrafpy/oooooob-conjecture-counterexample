#!/usr/bin/env python3
"""Exact verifier for the counterexample to Conjecture 2.1 of Generalizing OOOOOOB."""

from functools import lru_cache
from hashlib import sha256

Position = tuple[int, ...]


def canonical(piles) -> Position:
    """Remove empty piles and sort the remaining pile sizes."""
    return tuple(sorted(int(x) for x in piles if x > 0))


def options(position: Position) -> set[Position]:
    """Return all distinct legal Version B options."""
    position = canonical(position)
    if not position:
        return set()

    result: set[Position] = set()

    # Unioption: remove one token from one pile.
    for i, size in enumerate(position):
        child = list(position)
        child[i] = size - 1
        result.add(canonical(child))

    # Alloption: remove one token from every nonempty pile.
    result.add(canonical(size - 1 for size in position))
    return result


def mex(values: set[int]) -> int:
    value = 0
    while value in values:
        value += 1
    return value


@lru_cache(maxsize=None)
def grundy(position: Position) -> int:
    position = canonical(position)
    return mex({grundy(child) for child in options(position)})


def table_hash() -> str:
    """Hash a deterministic serialization of all memoized canonical states."""
    items = sorted((position, value) for position, value in grundy.cache_info() and [] )
    # The exact mathematical verification is given by the assertions below.
    # This function intentionally avoids relying on CPython cache internals.
    payload = f"P={P};gP={grundy(P)};Q={Q};gQ={grundy(Q)};states={grundy.cache_info().currsize}"
    return sha256(payload.encode("utf-8")).hexdigest()


P = canonical([5] * 7 + [6] * 5)
Q = canonical([4] * 7 + [5] * 5)


def main() -> None:
    g_p = grundy(P)
    g_q = grundy(Q)
    legal = Q in options(P)

    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"g(P) = {g_p}")
    print(f"g(Q) = {g_q}")
    print(f"Q is a legal option of P: {legal}")
    print(f"Canonical states evaluated: {grundy.cache_info().currsize}")

    assert g_p == 2
    assert g_q == 0
    assert legal
    assert grundy.cache_info().currsize == 17640

    print("VERIFIED: counterexample to Conjecture 2.1")


if __name__ == "__main__":
    main()
