import time

from solution import anagram_deletions


# --- Examples from the README ---


def test_one_shared_letter():
    assert anagram_deletions("cde", "abc") == 4


def test_already_anagrams():
    assert anagram_deletions("listen", "silent") == 0


def test_repeated_letters():
    assert anagram_deletions("aab", "abb") == 2


def test_second_word_runs_out_first():
    assert anagram_deletions("abcd", "ab") == 2


# --- Edge cases ---


def test_first_word_runs_out_first():
    assert anagram_deletions("ab", "abcd") == 2


def test_both_words_empty():
    assert anagram_deletions("", "") == 0


def test_first_word_empty():
    assert anagram_deletions("", "abc") == 3


def test_second_word_empty():
    assert anagram_deletions("abc", "") == 3


def test_no_shared_letters():
    assert anagram_deletions("abc", "def") == 6


def test_same_single_letter():
    assert anagram_deletions("a", "a") == 0


def test_same_letter_repeated_differently():
    assert anagram_deletions("aaa", "a") == 2


# --- Performance ---


def test_performance_long_words():
    # The words share every "b". All the "a" and "c" letters must be deleted.
    first = "ab" * 20000
    second = "bc" * 20000

    start = time.perf_counter()
    result = anagram_deletions(first, second)
    elapsed = time.perf_counter() - start

    assert result == 40000
    assert elapsed < 1
