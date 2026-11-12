import time

from solution import typed_text


# --- Examples from the README ---


def test_one_backspace_in_the_middle():
    assert typed_text("ab#c") == "ac"


def test_two_backspaces_at_the_end():
    assert typed_text("abc##") == "a"


def test_backspace_on_empty_screen():
    assert typed_text("#a") == "a"


def test_erase_everything_then_type_again():
    assert typed_text("a##b") == "b"


def test_empty_string():
    assert typed_text("") == ""


# --- Edge cases ---


def test_only_backspaces():
    assert typed_text("###") == ""


def test_no_backspace():
    assert typed_text("hello") == "hello"


def test_more_backspaces_than_letters():
    assert typed_text("ab####c") == "c"


def test_everything_erased():
    assert typed_text("abc###") == ""


# --- Performance ---


def test_performance_many_backspaces_on_long_text():
    # Slicing the string (screen[:-1]) copies it every time: O(n²) overall.
    keys = "a" * 100000 + "#" * 99999

    start = time.perf_counter()
    result = typed_text(keys)
    elapsed = time.perf_counter() - start

    assert result == "a"
    assert elapsed < 1
