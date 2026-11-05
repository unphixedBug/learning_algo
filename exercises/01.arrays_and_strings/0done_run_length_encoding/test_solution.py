import time

from solution import run_length_encode


# --- Examples from the README ---


def test_several_groups():
    assert run_length_encode("wwwggopp") == "3w2g1o2p"


def test_every_group_has_one_letter():
    assert run_length_encode("abc") == "1a1b1c"


def test_letter_comes_back_later():
    assert run_length_encode("aaabaa") == "3a1b2a"


def test_group_of_ten_or_more():
    assert run_length_encode("aaaaaaaaaaaa") == "12a"


def test_empty_string():
    assert run_length_encode("") == ""


# --- Edge cases ---


def test_single_letter():
    assert run_length_encode("a") == "1a"


def test_only_one_group():
    assert run_length_encode("zzzz") == "4z"


def test_last_group_has_one_letter():
    assert run_length_encode("aab") == "2a1b"


def test_last_group_has_several_letters():
    assert run_length_encode("abb") == "1a2b"


def test_alternating_letters():
    assert run_length_encode("ababa") == "1a1b1a1b1a"


def test_uppercase_and_lowercase_are_different():
    assert run_length_encode("aaAA") == "2a2A"


def test_group_of_one_hundred():
    assert run_length_encode("a" * 100) == "100a"


# --- Performance ---


def test_performance_many_small_groups():
    # Every letter is its own group, so slicing or copying the rest of the
    # string for each group takes far too long.
    text = "ab" * 200000

    start = time.perf_counter()
    result = run_length_encode(text)
    elapsed = time.perf_counter() - start

    assert result == "1a1b" * 200000
    assert elapsed < 1


def test_performance_one_huge_group():
    text = "a" * 400000

    start = time.perf_counter()
    result = run_length_encode(text)
    elapsed = time.perf_counter() - start

    assert result == "400000a"
    assert elapsed < 1
