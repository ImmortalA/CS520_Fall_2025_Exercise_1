from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[int], int]) -> Tuple[int, int]:
    cases = [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
        (8, 40320),
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



