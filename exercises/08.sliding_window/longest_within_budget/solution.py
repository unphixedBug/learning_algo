def longest_within_budget(costs: list[int], budget: int) -> int:
    """Find the longest run of consecutive days that fits in the budget.

    Args:
        costs: The spending of each day, all strictly positive. It must not
            be changed.
        budget: The maximum total allowed for the run, at least 0.

    Returns:
        The largest number of consecutive days whose total is at most
        budget, or 0 if no day fits.
    """
    longest = 0
    window = []
    actual_sum = 0

    for num in costs:
        window.append(num)
        actual_sum = sum(window)

        if actual_sum <= budget:

        else: