# First Unique Character: Summary

**Pattern:** Hash map / Hash set (frequency counting)

## Final solution

```python
import collections

def first_unique_char(s: str) -> int:
    s_dict = collections.Counter(s)

    for i, char in enumerate(s):
        if s_dict[char] == 1:
            return i

    return -1
```

## How it works

`Counter(s)` makes one pass over `s` and builds `{character: count}`. The second pass walks
`s` again, in its original order, and returns the index of the first character whose count is
`1`.

With `s = "aabbc"`:

| `i` | `char` | `s_dict[char]` | Action |
|---|---|---|---|
| 0 | `a` | 2 | skip |
| 1 | `a` | 2 | skip |
| 2 | `b` | 2 | skip |
| 3 | `b` | 2 | skip |
| 4 | `c` | 1 | return `4` |

## Why it works

- The problem hides **two questions**: "how many of each character?" then "which is the
  **first** one with a count of `1`?". You can't answer the second until you know the final
  count of every character, so one pass isn't enough.
- The second pass walks **`s`**, not the dict, which is what keeps `i` equal to the real index
  in the original string (see Mistakes below).
- `Counter` is a `dict` subclass: `s_dict[char]` is the same `O(1)` key lookup as a plain `dict`.

## Complexity

- **Time: `O(n)`:** building the `Counter` is `O(n)`, the second walk is `O(n)`.
- **Space: `O(1)` extra:** at most 26 keys (lowercase letters only), regardless of `len(s)`.

## Key lessons

**`enumerate` on a `dict` numbers its keys, not their position in the original data.**
`enumerate(s_dict)` gives the index of each key *within the dict's iteration order*
(first-occurrence order of the keys), which is not the same as that character's index in `s`.
The fix: `enumerate` the original sequence, and only use the dict for `O(1)` lookups by key.

**A `deque` is not a key → value lookup tool.** A `deque` gives `O(1)` insert/remove at the two
ends of a sequence; it answers nothing about "have I seen this key, and how many times?". That's
a `dict`'s job. Reach for `deque` when the problem is about order at the two ends (a sliding
window of positions, a BFS queue); reach for `dict`/`set` when it's about counting or existence
by key.

## Python syntax I learned

```python
from collections import Counter

counts = Counter("banana")   # Counter({'a': 3, 'n': 2, 'b': 1})
```

`Counter(s)` replaces the manual `counts[ch] = counts.get(ch, 0) + 1` loop in one line. It is
still a `dict` underneath, so lookups stay `O(1)`.

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `for i, char in enumerate(s_dict):` | `i` was the character's position among the dict's keys, not its index in `s` — wrong as soon as a repeated character came before the unique one | `for i, char in enumerate(s):`, keep `s_dict[char]` only for the count lookup |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| `s.count(ch)` inside a loop over `s` | `O(n²)` | `O(1)` | Each call rescans the whole string |
| `Counter` + `enumerate(s)` (mine) | `O(n)` | `O(1)` (26 letters max) | |

## In an interview

- Say out loud that the problem hides two questions (count, then find first with count 1) — that
  justifies the two passes.
- If asked to justify the data structure, be ready to contrast `dict`/`set` (key-based) with
  `deque` (position-based, both ends).

## Level

Stay at level 0 for Hashing — this is the first exercise actually finished for this pattern
(`two_sum_unsorted` is still open). Move to level 1 once an exercise needs little to no help
choosing and applying the data structure.
