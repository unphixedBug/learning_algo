# Folder Depth: Summary

**Pattern:** Recursion

## Final solution

```python
def folder_depth(folder: list) -> int:
    depth = 1

    for item in folder:
        if isinstance(item, list):
            depth = max(depth, folder_depth(item) + 1)

    return depth
```

## How it works

Each folder starts with a depth of `1` (itself). For each subfolder, the function asks
itself for the subfolder's depth, adds `1` for the current folder, and keeps the biggest
value seen so far. Files are ignored: they add no depth.

With `[[[1]]]`:

```
folder_depth([[[1]]])                      depth = 1
    folder_depth([[1]])                    depth = 1
        folder_depth([1])                  depth = 1
            item 1: file, ignored
        returns 1                          <- deepest folder, no subfolder
    depth = max(1, 1 + 1) = 2
    returns 2
depth = max(1, 2 + 1) = 3
returns 3
```

## Why it works

- **`depth = 1` runs once per call, not once per loop turn:** it is above the `for`. Each
  folder starts at `1`, and each call has its **own** `depth` variable.
- **The depth is built on the way back up:** nobody does `depth += 1` going down. The
  deepest folder returns `1`, and each parent adds `1` to what its child returned.
- **`max` keeps the best answer:** a shallow subfolder can't overwrite a deeper one seen
  before.
- **The base case is implicit:** a folder without subfolders (including `[]`) never enters
  the `if`, so it returns `1`.
- **The recipe, applied:**
  - **Base case:** a folder without subfolders returns `1`
  - **Smaller problem:** `item`, when it is a list
  - **Combine:** `max(depth, folder_depth(item) + 1)`

## Complexity

- **Time: `O(n)`:** each item is visited once.
- **Space: `O(d)`:** one call waits on the stack for each level. `d` is also the answer.

## Key lessons

**`=` overwrites, `max` keeps the best.** My first version was
`depth = folder_depth(item) + 1`. Each subfolder replaced the previous answer, so only the
**last** subfolder counted. The 4 failing tests all had a deeper subfolder before the last
one.

**Keep the best value in a loop:** `best = max(best, new_value)`. The variable is both the
current best and the starting point of the comparison.

**The combine step depends on the question:**

| Exercise | Question | Combine |
|---|---|---|
| `folder_size` | How much in total? | `total += folder_size(item)` |
| `folder_depth` | How deep at most? | `depth = max(depth, folder_depth(item) + 1)` |

**The current level counts:** a subfolder returns its own depth, not the parent's. The
`+ 1` adds the current folder. I got this part right on the first try.

**Read the failing tests together:** they all had the deepest subfolder somewhere other
than at the end, which pointed straight to the overwrite.

## Not fully understood yet

The tests pass, but I still find it hard to see **how the depth grows** when every call
starts at `depth = 1`. Things to review later:

- Draw the trace of `[[[1]]]` on paper, one box per call, each with its own `depth`.
- Then do `[[1], [[2]]]` the same way.
- Key idea to check: the value grows through the **returned values** (`+ 1` on the way
  back up), not through the variable going down.

## Python syntax I learned

**`max(a, b)`:** returns the bigger of two values.

**`max([])` raises a `ValueError`:** use `max(values, default=0)` when the list can be empty.

## In an interview

- Explain that the current folder counts for `1`, and that siblings don't stack.
- Trace a small example out loud, showing the values returned on the way back up.
- Test `[]`, `[[1], [2]]` and an input where the deepest subfolder is not the last one.
- Mention that it is the same idea as the **height of a tree**, a classic question.

## Level

I needed a snippet for `max(depth, ...)`, and the way the value grows through the calls is
not clear yet. Stay at level 0.
