# Pivot Index: Summary

**Pattern:** Prefix sum (running total, no stored list)

## Final solution

```python
def pivot_index(numbers: list[int]) -> int:
    total = sum(numbers)
    left_sum = 0

    for i, num in enumerate(numbers):
        if left_sum == total - left_sum - num:
            return i

        left_sum += num

    return -1
```

## How it works

`total` is computed once. `left_sum` only ever holds the sum of everything strictly
before `i`. At each step, the right side is rebuilt from numbers already known, never
re-summed:

```
numbers = [1, 7, 3, 6, 5, 6]   total = 28

i   num   left_sum   total - left_sum - num   equal?
0   1     0          27                       no
1   7     1          20                       no
2   3     8          17                       no
3   6     11         11                       yes -> return 3
```

## Why it works

- **No repeated summing:** `total - left_sum - num` replaces `sum(numbers[:i])` and
  `sum(numbers[i+1:])`, turning an `O(n)` recomputation per index into `O(1)`.
- **The check happens before the update:** `left_sum` must still exclude `numbers[i]`
  when it's compared, otherwise index `0` (where `left_sum` should be `0`) would be
  wrong. Update `left_sum` only after the comparison.
- **One running number is enough:** the scan only ever moves left to right, once, so
  there's nothing to look up later. That's different from `range_sum_queries`, where
  the full `prefix` list had to be stored because queries could ask about any range,
  in any order, after the whole list was already read.

## Key lessons

**A "safe-looking" early exit can be an unproven shortcut.** My first attempt added
`if left_sum > total: return -1`, assuming that once `left_sum` got too big, no pivot
could exist later. That's only true when every number is `>= 0` — then `left_sum` can
never exceed `total`, since everything left to add is non-negative. With negative
numbers, `left_sum` can legitimately be larger than `total` mid-scan and a pivot can
still show up right after. **Before adding a shortcut, check it against the case that
breaks the assumption you're relying on** (here: negative numbers) instead of assuming
it generalizes.

**The formula needs every term, not an approximation.** My first version compared
`left_sum == total - left_sum` (missing `- num`). That's checking "is `left_sum` half of
`total`?", a different question than "does `left_sum` equal the sum to the right of
`i`?". The two only coincide by accident. When a formula looks almost right, re-derive
it from the definition on a concrete index instead of guessing the missing piece.

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `elif left_sum == total - left_sum:` | Misses real pivots; checks if `left_sum` is half of `total`, not if it equals the right-side sum | `elif left_sum == total - left_sum - num:` |
| `if left_sum > total: return -1` | False shortcut: only possible when a later number is negative — exactly the case where a pivot can still exist further on. Breaks on negative numbers and on a pivot near the end | Remove it; the loop is already `O(n)`, no early exit needed |

## Other approaches

| Approach | Time / Space | Notes |
|---|---|---|
| **Running total (mine)** | `O(n)` time, `O(1)` extra space | One sweep, nothing stored |
| **Full `prefix` list (like `range_sum_queries`)** | `O(n)` time, `O(n)` extra space | Works, but the stored list is unused weight here — no repeated or out-of-order queries to justify it |

## In an interview

- Say out loud which case would break a shortcut before adding it (here: "what if a
  later number is negative?") — it catches invalid optimizations before they're coded.
- Compare this variant to a "stored prefix list" problem: name why one needs `O(n)`
  space and the other doesn't (single pass vs. repeated/arbitrary-order queries).

## Level

Stay at level 0 for Prefix sum. The core formula was found quickly, but an unproven
early-exit shortcut needed two rounds of hints to track down. Next prefix sum exercise:
try to question any shortcut against negative numbers and edge indexes before running
the tests.
