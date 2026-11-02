# Range Sum Queries

**Pattern:** Prefix sum | **Difficulty:** Easy

## Problem

You are given a list of integers and a list of **queries**. Each query is a pair
`(left, right)` of indices (inclusive). For each query, return the sum of the numbers
between `left` and `right`.

## Function to write

```python
def range_sum_queries(numbers: list[int], queries: list[tuple[int, int]]) -> list[int]:
```

## Examples

### Example 1

```
numbers = [2, 4, 6, 8, 10]
queries = [(0, 2), (1, 3), (0, 4)]
```

Output: `[12, 18, 30]`

- `(0, 2)` → `2 + 4 + 6 = 12`
- `(1, 3)` → `4 + 6 + 8 = 18`
- `(0, 4)` → `2 + 4 + 6 + 8 + 10 = 30`

### Example 2: single-element range

```
numbers = [5, 1, 9, 3]
queries = [(2, 2)]
```

Output: `[9]`

### Example 3: same query asked more than once

```
numbers = [1, 2, 3, 4]
queries = [(0, 3), (0, 3), (1, 2)]
```

Output: `[10, 10, 5]`

## Constraints

- `1 <= len(numbers) <= 100000`
- `1 <= len(queries) <= 100000`
- `0 <= left <= right < len(numbers)`
- `numbers` can contain negative numbers
- Target complexity: `O(n + q)` time, `O(n)` extra space (`n` = len(numbers), `q` = len(queries))
- Built-in tools only: no libraries to install

## Why a prefix sum is useful for this problem

The naive approach computes each query by slicing and summing: `sum(numbers[left:right+1])`.
That costs up to `O(n)` **per query**, so with `q` queries you get `O(n * q)` overall. With
large inputs, that is far too slow.

The key idea: **sum of a range can be rebuilt from two running totals.**

Build a `prefix` list once, where `prefix[k]` is the sum of the first `k` numbers
(`prefix[0] = 0`):

```
numbers = [2, 4, 6, 8, 10]
prefix  = [0, 2, 6, 12, 20, 30]
```

Then the sum between index `left` and `right` (inclusive) is just:

```
range_sum(left, right) = prefix[right + 1] - prefix[left]
```

No loop needed at query time. Building `prefix` costs `O(n)` once, and each query becomes
`O(1)`, so the whole problem is `O(n + q)` — you **trade a bit of memory for a lot of
speed**, the same idea as a hash map, but for *cumulative* information instead of
*membership*.

**Real use cases:**

- Getting total revenue between two dates from a list of daily sales, without re-adding every
  day each time someone asks.
- Quickly answering "how many events happened between timestamp A and B?" from a timeline of
  counts.
- Image processing: integral images let you sum pixel intensities over any rectangle in
  constant time.
- Checking if the net change over any stretch of a sequence (e.g. temperature, altitude)
  crosses some threshold, without re-summing the stretch every time.

**How to recognize a prefix sum problem:**

- You are asked for the sum (or average, or count) of a **range/sub-array**, possibly many
  times.
- The data does not change between queries (or changes rarely).
- A loop that re-sums the range for every query would be too slow.

## Python syntax that may help

- `itertools.accumulate(numbers)` returns the running totals of `numbers`, lazily. Wrap it in
  `list(...)` to get a list.
- `itertools.accumulate(numbers, initial=0)` (Python 3.8+) adds a leading `0`, which matches
  the `prefix[0] = 0` convention above and makes the `prefix[right + 1] - prefix[left]`
  formula work directly.
- You can also build the running total yourself with a simple loop and `enumerate`, if you
  prefer not to rely on `itertools`.

## Before you code

Answer these on paper, using Example 1. Tell Claude your answers if you want to check them.

1. Write out the `prefix` list for `numbers = [2, 4, 6, 8, 10]`, with `prefix[0] = 0`.
2. Using only `prefix`, what is the sum for the range `(1, 3)`? Which two entries of `prefix`
   did you subtract?
3. Why does `prefix` have `n + 1` entries instead of `n`?
4. If you had to answer the same query `(0, 4)` a thousand times, how many times would you
   recompute the sum with the prefix-sum approach? How many times with the naive slicing
   approach?

<details>
<summary>Hint: the tools you need</summary>

- `prefix[k]` = sum of `numbers[0]` through `numbers[k - 1]`.
- `range_sum(left, right) = prefix[right + 1] - prefix[left]`.
- `itertools.accumulate(numbers, initial=0)` builds `prefix` in one line.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
