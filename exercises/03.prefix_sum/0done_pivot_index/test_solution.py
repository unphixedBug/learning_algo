import time

from solution import pivot_index


# --- Examples from the README ---


def test_pivot_in_the_middle():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3


def test_no_pivot_exists():
    assert pivot_index([1, 2, 3]) == -1


def test_pivot_at_first_index():
    assert pivot_index([2, 1, -1]) == 0


# --- Edge cases ---


def test_empty_list():
    assert pivot_index([]) == -1


def test_single_element():
    assert pivot_index([5]) == 0


def test_pivot_at_last_index():
    assert pivot_index([1, -1, 0]) == 2


def test_all_zeros_returns_leftmost_index():
    assert pivot_index([0, 0, 0, 0]) == 0


def test_leftmost_pivot_is_returned_when_several_exist():
    assert pivot_index([0, 0, 0]) == 0


def test_negative_numbers():
    assert pivot_index([-1, -7, -3, -6, -5, -6]) == 3


def test_numbers_are_not_modified():
    numbers = [1, 7, 3, 6, 5, 6]

    pivot_index(numbers)

    assert numbers == [1, 7, 3, 6, 5, 6]


# --- Performance ---


def test_performance_large_list_without_pivot():
    # Re-slicing and re-summing both sides for every index would be O(n^2),
    # which is far too slow here.
    numbers = list(range(1, 100001))

    start = time.perf_counter()
    result = pivot_index(numbers)
    elapsed = time.perf_counter() - start

    assert result == -1
    assert elapsed < 1


def test_performance_large_list_with_pivot_near_the_end():
    numbers = [0] * 99999 + [99999]

    start = time.perf_counter()
    result = pivot_index(numbers)
    elapsed = time.perf_counter() - start

    assert result == 99999
    assert elapsed < 1
