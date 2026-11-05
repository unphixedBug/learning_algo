# Pair Sum in a Sorted List

**Pattern:** Two pointers | **Difficulty:** Easy

## Problem

You are given a list of integers sorted in increasing order, and a target number.

Exactly one pair of numbers in the list adds up to the target. Return the indices of
these two numbers as a tuple `(i, j)`, with `i < j`.

## Function to write

```python
def pair_sum(n: list[int], target: int) -> tuple[int, int]:
```

## Examples

### Example 1

```
numbers = [1, 3, 4, 6, 8, 11]
target = 10
```

Output: `(2, 3)` (because `4 + 6 = 10`)

### Example 2

```
numbers = [2, 7, 11, 15]
target = 9
```

Output: `(0, 1)` (because `2 + 7 = 9`)

### Example 3: the same value twice

```
numbers = [1, 2, 2, 9]
target = 4
```

Output: `(1, 2)` (because `2 + 2 = 4`, using two different positions)

## Constraints

- `2 <= len(numbers) <= 20000`
- `numbers` is sorted in increasing order and can contain negative numbers and duplicates
- Exactly one valid pair exists
- Target complexity: `O(n)` time and `O(1)` extra space (no extra list, set or dictionary)
- Built-in tools only: no libraries to install

## Why two pointers are useful for this problem

A "pointer" here is just a variable holding an index. You keep one at the start of
the list and one at the end, and move them toward each other.

The simple approach tries every possible pair. With 20000 numbers, that is about
200 million pairs, which is far too slow.

Two pointers are useful here because **the list is sorted**. Sorting means the sum of
the two pointed numbers tells you something about the other pairs too. So each
comparison lets you **throw away one number for good**, instead of ruling out only one
pair. Since one number disappears at each step, you need at most `n` steps.

**How to recognize a two pointers problem:**

- The list is **sorted**, or the problem is about both ends of a sequence
- You are looking for a **pair** of elements that meet a condition
- You are asked to use **no extra memory**

## Before you code

Answer these on paper, using Example 1. Tell Claude your answers if you want to check
them.

1. Start with the first and the last number: `1 + 11 = 12`. This is too big. One of
   these two numbers can never be part of the answer. Which one, and why?
2. What should you do when the sum is too small?
3. Write down each step until you reach `(2, 3)`. How many steps did it take?

<details>
<summary>Hint: check your answer to question 1</summary>

`11` can be thrown away. `1` is the smallest number in the list, and even `1 + 11` is
too big, so `11` is too big with every other number as well.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
