def pivot_index(numbers: list[int]) -> int:
    """Find the leftmost index where the sum to the left equals the sum to the right.

    Args:
        numbers: The integers to scan. This list must not be modified.

    Returns:
        The leftmost pivot index, or -1 if no pivot index exists.
    """
    total = sum(numbers)
    left_sum = 0

    for i, num in enumerate(numbers):
        if left_sum == total - left_sum - num:
            return i

        left_sum += num

    return -1