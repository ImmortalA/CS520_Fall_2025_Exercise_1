from __future__ import annotations

from typing import Callable, Tuple, List


def run_tests(func: Callable[[List[str]], str]) -> Tuple[int, int]:
    cases = [
        (([]), ""),
        ((["a"]), "a"),
        ((["flower", "flow", "flight"]), "fl"),
        ((["dog", "racecar", "car"]), ""),
        ((["interspecies", "interstellar", "interstate"]), "inters"),
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




