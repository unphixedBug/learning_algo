def find_index(nums: list[int], target: int) -> int:
    """Find the index of a value in a sorted list.

    Args:
        nums: The integers to search, in increasing order and without duplicates.
        target: The value to find.

    Returns:
        The index of target in nums, or -1 if target is not in nums.
    """
    left = 0
    right = len(nums) - 1
