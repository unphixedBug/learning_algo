def typed_text(keys: str) -> str:
    """Return the text left on screen after applying every key press.

    Args:
        keys: Typed characters, where '#' is a Backspace.

    Returns:
        The final text displayed on screen.
    """
    final_text = []

    for char in keys:
        if char == "#":
            if final_text:
                final_text.pop()
        else:
            final_text.append(char)

    return "".join(final_text)
