from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[str], str]) -> Tuple[int, int]:
    cases = [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("abc", "cba"),
        ("Hello, 世界!", "!界世 ,olleH"),
    ]
    passed = 0
    for inp, expected in cases:
        try:
            out = func(inp)
        except Exception:
            out = None  # count as failure
        if out == expected:
            passed += 1
    return passed, len(cases)



