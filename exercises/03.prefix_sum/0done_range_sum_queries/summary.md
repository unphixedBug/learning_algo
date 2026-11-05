# Range Sum Queries: Summary

**Pattern:** Prefix sum

## Final solution

```python
def range_sum_queries(numbers: list[int], queries: list[tuple[int, int]]) -> list[int]:
    prefix = [0]

    for num in numbers:
        prefix.append(prefix[-1] + num)

    return [prefix[right + 1] - prefix[left] for left, right in queries]
```

## How it works

The code has two steps: build `prefix` once, then use it to answer each query.

```
index:     0  1  2   3   4   5
numbers = [2, 4, 6,  8, 10]
prefix  = [0, 2, 6, 12, 20, 30]
```

| Query | Everything up to `right` | Everything before `left` | Answer |
|---|---|---|---|
| `(0, 2)` | `prefix[3] = 12` | `prefix[0] = 0` | 12 |
| `(1, 3)` | `prefix[4] = 20` | `prefix[1] = 2` | 18 |
| `(0, 4)` | `prefix[5] = 30` | `prefix[0] = 0` | 30 |

## Why it works

- **It avoids repeated work:** each query is one subtraction, because the running totals are already stored. In the performance test, this takes about 200,000 steps instead of up to 10 billion.
- **The formula uses `right + 1` and `left`:** `prefix[k]` is the sum of the first `k` numbers. Index `right` is number `right + 1` in the list, and exactly `left` numbers come before index `left`.
- **The leading `0` handles `left = 0`:** it means "the sum of the first 0 numbers", so the formula needs no special case.
- **A local variable is enough here:** all the queries arrive in the same function call, so `prefix` still exists when each query is answered.

## Key lessons

**Build once, outside the query loop.** Rebuilding `prefix` for each query would lose the whole benefit.

**A negative index doesn't raise an error.** Without the leading `0`, `prefix[left - 1]` becomes `prefix[-1]` when `left` is 0. That reads the last element, so the result is wrong with no error to warn you.

## Python syntax I learned

**Tuple unpacking in a loop:** each loop takes one tuple and splits it into variables. The number of variables must match the tuple's size, otherwise Python raises a `ValueError`.

```python
for left, right in [(0, 2), (1, 3)]:
    print(left, right)
```

**List comprehension:** use it when a loop only builds a list. The value comes first, followed by the loop header without the `:`.

```python
sums = []
for left, right in queries:
    sums.append(prefix[right + 1] - prefix[left])

# Same result
sums = [prefix[right + 1] - prefix[left] for left, right in queries]
```

If the logic gets long or needs several steps, a normal loop is easier to read.

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| Stopping after building `prefix` | The function never used `prefix` and returned nothing | Answer each query with `prefix`, then return the results |
| No leading `0` in `prefix` | `(0, 2)` reads `prefix[-1]` and gives `12 - 30 = -18` | Start with `prefix = [0]` |
| `prefix[left + 1] + prefix[right + 1]` | Wrong operation and wrong `left` index: `(1, 3)` gives 26 | Subtract, and use `prefix[left]` |
| `prefix[right] - prefix[left - 1]` with the leading `0` | Both indexes are too low: `(1, 3)` gives 12 | `prefix[right + 1] - prefix[left]` |
| `if i + 1 > len(numbers)` inside the loop | The condition is never true, so it's dead code | Remove it |
| `for i in range(len(numbers))` | The index was only used to read the value | `for num in numbers` |

## Other approaches

| Approach | Time | Notes |
|---|---|---|
| **Manual `prefix` loop (mine)** | `O(n + q)` | Shows the logic clearly |
| **`itertools.accumulate`** | `O(n + q)` | Builds `prefix` in one line |
| **`sum(numbers[left:right + 1])` per query** | `O(n * q)` | Simple, but too slow for many large queries |

```python
from itertools import accumulate

prefix = list(accumulate(numbers, initial=0))
```

## In an interview

- Start by naming the slow approach and its `O(n * q)` cost, then explain how `prefix` brings it down to `O(n + q)`.
- Mention the trade-off: `O(n)` extra memory for `O(1)` per query.
- Check the formula by hand on a small example, including a query with `left = 0`.

## Level

Stay at level 0 for Prefix sum for now. The two-step structure is clear, but the index shift needed help. Move to level 1 if the next exercise goes well without help on the formula.

## English corrections

| I wrote | More natural |
|---|---|
| "where do i have to calculate the prefix to make it useful ?" | "Where do I have to calculate the prefix to make it useful?" |
| "doesn't the current solution function make the calcul without save it ?" | "Doesn't the current solution function do the calculation without saving it?" |
| "for value1, value2 in array_of_tuple gives each element in the tuples at each loop ?" | "Does `for value1, value2 in array_of_tuples` give me each element of the tuple on each loop?" |

- Always capitalize "I".
- "Calcul" is French. In English, it's "calculation", and you "do" one rather than "make" one.
- Use the `-ing` form after "without": "without saving".
- English has no space before a question mark.
