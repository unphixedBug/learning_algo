import time

from solution import is_balanced


# --- Examples from the README ---


def test_pairs_side_by_side():
    assert is_balanced("()[]{}") is True


def test_nested_pairs():
    assert is_balanced("{[()]}") is True


def test_wrong_type():
    assert is_balanced("(]") is False


def test_right_brackets_wrong_order():
    assert is_balanced("([)]") is False


def test_bracket_never_closed():
    assert is_balanced("(()") is False


def test_nothing_to_close():
    assert is_balanced(")(") is False


def test_empty_string():
    assert is_balanced("") is True


# --- Edge cases ---


def test_single_opening_bracket():
    assert is_balanced("[") is False


def test_single_closing_bracket():
    assert is_balanced("}") is False


def test_only_opening_brackets():
    assert is_balanced("({[") is False


def test_only_closing_brackets():
    assert is_balanced(")}]") is False


def test_stack_becomes_empty_then_closing_bracket():
    # The first pair is fine, but nothing is left to match the last bracket.
    assert is_balanced("())") is False


def test_stack_becomes_empty_then_valid_again():
    assert is_balanced("(){[]}") is True


def test_same_count_of_each_type_but_mismatched():
    assert is_balanced("(}{)") is False


def test_mix_of_nested_and_side_by_side():
    assert is_balanced("([]{()})[{}]") is True


def test_mismatch_deep_inside():
    assert is_balanced("{[(])}") is False


def test_correct_start_with_unclosed_end():
    assert is_balanced("()[]{") is False


# --- Performance ---


def test_performance_deep_nesting():
    # Removing "()" from the string again and again takes far too long here,
    # because each pass only removes one pair.
    text = "(" * 200000 + ")" * 200000

    start = time.perf_counter()
    result = is_balanced(text)
    elapsed = time.perf_counter() - start

    assert result is True
    assert elapsed < 1


def test_performance_many_small_pairs():
    text = "()[]{}" * 66666

    start = time.perf_counter()
    result = is_balanced(text)
    elapsed = time.perf_counter() - start

    assert result is True
    assert elapsed < 1


def test_performance_never_closed():
    text = "(" * 400000

    start = time.perf_counter()
    result = is_balanced(text)
    elapsed = time.perf_counter() - start

    assert result is False
    assert elapsed < 1


def test_performance_mismatch_at_the_very_end():
    text = "(" * 200000 + ")" * 199999 + "]"

    start = time.perf_counter()
    result = is_balanced(text)
    elapsed = time.perf_counter() - start

    assert result is False
    assert elapsed < 1
