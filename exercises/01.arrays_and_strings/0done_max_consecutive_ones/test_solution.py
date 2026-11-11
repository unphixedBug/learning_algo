import time

from solution import max_consecutive_ones


# --- Examples from the README ---


def test_several_runs():
    assert max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3


def test_every_run_has_size_one():
    assert max_consecutive_ones([1, 0, 1, 0, 1]) == 1


def test_no_one_at_all():
    assert max_consecutive_ones([0, 0, 0]) == 0


def test_a_single_run_with_no_zero():
    assert max_consecutive_ones([1, 1, 1, 1]) == 4


def test_empty_list():
    assert max_consecutive_ones([]) == 0


# --- Edge cases ---


def test_single_item_one():
    assert max_consecutive_ones([1]) == 1


def test_single_item_zero():
    assert max_consecutive_ones([0]) == 0


def test_longest_run_is_first():
    assert max_consecutive_ones([1, 1, 1, 0, 1]) == 3


def test_longest_run_is_last():
    assert max_consecutive_ones([1, 0, 1, 1, 1]) == 3


def test_longest_run_is_in_the_middle():
    assert max_consecutive_ones([1, 0, 1, 1, 1, 0, 1]) == 3


def test_starts_with_zero():
    assert max_consecutive_ones([0, 1, 1]) == 2


def test_ends_with_zero():
    assert max_consecutive_ones([1, 1, 0]) == 2


def test_nums_is_not_modified():
    nums = [1, 1, 0, 1, 1, 1]

    max_consecutive_ones(nums)

    assert nums == [1, 1, 0, 1, 1, 1]


# --- Performance ---


def test_performance_alternating():
    # Every run has size 1, so this checks the scan stays O(n), not O(n^2).
    nums = [i % 2 for i in range(400000)]

    start = time.perf_counter()
    result = max_consecutive_ones(nums)
    elapsed = time.perf_counter() - start

    assert result == 1
    assert elapsed < 1


def test_performance_one_huge_run():
    nums = [1] * 400000

    start = time.perf_counter()
    result = max_consecutive_ones(nums)
    elapsed = time.perf_counter() - start

    assert result == 400000
    assert elapsed < 1


def test_performance_all_zeros():
    nums = [0] * 400000

    start = time.perf_counter()
    result = max_consecutive_ones(nums)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1
