import time
import tracemalloc

from solution import remove_duplicates


def check(nums: list[int], expected: list[int]) -> None:
    k = remove_duplicates(nums)

    assert k == len(expected)
    assert nums[:k] == expected


# --- Examples from the README ---


def test_some_duplicates():
    check([1, 1, 2, 3, 3], [1, 2, 3])


def test_no_duplicates():
    check([2, 5, 9], [2, 5, 9])


def test_only_one_distinct_value():
    check([7, 7, 7, 7], [7])


def test_empty_list():
    check([], [])


# --- Edge cases ---


def test_single_item():
    check([4], [4])


def test_two_identical_items():
    check([4, 4], [4])


def test_two_different_items():
    check([4, 5], [4, 5])


def test_duplicates_only_at_the_start():
    check([1, 1, 1, 2, 3], [1, 2, 3])


def test_duplicates_only_at_the_end():
    check([1, 2, 3, 3, 3], [1, 2, 3])


def test_negative_numbers_and_zero():
    check([-3, -3, -1, 0, 0, 2], [-3, -1, 0, 2])


def test_groups_of_different_sizes():
    check([0, 0, 0, 0, 1, 2, 2, 3, 3, 3], [0, 1, 2, 3])


# --- Performance ---


def test_performance_half_are_duplicates():
    # Removing the duplicates one by one shifts the rest of the list each
    # time, which takes far too long.
    nums = [i // 2 for i in range(400000)]

    start = time.perf_counter()
    k = remove_duplicates(nums)
    elapsed = time.perf_counter() - start

    assert k == 200000
    assert nums[:k] == list(range(200000))
    assert elapsed < 1


def test_performance_no_duplicates():
    nums = list(range(400000))

    start = time.perf_counter()
    k = remove_duplicates(nums)
    elapsed = time.perf_counter() - start

    assert k == 400000
    assert nums == list(range(400000))
    assert elapsed < 1


# --- Extra memory ---


def test_uses_no_extra_list_or_set():
    # A copy of this list would need more than 3 MB.
    nums = list(range(400000))

    tracemalloc.start()
    remove_duplicates(nums)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert peak < 100_000
