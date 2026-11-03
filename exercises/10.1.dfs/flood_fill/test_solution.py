import time

from solution import flood_fill


# --- Examples from the README ---


def test_bottom_right_cell_is_not_reached():
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    assert flood_fill(image, 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]


def test_new_color_is_the_same_as_the_old_one():
    # If this test never finishes, your code keeps coming back to the same cells.
    # Stop it with Ctrl+C.
    image = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert flood_fill(image, 0, 0, 0) == [
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_no_diagonal_moves():
    image = [
        [1, 0],
        [0, 1],
    ]
    assert flood_fill(image, 0, 0, 5) == [
        [5, 0],
        [0, 1],
    ]


def test_single_cell():
    assert flood_fill([[3]], 0, 0, 7) == [[7]]


# --- The fill must follow the connected cells, in every direction ---


def test_winding_region_needs_all_four_directions():
    # All the 1s form one snake, so the fill must go down, right, up, right, then down.
    image = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
    ]
    assert flood_fill(image, 0, 0, 4) == [
        [4, 0, 4, 4, 4],
        [4, 0, 4, 0, 4],
        [4, 4, 4, 0, 4],
    ]


def test_starts_from_the_bottom_right_corner():
    image = [
        [2, 2],
        [2, 2],
    ]
    assert flood_fill(image, 1, 1, 3) == [
        [3, 3],
        [3, 3],
    ]


def test_separate_region_of_the_same_color_is_not_painted():
    image = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
    ]
    assert flood_fill(image, 0, 0, 9) == [
        [9, 9, 0, 1, 1],
        [9, 9, 0, 1, 1],
    ]


# --- Edge cases ---


def test_fill_does_not_cross_a_neighbor_of_the_new_color():
    # The middle cell already has the new color, but it was never part of the region.
    assert flood_fill([[1, 2, 1]], 0, 0, 2) == [[2, 2, 1]]


def test_new_color_is_zero():
    image = [
        [1, 1],
        [1, 0],
    ]
    assert flood_fill(image, 0, 0, 0) == [
        [0, 0],
        [0, 0],
    ]


def test_single_row():
    assert flood_fill([[1, 1, 0, 1]], 0, 1, 6) == [[6, 6, 0, 1]]


def test_single_column():
    assert flood_fill([[1], [1], [0], [1]], 1, 0, 6) == [[6], [6], [0], [1]]


# --- Performance ---


def test_performance_largest_image():
    image = [[1] * 30 for _ in range(30)]

    start = time.perf_counter()
    result = flood_fill(image, 15, 15, 2)
    elapsed = time.perf_counter() - start

    assert result == [[2] * 30 for _ in range(30)]
    assert elapsed < 1


def test_performance_largest_image_with_the_same_color():
    # If this test never finishes, your code keeps coming back to the same cells.
    # Stop it with Ctrl+C.
    image = [[1] * 30 for _ in range(30)]

    start = time.perf_counter()
    result = flood_fill(image, 15, 15, 1)
    elapsed = time.perf_counter() - start

    assert result == [[1] * 30 for _ in range(30)]
    assert elapsed < 1
