import time

from solution import two_sum


# --- Examples from the README ---


def test_pair_at_the_end():
    assert two_sum([3, 8, 1, 6], 7) == (2, 3)


def test_pair_with_a_gap():
    assert two_sum([11, 2, 15, 7], 9) == (1, 3)


def test_same_value_twice():
    assert two_sum([3, 5, 3], 6) == (0, 2)


def test_number_cannot_pair_with_itself():
    assert two_sum([3, 2, 4], 6) == (1, 2)


# --- Edge cases ---


def test_two_numbers_only():
    assert two_sum([5, 1], 6) == (0, 1)


def test_pair_at_both_ends():
    assert two_sum([1, 8, 9, 4], 5) == (0, 3)


def test_duplicates_outside_the_pair():
    assert two_sum([5, 5, 1, 2], 3) == (2, 3)


def test_negative_numbers():
    assert two_sum([4, -2, 9, -6], 2) == (0, 1)


def test_negative_target():
    assert two_sum([5, -3, 8, -4], -7) == (1, 3)


def test_target_is_zero():
    assert two_sum([-3, 7, 3], 0) == (0, 2)


# --- Performance ---


def test_performance_large_list():
    # The pair is at the very end, so trying every pair takes far too long.
    numbers = list(range(20000, 0, -1))

    start = time.perf_counter()
    result = two_sum(numbers, 3)
    elapsed = time.perf_counter() - start

    assert result == (19998, 19999)
    assert elapsed < 1
