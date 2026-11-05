def max_window_sum(nums: list[int], k: int) -> int | None:
    """Find the largest sum of k items that are next to each other.

    Args:
        nums: The list of integers. It must not be changed.
        k: The size of the window, at least 1.

    Returns:
        The largest window sum, or None if nums has fewer than k items.
    """
    
    if k > len(nums):
        return None

    current_sum = sum(nums[:k])
    largest_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        largest_sum = max(largest_sum, current_sum)

    return largest_sum
