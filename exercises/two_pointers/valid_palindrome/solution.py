def is_palindrome(text: str) -> bool:
    """Return whether the text is a palindrome.

    Only letters and digits count, and uppercase and lowercase are the same.

    Args:
        text: The text to check.

    Returns:
        True if the text is a palindrome, False otherwise.
    """
    i, j = 0, len(text) - 1

    while i < j:
        while i < j and not text[i].isalnum():
            i += 1

        while i < j and not text[j].isalnum():
            j -= 1            

        if text[i].lower() != text[j].lower():
            return False


        i += 1
        j -= 1

    return True
