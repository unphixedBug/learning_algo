# Assign Cookies

**Pattern:** Greedy | **Difficulty:** Easy

## Problem

You want to give cookies to children. Each child has an **appetite**, and each cookie
has a **size**.

A child is happy if they receive a cookie whose size is **greater than or equal to**
their appetite. Each child can receive **at most one cookie**, and each cookie can go
to **only one child**.

Return the maximum number of happy children.

## Function to write

```python
def assign_cookies(appetites: list[int], cookies: list[int]) -> int:
```

Do not modify the lists you receive.

## Examples

### Example 1: not enough cookies

```
appetites = [1, 2, 3]
cookies = [1, 1]
```

Output: `1`

Both cookies have size 1, so they only work for the child with appetite 1.

### Example 2: more cookies than children

```
appetites = [1, 2]
cookies = [1, 2, 3]
```

Output: `2`

### Example 3: a bad choice costs a child

```
appetites = [1, 5]
cookies = [5, 1]
```

Output: `2`

If you give the cookie of size 5 to the child with appetite 1, the other child cannot
be happy with the cookie that is left. The answer would be 1 instead of 2.

### Example 4: the lists are not sorted

```
appetites = [4, 1, 3]
cookies = [2, 5, 1]
```

Output: `2`

### Example 5: no cookies

```
appetites = [1, 2]
cookies = []
```

Output: `0`

## Constraints

- `0 <= len(appetites), len(cookies) <= 100_000`
- `1 <= appetite, cookie size <= 1_000_000_000`
- Target complexity: `O(n log n + m log m)` time, with `n` children and `m` cookies
- Standard library only

## Why greedy is useful for this problem

Greedy means: **make the choice that looks best right now, never come back to it, and
repeat.**

Imagine you have 20 euros and want to buy as many items as possible. You do not need
to compare every possible basket: you buy the cheapest item, then the next cheapest,
until you run out of money. No other basket can contain more items.

Here, trying every way to hand out the cookies would take a huge amount of time: with
only 15 children and 15 cookies, there are already more than a trillion ways to give
one cookie to each child. A greedy solution needs one sort and one pass.

The hard part of greedy is not the code, which is often short. It is finding **which
choice is safe**: a choice that can never make the final answer worse. Example 3 shows
that not every choice is safe here.

**How to recognize a greedy problem:**

- The problem asks for a **maximum or minimum** ("the most children", "the fewest
  rooms")
- You can **sort** the input, and the order makes the next choice obvious
- After each choice, **what is left is a smaller version of the same problem**
- You can explain **why the choice is safe**, in one sentence

**Greedy does not always work.** Try to give 6 euros with the fewest coins, using
coins of 1, 3 and 4. Taking the biggest coin each time gives `4 + 1 + 1`, so 3 coins.
The best answer is `3 + 3`, so 2 coins. Here the first choice can hurt you later, so
you need dynamic programming.

| | Greedy | Dynamic programming |
| --- | --- | --- |
| Choices explored | One at each step | All of them, with saved answers |
| Goes back on a choice | Never | Compares the options first |
| Typical speed | Very fast, often just a sort and a loop | Slower, one answer per small question |
| Risk | Wrong answer if the choice is not safe | Always correct if the small questions are right |

**A quick way to test a greedy idea:** try to find a small input that breaks it, as the
coins do above. If you cannot, try to say why the choice is safe.

## Real use cases

- File compression (ZIP, gzip): Huffman coding repeatedly merges the two least frequent
  symbols
- GPS and network routing: Dijkstra's algorithm always continues from the closest
  unvisited point
- Meeting rooms: fitting as many meetings as possible into one room
- Network cabling: connecting all the buildings with the least cable (Kruskal's
  algorithm)
- Cash registers: giving change, with coin systems where taking the biggest coin works

## Useful Python syntax

These examples are about other problems, so that you can find the logic yourself.

```python
prices = [8, 3, 5]

# sorted() returns a new list and leaves the original unchanged
ordered = sorted(prices)  # ordered is [3, 5, 8], prices is still [8, 3, 5]

# .sort() changes the list itself and returns None
prices.sort()  # prices is now [3, 5, 8]

# Sort from largest to smallest
sorted(prices, reverse=True)  # [8, 5, 3]

# Sort by a custom rule: here, by length of the word
sorted(["kiwi", "fig", "banana"], key=len)  # ['fig', 'kiwi', 'banana']


# A complete greedy example: buy as many items as possible with a budget
def count_items_bought(prices: list[int], budget: int) -> int:
    bought = 0

    for price in sorted(prices):  # the safe choice: always the cheapest item left
        if price > budget:
            break  # the next items cost even more, so we can stop

        budget -= price
        bought += 1

    return bought


# Walk through two lists at the same time, each at its own speed
first = [1, 3, 5]
second = [2, 3, 4]
first_index = second_index = 0

while first_index < len(first) and second_index < len(second):
    if first[first_index] < second[second_index]:
        first_index += 1
    else:
        second_index += 1
```

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. Look at Example 3. What exactly was wasted by the bad choice?
2. Take `appetites = [2, 4, 7]` and `cookies = [1, 3, 5, 8]`. Hand out the cookies by
   hand. What order did you naturally follow?
3. Look at the cookie of size 1 in question 2. Who can eat it? What should you do with
   a cookie like this one?
4. Write your rule as one sentence, starting with "I always...". Then explain why it
   can never make the final answer worse.

<details>
<summary>Hint: start from the smallest</summary>

Think about the smallest cookie and the child with the smallest appetite. If this
cookie is too small for this child, can it make anyone else happy? And if it is big
enough, is there any reason to keep it for someone else?

</details>

## Suggested path

1. Answer the questions above and write your rule in plain words.
2. Try to break your rule with a small example on paper.
3. Code it. Sort first, then make your choices one by one.

Run the tests with `pytest -x`. It stops at the first failure, so a slow solution will
not get stuck on the biggest performance test. If a test never finishes, stop it with
Ctrl+C.

Stuck? Ask Claude for a code snippet of the part that blocks you.
