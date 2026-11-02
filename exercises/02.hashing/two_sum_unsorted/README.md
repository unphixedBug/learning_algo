# Two Sum in an Unsorted List

**Pattern:** Hash map / Hash set | **Difficulty:** Easy

## Problem

You are given a list of integers, **in any order**, and a target number.

Exactly one pair of numbers at two different positions adds up to the target. Return the
indices of these two numbers as a tuple `(i, j)`, with `i < j`.

## Function to write

```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
```

## Examples

### Example 1

```
numbers = [3, 8, 1, 6]
target = 7
```

Output: `(2, 3)` (because `1 + 6 = 7`)

### Example 2

```
numbers = [11, 2, 15, 7]
target = 9
```

Output: `(1, 3)` (because `2 + 7 = 9`)

### Example 3: the same value twice

```
numbers = [3, 5, 3]
target = 6
```

Output: `(0, 2)` (because `3 + 3 = 6`, using two different positions)

### Example 4: a number cannot pair with itself

```
numbers = [3, 2, 4]
target = 6
```

Output: `(1, 2)` (because `2 + 4 = 6`; using the `3` twice is not allowed)

## Constraints

- `2 <= len(numbers) <= 20000`
- `numbers` can contain negative numbers and duplicates
- Exactly one valid pair exists
- Target complexity: `O(n)` time and `O(n)` extra space
- Built-in tools only: no libraries to install

## Why a hash map is useful for this problem

This is `pair_sum_sorted` without the sorted order. Two pointers no longer work: a sum that
is too big tells you nothing about the other numbers, so you cannot throw any of them away.

The simple approach tries every pair, which takes `O(n²)` time. For each number, it searches
through the list for its partner. **That repeated searching is the slow part.**

A hash map (`dict` in Python) removes the searching, because it finds a key in about one
step, however large it is. So you can **remember the numbers you have already read**, and
each new number can instantly ask: "Has my partner already gone by?"

Compare the two exercises:

| | Two pointers (`pair_sum_sorted`) | Hash map (this exercise) |
|---|---|---|
| Needs a sorted list | yes | no |
| Time | `O(n)` | `O(n)` |
| Extra memory | `O(1)` | `O(n)` |

This is the usual deal with hash maps: **you spend memory to save time**.

**Hash map or hash set?**

- A hash set (`set`) only answers "have I seen this?"
- A hash map (`dict`) also stores information about it, like "where did I see it?"

**How to recognize a hash map / hash set problem:**

- You keep asking "**have I already seen this?**" or "**does this exist?**"
- You need to **count** things or find **duplicates**
- A solution with two nested loops works but is **too slow**
- The list is **not sorted**, and sorting would not help

## Before you code

Answer these on paper, using Example 1 with `target = 7`. Tell Claude your answers if you want
to check them.

1. You read the `3`. Which number would complete the pair? Have you seen it yet?
2. You read each number in turn. At which number do you find the pair, and why not earlier?
3. Do you need a `dict` or a `set` here? Think about what the function must return.
4. In Example 4, what could go wrong if you store the current number **before** looking for
   its partner?

<details>
<summary>Hint: the tools you need</summary>

- The partner of a number is `target - number`.
- `key in my_dict` checks whether a key exists, in about one step.
- `enumerate(numbers)` gives you each index and number together.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
