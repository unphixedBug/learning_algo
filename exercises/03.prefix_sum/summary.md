# Prefix Sum: Summary

**Current level:** 0

## The pattern: store running totals

Build a list of running totals once, then calculate the sum of any range with one subtraction.

It costs `O(n)` to build and `O(n)` extra memory, then `O(1)` per query. With `q` queries, the total goes from `O(n * q)` to `O(n + q)`.

## When to use it

- The problem asks for the sum, average or count of a **range** or **sub-array**
- The same kind of question is asked **many times**
- The data **doesn't change** between queries
- Adding up the range again for each query would be too slow

**Don't confuse it with a sliding window.** A prefix sum can answer any range, in any order. A sliding window moves through the data from left to right, and is usually used to find one best range.

## How to think about it

Before coding, answer these questions:

1. Which work would the slow approach **repeat**?
2. What can I **calculate once** to avoid repeating it?
3. How do I write the range as **"everything up to the end, minus everything before the start"**?
4. Does the formula still work when the range **starts at index 0**?

## The structure

`prefix[k]` is the sum of the first `k` numbers, so `prefix` has `n + 1` entries.

```
index:     0  1  2   3   4   5
numbers = [2, 4, 6,  8, 10]
prefix  = [0, 2, 6, 12, 20, 30]
```

```python
prefix = [0]

for num in numbers:
    prefix.append(prefix[-1] + num)

# Sum from left to right, both included
range_sum = prefix[right + 1] - prefix[left]
```

`list(itertools.accumulate(numbers, initial=0))` builds the same list in one line.

## Variant: a running total instead of a stored list

The full `prefix` list is only needed when queries can ask about any range, in any
order, after the whole list has been read. If you only ever scan **once, left to
right**, and only need "everything so far", a single running number replaces the
whole list:

```python
total = sum(numbers)       # computed once
left_sum = 0                # running total, no stored list

for i, num in enumerate(numbers):
    right_sum = total - left_sum - num   # rebuilt, not re-summed
    ...
    left_sum += num
```

Same idea ("calculate once, reuse instead of re-summing"), but `O(1)` extra space
instead of `O(n)`. Ask: *do I need to look something up later, or only "what's the
total so far, right now"?* The answer decides whether to store the list or just a
number.

## Traps

- **Index shift:** `prefix` is shifted by one compared with `numbers`. Use `right + 1` to include `right`, and `left` to exclude everything before it.
- **Missing leading `0`:** `prefix[left - 1]` becomes `prefix[-1]` when `left` is 0. That reads the last element, so the result is wrong with no error to warn you.
- **Building in the wrong place:** build `prefix` once, outside the query loop. Rebuilding it for each query loses the whole benefit.
- **Changing data:** if the numbers change between queries, `prefix` has to be updated too.
- **Unproven early exits:** a shortcut like "stop once the running total passes some bound" often relies on every number being non-negative. Check it against negative numbers before trusting it — a negative number later can undo the assumption.

## In an interview

- Name the slow approach and its `O(n * q)` cost first, then explain how `prefix` improves it.
- Mention the trade-off: more memory for faster queries.
- Check the formula by hand on a small example, including a query with `left = 0`.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `range_sum_queries` | Easy | Answering many range sums with one `prefix` list | The index shift and the leading `0` |
| `pivot_index` | Easy | A running total instead of a stored list, for a single left-to-right scan | An unproven early-exit shortcut that broke with negative numbers |

## Next step

Stay at level 0 for now. Move to level 1 if the next exercise goes well without help on the formula or on checking shortcuts against negative numbers.
