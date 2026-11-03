# Remove Duplicates from a Sorted List

**Pattern:** Two pointers (same direction) | **Difficulty:** Easy to medium

## Problem

You are given a list of integers **sorted in non-decreasing order**. Some values may appear
several times.

Change the list **in place** so that each distinct value appears exactly once at the start of
the list, in the original order. Then return `k`, the number of distinct values.

Only the first `k` items are checked. What you leave after them does not matter.

## Function to write

```python
def remove_duplicates(nums: list[int]) -> int:
```

## Examples

### Example 1

```
nums = [1, 1, 2, 3, 3]
```

Output: `3`, and the list starts with `[1, 2, 3]`

### Example 2: no duplicates

```
nums = [2, 5, 9]
```

Output: `3`, and the list starts with `[2, 5, 9]`

### Example 3: only one distinct value

```
nums = [7, 7, 7, 7]
```

Output: `1`, and the list starts with `[7]`

### Example 4: an empty list

```
nums = []
```

Output: `0`

## Constraints

- `0 <= len(nums) <= 400000`
- `-1000000 <= nums[i] <= 1000000`
- `nums` is sorted in non-decreasing order
- Target complexity: `O(n)` time and `O(1)` extra memory, so no second list, `set` or `dict`
- Standard library only

## How this differs from your previous exercises

In `pair_sum_sorted` and `valid_palindrome`, the two pointers started at **opposite ends** and
moved toward each other. Here, they both start on the **left** and move in the **same
direction**, but at different speeds and with different jobs.

**How to recognize this variant:**

- The list must be changed **in place**
- You keep some items and drop others, without changing their order
- The words **remove**, **filter**, **compact** or **move to the end** appear

## Before you code

Answer these on paper, using `[1, 1, 2, 3, 3]`. Tell Claude your answers if you want to check
them.

1. What is the job of each pointer? Try to describe each one in a single sentence.
2. Which pointer moves at every step, and which one moves only sometimes?
3. Why does the list being sorted make it easy to detect a duplicate?
4. Can writing a value ever overwrite an item you have not read yet? Why or why not?
5. Why is calling `nums.pop(i)` for each duplicate too slow?

<details>
<summary>Hint 1: the two jobs</summary>

One pointer **reads** every item. The other one marks **where the next item to keep goes**.

</details>

<details>
<summary>Hint 2: an invariant to keep true</summary>

At every step, the part of the list before the second pointer contains only distinct values,
in order. What must happen to keep this true when the reader finds a new value?

</details>

<details>
<summary>Hint 3: the return value</summary>

Once the loop ends, what does the position of the second pointer tell you?

</details>

Stuck? Ask Claude for guidance on the part that blocks you.
