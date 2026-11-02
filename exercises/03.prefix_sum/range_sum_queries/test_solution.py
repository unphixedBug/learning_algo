import time

from solution import range_sum_queries


# --- Examples from the README ---


def test_basic_ranges():
    numbers = [2, 4, 6, 8, 10]
    queries = [(0, 2), (1, 3), (0, 4)]
    assert range_sum_queries(numbers, queries) == [12, 18, 30]


def test_single_element_range():
    numbers = [5, 1, 9, 3]
    queries = [(2, 2)]
    assert range_sum_queries(numbers, queries) == [9]


def test_repeated_query():
    numbers = [1, 2, 3, 4]
    queries = [(0, 3), (0, 3), (1, 2)]
    assert range_sum_queries(numbers, queries) == [10, 10, 5]


# --- Edge cases ---


def test_single_number_array():
    numbers = [7]
    queries = [(0, 0)]
    assert range_sum_queries(numbers, queries) == [7]


def test_full_array_range():
    numbers = [3, 1, 4, 1, 5]
    queries = [(0, 4)]
    assert range_sum_queries(numbers, queries) == [14]


def test_negative_numbers():
    numbers = [4, -2, 9, -6, 3]
    queries = [(0, 1), (1, 3), (3, 4)]
    assert range_sum_queries(numbers, queries) == [2, 1, -3]


def test_no_queries():
    numbers = [1, 2, 3]
    queries = []
    assert range_sum_queries(numbers, queries) == []


def test_many_overlapping_queries():
    numbers = [1, 2, 3, 4, 5]
    queries = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    assert range_sum_queries(numbers, queries) == [1, 3, 6, 10, 15]


# --- Performance ---


def test_performance_many_queries_on_large_array():
    # Each query spans the whole array. Re-summing the range for every
    # query would be O(n * q), which is far too slow here.
    n = 100000
    numbers = list(range(1, n + 1))
    expected_total = n * (n + 1) // 2
    queries = [(0, n - 1)] * 100000

    start = time.perf_counter()
    result = range_sum_queries(numbers, queries)
    elapsed = time.perf_counter() - start

    assert result == [expected_total] * 100000
    assert elapsed < 1
