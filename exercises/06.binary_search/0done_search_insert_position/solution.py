def search_insert(nums: list[int], target: int) -> int:
    """Find the index of target in a sorted list, or where it should be inserted.

    Args:
        nums: The integers to search, in increasing order and without duplicates.
        target: The value to find.

    Returns:
        The index of target in nums if it is there. Otherwise, the index where
        target should be inserted to keep nums sorted.
    """
    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle

    return (left + right) // 2