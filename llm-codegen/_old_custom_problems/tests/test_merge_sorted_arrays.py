from __future__ import annotations

from typing import Callable, Tuple, List


def run_tests(func: Callable[[List[int], List[int]], List[int]]) -> Tuple[int, int]:
    cases = [
        (([], []), []),
        (([1], []), [1]),
        (([], [2]), [2]),
        (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
        (([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3]),
    ]
    passed = 0
    for (a, b), expected in cases:
        try:
            out = func(a, b)
        except Exception:
            out = None
        if out == expected:
            passed += 1
    return passed, len(cases)



