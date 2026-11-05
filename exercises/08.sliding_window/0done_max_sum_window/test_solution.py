import time
import tracemalloc

from solution import max_window_sum


# --- Examples from the README ---


def test_several_windows():
    assert max_window_sum([2, 1, 5, 1, 3, 2], 3) == 9


def test_window_of_one_item():
    assert max_window_sum([4, 9, 2], 1) == 9


def test_window_is_the_whole_list():
    assert max_window_sum([1, 2, 3], 3) == 6


def test_only_negative_numbers():
    assert max_window_sum([-5, -2, -8, -1], 2) == -7


def test_list_too_short():
    assert max_window_sum([1, 2], 3) is None


def test_empty_list():
    assert max_window_sum([], 1) is None


# --- Edge cases ---


def test_single_item():
    assert max_window_sum([-7], 1) == -7


def test_best_window_at_the_start():
    assert max_window_sum([9, 9, 1, 1, 1], 2) == 18


def test_best_window_at_the_end():
    # Fails if the last window is never checked.
    assert max_window_sum([1, 1, 1, 9, 9], 2) == 18


def test_best_window_in_the_middle():
    assert max_window_sum([1, 8, 9, 1, 1], 2) == 17


def test_sum_drops_then_never_recovers():
    # Fails if the best sum is replaced by the latest sum.
    assert max_window_sum([5, 5, -100, 1, 1], 2) == 10


def test_positive_and_negative_numbers():
    assert max_window_sum([3, -1, 4, -1, 5], 3) == 8


def test_best_sum_is_zero():
    # The answer is 0, which is not the same as None.
    assert max_window_sum([-1, 1, -2, 2], 2) == 0


def test_only_zeros():
    assert max_window_sum([0, 0, 0], 2) == 0


def test_whole_list_of_negative_numbers():
    assert max_window_sum([-1, -2], 2) == -3


def test_list_one_item_too_short():
    assert max_window_sum([1, 2, 3], 4) is None


def test_list_is_not_changed():
    nums = [2, 1, 5, 1, 3, 2]

    max_window_sum(nums, 3)

    assert nums == [2, 1, 5, 1, 3, 2]


# --- Performance ---


def test_performance_large_window():
    # Summing each window from scratch takes far too long here, because
    # there are 200001 windows of 200000 items each.
    nums = list(range(400000))

    start = time.perf_counter()
    result = max_window_sum(nums, 200000)
    elapsed = time.perf_counter() - start

    assert result == sum(range(200000, 400000))
    assert elapsed < 1


def test_performance_best_window_at_the_start():
    nums = list(range(400000, 0, -1))

    start = time.perf_counter()
    result = max_window_sum(nums, 200000)
    elapsed = time.perf_counter() - start

    assert result == sum(range(400000, 200000, -1))
    assert elapsed < 1


def test_performance_medium_window():
    nums = [1] * 400000

    start = time.perf_counter()
    result = max_window_sum(nums, 5000)
    elapsed = time.perf_counter() - start

    assert result == 5000
    assert elapsed < 1


def test_performance_window_of_one_item():
    nums = list(range(400000))

    start = time.perf_counter()
    result = max_window_sum(nums, 1)
    elapsed = time.perf_counter() - start

    assert result == 399999
    assert elapsed < 1


# --- Extra memory ---


def test_uses_no_extra_list():
    # A list of all the window sums would need more than 1 MB.
    nums = list(range(400000))

    tracemalloc.start()
    max_window_sum(nums, 3)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert peak < 100_000
