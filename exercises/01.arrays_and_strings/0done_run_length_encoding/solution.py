def run_length_encode(text: str) -> str:
    """Compress each group of consecutive identical letters.

    Args:
        text: The string to compress, containing only letters.

    Returns:
        The compressed string, where each group is written as its size
        followed by its letter.
    """
    pointer = 0
    parts = []

    while pointer < len(text):
        current_char = text[pointer]
        current_count = 1

        while pointer + current_count < len(text) and current_char == text[pointer + current_count]:
            current_count += 1

        pointer += current_count

        parts.append(str(current_count))
        parts.append(current_char)

    return "".join(parts)