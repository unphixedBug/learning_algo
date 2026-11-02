import time

from solution import pair_sum


# --- Examples from the README ---


def test_pair_in_the_middle():
    assert pair_sum([1, 3, 4, 6, 8, 11], 10) == (2, 3)


def test_pair_at_the_start():
    assert pair_sum([2, 7, 11, 15], 9) == (0, 1)


def test_same_value_twice():
    assert pair_sum([1, 2, 2, 9], 4) == (1, 2)


# --- Edge cases ---


def test_two_numbers_only():
    assert pair_sum([2, 4], 6) == (0, 1)


def test_pair_at_both_ends():
    assert pair_sum([1, 2, 3, 10], 11) == (0, 3)


def test_pair_at_the_end():
    assert pair_sum([1, 2, 3, 4], 7) == (2, 3)


def test_negative_numbers():
    assert pair_sum([-4, -1, 2, 7], 1) == (1, 2)


def test_negative_target():
    assert pair_sum([-8, -3, 1, 4], -11) == (0, 1)


def test_target_is_zero():
    assert pair_sum([-3, 0, 3], 0) == (0, 2)


# --- Performance ---


def test_performance_large_list():
    # The pair is at the very end, so trying every pair takes far too long.
    numbers = list(range(20000))

    start = time.perf_counter()
    result = pair_sum(numbers, 39997)
    elapsed = time.perf_counter() - start

    assert result == (19998, 19999)
    assert elapsed < 1
