#!/usr/bin/env python3

from functools import lru_cache

Position = tuple[int, ...]


def canonical(piles) -> Position:
    return tuple(sorted(int(x) for x in piles if x > 0))


def options(position: Position) -> set[Position]:
    position = canonical(position)
    if not position:
        return set()

    result: set[Position] = set()

    for i, size in enumerate(position):
        child = list(position)
        child[i] = size - 1
        result.add(canonical(child))

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


P = canonical([5] * 7 + [6] * 5)
Q = canonical([4] * 7 + [5] * 5)


def main() -> None:
    g_p = grundy(P)
    g_q = grundy(Q)
    legal = Q in options(P)
    states = grundy.cache_info().currsize

    assert g_p == 2
    assert g_q == 0
    assert legal
    assert states == 17640

    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"g(P) = {g_p}")
    print(f"g(Q) = {g_q}")
    print(f"Q is a legal option of P: {legal}")
    print(f"Canonical states evaluated: {states}")
    print("Verification completed successfully.")


if __name__ == "__main__":
    main()
