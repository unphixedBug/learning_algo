# Run-Length Encoding: Summary

**Pattern:** Arrays and strings (single-pass scan)

## Final solution

```python
def run_length_encode(text: str) -> str:
    pointer = 0
    parts = []

    while pointer < len(text):
        current_char = text[pointer]
        current_count = 1

        while pointer + current_count < len(text) and current_char == text[pointer + current_count]:
            current_count += 1

        pointer += current_count

        parts.append(str(current_count))
        parts.append(current_char)

    return "".join(parts)
```

## How it works

The code reads the string one group at a time. With `"aaab"`:

| `pointer` | `current_char` | Inner loop stops because | `current_count` | Pieces added | Next `pointer` |
|---|---|---|---|---|---|
| 0 | `a` | `text[3]` is `b`, a different letter | 3 | `"3"`, `"a"` | 3 |
| 3 | `b` | position 4 is past the end | 1 | `"1"`, `"b"` | 4 |

At `pointer = 4`, the outer loop stops, and `join` builds `"3a1b"`.

## Why it works

- **It only checks neighbors:** one different letter proves that a group has ended. A `dict` would give a wrong answer, because it would merge the two groups of `a` in `"aaabaa"` into `5a`.
- **It's `O(n)`, despite the nested loops:** `pointer` jumps past every letter the inner loop has counted, so each letter is counted only once.
- **The last group isn't forgotten:** each group is added right after it is measured, so no extra code is needed after the loop.
- **The empty string works:** the outer loop never starts, and joining an empty list gives `""`.

## Key lessons

**Nested loops don't automatically mean `O(n²)`.** Check how many times each item is really processed.

**The order of the checks in `and` matters.** Python evaluates `and` from left to right and stops early if the left side is `False`. This is called **short-circuiting**. Put the bounds check first:

```python
pointer + current_count < len(text) and current_char == text[pointer + current_count]  # safe
current_char == text[pointer + current_count] and pointer + current_count < len(text)  # IndexError
```

**Build strings with a list and one `join`.** Strings are immutable, so `result += piece` may copy the whole result each time, which is `O(n²)` in the worst case. CPython often avoids this copy, but Python doesn't guarantee it.

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| `text[pointer] + 1` | Adds 1 to a letter: `TypeError` | Put the addition inside the brackets |
| Comparing fixed positions in the inner loop | The condition never changes: infinite loop | Use `current_count` in the position |
| No bounds check | The last group always reads past the end: `IndexError` | Check the position before reading it |
| Letter comparison before the bounds check | The invalid read still happens: `IndexError` | Put the bounds check on the left of `and` |
| `current_count.join(compressed_string)` | `join` is called on the separator, and an `int` has no `join` | `"".join(parts)` |
| Not storing the result of `join` | `join` returns a new string, so the result is lost | Store or return the result |
| `result += "".join([a, b])` inside the loop | `+=` keeps the `O(n²)` risk | `append` in the loop, `join` once after it |

## How `join` works

```python
parts = []
parts.append("hello")       # during the loop: collect the pieces
parts.append("world")
"".join(parts)              # after the loop: 'helloworld'
" ".join(parts)             # the string before .join is the separator: 'hello world'
```

Every piece must be a string, so numbers need `str()` first.

## Other approaches

| Approach | How it finds a group | Notes |
|---|---|---|
| **Nested `while` (mine)** | Looks ahead until the letter changes | No extra code for the last group |
| **Single `for` loop** | Compares each letter with the previous one | Also very common, but it's easy to forget the last group |
| **`groupby()`** | Python finds the groups for you | The shortest, but it hides the logic |

### `itertools.groupby`

`groupby()` is in the standard library and groups **consecutive** identical items.

```python
from itertools import groupby

def run_length_encode(text: str) -> str:
    return "".join(
        f"{sum(1 for _ in group)}{letter}"
        for letter, group in groupby(text)
    )
```

Traps:

- **`group` is an iterator, not a list:** `len(group)` raises a `TypeError`. Use `sum(1 for _ in group)`, or `len(list(group))`, which builds a temporary list.
- **It only groups neighbors:** `groupby("aaabaa")` gives `aaa`, `b` and `aa`. To group all identical items together, sort the data first.

## In an interview

- Learn the manual version first, and treat `groupby()` as a bonus. An interviewer may ask how it works or tell you not to use it.
- Write the version you're most confident with, then mention the other: "I could also write this in one line with `itertools.groupby`."
- Practice explaining out loud why the solution is `O(n)`.

## How to recognize this pattern

Think of a single-pass scan when:

- The problem mentions **consecutive** or **adjacent** items, or a **run** or **streak**
- The order of the items matters

The same approach can find the longest run of a letter in a string, for example.

## Level

Stay at level 0 for Arrays / Strings for now. The structure was right from the start, but the `and` order and `join` needed hints. Move to level 1 after solving the next exercise with few hints.

## English corrections

| I wrote | More natural |
|---|---|
| "have my solution potential or is it better to delete et start from zero ?" | "Does my solution have potential, or is it better to delete it and start from scratch?" |
| "is it an original solution or an usual one ?" | "Is it an original solution or a common one?" |

- Use **a** before "usual": it starts with a "y" sound, even though its first letter is a vowel.
- English has no space before a question mark.
