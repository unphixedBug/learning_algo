import time

from solution import is_palindrome


# --- Examples from the README ---


def test_simple_word():
    assert is_palindrome("level") is True


def test_spaces_punctuation_and_uppercase():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_a_palindrome():
    assert is_palindrome("race a car") is False


def test_only_punctuation():
    assert is_palindrome(".,!") is True


# --- Even and odd lengths ---


def test_even_length():
    assert is_palindrome("abba") is True


def test_odd_length():
    assert is_palindrome("abcba") is True


# --- Edge cases ---


def test_empty_text():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("a") is True


def test_two_different_characters():
    assert is_palindrome("ab") is False


def test_uppercase_and_lowercase_are_the_same():
    assert is_palindrome("LeVel") is True


def test_digits_count():
    assert is_palindrome("12321") is True


def test_digit_and_letter_differ():
    assert is_palindrome("0P") is False


def test_punctuation_at_the_start():
    assert is_palindrome(".a") is True


def test_punctuation_at_the_end():
    assert is_palindrome("a.") is True


def test_punctuation_between_different_letters():
    assert is_palindrome(",,a,,b") is False


# --- Performance ---


def test_performance_long_palindrome():
    text = "a" * 400000

    start = time.perf_counter()
    result = is_palindrome(text)
    elapsed = time.perf_counter() - start

    assert result is True
    assert elapsed < 1


def test_performance_difference_in_the_middle():
    # The only pair that differs is the last one to be compared.
    text = "a" * 200000 + "b" + "a" * 199999

    start = time.perf_counter()
    result = is_palindrome(text)
    elapsed = time.perf_counter() - start

    assert result is False
    assert elapsed < 1


def test_performance_only_punctuation():
    text = "." * 400000

    start = time.perf_counter()
    result = is_palindrome(text)
    elapsed = time.perf_counter() - start

    assert result is True
    assert elapsed < 1
