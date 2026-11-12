# Search Insert Position: Summary

**Pattern:** Binary search (find a boundary, not only a value)

## Final solution

```python
def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle

    return (left + right) // 2
```

It's the same loop as `find_in_sorted_list`. Only the line after the loop changes: instead of `-1`, it returns a position.

## How it works

With `nums = [1, 3, 5, 6]` and `target = 2` (zone `[left, right)`):

| step | `left` | `right` | `middle` | `nums[middle]` | action |
|---|---|---|---|---|---|
| 1 | 0 | 4 | 2 | 5 | 5 > 2 → `right = 2` |
| 2 | 0 | 2 | 1 | 3 | 3 > 2 → `right = 1` |
| 3 | 0 | 1 | 0 | 1 | 1 < 2 → `left = 1` |
| end | 1 | 1 | | | zone empty → return `1` |

Inserting `2` at index `1` gives `[1, 2, 3, 5, 6]`, still sorted.

## Why it works: the invariant

Each update keeps two facts true from the first step to the last:

- `left = middle + 1` only happens when `nums[middle] < target`, so **everything before `left` is smaller than `target`**.
- `right = middle` only happens when `nums[middle] > target`, so **everything from `right` on is bigger than `target`**.

```
           left            right
             |               |
  [ < target | unknown zone  | > target ]
```

When the unknown zone is empty, `left == right`, and that index is the border between "smaller" and "bigger": exactly where `target` belongs. A property that every step keeps true is called an **invariant**. Here it proves why the answer is right.

**Edge cases come for free:**

- Target bigger than everything: `left` keeps moving right and stops at `len(nums)`.
- Target smaller than everything: only `right` moves, and `left` stays at `0`.
- Empty list: `0 < 0` is `False`, the loop never runs, and the function returns `0`.

## Complexity

- **Time: `O(log n)`:** the zone is about 2× smaller at each step.
- **Space: `O(1)`:** a few integers, no copy.

## Key lessons

**Binary search can find a boundary, not only a value.** Even when the target is missing, the loop ends with useful information: `left` is the first index whose value is not smaller than `target`. Many medium problems are "find the boundary" problems in disguise.

**The loop condition should say what it means.** The zone `[left, right)` has items exactly when `left < right`. `left != right` works when the updates are correct, but if a bug makes `left` jump over `right`, `!=` keeps looping (and can raise an `IndexError`), while `<` stops.

**When the loop ends, `left == right`.** So `(left + right) // 2` is always `left`. I kept `(left + right) // 2` because I understand it. The usual version is `return left`, because it says "the target goes at index `left`", which is exactly the invariant. To revisit later.

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `left = middle` (again, same as in `find_in_sorted_list`) | `middle` stayed in the zone. With `nums = [1, 3]`, `target = 4`, `middle` stays `1` forever | `left = middle + 1` |
| `while left != right` | Correct here, but less clear and less safe than the standard condition | `while left < right` |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Linear scan** (count values `< target`) | `O(n)` | `O(1)` | Ignores that the list is sorted |
| **Binary search (mine)** | `O(log n)` | `O(1)` | The expected solution |
| **`bisect.bisect_left(nums, target)`** | `O(log n)` | `O(1)` | Stdlib, does exactly this. Fine in an interview if I can explain it |

## In an interview

- Say: "Binary search, and if the target is missing, `left` ends at the insertion point."
- Explain the invariant in one sentence: everything before `left` is smaller, everything from `right` on is bigger.
- Test by hand: target before the first item, after the last item, and an empty list.

## Level

Stay at level 0 for one more exercise: the version **with duplicates** (find the **first** `3` in `[1, 3, 3, 3, 5]`). The structure came alone, but `left = middle` came back, so the `+ 1` isn't automatic yet. Move to level 1 if the duplicates exercise goes mostly alone.
