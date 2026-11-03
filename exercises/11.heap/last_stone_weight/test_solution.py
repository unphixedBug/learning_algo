import time

from solution import last_stone_weight


# --- Examples from the README ---


def test_example_from_readme():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_single_stone():
    assert last_stone_weight([1]) == 1


# --- Edge cases ---


def test_two_equal_stones_destroy_each_other():
    assert last_stone_weight([5, 5]) == 0


def test_two_different_stones():
    assert last_stone_weight([3, 7]) == 4


def test_all_stones_equal_weight():
    assert last_stone_weight([2, 2, 2, 2]) == 0


def test_already_sorted_ascending():
    assert last_stone_weight([1, 2, 3, 4, 5]) == 1


def test_single_large_stone_value():
    assert last_stone_weight([1000]) == 1000


# --- Performance ---


def test_performance_max_size():
    # 30 stones at the maximum weight: still must resolve well under a second.
    stones = [1000] * 30

    start = time.perf_counter()
    result = last_stone_weight(stones)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1
