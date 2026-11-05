# Maximum Sum of a Window: Summary

**Pattern:** Sliding window (fixed size)

## Final solution

```python
def max_window_sum(nums: list[int], k: int) -> int | None:
    if k > len(nums):
        return None

    current_sum = sum(nums[:k])
    largest_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]

        largest_sum = max(largest_sum, current_sum)

    return largest_sum
```

## How it works

The first window is summed in full, and it's the best so far because it's the only one seen. Each move then subtracts the item that leaves and adds the item that enters.

With `nums = [2, 1, 5, 1, 3, 2]` and `k = 3`:

| `i` | Window | Enters | Leaves | `current_sum` | `largest_sum` |
|---|---|---|---|---|---|
| start | `[2, 1, 5]` | | | 8 | 8 |
| 3 | `[1, 5, 1]` | `nums[3] = 1` | `nums[0] = 2` | 7 | 8 |
| 4 | `[5, 1, 3]` | `nums[4] = 3` | `nums[1] = 1` | 9 | 9 |
| 5 | `[1, 3, 2]` | `nums[5] = 2` | `nums[2] = 5` | 6 | 9 |

The function returns `9`.

## Why it works

- **Neighboring windows are almost the same:** in `[1, 5, 1]` and `[5, 1, 3]`, the items `5` and `1` are in both, so only the two edges need updating.
- **The formula needs the previous window:** `new sum = old sum - leaving + entering` is only true if "old sum" is the sum of the window just before.
- **The first window counts as a candidate:** starting `largest_sum` with its sum handles negative numbers, a best window at the start, and a window that is the whole list.
- **`i - k` is the leaving item:** the window holds `k` items, so the item that leaves is always `k` positions behind the item that enters.

## Complexity

- **Time: `O(n)`:** the first sum costs `O(k)`, then each of the `n - k` slides costs `O(1)`. With `n = 400000` and `k = 200000`, about 40 billion additions become about 400,000 operations.
- **Space: `O(k)`, briefly:** `nums[:k]` makes a temporary copy of `k` items. Everything else is `O(1)`. The tests accept this, and `islice` removes the copy (see below).

## Key lessons

**Keep the window's state and the answer separate.** `current_sum` always describes the current window, even when that window is bad. `largest_sum` only remembers the best one, and is never used to calculate the next sum.

**Count the first window before sliding.** A loop over the items that enter only sees the windows after the first one. Whatever you set up before the loop must also be a candidate for the answer.

**Don't use `0` as the starting "best".** If all the values can be negative, `0` beats them all and is returned even though no window has that sum. Start from a real value instead.

## Python syntax I learned

**A slice is a copy, not a live view.** Changing the indexes later doesn't change the slice.

```python
left, right = 0, 3
window = nums[left:right]

left += 1
right += 1
# window still holds the first 3 items
```

**`range` can start at any number:** this visits only the items that enter the window.

```python
for i in range(k, len(nums)):
    ...
```

**`+=` evaluates the whole right side first:**

```python
current_sum += nums[i] - nums[i - k]
# same as: current_sum = current_sum + (nums[i] - nums[i - k])
```

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `window = nums[left:right]` once, before the loop | The window never moved, so every step summed the first window | Store only the sum, and update it at each step |
| `while right < len(nums)` with the check before the move | The last window was never checked | Loop over the entering items, and check after each slide |
| `largest_sum = 0` | Wrong for negative sums, and the first window was ignored | `largest_sum = current_sum` |
| `current_sum = largest_sum + nums[i] - nums[i - k]` | Continued from the best sum, which may belong to an older window | Continue from `current_sum` |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Sum each window from scratch** | `O(n * k)` | `O(k)` | Simple, but too slow for the performance tests |
| **Sliding window with a slice (mine)** | `O(n)` | `O(k)` | Clear and normal in an interview |
| **Sliding window with `islice`** | `O(n)` | `O(1)` | Reads the first `k` items without copying them |

```python
from itertools import islice

current_sum = sum(islice(nums, k))
```

## In an interview

- Name the slow `O(n * k)` approach first, then explain that neighboring windows share all items except the edges.
- Say what each variable means: the current window's sum, and the best sum so far.
- Test by hand a list of negative numbers, a window that is the whole list, and a list that is too short.

## Level

Stay at level 0 for Sliding window for now, because this was the first exercise. The key formula and the starting value needed direct help. Move to level 1 if the next fixed-window exercise goes mostly alone.

## English corrections

| I wrote | More natural |
|---|---|
| "i am on the sliding__window/max_sum_window exercise and i dont understand why it is not working" | "I'm working on the sliding_window/max_sum_window exercise, and I don't understand why it isn't working." |
| "really stuck..." | "I'm really stuck..." |
| "i pass most of the tests, 5 left" | "Most of the tests pass, and 5 are still failing." |
| "don't understand where i am doing wrong" | "I don't understand where I'm going wrong." |
| "review" | "Please review my code." |

- Always capitalize "I".
- "Don't" needs an apostrophe.
- Use "going wrong" for a mistake in a process. "Doing wrong" needs an object, as in "What am I doing wrong?"
