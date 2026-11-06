import pytest

from solution import guess_number

# A safety limit: if a solution makes more guesses than this, its loop probably never ends.
SAFETY_LIMIT = 100


def make_check(n, secret):
    """Build a check() function for a secret, and a list that records every guess."""
    guesses = []

    def check(guess):
        guesses.append(guess)
        if len(guesses) > SAFETY_LIMIT:
            raise RuntimeError(
                f"Too many guesses ({len(guesses)}): your loop may never end. "
                f"Last guesses: {guesses[-5:]}"
            )
        if not isinstance(guess, int):
            raise TypeError(f"A guess must be an int, got {guess!r}. Did you use / instead of //?")
        if not 1 <= guess <= n:
            raise ValueError(f"The guess {guess} is outside 1..{n}")
        if guess < secret:
            return "higher"
        if guess > secret:
            return "lower"
        return "correct"

    return check, guesses


def play(n, secret):
    """Run guess_number, check the result, and return the list of guesses."""
    check, guesses = make_check(n, secret)
    assert guess_number(n, check) == secret
    return guesses


# --- Examples from the README ---


def test_example_secret_7_out_of_10():
    guesses = play(10, 7)
    assert guesses[-1] == 7


def test_example_secret_1_out_of_100():
    guesses = play(100, 1)
    assert len(guesses) <= 7


def test_example_only_one_possible_number():
    guesses = play(1, 1)
    assert guesses == [1]


# --- Edge cases ---


def test_two_numbers_secret_is_1():
    play(2, 1)


def test_two_numbers_secret_is_2():
    # With low = guess instead of low = guess + 1, this one never ends.
    play(2, 2)


def test_secret_is_the_biggest_number():
    play(100, 100)


def test_stops_as_soon_as_the_answer_is_correct():
    guesses = play(20, 13)
    assert guesses.count(13) == 1, "You called check() again after finding the secret"
    assert guesses[-1] == 13


def test_never_guesses_the_same_number_twice():
    # Calling check() twice for one guess wastes a guess.
    guesses = play(1000, 777)
    assert len(guesses) == len(set(guesses)), f"Same number guessed twice: {guesses}"


@pytest.mark.parametrize("n", range(1, 41))
def test_every_secret_for_small_n(n):
    # Off-by-one mistakes often appear only for some values of n.
    for secret in range(1, n + 1):
        guesses = play(n, secret)
        assert len(guesses) <= n.bit_length(), f"n={n}, secret={secret}: {guesses}"


# --- Number of guesses (this is the "performance" of this exercise) ---


@pytest.mark.parametrize("secret", [1, 2, 499_999, 500_000, 500_001, 999_999, 1_000_000])
def test_at_most_20_guesses_for_one_million(secret):
    guesses = play(1_000_000, secret)
    assert len(guesses) <= 20, f"{len(guesses)} guesses: {guesses}"


@pytest.mark.parametrize("secret", [1, 123_456_789, 1_000_000_000])
def test_at_most_30_guesses_for_one_billion(secret):
    guesses = play(1_000_000_000, secret)
    assert len(guesses) <= 30, f"{len(guesses)} guesses: {guesses}"
