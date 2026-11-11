import time

from solution import first_unique_char


# --- Examples from the README ---


def test_first_character_is_unique():
    assert first_unique_char("leetcode") == 0


def test_unique_character_in_the_middle():
    assert first_unique_char("loveleetcode") == 2


def test_every_character_repeats():
    assert first_unique_char("aabb") == -1


def test_empty_string():
    assert first_unique_char("") == -1


def test_single_character():
    assert first_unique_char("z") == 0


def test_unique_character_is_not_the_first_seen():
    assert first_unique_char("ccv") == 2


# --- Edge cases ---


def test_all_same_character():
    assert first_unique_char("zzzzz") == -1


def test_unique_character_at_the_end():
    assert first_unique_char("aabbc") == 4


def test_two_unique_characters_returns_the_first_one():
    assert first_unique_char("abcabd") == 2


def test_repeats_separated_by_other_letters():
    assert first_unique_char("abab" + "c") == 4


# --- Performance ---


def test_performance_large_string():
    # Only the last character is unique, so a naive s.count(ch) per
    # character would scan the whole string again and again.
    s = "a" * 99999 + "b"

    start = time.perf_counter()
    result = first_unique_char(s)
    elapsed = time.perf_counter() - start

    assert result == 99999
    assert elapsed < 1
