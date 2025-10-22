from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[str], bool]) -> Tuple[int, int]:
    cases = [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([{}])", True),
        ("([)]", False),
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




