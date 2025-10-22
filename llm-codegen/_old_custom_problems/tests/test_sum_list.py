from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[list[int]], int]) -> Tuple[int, int]:
    cases = [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 6),
        ([-1, 1, -2, 2], 0),
        ([10**6, 10**6], 2 * 10**6),
    ]
    passed = 0
    for inp, expected in cases:
        try:
            out = func(inp)
        except Exception:
            out = None
        if out == expected:
            passed += 1
    return passed, len(cases)



