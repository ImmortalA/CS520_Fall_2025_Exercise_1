def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            i = seen[need]
            if i < j:
                return (i, j)
        if x not in seen:
            seen[x] = j
    return (-1, -1)


