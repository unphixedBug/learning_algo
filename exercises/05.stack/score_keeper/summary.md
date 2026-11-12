# Score Keeper: Summary

**Pattern:** Stack

## Final solution

```python
def final_score(operations: list[str]) -> int:
    record = []

    for op in operations:
        if not record and (op == "C" or op == "D") or len(record) < 2 and op == "+":
            return

        if op == "+":
            record.append(record[-1] + record[-2])
        elif op == "D":
            record.append(record[-1] * 2)
        elif op == "C":
            record.pop()
        else:
            record.append(int(op))

    return sum(record)
```

## How it works

Each operation either pushes a new score on the stack or pops the last one. At the end, the answer is the sum of what is left.

With `["5", "2", "C", "D", "+"]`:

| `op` | Action | Record after |
|---|---|---|
| `"5"` | Push `5` | `[5]` |
| `"2"` | Push `2` | `[5, 2]` |
| `"C"` | Pop | `[5]` |
| `"D"` | Push `5 * 2` | `[5, 10]` |
| `"+"` | Push `5 + 10` | `[5, 10, 15]` |

`sum([5, 10, 15])` gives `30`.

## Why it works

- **The stack is the history:** every round is kept as its own value, so `"C"` can undo the last round with one `pop()`.
- **Only the top matters:** `"+"` reads `[-1]` and `[-2]`, `"D"` reads `[-1]`, and `"C"` removes `[-1]`. No operation ever reaches deeper, which is the LIFO rule.
- **The `else` handles numbers:** once the three symbols are handled, everything else is a number, and `int()` parses negative strings like `"-2"` correctly.
- **The empty input works:** the loop never starts, and `sum([])` is `0`.

## Complexity

- **Time: `O(n)`:** each operation is `O(1)`, and the final `sum` is `O(n)`.
- **Space: `O(n)`:** in the worst case, every operation is a number and stays on the stack.

## Key lessons

**A running total is not enough when you can undo.** Once a score is added into a total, the total forgets it, so there is nothing to subtract when `"C"` arrives. Keep the history, not just its sum.

**`"+"` pushes, it doesn't replace.** The two scores it reads stay on the stack, and the new score goes on top of them.

**The answer can come from the whole stack.** In `balanced_brackets`, the question at the end was "is the stack empty?". Here it's "what do the items left add up to?".

## Design choice: input validation

The constraints say the input is always valid, so lines 15-16 never run. I chose to keep them anyway.

If I keep a check like this, two improvements are worth knowing:

- **Raise instead of returning `None`:** the signature promises an `int`, and a bare `return` gives `None`.
- **Use parentheses and `in`:** `and` binds tighter than `or`, so the condition is correct, but it's hard to read.

```python
if (op in ("C", "D") and not record) or (op == "+" and len(record) < 2):
    raise ValueError(f"invalid operation {op!r}")
```

## Python syntax I learned

**`int()` parses signs:** `int("-2")` gives `-2`, so negative numbers need no special case.

**`sum()` of an empty list is `0`:** no need to handle the empty case separately.

**`x in (a, b)` is shorter than `x == a or x == b`:**

```python
op == "C" or op == "D"   # works
op in ("C", "D")         # more Pythonic
```

## In an interview

- Explain why a running total fails, using `"C"` as the example.
- Point out that the input is guaranteed to be valid, and ask the interviewer whether you should still validate it.
- Test `[]`, a single number, and a `"C"` right after a `"+"` by hand.

## Level

The push and pop logic was right on the first try, and I fixed the remaining bug on my own. Stack can move to level 1.
