# Find in a Sorted List: Summary

**Pattern:** Binary search (find an exact value)

## Final solution

```python
def find_index(nums: list[int], target: int) -> int:
    index_target = -1

    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2
        middle_num = nums[middle]

        if middle_num > target:
            right = middle
        elif middle_num < target:
            left = middle + 1
        else:
            index_target = middle
            break

    return index_target
```

## How it works

`left` and `right` are a fence around the part of `nums` that can still hold the target. `left` is **included** in the zone, and `right` is **excluded**, so the zone is `[left, right)`. Each step checks the middle of the zone, then removes the middle and the half that can't contain the target.

With `nums = [1, 3, 5, 7, 9, 11, 13, 15]` and `target = 11`:

| step | `left` | `right` | `middle` | `nums[middle]` | action |
|---|---|---|---|---|---|
| 1 | 0 | 8 | 4 | 9 | 9 < 11 → `left = 5` |
| 2 | 5 | 8 | 6 | 13 | 13 > 11 → `right = 6` |
| 3 | 5 | 6 | 5 | 11 | found → return `5` |

With `target = 12`, the zone becomes empty (`left == right`), the loop stops, and the function returns `-1`.

## Why it works

- **Sorting is the key:** if `nums[middle]` is too small, every value on its left is too small too, so one comparison removes a whole half.
- **The "subarray" is only indexes:** the zone is the range `left` to `right` in the **original** list. `middle = (left + right) // 2` is a real index of `nums`, so the answer is the right position. A slice would copy values (`O(k)`) and lose the original indexes.
- **`middle` must leave the zone:** it's already checked. With an included `left`, removing it means `left = middle + 1`. With an excluded `right`, removing it means `right = middle`. The two lines look different but do the same job.
- **The zone must shrink at every step:** `//` rounds down, so `middle` can be equal to `left`. With `left = middle`, the zone stops shrinking and the loop never ends.
- **An empty list needs no special code:** `left = 0` and `right = 0`, so `0 < 0` is `False` and the loop never runs.

## Complexity

- **Time: `O(log n)`:** the zone is about 2× smaller at each step. A list of 1,000,000 items needs about 20 checks.
- **Space: `O(1)`:** only a few integer variables, no copy.

## Key lessons

**Binary search is not two pointers, even with two variables.** In two pointers, you look at the values **at** `left` and `right`, and they move one step at a time. In binary search, `left` and `right` are the edges of a zone, you look at the value **between** them, and they jump past the middle.

**Choose a convention for the edges and keep it.** Decide whether `right` is included or excluded, then make the start value, the loop condition and the updates match it.

| Convention | Start | Condition | Too big | Too small |
|---|---|---|---|---|
| `right` excluded (mine) | `right = len(nums)` | `left < right` | `right = middle` | `left = middle + 1` |
| `right` included | `right = len(nums) - 1` | `left <= right` | `right = middle - 1` | `left = middle + 1` |

**A frozen `pytest` usually means a zone that doesn't shrink.** Trace a 2-item list by hand to find it.

## Python syntax I learned

**`//` divides and rounds down, so the result can be used as an index:**

```python
(1 + 2) // 2    # 1
(1 + 2) / 2     # 1.5, a float, which can't be an index
```

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `index_target = middle_num` | Returned the value instead of its position | `index_target = middle` |
| `left = middle` | `middle` stayed in the zone. When `middle == left`, the zone never shrank and the loop ran forever | `left = middle + 1` |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Linear scan** | `O(n)` | `O(1)` | Ignores that the list is sorted |
| **Slicing the list in half** | `O(n)` | `O(n)` | Each slice copies values, and the indexes are lost |
| **Binary search with indexes (mine)** | `O(log n)` | `O(1)` | The expected solution |
| **`bisect.bisect_left`** | `O(log n)` | `O(1)` | The stdlib version, forbidden in this exercise but useful in an interview |

A more Pythonic version returns as soon as it finds the target, so `index_target` and `break` are not needed:

```python
        else:
            return middle

    return -1
```

## In an interview

- Say that the list is sorted, so one comparison removes half of it.
- Say which convention you use for `right` (included or excluded) before coding.
- Test by hand an empty list, a 1-item list, a 2-item list with a missing target, and the first and last values.

## Level

Stay at level 0 for Binary search. The structure was right from the start, but the `+ 1` and the index vs value mix-up needed help. Move to level 1 if the next exercise goes mostly alone.

## English corrections

| I wrote | More natural |
|---|---|
| "i'm on the binary_search/find_in_sorted_list exercise, does this "binary search" exercise also need two pointers ?" | "I'm working on the binary_search/find_in_sorted_list exercise. Does this binary search exercise also use two pointers?" |
| "i don't understand how to check the middle of the "subarray" without having a copy" | "I don't understand how to check the middle of the subarray without making a copy." |
| "check y answer, i dont understand why it doesnt work" | "Check my answer, please. I don't understand why it doesn't work." |
| "it works with middle + 1 but dont understood why" | "It works with middle + 1, but I don't understand why." |

- Always capitalize "I".
- Contractions need an apostrophe: don't, doesn't.
- After "don't" or "didn't", use the base verb: "I don't understand", not "I don't understood".
- In English, there's no space before `?`.
