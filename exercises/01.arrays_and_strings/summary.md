# Arrays and Strings: Summary

**Current level:** 0

## The pattern: single-pass scan

Read the items from left to right once, and remember only a small amount of information about what you have already read.

Hash maps, two pointers and sliding windows all build on this idea.

## When to use it

- The problem mentions **consecutive** or **adjacent** items, or a **run** or **streak**
- The order of the items matters, so sorting would destroy the answer
- You can decide what to do with each item using only what you have already read
- The words **longest streak**, **current group** or **best so far** appear

**Don't confuse it with a `dict` count.** A `dict` counts all identical items, wherever they are. A scan respects their order:

| Question about `"aaabaa"` | Tool | Answer |
|---|---|---|
| How many `a` in total? | `dict` count | 5 |
| What are the consecutive groups? | Scan | `aaa`, `b`, `aa` |

## How to think about it

Before coding, answer these questions:

1. What do I need to **remember** while reading?
2. Which **event** changes what I remember? In a run problem, it's the item being different from its neighbor.
3. What do I do **when that event happens**?
4. Is anything **left to handle after the loop**?

## Two ways to find a group

| Approach | How it finds a group | Watch out for |
|---|---|---|
| **Look ahead** (nested `while`) | Extends from the start of the group until the item changes | The bounds check, and moving the main position past the group |
| **Compare with the previous item** (single `for`) | Checks each item against the one before it | Handling the last group after the loop |

The look-ahead structure:

```python
position = 0

while position < len(items):
    size = 1

    while position + size < len(items) and items[position + size] == items[position]:
        size += 1

    # The group is items[position : position + size]: process it here
    position += size
```

## Traps

- **Bounds check first:** `and` stops early if its left side is `False`, so check the position before reading it. Otherwise, you get an `IndexError`.
- **Nested loops don't automatically mean `O(n²)`:** if the position jumps past everything the inner loop has read, each item is processed once, so the scan is `O(n)`.
- **Empty input:** make sure the code doesn't read `items[0]` before checking that the input has items.
- **Building a string:** `append` the pieces to a list, then call `"".join(parts)` once after the loop. `result += piece` risks `O(n²)` because strings are immutable.
- **Slices copy:** `text[i:j]` costs `O(j - i)`, so slicing inside a loop can make the scan slower than it looks.

## In an interview

- Write the manual scan first, and mention `itertools.groupby` as a bonus. It only groups neighbors, and each group it returns is an iterator, so `len(group)` fails.
- Explain out loud why the solution is `O(n)`, especially when the loops are nested.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `run_length_encoding` | Easy | Finding groups of consecutive items | The `and` order and `join` |

## Next step

Stay at level 0 for now. Move to level 1 after solving the next exercise with few hints.
