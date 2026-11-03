# Climbing Stairs

**Pattern:** Dynamic programming | **Difficulty:** Easy

## Problem

You are at the bottom of a staircase with `steps` steps. With each move, you climb
either **1 step** or **2 steps**.

Return the number of different ways to reach the top.

Two ways are different if their moves are in a different order: `1 + 2` and `2 + 1`
count as two ways.

## Function to write

```python
def count_ways(steps: int) -> int:
```

## Examples

### Example 1: a single step

```
steps = 1
```

Output: `1`

There is one way: `1`.

### Example 2: two steps

```
steps = 2
```

Output: `2`

The ways are `1 + 1` and `2`.

### Example 3: the order matters

```
steps = 3
```

Output: `3`

The ways are `1 + 1 + 1`, `1 + 2` and `2 + 1`.

### Example 4: four steps

```
steps = 4
```

Output: `5`

The ways are `1 + 1 + 1 + 1`, `1 + 1 + 2`, `1 + 2 + 1`, `2 + 1 + 1` and `2 + 2`.

## Constraints

- `1 <= steps <= 500`
- Target complexity: `O(steps)` time
- Standard library only

## Why dynamic programming is useful for this problem

Dynamic programming (DP) means: **solve small questions, remember their answers,
and build the big answer from them.**

Imagine someone writes `1 + 1 + 1 + 1 + 1` on a board and asks for the total. You
count and say 5. They add `+ 1` at the end and ask again. You answer 6 immediately,
because you remembered 5. You did not count everything again. That is the whole
idea.

Here, the number of ways is huge: more than 165 million for 40 steps. Listing them
one by one is far too slow. But the question "how many ways to reach this step?" has
only `steps` different versions, one per step. If you answer each version once and
keep the result, the work becomes small.

A plain recursive solution asks the same small question again and again, millions of
times. DP changes nothing about the logic: it only stops the repeated work.

**How to recognize a DP problem:**

- The problem asks for a **count** ("how many ways?") or a **best value** ("minimum
  cost", "maximum profit", "longest..."), not for the list of all solutions
- You make a **series of choices**, and each choice leaves a smaller version of the
  same problem
- If you draw the recursive calls, **the same call appears several times**

| | Plain recursion | DP |
| --- | --- | --- |
| Same question asked twice | Computed twice | Computed once, then reused |
| Typical speed | Often exponential | Number of different questions |
| Extra memory | Only the call stack | One saved answer per question |

## Real use cases

- `git diff`: finding the longest part that two versions of a file have in common
- Spell checkers: measuring how close a typo is to a real word (edit distance)
- Budgets: choosing the best set of items without going over a limit (knapsack)
- DNA comparison: aligning two sequences to measure how similar they are
- Giving change: using the fewest coins for an amount

## The two ways to write DP

**1. Top-down (memoization):** write the recursive function, and save each result
in a dictionary. Before computing, check whether the answer is already saved.

**2. Bottom-up (tabulation):** no recursion. Fill a list with a loop, from the
smallest question to the biggest one.

Both are DP and have the same complexity. Top-down is usually easier to find,
because it starts from the plain recursive idea. Bottom-up avoids the recursion
limit.

## Useful Python syntax

These examples are about other problems, so that you can find the logic yourself.

```python
# A dictionary used as a memory of results
saved: dict[int, int] = {}


def square(number: int) -> int:
    if number in saved:  # already computed: reuse it
        return saved[number]

    saved[number] = number * number
    return saved[number]


# The standard library can do the same with a decorator.
# The first call with a given argument runs the function, the next ones reuse the result.
from functools import cache


@cache
def cube(number: int) -> int:
    return number * number * number


# A list of a given size, filled with zeros
table = [0] * 5  # [0, 0, 0, 0, 0]

# A loop where each cell uses the previous cell
totals = [0] * 5
for index in range(1, 5):
    totals[index] = totals[index - 1] + index  # [0, 1, 3, 6, 10]

# Assign several variables at once: the right side is computed first
left, right = 1, 2
left, right = right, left  # left is 2, right is 1
```

Python integers have no size limit, so the very large answers here are not a problem.
Avoid floats: they would lose precision on these numbers.

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. You are standing on step 5, and you just finished your last move. Which steps
   could you have been on just before this move?
2. Suppose someone tells you the number of ways to reach each of those steps. How do
   you get the number of ways to reach step 5? Why can no way be counted twice?
3. Which are the smallest questions, the ones you can answer without any calculation?
4. Draw the calls for `steps = 5` as a tree. Which questions appear more than once?

<details>
<summary>Hint: name the small question</summary>

The first step in any DP problem is to write the small question as one sentence.
Here: "How many ways are there to reach step `i`?" Then look for how the answer for
`i` uses the answers for smaller values of `i`.

</details>

## Suggested path

1. Write the plain recursive version, without any memory. It should pass the small
   tests, then fail the first performance test. This is expected: it shows the problem
   that DP solves.
2. Add memory to it (top-down). The performance tests should now pass.
3. Rewrite it with a list and a loop (bottom-up).

Run the tests with `pytest -x`. It stops at the first failure, so the plain recursive
version will not get stuck on the bigger performance tests. If a test never finishes,
stop it with Ctrl+C.

Stuck? Ask Claude for a code snippet of the part that blocks you.
