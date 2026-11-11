# Score Keeper

**Pattern:** Stack | **Difficulty:** Easy

## Problem

You are keeping the score of a game, one round at a time. You are given a list of
**operations**, applied in order to a running **record** of round scores:

- A string that looks like a number, e.g. `"5"` or `"-2"`: this round's score is that
  number. Add it to the record.
- `"+"`: this round's score is the **sum of the last two scores** in the record. Add it
  to the record (the two earlier scores stay in the record too).
- `"D"`: this round's score is **double the last score** in the record. Add it to the
  record.
- `"C"`: **cancel** the last score in the record: remove it. This operation adds nothing.

Return the **sum of every score left in the record** once all operations are applied.

## Function to write

```python
def final_score(operations: list[str]) -> int:
```

## Examples

### Example 1

```
operations = ["5", "2", "C", "D", "+"]
```

Walking through it:

| Operation | Record after |
|---|---|
| `"5"` | `[5]` |
| `"2"` | `[5, 2]` |
| `"C"` | `[5]` (the `2` is cancelled) |
| `"D"` | `[5, 10]` (double of `5`) |
| `"+"` | `[5, 10, 15]` (sum of `5` and `10`) |

Output: `30` (`5 + 10 + 15`)

### Example 2

```
operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
```

Output: `27`

### Example 3: a single round

```
operations = ["1"]
```

Output: `1`

### Example 4: no operations at all

```
operations = []
```

Output: `0`

## Constraints

- `0 <= len(operations) <= 100000`
- Each operation is `"+"`, `"D"`, `"C"`, or a string representing an integer in
  `[-30000, 30000]`
- The input is always **valid**: `"+"` never appears when the record has fewer than two
  scores, and `"D"` or `"C"` never appear when the record is empty
- Target complexity: `O(n)` time
- Standard library only

## Why a stack is useful for this problem

Three of the four operations only care about the **most recently added** scores:
`"D"` reads the last one, `"+"` reads the last two, and `"C"` removes the last one. None of
them ever touch a score that is further back. That is the LIFO rule again: **the last score
in is the first one these operations look at or remove**.

A single running total is not enough here. Once you add a score into a total, the total
no longer remembers that score on its own — so when `"C"` says "undo the last round," there
is nothing left to subtract back out. You need the actual **history**, in order, not just
its sum. A stack is exactly that history, with the most recent round always on top, in reach.

**Real use cases:**

- **Undo / redo:** a text editor or drawing app pushes each action onto a stack. Ctrl+Z pops
  the most recent one, exactly like `"C"` here.
- **Version control:** `git revert` or `git reset --soft HEAD~1` undoes the most recent
  commit first, never one from the middle of the history.
- **Calculators and spreadsheets:** some operations (like `"D"` and `"+"` above) combine the
  most recent results instead of asking you to re-enter them.
- **Call stacks:** when a function returns, control goes back to whichever function called
  it most recently, not to some earlier one.

**How to recognize a stack problem:**

- An operation only ever reads or removes the **most recent** item(s), never an older one
- The problem explicitly describes **undoing**, **cancelling**, or **replaying** history
- You need the actual past values, not just a running total, because a later step can
  reach back and change what came before

## Useful Python syntax

```python
record = []
record.append(5)        # push: [5]
record.append(-2)       # push: [5, -2]

record[-1]              # peek the top: -2 (does not remove it)
record[-2]              # peek one below the top: 5 (does not remove it either)

record.pop()            # pop: returns -2, record is now [5]

# Telling a number apart from an operation symbol
op = "-2"
op in ("+", "D", "C")   # False -> op is a number, not a symbol
int(op)                  # -2 (int() parses the leading "-" correctly)

sum(record)              # adds up every item currently on the stack
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `record.append(x)` | `O(1)` on average | Adds at the end of a list |
| `record.pop()` | `O(1)` | Removes from the end, nothing else moves |
| `record[-1]`, `record[-2]` | `O(1)` | Goes straight to the position |
| `sum(record)` | `O(n)` | Has to add every item once |

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. For each kind of operation (`"5"`, `"+"`, `"D"`, `"C"`), does it push to the record, pop
   from it, both, or neither?
2. For `"+"`, the record grows from two scores to three, not from two to one. Which existing
   scores stay, and which one is new?
3. Walk through `operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]` by hand, drawing the
   record after each operation. What is the final record, and what does it sum to?
4. If you kept a single running total instead of a list, what exact piece of information
   would you be missing the moment `"C"` needs to undo the last round?
5. What should the function return when `operations` is empty?

<details>
<summary>Hint: how to structure your code</summary>

Each operation needs exactly one case: a number string pushes `int(op)`; `"+"` pushes the
sum of the last two items; `"D"` pushes double the last item; `"C"` pops. Once the loop
ends, the answer is one built-in call away from the record.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
