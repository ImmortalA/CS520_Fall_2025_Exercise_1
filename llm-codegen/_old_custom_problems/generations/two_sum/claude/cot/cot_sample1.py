def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    # BUG: Returns values instead of indices and fails when no solution
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return (-1, -1)


