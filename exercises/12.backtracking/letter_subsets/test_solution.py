import time

from solution import letter_subsets


# --- Examples from the README ---


def test_two_letters():
    assert sorted(letter_subsets("ab")) == ["", "a", "ab", "b"]


def test_three_letters():
    assert sorted(letter_subsets("abc")) == [
        "",
        "a",
        "ab",
        "abc",
        "ac",
        "b",
        "bc",
        "c",
    ]


def test_input_order_is_kept():
    assert sorted(letter_subsets("cab")) == [
        "",
        "a",
        "ab",
        "b",
        "c",
        "ca",
        "cab",
        "cb",
    ]


def test_no_letter():
    assert letter_subsets("") == [""]


# --- Edge cases ---


def test_single_letter():
    assert sorted(letter_subsets("a")) == ["", "a"]


def test_uppercase_and_lowercase_are_different_letters():
    assert sorted(letter_subsets("aA")) == ["", "A", "a", "aA"]


def test_calling_twice_gives_the_same_result():
    # If this test fails, something is kept between two calls of the function.
    first = sorted(letter_subsets("ab"))
    second = sorted(letter_subsets("ab"))
    assert first == second == ["", "a", "ab", "b"]


# --- The result must be complete, without duplicates ---


def test_no_missing_subset_and_no_duplicate():
    result = letter_subsets("abcd")

    assert len(result) == 16
    assert len(set(result)) == 16


def test_every_subset_is_valid():
    # The letters of "abcd" are in alphabetical order, so every valid subset is too.
    # If this test fails, a subset has a foreign or repeated letter, or a wrong order.
    for subset in letter_subsets("abcd"):
        assert set(subset) <= set("abcd")
        assert len(set(subset)) == len(subset)
        assert "".join(sorted(subset)) == subset


def test_contains_the_empty_and_the_full_subsets():
    result = letter_subsets("abcdefgh")

    assert "" in result
    assert "abcdefgh" in result


# --- Performance ---


def test_performance_largest_input():
    letters = "abcdefghijklmnop"

    start = time.perf_counter()
    result = letter_subsets(letters)
    elapsed = time.perf_counter() - start

    assert len(set(result)) == 2**16
    assert elapsed < 1
