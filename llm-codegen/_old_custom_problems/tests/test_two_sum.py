from __future__ import annotations

from typing import Callable, Tuple, List


def run_tests(func: Callable[[List[int], int], tuple[int, int]]) -> Tuple[int, int]:
    cases = [
        (([2, 7, 11, 15], 9), (0, 1)),
        (([3, 2, 4], 6), (1, 2)),
        (([3, 3], 6), (0, 1)),
        (([1, 2, 3], 7), (-1, -1)),
        (([], 5), (-1, -1)),
    ]
    passed = 0
    for (nums, target), expected in cases:
        try:
            out = func(nums, target)
        except Exception:
            out = None
        if out == expected:
            passed += 1
    return passed, len(cases)



