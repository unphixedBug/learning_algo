# Shortest Path in a Maze

**Pattern:** BFS | **Difficulty:** Easy

## Problem

You are given a maze as a grid of `0`s and `1`s:

- `0` is an open cell
- `1` is a wall

You start in the top-left cell and want to reach the bottom-right cell. Each move
goes one cell up, down, left or right (no diagonals), and you cannot enter a wall.

Return the **minimum number of moves** needed to reach the bottom-right cell.

## Function to write

```python
def shortest_path(grid: list[list[int]]) -> int:
```

## Examples

### Example 1: open grid

```
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
```

Output: `4`

### Example 2: the walls force a detour

```
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0],
]
```

Output: `10`

### Example 3: no diagonal moves

```
grid = [
    [0, 1],
    [0, 0],
]
```

Output: `2` (down, then right)

### Example 4: already there

```
grid = [[0]]
```

Output: `0`

## Constraints

- `1 <= rows, columns <= 200`, and all rows have the same length
- The start and end cells are always open
- A path to the end cell always exists
- Target complexity: `O(rows * columns)` time
- Built-in tools only: no libraries to install

## Why BFS is useful for this problem

BFS (Breadth-First Search) explores in growing layers, like a ripple in water:
first every cell 1 move from the start, then every cell 2 moves away, then 3, and
so on.

This is useful here because the layers are in order of distance. A cell in layer 5
cannot be reached in fewer than 5 moves, otherwise it would already have been found
in an earlier layer. So **the first time you reach the end cell, you have found the
shortest path**, and you can stop right there.

Compare this with DFS (Depth-First Search), which follows one route as far as it
can before trying another. When DFS reaches the end, it only knows that this route
works, not that it is the shortest. It would have to keep comparing routes.

**How to recognize a BFS problem:**

- You are asked for the **minimum** number of moves or steps
- **Every move costs the same** (here, 1 move is always 1 move)
- The problem can be seen as positions connected to each other (cells, words, people...)

## Before you code

Answer these on paper, using Example 2. Tell Claude your answers if you want to
check them.

1. Which cells are in layer 1? In layer 2?
2. Each cell has up to 4 neighbors. Which ones must you skip?
3. What goes wrong if you never remember the cells you have already seen?

<details>
<summary>Hint: the tools you need</summary>

- A queue, to process cells in the order you discovered them (first in, first out).
  In Python, use `collections.deque`.
- A way to remember the cells you have already seen.
- A way to know the distance of each cell.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
