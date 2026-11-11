def max_consecutive_ones(nums: list[int]) -> int:
    """Find the length of the longest run of consecutive 1s.

    Args:
        nums: A list containing only 0s and 1s.

    Returns:
        The length of the longest run of consecutive 1s, or 0 if there is none.
    """
    record = 0
    current = 0

    for num in nums:
        if num == 0:
            current = 0
        else:
            current += 1

        record = max(record, current)

    return record