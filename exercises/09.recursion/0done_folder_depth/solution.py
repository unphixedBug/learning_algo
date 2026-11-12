def folder_depth(folder: list) -> int:
    """Calculate the depth of a folder.

    Args:
        folder: A list where each item is a file (its size, as an integer) or a
            subfolder (a list that follows the same rules).

    Returns:
        The number of folders on the longest path, starting with this folder (which
        counts as 1). Files do not add depth.
    """
    depth = 1

    for item in folder:
        if isinstance(item, list):
            depth = max(depth, folder_depth(item) + 1)

    return depth