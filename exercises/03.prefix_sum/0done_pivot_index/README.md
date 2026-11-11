# Pivot Index

**Pattern:** Prefix sum (running total, no stored list) | **Difficulty:** Easy

## Problem

You are given a list of integers. The **pivot index** is an index `i` where the sum of all
numbers **to the left** of `i` equals the sum of all numbers **to the right** of `i`. The
number at `i` itself counts in neither side.

Return the **leftmost** pivot index, or `-1` if none exists.

## Function to write

```python
def pivot_index(numbers: list[int]) -> int:
```

## Examples

### Example 1

```
numbers = [1, 7, 3, 6, 5, 6]
```

Output: `3`

- Left of index `3`: `1 + 7 + 3 = 11`
- Right of index `3`: `5 + 6 = 11`

### Example 2: no pivot exists

```
numbers = [1, 2, 3]
```

Output: `-1`

### Example 3: pivot at the very first index

```
numbers = [2, 1, -1]
```

Output: `0`

- Left of index `0` is empty, so its sum is `0`.
- Right of index `0`: `1 + (-1) = 0`.

## Constraints

- `0 <= len(numbers) <= 100000`
- `-1000 <= numbers[i] <= 1000`
- `numbers` must not be modified
- Target complexity: `O(n)` time, `O(1)` extra space
- Standard library only

## Why a running prefix sum is useful for this problem

The naive approach re-slices and re-sums both sides for every index:
`sum(numbers[:i])` and `sum(numbers[i + 1:])`. Each of those costs `O(n)`, and you repeat it
for every index, so the total cost is `O(n²)`.

The key idea is the same as in `range_sum_queries`: **the sum to the right of `i` can be
rebuilt from totals you already know**, instead of being re-summed.

```
right_sum = total - left_sum - numbers[i]
```

Where `total` is the sum of the whole list (computed once), and `left_sum` is the sum of
everything strictly before `i` (updated as you scan).

**This exercise is a variant of the pattern, not a repeat:** in `range_sum_queries`, you stored
the _whole_ `prefix` list because queries could ask about any range, in any order, after the
fact. Here, you only ever move left to right, once, and only ever need "the running total up to
here" — so a single variable (`left_sum`) replaces the entire stored list. Same idea
("calculate once, reuse instead of re-summing"), smaller footprint.

**Real use cases:**

- Finding the point in a ledger where the money already spent equals the money still to come.
- Splitting a list of tasks (each with a cost) into two groups of equal total cost, at a single
  cut point.
- Finding the point in a race where the distance already covered equals the distance still
  remaining.

**How to recognize this form of the pattern:**

- You need a running total as you scan, but never need to look back at an arbitrary earlier
  point.
- "Sum of everything before/after `i`" appears in the problem.
- You only scan once, left to right — no repeated or out-of-order queries.

## Python syntax that may help

```python
# Sum of a whole list, once
total = sum(numbers)

# Looping with both index and value
for i, num in enumerate(numbers):
    ...
```

## Before you code

Answer these on paper, using `numbers = [1, 7, 3, 6, 5, 6]`. Tell Claude your answers if you
want to check them.

1. What is `total`? Compute it once, by hand.
2. At index `0`, what is `left_sum`? Using `total`, `left_sum`, and `numbers[0]`, what is
   `right_sum`, without slicing or re-summing anything?
3. Walk through indices `0` to `5` by hand, tracking `left_sum` and the matching `right_sum` at
   each step. At which index are they equal first?
4. In this exercise you keep a single running number (`left_sum`) instead of a full `prefix`
   list like in `range_sum_queries`. Why is that enough here, when it wasn't enough there?
5. In what order should you check "are the two sums equal?" and "update `left_sum`" at each
   index? Does swapping that order break index `0`?

<details>
<summary>Hint: the formula you need</summary>

- `total = sum(numbers)`, computed once before the loop.
- At each index `i`: `right_sum = total - left_sum - numbers[i]`.
- Check `left_sum == right_sum` **before** adding `numbers[i]` into `left_sum`.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
