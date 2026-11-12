import time

from solution import folder_depth


# --- Examples from the README ---


def test_only_files():
    assert folder_depth([10, 20, 5]) == 1


def test_one_subfolder():
    assert folder_depth([10, [20, 5], 2]) == 2


def test_several_levels():
    assert folder_depth([10, [20, 5], [[3]], 2]) == 3


def test_empty_folder():
    # An empty folder is still a folder.
    assert folder_depth([]) == 1


def test_deepest_is_in_the_middle():
    assert folder_depth([[1], [[[2]]], [3]]) == 4


# --- Edge cases ---


def test_single_file():
    assert folder_depth([7]) == 1


def test_only_empty_folders():
    assert folder_depth([[], [[]], []]) == 3


def test_nested_empty_folders():
    assert folder_depth([[[[]]]]) == 4


def test_files_do_not_add_depth():
    assert folder_depth([[1, 2, 3, 4, 5]]) == 2


def test_siblings_do_not_stack():
    # If this test gives 3, the depths of the subfolders are added instead of compared.
    assert folder_depth([[1], [2]]) == 2


def test_many_siblings_do_not_stack():
    assert folder_depth([[], [], [], [], []]) == 2


def test_deepest_is_first():
    assert folder_depth([[[[1]]], [2], 3]) == 4


def test_deepest_is_last():
    # If this test fails, only the first subfolder is kept.
    assert folder_depth([1, [2], [[[3]]]]) == 4


def test_deeper_then_shallower():
    # If this test fails, the last subfolder overwrites a deeper one.
    assert folder_depth([[[[1]]], [2]]) == 4


def test_file_after_a_subfolder():
    assert folder_depth([[1], 2]) == 2


def test_input_is_not_modified():
    folder = [10, [20, 5], [[3]], 2]

    folder_depth(folder)

    assert folder == [10, [20, 5], [[3]], 2]


def test_calling_twice_gives_the_same_result():
    # If this test fails, something is kept between two calls of the function.
    folder = [10, [20, 5], [[3]], 2]

    assert folder_depth(folder) == 3
    assert folder_depth(folder) == 3


# --- Deep and wide folders ---


def test_deep_folder():
    folder = []
    for _ in range(199):
        folder = [folder]

    assert folder_depth(folder) == 200


def test_deep_folder_with_files_at_every_level():
    folder = [1]
    for _ in range(199):
        folder = [1, folder, 2]

    assert folder_depth(folder) == 200


def test_big_flat_folder():
    # If this test raises a RecursionError, you make one call per item instead of one
    # call per level.
    assert folder_depth([1] * 100_000) == 1


# --- Performance ---


def test_performance_wide_folder():
    folder = [[1] * 1_000 for _ in range(100)]

    start = time.perf_counter()
    result = folder_depth(folder)
    elapsed = time.perf_counter() - start

    assert result == 2
    assert elapsed < 1


def test_performance_many_subfolders():
    # Each level contains the previous level twice, so 16 levels give 2^16 files.
    folder = [1]
    for _ in range(16):
        folder = [folder, folder]

    start = time.perf_counter()
    result = folder_depth(folder)
    elapsed = time.perf_counter() - start

    assert result == 17
    assert elapsed < 1
