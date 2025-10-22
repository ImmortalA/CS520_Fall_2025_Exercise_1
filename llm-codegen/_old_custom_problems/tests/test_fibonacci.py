from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[int], int]) -> Tuple[int, int]:
    cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (7, 13),
        (10, 55),
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



