import time
import tracemalloc

from solution import longest_within_budget


# --- Examples from the README ---


def test_example_mixed():
    assert longest_within_budget([3, 1, 2, 7, 1, 1], 6) == 3


def test_everything_fits():
    assert longest_within_budget([1, 2, 1], 10) == 3


def test_nothing_fits():
    assert longest_within_budget([8, 9, 12], 5) == 0


def test_best_run_at_the_end():
    assert longest_within_budget([5, 5, 1, 1, 1, 1], 4) == 4


def test_empty_list():
    assert longest_within_budget([], 3) == 0


# --- Edge cases ---


def test_budget_zero():
    # Every cost is at least 1, so nothing fits.
    assert longest_within_budget([1, 1, 1], 0) == 0


def test_single_day_fits():
    assert longest_within_budget([4], 4) == 1


def test_single_day_too_expensive():
    assert longest_within_budget([5], 4) == 0


def test_total_exactly_equal_to_budget():
    # "At most" includes "equal".
    assert longest_within_budget([2, 2, 2], 6) == 3


def test_best_run_at_the_start():
    assert longest_within_budget([1, 1, 1, 9, 2], 3) == 3


def test_best_run_in_the_middle():
    assert longest_within_budget([9, 1, 1, 1, 1, 9], 4) == 4


def test_expensive_day_splits_the_list():
    # The window must become empty when 50 enters, then grow again.
    assert longest_within_budget([1, 1, 50, 1, 1, 1], 3) == 3


def test_must_remove_several_days_at_once():
    # When 6 enters, three days leave before the window is valid again.
    assert longest_within_budget([1, 1, 1, 6, 1], 7) == 3


def test_restarting_from_scratch_is_wrong():
    # Fails if the window restarts at the current day when the budget is
    # exceeded, instead of removing days on the left one by one:
    # the best run [1, 1, 1, 1] starts in the middle of [4, 1, 1].
    assert longest_within_budget([4, 1, 1, 1, 1], 5) == 4


def test_best_is_kept_when_window_shrinks():
    # Fails if the best length is replaced by the current length.
    assert longest_within_budget([1, 1, 1, 1, 5, 5], 5) == 4


def test_list_is_not_changed():
    costs = [3, 1, 2, 7, 1, 1]

    longest_within_budget(costs, 6)

    assert costs == [3, 1, 2, 7, 1, 1]


# --- Performance ---


def test_performance_long_runs():
    # Trying each start day and extending it costs about 200000 * 100000
    # steps here, which is far too slow.
    costs = [1] * 200000

    start = time.perf_counter()
    result = longest_within_budget(costs, 100000)
    elapsed = time.perf_counter() - start

    assert result == 100000
    assert elapsed < 1


def test_performance_everything_fits():
    costs = [10000] * 200000

    start = time.perf_counter()
    result = longest_within_budget(costs, 10**9)
    elapsed = time.perf_counter() - start

    assert result == 100000
    assert elapsed < 1


def test_performance_alternating_costs():
    costs = [1, 10000] * 100000

    start = time.perf_counter()
    result = longest_within_budget(costs, 50000)
    elapsed = time.perf_counter() - start

    # 4 cheap days and 4 expensive days cost 40004, one more day breaks it:
    # the best is 9 days starting with a cheap one (5 cheap + 4 expensive).
    assert result == 9
    assert elapsed < 1


def test_performance_nothing_fits():
    costs = [10000] * 200000

    start = time.perf_counter()
    result = longest_within_budget(costs, 9999)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1


# --- Extra memory ---


def test_uses_no_extra_list():
    # A copy of the list or a list of totals would need more than 1 MB.
    costs = [1] * 200000

    tracemalloc.start()
    longest_within_budget(costs, 100)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert peak < 100_000
