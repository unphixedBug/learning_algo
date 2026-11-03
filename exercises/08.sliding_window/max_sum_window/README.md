# Maximum Sum of a Window

**Pattern:** Sliding window (fixed size) | **Difficulty:** Easy

## Problem

You are given a list of integers `nums` and an integer `k`.

A **window** is a group of exactly `k` items that are **next to each other** in the list.

Return the largest sum that a window can have. If the list is too short to contain a window of
`k` items, return `None`.

## Function to write

```python
def max_window_sum(nums: list[int], k: int) -> int | None:
```

## Examples

### Example 1

```
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

Output: `9`

There are 4 possible windows:

```
[2, 1, 5] 1  3  2     sum = 8
 2 [1, 5, 1] 3  2     sum = 7
 2  1 [5, 1, 3] 2     sum = 9   <- the largest
 2  1  5 [1, 3, 2]    sum = 6
```

### Example 2: a window of one item

```
nums = [4, 9, 2]
k = 1
```

Output: `9`

### Example 3: the window is the whole list

```
nums = [1, 2, 3]
k = 3
```

Output: `6`

### Example 4: only negative numbers

```
nums = [-5, -2, -8, -1]
k = 2
```

Output: `-7` (the windows sum to `-7`, `-10` and `-9`)

### Example 5: the list is too short

```
nums = [1, 2]
k = 3
```

Output: `None`

### Example 6: an empty list

```
nums = []
k = 1
```

Output: `None`

## Constraints

- `0 <= len(nums) <= 400000`
- `1 <= k <= 400000`
- `-1000000 <= nums[i] <= 1000000`
- `nums` must not be changed
- Target complexity: `O(n)` time and `O(1)` extra memory
- Standard library only

## Why a sliding window is useful for this problem

The obvious solution computes the sum of each window from scratch. With a large list and a large
`k`, this means adding up `k` numbers about `n` times, so `O(n * k)`.

But two neighboring windows are almost the same:

```
 2 [1, 5, 1] 3  2     sum = 7
 2  1 [5, 1, 3] 2     sum = ?
```

The items `5` and `1` are in both windows, so adding them again is wasted work. **Only the two
items at the edges change.** A sliding window takes advantage of this: it reuses what it already
knows about the previous window, and updates it in `O(1)` instead of starting over.

Think of a frame that you move along the list, one step at a time.

It is also a close relative of your same-direction two pointers: here, the two edges of the
window both move right, and stay exactly `k` apart.

**Real use cases:**

- **Connect Four:** to detect four aligned tokens, slide a window of length 4 across each row,
  column and diagonal.
- **Calorie counter:** a total over the last 24 hours. Meals older than 24 hours leave the window
  and are subtracted, so the app never adds everything up again.
- **API rate limiter:** allow at most N requests per minute, by tracking only the requests that
  are still inside the last minute.
- **Stock and weather charts:** a "7-day moving average" is a window of 7 days sliding along the
  data.

**How to recognize a sliding window problem:**

- The data is a **list or a string**, and the order matters
- The question is about items **next to each other**: the words **consecutive**, **contiguous**,
  **subarray**, **substring** or **in a row** appear
- The words **largest**, **smallest**, **longest** or **shortest** often appear too
- Going from one group to the next changes only **a few items at the edges**

This exercise uses the simplest variant, where the window has a **fixed size**. In a later
exercise, the window will grow and shrink.

## Useful Python syntax

```python
nums = [10, 20, 30, 40, 50]

# Slicing and summing
nums[:3]                    # [10, 20, 30]  (the first 3 items)
nums[1:4]                   # [20, 30, 40]  (from index 1, up to but not including 4)
sum([10, 20, 30])           # 60
sum(nums[:3])               # 60

# A range that does not start at 0
for i in range(2, 5):       # i takes the values 2, 3, 4
    print(i, nums[i])

# Keeping the largest value seen so far
best = 7
best = max(best, 12)        # 12
best = max(best, 3)         # still 12

# Returning nothing, and checking for it
def first_or_none(items):
    if not items:
        return None
    return items[0]

first_or_none([]) is None   # True (always compare with None using "is")
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `nums[i]` | `O(1)` | Goes straight to the position |
| `nums[a:b]` | `O(b - a)` | Copies each item into a new list |
| `sum(items)` | `O(len(items))` | Reads each item |
| `total += x` | `O(1)` | A single addition |

This is why `sum(nums[i:i + k])` inside a loop is too slow: this one short line costs `O(k)`, and
it runs for each window.

## Before you code

Answer these on paper, using `nums = [2, 1, 5, 1, 3, 2]` and `k = 3`. Tell Claude your answers if
you want to check them.

1. In the second diagram above, what is the missing sum? Compute it **using only the previous sum
   (`7`) and the items that changed**, without adding up the whole window.
2. When the window moves one step right, which item leaves and which item enters? Write their
   indexes for each move.
3. If `i` is the index of the item entering the window, what is the index of the item leaving it?
   Express it using `i` and `k`.
4. You need a starting point before you can slide. Which window comes first, and how do you
   compute its sum?
5. Look at example 4. What goes wrong if you start with `best = 0`?

<details>
<summary>Hint: how to structure your code</summary>

Your function has three steps:

1. Handle the case where no window fits.
2. Compute the sum of the first window. It is your first "best" sum.
3. Loop over the items that enter the window, one by one. Update the sum, then the best.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
