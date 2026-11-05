def is_balanced(text: str) -> bool:
    """Check if every bracket in a string is correctly closed.

    Args:
        text: The string to check, containing only the characters ()[]{}.

    Returns:
        True if the string is balanced, False otherwise.
    """

    brackets = []

    for char in text:
        if char in ["(", "[", "{"]:
            brackets.append(char)
        elif brackets and char == ")" and brackets[-1] == "(":
            brackets.pop()
        elif brackets and char == "]" and brackets[-1] == "[":
            brackets.pop()
        elif brackets and char == "}" and brackets[-1] == "{":
            brackets.pop()
        else:
            return False

    return not brackets