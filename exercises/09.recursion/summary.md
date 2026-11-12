# Recursion: Summary

**Current level:** 0

## The pattern: a function that asks itself

A recursive function solves a problem by calling itself on a **smaller version of the
same problem**, then using the answer.

It fits when the data **contains smaller versions of itself** (folders, nested lists,
JSON, trees) and the depth is only known when the code runs, so you can't write the right
number of nested loops.

Recursion is more a tool than a pattern: DFS, backtracking and dynamic programming are
built on it.

| Pattern | What it adds to recursion |
|---|---|
| DFS | Remembers the places already visited |
| Backtracking | Makes a choice, explores, then undoes the choice |
| Dynamic programming | Saves the results, because the same calls come back |

## When to use it

- The input is **nested** and each nested part has the **same shape** as the whole
- The **depth is unknown** before running the code
- You can describe the answer using the answer to a smaller version of the problem

**When not to use it:** a plain loop is better for a flat list. Python stops at about
1000 nested calls, so recursion fits when the number of **levels** is small, not when the
number of **items** is big.

## How to think about it

Before coding, answer these three questions (the recipe):

1. **Base case:** what is the smallest input, the one I can answer without calling the
   function again?
2. **Smaller problem:** which part of the input has the same shape as the whole input?
3. **Combine:** once I receive the answer for the smaller part, how do I use it?

Then **trust the recursive call**: assume it returns the right answer, and check one level
only. Don't follow every level in your head.

## The structure

For nested data, combine a loop and recursion: the loop handles the width, the recursion
handles the depth.

```python
def solve(node) -> int:
    result = start_value                      # 0 for a sum, ...

    for item in node:
        if is_simple(item):
            result = combine(result, value_of(item))
        else:
            result = combine(result, solve(item))   # use the returned value!

    return result
```

The base case is often **implicit**: a node with no nested part makes no recursive call,
and the loop ends by itself.

**What happens in the machine:** each call waits on the call stack with its **own local
variables**. When the inner call returns, the waiting call resumes where it stopped.

| Cost | Value |
|---|---|
| Time | Number of calls × work per call, usually `O(n)` |
| Space | `O(d)`, one waiting call per level of depth |

## Traps

- **Discarding the returned value:** `solve(item)` alone on a line computes the answer and
  throws it away. Assign it, add it, or return it.
- **Recursing on the same input:** calling `solve(node)` instead of `solve(item)` never
  gets closer to the base case: `RecursionError`.
- **`return` inside the loop:** it stops the function at the first item, so the other
  items are never visited.
- **One recursive call per item instead of per level:** a flat list of 100,000 items then
  goes beyond the recursion limit.
- **An unnecessary helper function:** if the main function already has the right
  signature, it can call itself directly.
- **Comparing types with `type(x) == list`:** use `isinstance(x, list)`.

## In an interview

- Say the three parts of the recipe out loud before coding.
- Explain why the stack depth is the number of levels, and mention the limit of about 1000.
- Test the empty input, an empty nested part, and an item placed after a nested part.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `folder_size` | Easy | Loop for width, recursion for depth, combining with a sum | Using the returned value (combine step) |

## Next step

Stay at level 0 for one more exercise, with a different combine step (for example `max`
for the depth of a folder). Then move to level 1.
