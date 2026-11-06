# Find in a Sorted List

**Pattern:** Binary search | **Difficulty:** Easy

## Problem

You are given a list of integers `nums`, sorted in **increasing order**, and an integer `target`.
All the values in `nums` are different.

Return the **index** of `target` in `nums`. If `target` is not in the list, return `-1`.

Write the search yourself: do not use `bisect`, `in`, `.index()` or `.find()` for this exercise.

## Function to write

```python
def find_index(nums: list[int], target: int) -> int:
```

## Examples

### Example 1: the target is in the middle area

```
nums = [1, 3, 5, 7, 9, 11]
target = 7
```

Output: `3`

### Example 2: the target is the first value

```
nums = [1, 3, 5, 7, 9, 11]
target = 1
```

Output: `0`

### Example 3: the target is the last value

```
nums = [1, 3, 5, 7, 9, 11]
target = 11
```

Output: `5`

### Example 4: the target falls between two values

```
nums = [1, 3, 5, 7, 9, 11]
target = 6
```

Output: `-1`

### Example 5: the target is outside the range of the list

```
nums = [1, 3, 5, 7, 9, 11]
target = 12
```

Output: `-1`

### Example 6: an empty list

```
nums = []
target = 4
```

Output: `-1`

## Constraints

- `0 <= len(nums) <= 1000000`
- `nums` is sorted in increasing order, with no duplicates
- Values in `nums` and `target` can be negative
- Target complexity: `O(log n)` time and `O(1)` extra space
- Standard library only

## Why binary search is useful for this problem

Think about how you look for a word in a paper dictionary. You do not read from the first page.
You open it near the middle, see whether your word comes before or after that page, and **ignore
the half that cannot contain it**. Then you do the same with the half that is left.

Here is the same idea, searching for `11`:

```
[1, 3, 5, 7, 9, 11, 13, 15]     the middle value is 7. 11 is bigger, so 7 and
          ^                     everything on its left can be ignored.

               [9, 11, 13, 15]  the middle value is 11. Found it!
                    ^
```

A simple loop could need to look at all 8 values. This search needed only 2.

**Sorting is what makes this possible.** One comparison tells you about a whole half: if `7` is
too small, everything on its left is also too small. In an unsorted list like `[7, 1, 15, 3]`, one
value says nothing about its neighbors, so you cannot ignore anything.

Each check removes half of the remaining values, so the number of checks grows very slowly:

| Size of the list | Simple loop (worst case) | Binary search (worst case) |
|---|---|---|
| 1,000 | 1,000 checks | 10 checks |
| 1,000,000 | 1,000,000 checks | 20 checks |
| 1,000,000,000 | 1,000,000,000 checks | 30 checks |

This is what `O(log n)` means: when the list becomes twice as long, you need only **one** more
check.

**Real use cases:**

- **Watch history:** a log sorted by date can jump straight to the first film watched after a given
  day, even with years of entries.
- **Autocomplete:** in a sorted list of titles, find where the titles starting with the typed text
  begin.
- **Game levels:** when evolution stages start at sorted level thresholds, find a creature's stage
  from its level.
- **`git bisect`:** finds the commit that introduced a bug by testing the middle commit, then
  keeping the half that contains the bug.

**How to recognize a binary search problem:**

- The data is **sorted**, or the problem tells you so (this is the biggest clue)
- You must **find a value or a position** in that data
- The input is very large, or the target complexity is `O(log n)`
- One check tells you which side to **ignore**: "too small" or "too big"

## Useful Python syntax

```python
# Floor division: divides, then rounds down to a whole number
7 // 2                      # 3
8 // 2                      # 4
7 / 2                       # 3.5 (a float, which cannot be used as an index)

# Indexes must be integers
values = [10, 20, 30, 40]
values[7 // 2]              # 40
values[7 / 2]               # TypeError

# The last valid index of a list
len(values) - 1             # 3
len([]) - 1                 # -1 (an empty list has no valid index)

# Assigning two variables on one line
first, second = 0, 10

# A while loop runs as long as its condition is True
count = 3
while count > 0:
    count -= 1
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `nums[i]` | `O(1)` | Goes straight to the position |
| `target in nums` | `O(n)` | Checks the values one by one |
| `nums.index(target)` | `O(n)` | Checks the values one by one |
| `nums[start:end]` | `O(k)` | Copies the `k` values of the slice |

The last line is a classic trap. If you slice the list at each step, you copy a lot of values, and
the slices also lose the original indexes. **Keep the list as it is, and use two variables to
remember which part of it is still possible.**

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. Take `nums = [2, 4, 6, 8, 10, 12, 14]` and `target = 12`. Use `left` and `right` for the first
   and last index still possible. Write `left`, `right` and the middle index at each step. How
   many checks do you need?
2. Do the same with `nums = [2, 4, 6, 8]` and `target = 5`. What happens to `left` and `right` at
   the end? What tells you that the target is not in the list?
3. Take `nums = [4]` and `target = 4`. Here, `left` and `right` are equal. Should your loop still
   run in this case? So what is the correct loop condition?
4. When the middle value is too small, why can the new `left` be `middle + 1`, and not `middle`?
   Try `left = middle` by hand with `nums = [2, 4]` and `target = 4`. What happens?
5. What are `left` and `right` at the start if `nums` is empty? Does your loop handle this case
   without any special code?

<details>
<summary>Hint: how to structure your code</summary>

At each step, the middle value leads to exactly three cases: it is the target, it is too small, or
it is too big. Decide what each case does. Then decide what to return if the loop ends without
finding anything.

</details>

If `pytest` seems frozen, your loop probably never ends: press `Ctrl+C`, then look at question 4.

Stuck? Ask Claude for a code snippet of the part that blocks you.
