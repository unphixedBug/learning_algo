def has_double_badge(badges: list[int]) -> bool:
    """Return True if at least one badge ID appears more than once.

    Args:
        badges: Badge IDs in the order they were scanned.

    Returns:
        True if any badge was scanned twice or more, False otherwise.
    """
    
    return len(badges) != len(set(badges))