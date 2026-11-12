import time

from solution import has_double_badge


# --- Examples from the README ---


def test_duplicate_in_the_middle():
    assert has_double_badge([12, 7, 33, 7]) is True


def test_all_different():
    assert has_double_badge([1, 2, 3, 4]) is False


def test_empty_list():
    assert has_double_badge([]) is False


def test_single_badge():
    assert has_double_badge([42]) is False


def test_duplicate_at_the_start():
    assert has_double_badge([5, 5, 8, 9, 10]) is True


# --- Edge cases ---


def test_duplicate_at_both_ends():
    assert has_double_badge([3, 1, 2, 3]) is True


def test_all_same_badge():
    assert has_double_badge([9, 9, 9, 9]) is True


def test_negative_ids():
    assert has_double_badge([-1, 0, 1, -1]) is True


def test_zero_is_a_valid_id():
    assert has_double_badge([0, 1, 2]) is False


# --- Performance ---


def test_performance_no_duplicate():
    # No duplicate: a nested-loop O(n²) solution must check every pair.
    badges = list(range(100000))

    start = time.perf_counter()
    result = has_double_badge(badges)
    elapsed = time.perf_counter() - start

    assert result is False
    assert elapsed < 1


def test_performance_duplicate_at_the_end():
    badges = list(range(100000)) + [0]

    start = time.perf_counter()
    result = has_double_badge(badges)
    elapsed = time.perf_counter() - start

    assert result is True
    assert elapsed < 1
