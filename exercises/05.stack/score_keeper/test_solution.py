import time

from solution import final_score


# --- Examples from the README ---


def test_cancel_double_and_plus():
    assert final_score(["5", "2", "C", "D", "+"]) == 30


def test_longer_sequence():
    assert final_score(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27


def test_single_round():
    assert final_score(["1"]) == 1


def test_no_operations():
    assert final_score([]) == 0


# --- Edge cases ---


def test_double_applied_once():
    assert final_score(["3", "D"]) == 9


def test_double_applied_twice_in_a_row():
    assert final_score(["3", "D", "D"]) == 21


def test_plus_applied_twice_in_a_row():
    assert final_score(["1", "2", "+", "+"]) == 11


def test_cancel_twice_in_a_row():
    assert final_score(["1", "2", "+", "C", "C"]) == 1


def test_negative_scores():
    assert final_score(["-5", "-3", "+"]) == -16


def test_cancel_down_to_an_empty_record():
    assert final_score(["4", "C"]) == 0


def test_zero_scores():
    assert final_score(["0", "0", "+"]) == 0


def test_cancel_a_score_produced_by_double():
    # "D" pushes 10, then "C" removes exactly that 10, not the 5 below it.
    assert final_score(["5", "D", "C"]) == 5


def test_cancel_a_score_produced_by_plus():
    # "+" pushes 3, then "C" removes exactly that 3, leaving 1 and 2 in place.
    assert final_score(["1", "2", "+", "C"]) == 3


# --- Performance ---


def test_performance_many_simple_pushes():
    operations = ["3"] * 100000

    start = time.perf_counter()
    result = final_score(operations)
    elapsed = time.perf_counter() - start

    assert result == 300000
    assert elapsed < 1


def test_performance_push_then_cancel():
    operations = ["5", "C"] * 50000

    start = time.perf_counter()
    result = final_score(operations)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1


def test_performance_mixed_operations():
    # Each cycle pushes "2", doubles it with "D", immediately cancels that
    # double with "C", then pushes "3" and "+" (2 + 3). Only 2, 3 and 5
    # survive each cycle, so the record grows without the values themselves
    # growing.
    operations = ["2", "D", "C", "3", "+"] * 20000

    start = time.perf_counter()
    result = final_score(operations)
    elapsed = time.perf_counter() - start

    assert result == 200000
    assert elapsed < 1
