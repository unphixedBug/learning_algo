import time

from solution import shortest_path


# --- Examples from the README ---


def test_open_grid():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert shortest_path(grid) == 4


def test_walls_force_a_detour():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
    ]
    assert shortest_path(grid) == 10


def test_no_diagonal_moves():
    # A diagonal move would give 1.
    grid = [
        [0, 1],
        [0, 0],
    ]
    assert shortest_path(grid) == 2


def test_single_open_cell():
    assert shortest_path([[0]]) == 0


# --- The answer must be the shortest route, not just any route ---


def test_picks_the_shorter_of_two_routes():
    # Along the top then down the right side: 8 moves.
    # Through the middle then along the bottom: 12 moves.
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert shortest_path(grid) == 8


# --- Edge cases ---


def test_ignores_dead_ends():
    # The bottom-left cell leads nowhere.
    grid = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
    ]
    assert shortest_path(grid) == 4


def test_single_row():
    assert shortest_path([[0, 0, 0, 0]]) == 3


def test_single_column():
    assert shortest_path([[0], [0], [0]]) == 2


# --- Performance ---


def test_performance_large_open_grid():
    # If this test never finishes, your code is probably visiting the same cells
    # again and again. Stop it with Ctrl+C.
    grid = [[0] * 200 for _ in range(200)]

    start = time.perf_counter()
    result = shortest_path(grid)
    elapsed = time.perf_counter() - start

    assert result == 398
    assert elapsed < 2
