def range_sum_queries(numbers: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """Return the sum of numbers[left:right + 1] for each (left, right) query.

    Args:
        numbers: The integers to query ranges over.
        queries: Pairs of (left, right) inclusive indices.

    Returns:
        One sum per query, in the same order as queries.
    """

    prefix = [0]
    
    for num in numbers:
        prefix.append(prefix[-1] + num)
    
    return [prefix[right + 1] - prefix[left] for left, right in queries]