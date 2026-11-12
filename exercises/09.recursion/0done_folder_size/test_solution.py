import time

from solution import folder_size


# --- Examples from the README ---


def test_only_files():
    assert folder_size([10, 20, 5]) == 35


def test_one_subfolder():
    assert folder_size([10, [20, 5], 2]) == 37


def test_several_levels():
    assert folder_size([10, [20, 5], [[3]], 2]) == 40


def test_empty_folder():
    assert folder_size([]) == 0


def test_only_empty_folders():
    assert folder_size([[], [[]], []]) == 0


# --- Edge cases ---


def test_single_file():
    assert folder_size([7]) == 7


def test_files_of_size_zero():
    assert folder_size([0, [0, [0]]]) == 0


def test_large_file_sizes():
    assert folder_size([10**9, [10**9, [10**9]]]) == 3 * 10**9


def test_file_after_a_subfolder_is_counted():
    # If this test fails, the top call stops after its first subfolder.
    assert folder_size([[1], 2]) == 3


def test_every_subfolder_is_counted():
    # If this test fails, the top call stops after its first subfolder.
    assert folder_size([[1], [2], [3]]) == 6


def test_empty_subfolder_before_a_file():
    assert folder_size([[], 5]) == 5


def test_files_at_every_level():
    assert folder_size([1, [2, [3, [4, [5]]]]]) == 15


def test_input_is_not_modified():
    folder = [10, [20, 5], [[3]], 2]

    folder_size(folder)

    assert folder == [10, [20, 5], [[3]], 2]


def test_calling_twice_gives_the_same_result():
    # If this test fails, something is kept between two calls of the function.
    folder = [10, [20, 5], 2]

    assert folder_size(folder) == 37
    assert folder_size(folder) == 37


# --- Deep and wide folders ---


def test_deep_folder_with_one_file():
    folder = [7]
    for _ in range(199):
        folder = [folder]

    assert folder_size(folder) == 7


def test_deep_folder_with_a_file_at_every_level():
    folder = [1]
    for _ in range(199):
        folder = [1, folder]

    assert folder_size(folder) == 200


def test_big_flat_folder():
    # If this test raises a RecursionError, see the hints at the end of the README.
    assert folder_size([1] * 100_000) == 100_000


# --- Performance ---


def test_performance_wide_folder():
    folder = [[1] * 1_000 for _ in range(100)]

    start = time.perf_counter()
    result = folder_size(folder)
    elapsed = time.perf_counter() - start

    assert result == 100_000
    assert elapsed < 1


def test_performance_many_subfolders():
    # Each level contains the previous level twice, so 16 levels give 2^16 files.
    folder = [1]
    for _ in range(16):
        folder = [folder, folder]

    start = time.perf_counter()
    result = folder_size(folder)
    elapsed = time.perf_counter() - start

    assert result == 2**16
    assert elapsed < 1
