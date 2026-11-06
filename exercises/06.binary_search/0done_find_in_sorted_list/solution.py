def find_index(nums: list[int], target: int) -> int:
    """Find the index of a value in a sorted list.

    Args:
        nums: The integers to search, in increasing order and without duplicates.
        target: The value to find.

    Returns:
        The index of target in nums, or -1 if target is not in nums.
    """
    
    index_target = -1

    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2
        middle_num = nums[middle]

        if middle_num > target:
            right = middle
        elif middle_num < target:
            left = middle + 1
        else:
            return middle

    return -1
