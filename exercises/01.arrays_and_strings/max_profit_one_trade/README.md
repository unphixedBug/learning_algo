# Max Profit From One Trade

**Pattern:** Arrays and strings (single-pass scan, "best so far") | **Difficulty:** Easy

## Problem

You are given the price of an item on each day, in order. You may **buy one item on one day**
and **sell it on a later day**.

Return the largest profit you can make. If no trade makes money, return `0`.

## Function to write

```python
def max_profit(prices: list[int]) -> int:
```

## Examples

### Example 1

```
prices = [8, 2, 6, 4, 9, 3]
```

Output: `7` (buy at `2`, sell at `9`)

### Example 2: the lowest price comes after the highest price

```
prices = [5, 9, 1, 3]
```

Output: `4` (buy at `5`, sell at `9`)

`9 - 1 = 8` is not allowed, because you can't sell before you buy.

### Example 3: the price only goes down

```
prices = [9, 7, 4, 1]
```

Output: `0` (the best choice is not to trade)

### Example 4: an empty list

```
prices = []
```

Output: `0`

## Constraints

- `0 <= len(prices) <= 400000`
- `0 <= prices[i] <= 10000`
- You must sell on a **strictly later** day than the day you buy
- `prices` must not be modified
- Target complexity: `O(n)` time and `O(1)` extra space
- Standard library only

## Why a single-pass scan is useful for this problem

The direct approach is to try every pair of days. It works, but with 400,000 days, that is
about 80 billion pairs.

A scan avoids this because most of those pairs can never be the best answer. When you reach a
day, you don't need to remember **every** earlier price. A small summary of the past is enough
to know the best profit you could make by selling today.

This is the "best so far" form of the scan. In `run_length_encoding`, what you remembered was
about the **current group**. Here, it's about **everything you have read so far**.

**Real use cases:**

- **Finance:** finding the largest gain in a price history, where the buy must come before the sell.
- **Weather:** finding the largest temperature rise over a period, where the low must come before the high.
- **Monitoring:** tracking the largest increase in a server's memory use from a stream of measurements, without storing them all.

**How to recognize this form of the scan:**

- The answer depends on a pair of items, and their **order** matters (one must come before the other)
- The words **best**, **largest**, **smallest** or **so far** appear
- The direct solution compares every pair, which is `O(n²)`
- At each item, a small summary of the past is enough to make a decision

## Useful Python syntax

```python
# Looping over the values
for price in prices:
    ...

# Skipping the first item without copying the list
for i in range(1, len(prices)):
    price = prices[i]

# Comparing two values
min(3, 7)                   # 3
max(3, 7)                   # 7

# Checking if a list is empty
if not prices:
    ...

# Assigning a starting value that any real number can beat
float("inf")                # larger than any number
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `min(a, b)` | `O(1)` | Compares two values |
| `min(prices)` | `O(n)` | Reads the whole list |
| `prices[i:]` | `O(n - i)` | A slice **copies** the items |
| `max(prices[i:])` inside a loop | `O(n²)` overall | The cost above, repeated for every item |

## Before you code

Answer these on paper, using `[5, 9, 1, 3]`. Tell Claude your answers if you want to check them.

1. Why is `max(prices) - min(prices)` a wrong answer here? Which rule does it break?
2. Imagine you are on the last day, at price `3`, and you decide to sell. Which single earlier
   price do you want to know? Do you need the other earlier prices?
3. So, while reading from left to right, which **two pieces of information** do you need to
   remember at each moment?
4. For each day, you can update what you remember first, or compute the profit first. Try both
   orders on `[9, 7, 4, 1]`. Does the order change the answer? Why or why not?
5. In `run_length_encoding`, nested loops were still `O(n)`. Why would a nested loop that tries
   every pair of days here be `O(n²)`?

<details>
<summary>Hint: how to structure your code</summary>

Use the four questions from `exercises/01.arrays_and_strings/summary.md`: what do I remember,
which event changes it, what do I do when it happens, and is anything left after the loop?

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
