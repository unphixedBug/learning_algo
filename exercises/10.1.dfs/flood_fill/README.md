# Flood Fill

**Pattern:** DFS | **Difficulty:** Easy

## Problem

You are given an image as a grid of integers, where each integer is a color. This
is the "paint bucket" tool of a drawing app: you click on one cell and give a new
color.

The new color replaces the color of the clicked cell, and of every cell connected
to it that has the **same original color**. Two cells are connected if you can go
from one to the other through cells of that color, moving up, down, left or right
(no diagonals).

Return the image after the fill.

## Function to write

```python
def flood_fill(
    image: list[list[int]], row: int, col: int, new_color: int
) -> list[list[int]]:
```

You may modify `image` directly and return it.

## Examples

### Example 1: the bottom-right `1` is not reached

```
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
]
row = 1, col = 1, new_color = 2
```

Output:

```
[
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1],
]
```

The bottom-right `1` touches the others only through a diagonal, so it keeps its
color.

### Example 2: the new color is the same as the old one

```
image = [
    [0, 0, 0],
    [0, 0, 0],
]
row = 0, col = 0, new_color = 0
```

Output: the image does not change.

### Example 3: no diagonal moves

```
image = [
    [1, 0],
    [0, 1],
]
row = 0, col = 0, new_color = 5
```

Output:

```
[
    [5, 0],
    [0, 1],
]
```

### Example 4: a single cell

```
image = [[3]]
row = 0, col = 0, new_color = 7
```

Output: `[[7]]`

## Constraints

- `1 <= rows, columns <= 30`, and all rows have the same length
- `row` and `col` are always inside the image
- Colors are integers from `0` to `9`
- Target complexity: `O(rows * columns)` time
- Standard library only

## Why DFS is useful for this problem

DFS (Depth-First Search) follows one route as far as it can. When it is blocked, it
goes back to the last cell where another direction was possible, and tries that
one. It is like exploring a cave with a rope: you go deep, then you follow the rope
back to the last junction.

This is useful here because the question is **"which cells can I reach?"**, not
"how far are they?". You have to visit every connected cell anyway, so the order
does not matter. DFS gives you the simplest code for "visit this cell, then do the
same thing from each neighbor".

You already met BFS with the maze exercise. Here is how to choose:

| | BFS | DFS |
| --- | --- | --- |
| Explores | Layer by layer | One route to its end, then back |
| Tool | Queue (first in, first out) | Stack or recursion (last in, first out) |
| Best for | Minimum number of steps | Visiting everything, exploring all routes |

BFS would also solve this problem. DFS is simply shorter to write here, and it is
the only one of the two you can write with recursion.

**How to recognize a DFS problem:**

- You must visit **everything connected** to a starting point
- You must count or measure connected groups (islands, regions, friend circles)
- You must explore **all possible routes**, or check that one exists
- The data is a tree or nested (folders, comments and their replies)
- The problem does **not** ask for a minimum number of steps

## Real use cases

- The paint bucket tool in Paint or Photoshop
- Going through all the files and subfolders of a folder (`os.walk` can do this)
- Finding everything a package needs before installing it (its dependencies, and
  their dependencies)
- Detecting a circular import or a circular dependency
- A web crawler following links from page to page

## The two ways to write DFS

**1. Recursion:** a function calls itself on each neighbor. Python remembers where
to come back to, on its own "call stack".

**2. An explicit stack:** you keep a list of the cells still to visit, and you
always take the last one added.

Both are DFS. Recursion is usually shorter, so try it first. Every recursive
function needs a **base case**: a condition that makes it stop and return without
calling itself.

## Useful Python syntax

```python
# A function defined inside another one can read the variables around it.
# This avoids passing the same arguments on every recursive call.
def outer(numbers: list[int]) -> int:
    def helper(index: int) -> int:
        if index == len(numbers):  # base case: stop here
            return 0
        return numbers[index] + helper(index + 1)  # recursive call

    return helper(0)


# Loop over directions, unpacking each tuple into two variables
for dx, dy in ((1, 0), (0, 1)):
    print(x + dx, y + dy)

# Chained comparison: is this value between two limits?
if 0 <= value < limit:
    ...

# A list used as a stack
stack = [first_item]
stack.append(other_item)  # add at the end
item = stack.pop()        # remove and return the last one
```

Python stops a recursion after about 1000 nested calls with a `RecursionError`. The
grids here are small enough (900 cells at most) to stay below this limit. A later
exercise will deal with bigger ones.

## Before you code

Answer these on paper, using Example 1. Tell Claude your answers if you want to
check them.

1. Starting from `(1, 1)` and trying up, then down, then left, then right: in which
   order are the cells visited?
2. You are on a cell and look at a neighbor. In which cases must you skip it? There
   are several.
3. Why must you save the original color before you paint anything?
4. In Example 2, what happens if your only check is "does this cell have the
   original color?"

<details>
<summary>Hint: the base case</summary>

Your recursive function can be called on any position. Before painting, ask: is
this position a cell I must paint? If not, return immediately. All the checks can
live in this one place, so the recursive calls stay simple.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
