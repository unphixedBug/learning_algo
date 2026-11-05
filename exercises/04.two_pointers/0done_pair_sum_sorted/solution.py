def pair_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """Return the indices of the two numbers that add up to target.

    Args:
        numbers: The integers, sorted in increasing order.
        target: The sum to reach.

    Returns:
        The indices (i, j) of the two numbers, with i < j.
    """
    i, j = 0, len(numbers) - 1

    while i < j:
        current = numbers[i] + numbers[j]

        if current == target:
            return (i, j)
        elif current > target:
            j -= 1
        else:
            i += 1