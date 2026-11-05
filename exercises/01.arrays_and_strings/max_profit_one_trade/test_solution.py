import time

from solution import max_profit


# --- Examples from the README ---


def test_buy_low_sell_high():
    assert max_profit([8, 2, 6, 4, 9, 3]) == 7


def test_lowest_price_comes_after_highest_price():
    assert max_profit([5, 9, 1, 3]) == 4


def test_price_only_goes_down():
    assert max_profit([9, 7, 4, 1]) == 0


def test_empty_list():
    assert max_profit([]) == 0


# --- Edge cases ---


def test_single_day():
    assert max_profit([5]) == 0


def test_two_days_going_up():
    assert max_profit([3, 8]) == 5


def test_two_days_going_down():
    assert max_profit([8, 3]) == 0


def test_all_prices_are_equal():
    assert max_profit([4, 4, 4]) == 0


def test_price_only_goes_up():
    assert max_profit([1, 2, 3, 4]) == 3


def test_price_of_zero():
    assert max_profit([0, 5]) == 5


def test_earlier_low_stays_the_best_buy():
    # A new lowest price appears at 1, but buying at 3 still gives the best profit.
    assert max_profit([3, 10, 1, 6]) == 7


def test_later_low_becomes_the_best_buy():
    assert max_profit([6, 8, 1, 9]) == 8


def test_best_sell_is_not_the_last_day():
    assert max_profit([2, 9, 4, 5]) == 7


def test_prices_are_not_modified():
    prices = [8, 2, 6, 4, 9, 3]

    max_profit(prices)

    assert prices == [8, 2, 6, 4, 9, 3]


# --- Performance ---


def test_performance_price_only_goes_down():
    # Trying every pair of days takes far too long, and so does slicing the
    # rest of the list for every day.
    prices = list(range(400000, 0, -1))

    start = time.perf_counter()
    result = max_profit(prices)
    elapsed = time.perf_counter() - start

    assert result == 0
    assert elapsed < 1


def test_performance_price_only_goes_up():
    prices = list(range(400000))

    start = time.perf_counter()
    result = max_profit(prices)
    elapsed = time.perf_counter() - start

    assert result == 399999
    assert elapsed < 1


def test_performance_repeating_prices():
    prices = [i % 1000 for i in range(400000)]

    start = time.perf_counter()
    result = max_profit(prices)
    elapsed = time.perf_counter() - start

    assert result == 999
    assert elapsed < 1
