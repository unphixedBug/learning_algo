def run_length_encode(text: str) -> str:
    """Compress each group of consecutive identical letters.

    Args:
        text: The string to compress, containing only letters.

    Returns:
        The compressed string, where each group is written as its size
        followed by its letter.
    """
    pointer = 0
    compressed_string = ""

    while pointer < len(text):
        current_char = text[pointer]
        current_count = 1

        while text[pointer] == text[pointer] + 1:
            current_count += 1

        pointer += current_count

        compressed_string += str(current_count)
        compressed_string += current_char

    return compressed_string