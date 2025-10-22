def matrix_transpose(m: list[list[int]]) -> list[list[int]]:
    if not m:
        return []
    return [list(row) for row in zip(*m)]




