import time

from solution import find_index

SIZE = 1_000_000
LARGE_NUMS = list(range(0, SIZE * 2, 2))  # 0, 2, 4, ... so all odd values are missing
SEARCH_COUNT = 1000


# --- Examples from the README ---


def test_target_in_the_middle_area():
    assert find_index([1, 3, 5, 7, 9, 11], 7) == 3


def test_target_is_first_value():
    assert find_index([1, 3, 5, 7, 9, 11], 1) == 0


def test_target_is_last_value():
    assert find_index([1, 3, 5, 7, 9, 11], 11) == 5


def test_target_between_two_values():
    assert find_index([1, 3, 5, 7, 9, 11], 6) == -1


def test_target_above_the_largest_value():
    assert find_index([1, 3, 5, 7, 9, 11], 12) == -1


def test_empty_list():
    assert find_index([], 4) == -1


# --- Edge cases ---


def test_target_below_the_smallest_value():
    assert find_index([1, 3, 5, 7, 9, 11], 0) == -1


def test_single_value_found():
    assert find_index([4], 4) == 0


def test_single_value_target_too_small():
    assert find_index([4], 3) == -1


def test_single_value_target_too_big():
    assert find_index([4], 5) == -1


def test_two_values_target_is_first():
    assert find_index([2, 4], 2) == 0


def test_two_values_target_is_last():
    # With a wrong update such as left = middle, this one loops forever.
    assert find_index([2, 4], 4) == 1


def test_two_values_target_between_them():
    assert find_index([2, 4], 3) == -1


def test_negative_values():
    assert find_index([-9, -4, 0, 3, 8], -4) == 1


def test_target_is_zero():
    assert find_index([-9, -4, 0, 3, 8], 0) == 2


def test_only_negative_values_with_missing_target():
    assert find_index([-9, -7, -5], -6) == -1


def test_gaps_between_values():
    assert find_index([1, 100, 10000, 1000000], 10000) == 2


def test_every_position_in_lists_of_many_sizes():
    # Off-by-one mistakes often appear only for some list sizes and positions.
    for length in range(21):
        nums = list(range(0, length * 2, 2))

        for index, value in enumerate(nums):
            assert find_index(nums, value) == index

        for missing in range(-1, length * 2, 2):
            assert find_index(nums, missing) == -1


# --- Performance ---
# One search is fast even with a simple loop, so these tests run many searches.


def test_performance_targets_near_the_end():
    # A simple loop, "in" or .index() must read almost the whole list every time.
    start = time.perf_counter()
    results = [find_index(LARGE_NUMS, LARGE_NUMS[i]) for i in range(SIZE - SEARCH_COUNT, SIZE)]
    elapsed = time.perf_counter() - start

    assert results == list(range(SIZE - SEARCH_COUNT, SIZE))
    assert elapsed < 1


def test_performance_missing_targets():
    start = time.perf_counter()
    results = [
        find_index(LARGE_NUMS, LARGE_NUMS[i] + 1) for i in range(SIZE - SEARCH_COUNT, SIZE)
    ]
    elapsed = time.perf_counter() - start

    assert results == [-1] * SEARCH_COUNT
    assert elapsed < 1


def test_performance_targets_near_the_start():
    # A simple loop is fast here, but copying slices of the list at each step is not.
    start = time.perf_counter()
    results = [find_index(LARGE_NUMS, LARGE_NUMS[i]) for i in range(SEARCH_COUNT)]
    elapsed = time.perf_counter() - start

    assert results == list(range(SEARCH_COUNT))
    assert elapsed < 1
