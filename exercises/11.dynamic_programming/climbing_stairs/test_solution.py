import time
from math import comb

from solution import count_ways


def count_with_formula(steps: int) -> int:
    """Count the ways with a math formula, to check the answers independently.

    For each possible number of 2-step moves, comb() counts where they can go among
    all the moves. This is not the DP approach you are asked to write.
    """
    return sum(comb(steps - twos, twos) for twos in range(steps // 2 + 1))


# --- Examples from the README ---


def test_single_step():
    assert count_ways(1) == 1


def test_two_steps():
    assert count_ways(2) == 2


def test_three_steps_the_order_matters():
    assert count_ways(3) == 3


def test_four_steps():
    assert count_ways(4) == 5


# --- Bigger staircases ---


def test_five_steps():
    assert count_ways(5) == 8


def test_ten_steps():
    assert count_ways(10) == 89


def test_twenty_steps():
    assert count_ways(20) == 10946


def test_all_small_staircases():
    for steps in range(1, 26):
        assert count_ways(steps) == count_with_formula(steps)


# --- Edge cases ---


def test_returns_an_integer():
    assert isinstance(count_ways(10), int)


def test_calls_do_not_affect_each_other():
    # If you keep a memory between calls, it must not change the next answers.
    assert count_ways(10) == 89
    assert count_ways(3) == 3
    assert count_ways(10) == 89


# --- Performance ---
# A plain recursive solution makes hundreds of millions of calls on the first test
# below: it can take a while, then fail. On the next ones, it would never finish, so
# run the tests with `pytest -x`, or stop them with Ctrl+C.


def test_performance_forty_steps():
    start = time.perf_counter()
    result = count_ways(40)
    elapsed = time.perf_counter() - start

    assert result == 165580141
    assert elapsed < 1


def test_performance_hundred_steps_needs_exact_integers():
    # A solution using floats would lose precision on a number this big.
    start = time.perf_counter()
    result = count_ways(100)
    elapsed = time.perf_counter() - start

    assert result == 573147844013817084101
    assert elapsed < 1


def test_performance_largest_staircase():
    expected = count_with_formula(500)

    start = time.perf_counter()
    result = count_ways(500)
    elapsed = time.perf_counter() - start

    assert result == expected
    assert elapsed < 1
