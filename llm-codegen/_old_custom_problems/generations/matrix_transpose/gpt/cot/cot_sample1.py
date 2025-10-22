from typing import List


def matrix_transpose(mat: List[List[int]]) -> List[List[int]]:
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]


