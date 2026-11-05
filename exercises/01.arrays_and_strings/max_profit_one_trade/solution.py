def max_profit(prices: list[int]) -> int:
    """Find the largest profit from buying once and selling on a later day.

    Args:
        prices: The price on each day, in order. This list must not be modified.

    Returns:
        The largest possible profit, or 0 if no trade makes money.
    """
    profit = 0

    for price in prices:
