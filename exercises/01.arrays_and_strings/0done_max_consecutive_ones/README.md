# Max Consecutive Ones

**Pattern:** Arrays and strings (single-pass scan, "current streak vs. best so far") | **Difficulty:** Easy

## Problem

You are given a list that contains only `0`s and `1`s.

Return the length of the **longest run of consecutive `1`s**.

## Function to write

```python
def max_consecutive_ones(nums: list[int]) -> int:
```

## Examples

### Example 1

```
nums = [1, 1, 0, 1, 1, 1]
```

Output: `3` (the last group, `1, 1, 1`)

### Example 2: every run has size 1

```
nums = [1, 0, 1, 0, 1]
```

Output: `1`

### Example 3: no `1` at all

```
nums = [0, 0, 0]
```

Output: `0`

### Example 4: a single run, with no `0`

```
nums = [1, 1, 1, 1]
```

Output: `4`

### Example 5: an empty list

```
nums = []
```

Output: `0`

## Constraints

- `0 <= len(nums) <= 400000`
- Every item is `0` or `1`
- Target complexity: `O(n)` time and `O(1)` extra space
- Standard library only

## Why a single-pass scan is useful for this problem

The answer depends on **runs of consecutive items**, just like `run_length_encoding`. But here
you don't need to record every run, only the **longest** one.

That changes what you remember while scanning. You no longer need "the current group and its
size" for every group; you only need two small numbers: the size of the run you are currently
in, and the best size you have seen so far. A `0` breaks the current run; a `1` grows it.

**Real use cases:**

- **Monitoring:** the longest streak of consecutive successful health checks for a server.
- **Sports:** the longest winning streak in a season.
- **Manufacturing:** the longest run of parts that passed a quality check on a line.

**How to recognize this form of the scan:**

- The problem asks for the **longest/maximum run** or **streak**, not every run
- Only `0`s and `1`s (or "pass/fail", "true/false") are involved
- The order matters, so sorting would destroy the answer
- A small summary of the past (the current run, the best run) is enough to decide what to do next

## Useful Python syntax

```python
# Looping with the value directly, since you don't need the index
for num in nums:
    ...

# Comparing two values
max(3, 7)                   # 7

# Checking if a list is empty
if not nums:
    ...
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `max(a, b)` | `O(1)` | Compares two values |
| `max(nums)` | `O(n)` | Reads the whole list |
| `nums.count(1)` | `O(n)` | Counts **all** `1`s, not consecutive ones |

**Trap:** `nums.count(1)` counts every `1` in the list, wherever it is. It does not know about
runs, so it gives the wrong answer for `[1, 0, 1, 0, 1]` (it returns `3`, not `1`).

## Before you code

Answer these on paper, using `[1, 1, 0, 1, 1, 1]`. Tell Claude your answers if you want to check
them.

1. While reading from left to right, which **two pieces of information** do you need to
   remember at each moment?
2. What exact event **resets** the current run? What event **grows** it?
3. Do you update the best-so-far on every item, or only when a run ends? Walk through
   `[1, 1, 1, 1]` by hand: if you only update when a run ends, what happens, since this list has
   no `0` to end the run?
4. How is this different from `run_length_encoding`, which also tracks runs? What do you no
   longer need to remember?
5. What should happen with an empty list? Does your loop need a special case for it, or does it
   handle it naturally?

<details>
<summary>Hint: how to structure your code</summary>

Keep two counters: the current run length, and the best length so far. Decide, for each item,
how each counter changes — and make sure the best counter can never miss the **last** run.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
