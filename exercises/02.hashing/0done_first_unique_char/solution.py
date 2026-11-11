from collections import Counter

def first_unique_char(s: str) -> int:
    """Return the index of the first character that appears exactly once.

    Args:
        s: A string of lowercase English letters.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    counts = Counter(s)

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    return -1