import random
import time

from solution import search_insert


# --- Examples from the README ---


def test_target_found():
    assert search_insert([1, 3, 5, 6], 5) == 2


def test_target_missing_in_the_middle():
    assert search_insert([1, 3, 5, 6], 2) == 1


def test_target_bigger_than_everything():
    assert search_insert([1, 3, 5, 6], 7) == 4


def test_target_smaller_than_everything():
    assert search_insert([1, 3, 5, 6], 0) == 0


def test_empty_list():
    assert search_insert([], 4) == 0


# --- Edge cases ---


def test_single_item_found():
    assert search_insert([5], 5) == 0


def test_single_item_target_smaller():
    assert search_insert([5], 2) == 0


def test_single_item_target_bigger():
    assert search_insert([5], 9) == 1


def test_two_items_target_between():
    assert search_insert([1, 3], 2) == 1


def test_two_items_target_after():
    assert search_insert([1, 3], 4) == 2


def test_first_item_found():
    assert search_insert([2, 4, 6, 8, 10], 2) == 0


def test_last_item_found():
    assert search_insert([2, 4, 6, 8, 10], 10) == 4


def test_negative_numbers():
    assert search_insert([-9, -5, -1, 0, 4], -3) == 2


def test_every_position_in_a_small_list():
    # Each even value is found at its index; each odd value goes just after it.
    nums = [0, 2, 4, 6, 8]
    for index, value in enumerate(nums):
        assert search_insert(nums, value) == index
        assert search_insert(nums, value + 1) == index + 1
    assert search_insert(nums, -1) == 0


def test_returns_an_int_not_a_value():
    # The answer is a position, so it must be an int index, never None.
    result = search_insert([10, 20, 30], 25)
    assert isinstance(result, int)
    assert result == 2


def test_list_is_not_modified():
    nums = [1, 3, 5, 6]
    search_insert(nums, 4)
    assert nums == [1, 3, 5, 6]


def test_matches_a_slow_reference_on_random_lists():
    rng = random.Random(42)
    for _ in range(300):
        nums = sorted(rng.sample(range(-50, 50), rng.randint(0, 20)))
        target = rng.randint(-55, 55)
        expected = sum(1 for value in nums if value < target)
        assert search_insert(nums, target) == expected, (nums, target)


# --- Performance ---


def test_performance_many_searches_in_a_big_list():
    # 1,000,000 even numbers, 20,000 searches. A linear scan (or "in" / .index())
    # is far too slow here; O(log n) per search needs about 20 steps each.
    nums = list(range(0, 2_000_000, 2))
    rng = random.Random(7)
    targets = [rng.randint(-10, 2_000_010) for _ in range(20_000)]

    start = time.perf_counter()
    results = [search_insert(nums, target) for target in targets]
    elapsed = time.perf_counter() - start

    for target, result in zip(targets, results):
        expected = min(max((target + 1) // 2, 0), len(nums))
        assert result == expected, (target, result)
    assert elapsed < 1


def test_performance_target_at_the_far_end():
    nums = list(range(1_000_000))

    start = time.perf_counter()
    result = search_insert(nums, 2_000_000)
    elapsed = time.perf_counter() - start

    assert result == 1_000_000
    assert elapsed < 0.01
