# Binary Search: Summary

**Current level:** 0

## The pattern: remove half of the possibilities at each step

When data is sorted, one comparison tells you about a whole half: if the middle value is too small, everything on its left is too small too. So you check the middle, keep only the half that can hold the answer, and repeat.

The zone gets about 2× smaller at each step, so the search costs `O(log n)`: 1,000,000 items need about 20 checks.

## When to use it

- The data is **sorted**, or the problem says so (the biggest clue)
- You must **find a value or a position** in that data
- The input is very large, or the target complexity is `O(log n)`
- One check tells you which side to **ignore**: "too small" or "too big"

**Don't confuse it with two pointers.** Both use `left` and `right`, but:

| | Two pointers | Binary search |
|---|---|---|
| What `left` and `right` are | Two items you look at | The edges of a zone where the answer may be |
| Value you check | `nums[left]`, `nums[right]` | `nums[middle]` |
| How they move | One step at a time | They jump past the middle |
| Cost | `O(n)` | `O(log n)` |

## How to think about it

Before coding, answer these questions:

1. What is the **zone** at the start? Is `right` **included** or **excluded**?
2. What are the **three cases** for the middle value: found, too small, too big?
3. In each case, how does the zone shrink, and is `middle` **removed** from it?
4. When does the zone become **empty**, and what do I return then?

## The structure

The zone is only a range of indexes in the original list. Never slice the list: a slice copies values and loses the original indexes.

```python
left, right = 0, len(items)        # right is excluded: the zone is [left, right)

while left < right:                # stops when the zone is empty
    middle = (left + right) // 2
    if items[middle] > target:
        right = middle             # removes middle (right is excluded)
    elif items[middle] < target:
        left = middle + 1          # removes middle (left is included)
    else:
        return middle

return -1
```

**Pick one convention and keep it everywhere:**

| Convention | Start | Condition | Too big | Too small |
|---|---|---|---|---|
| `right` excluded | `right = len(nums)` | `left < right` | `right = middle` | `left = middle + 1` |
| `right` included | `right = len(nums) - 1` | `left <= right` | `right = middle - 1` | `left = middle + 1` |

| Operation | Cost |
|---|---|
| `nums[i]` | `O(1)` |
| `x in nums`, `nums.index(x)` | `O(n)` |
| `nums[a:b]` | `O(b - a)`, because it copies the items |

## Traps

- **The zone doesn't shrink:** `//` rounds down, so `middle` can be equal to `left`. With `left = middle`, the loop runs forever. A frozen `pytest` often means this.
- **Mixing conventions:** for example `right = len(nums)` with `left <= right` reads `nums[len(nums)]` and crashes.
- **Returning the value instead of the index:** `nums[middle]` is the value, `middle` is the position.
- **Slicing the list:** the code looks shorter, but it costs `O(n)` and the indexes are wrong.

## In an interview

- Say that the data is sorted, so one comparison removes half of it.
- Say which convention you use for `right` before coding.
- Test by hand an empty list, a 1-item list, a 2-item list with a missing target, and the first and last values.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `find_in_sorted_list` | Easy | Searching a sorted list with `left` and `right` as edges of a zone, without copying | Seeing the subarray as indexes instead of a copy, and why `left` needs `middle + 1` |

## Next step

Stay at level 0 for now. The next idea is a search where the answer is a **position**, not an exact value (for example, where to insert a target). Move to level 1 if that exercise goes mostly alone.
