from __future__ import annotations

from typing import Callable, Tuple


def run_tests(func: Callable[[str], bool]) -> Tuple[int, int]:
    cases = [
        ("", True),
        ("a", True),
        ("ab", False),
        ("A man, a plan, a canal: Panama", True),
        ("No 'x' in Nixon", True),
        ("hello", False),
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



