import random
import time

from solution import assign_cookies


def try_every_assignment(appetites: list[int], cookies: list[int]) -> int:
    """Find the best answer by trying everything, to check the answers independently.

    The first child either gets nothing or gets one of the cookies that fit. This is
    far too slow for big lists, and it is not the greedy approach you are asked to write.
    """
    if not appetites:
        return 0

    first, *others = appetites
    best = try_every_assignment(others, cookies)

    for index, cookie in enumerate(cookies):
        if cookie >= first:
            remaining = cookies[:index] + cookies[index + 1:]
            best = max(best, 1 + try_every_assignment(others, remaining))

    return best


# --- Examples from the README ---


def test_not_enough_cookies():
    assert assign_cookies([1, 2, 3], [1, 1]) == 1


def test_more_cookies_than_children():
    assert assign_cookies([1, 2], [1, 2, 3]) == 2


def test_a_bad_choice_costs_a_child():
    assert assign_cookies([1, 5], [5, 1]) == 2


def test_lists_not_sorted():
    assert assign_cookies([4, 1, 3], [2, 5, 1]) == 2


def test_no_cookies():
    assert assign_cookies([1, 2], []) == 0


# --- Bigger examples ---


def test_question_from_the_readme():
    assert assign_cookies([2, 4, 7], [1, 3, 5, 8]) == 3


def test_lists_in_opposite_orders():
    assert assign_cookies([10, 9, 8, 7], [5, 6, 7, 8]) == 2


def test_smallest_cookies_are_useless():
    assert assign_cookies([5, 5], [1, 2, 3, 5, 5]) == 2


def test_hungriest_child_cannot_be_happy():
    assert assign_cookies([1, 2, 100], [2, 3, 4]) == 2


def test_matches_trying_every_assignment():
    rng = random.Random(42)

    for _ in range(300):
        appetites = [rng.randint(1, 8) for _ in range(rng.randint(0, 5))]
        cookies = [rng.randint(1, 8) for _ in range(rng.randint(0, 5))]

        assert assign_cookies(appetites, cookies) == try_every_assignment(
            appetites, cookies
        ), f"appetites={appetites}, cookies={cookies}"


# --- Edge cases ---


def test_no_children():
    assert assign_cookies([], [1, 2]) == 0


def test_no_children_and_no_cookies():
    assert assign_cookies([], []) == 0


def test_no_cookie_is_big_enough():
    assert assign_cookies([5, 6], [1, 2, 3]) == 0


def test_exact_fit_makes_a_child_happy():
    assert assign_cookies([2], [2]) == 1


def test_a_cookie_cannot_be_used_twice():
    assert assign_cookies([1, 1, 1], [1]) == 1


def test_a_child_cannot_eat_two_cookies_to_be_happy():
    assert assign_cookies([5], [2, 3]) == 0


def test_identical_values():
    assert assign_cookies([2, 2], [2, 2]) == 2


def test_largest_values():
    assert assign_cookies([1_000_000_000], [1_000_000_000]) == 1


def test_input_lists_are_not_modified():
    appetites = [3, 1, 2]
    cookies = [2, 3, 1]

    assign_cookies(appetites, cookies)

    assert appetites == [3, 1, 2]
    assert cookies == [2, 3, 1]


# --- Performance ---
# A solution comparing each child with each cookie fails the first test below, after
# a few seconds. It could run for minutes on the second one, so run the tests with
# `pytest -x`, or stop them with Ctrl+C.


def test_performance_no_cookie_fits():
    appetites = [2_000_000] * 10_000
    cookies = [1] * 10_000

    start = time.perf_counter()
    result = assign_cookies(appetites, cookies)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1


def test_performance_largest_lists():
    rng = random.Random(42)
    appetites = list(range(1, 100_001))
    cookies = list(range(1, 100_001))
    rng.shuffle(appetites)
    rng.shuffle(cookies)

    start = time.perf_counter()
    result = assign_cookies(appetites, cookies)
    elapsed = time.perf_counter() - start

    assert result == 100_000
    assert elapsed < 1
