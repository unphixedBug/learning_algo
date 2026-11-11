# Max Consecutive Ones: Summary

**Pattern:** Arrays and strings (single-pass scan)

## Final solution

```python
def max_consecutive_ones(nums: list[int]) -> int:
    record = 0
    current = 0

    for num in nums:
        if num == 0:
            current = 0
        else:
            current += 1

        record = max(record, current)

    return record
```

## How it works

`current` tracks the run of `1`s in progress, and `record` remembers the best run seen so far.
Both are updated at every item, not only when a run ends.

With `nums = [1, 1, 0, 1, 1, 1]`:

| `num` | `current` | `record` |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 0 | 0 | 2 |
| 1 | 1 | 2 |
| 1 | 2 | 2 |
| 1 | 3 | 3 |

The function returns `3`.

## Why it works

- **`0` resets, `1` grows:** this is enough to track "the run in progress" without remembering its start position.
- **Comparing on every item, not only when a run ends:** this is what makes the last run count, even when the list ends on a `1` and no `0` ever closes it.
- **The empty list needs no special case:** the loop body never runs, and `record` is already `0`.

## Complexity

- **Time: `O(n)`:** one pass, `O(1)` work per item.
- **Space: `O(1)`:** two integers, no copy of `nums`.

## Key lessons

**Update the best value on every item, not only when an event ends.** This removes a whole category of "forgot the last group" bugs. In `run_length_encoding`, the last group needed an explicit step after the loop. Here, checking `record = max(record, current)` unconditionally on every item makes that explicit step unnecessary — the last run is just like any other.

**A constant-factor difference is not a reason to avoid the readable version.** `max(record, current)` costs a tiny bit more than `if current > record: record = current`, because of Python's function-call overhead. Both are `O(1)` per item, so the complexity is unchanged — the gap is a constant factor, not a complexity difference. Optimizing for that before it's ever measured as a real problem is premature optimization. Readability wins here.

**A variable name can silently shadow a built-in.** `max = 0` works, but it hides the `max()` function for the rest of the scope. Easy to miss, since Python doesn't warn about it.

## Python syntax I learned

**`max(a, b)` as a one-line "keep the best so far":**

```python
record = max(record, current)
# same idea as:
if current > record:
    record = current
```

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| Never reset `current` on a `0` | `current` kept growing past the end of a run, instead of restarting | `current = 0` inside the `if num == 0` branch |
| Only compared `current` to `record` inside the `num == 0` branch | The last run was missed whenever the list didn't end on a `0` (e.g. `[1, 1, 1, 1]`) | Move the comparison so it runs after every item, not only when a run ends |
| Kept the comparison in both the `num == 0` branch and after the `if/else` | The first one became dead code: the previous iteration's unconditional check had already caught the same value | Keep a single comparison, after the `if/else` |
| `if nums: ... (loop) ...` guard, with `current` declared inside it | Unneeded: looping over an empty list does nothing, and `record` already starts at `0` | Removed the guard |
| `max` as a variable name | Shadows the built-in `max()` | Renamed to `record` |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| **`nums.count(1)`** | `O(n)` | `O(1)` | Wrong: counts every `1`, ignoring whether they're consecutive |
| **Current run + best so far (mine)** | `O(n)` | `O(1)` | Clear, and the expected interview answer |
| **`itertools.groupby`** | `O(n)` | `O(1)` amortized | Groups neighbors lazily; needs filtering on the group's value |

```python
from itertools import groupby

def max_consecutive_ones(nums: list[int]) -> int:
    return max((sum(1 for _ in group) for value, group in groupby(nums) if value == 1), default=0)
```

- `default=0` avoids a `ValueError` from `max()` on an empty sequence, which happens if `nums` has no `1` at all.

## In an interview

- Name the two variables out loud before coding: "the run in progress" and "the best run so far".
- Explain why the comparison must happen on every item: it's what covers the last run without a special case.
- Test by hand: an empty list, all zeros, all ones, and a list that ends on a `1`.

## Level

Stay at level 0 for Arrays and strings. This was the second exercise, and it needed more rounds of hints than the first one (`run_length_encoding`): the missing reset, the missing update for the last run, and a redundant check. On the other hand, I spotted the redundant check and the `max()` micro-performance question on my own, which are good instincts. Move to level 1 once an exercise needs little to no guidance on the core logic.
