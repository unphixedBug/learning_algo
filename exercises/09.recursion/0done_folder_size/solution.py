def folder_size(folder: list) -> int:
    """Calculate the total size of the files in a folder.

    Args:
        folder: A list where each item is a file (its size, as an integer) or a
            subfolder (a list that follows the same rules).

    Returns:
        The total size of all the files, including those in the subfolders.
    """
    total = 0

    for item in folder:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += folder_size(item)

    return total