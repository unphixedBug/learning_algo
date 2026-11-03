# Letter Subsets

**Pattern:** Backtracking | **Difficulty:** Easy

## Problem

A pizzeria gives each topping a letter. You receive a string with all the available
letters, and you must list **every pizza you can make**. For each topping, you either
put it on the pizza or you don't.

Return all the subsets of the letters, each one as a string. A pizza with no topping
counts too: it is the empty string `""`.

Inside a subset, the letters must keep the same order as in the input (`"ab"` is
valid for the input `"abc"`, `"ba"` is not). The subsets themselves can be returned
in any order.

## Function to write

```python
def letter_subsets(letters: str) -> list[str]:
```

## Examples

### Example 1: two letters

```
letters = "ab"
```

Output: `["", "a", "ab", "b"]`, in any order

### Example 2: three letters

```
letters = "abc"
```

Output: `["", "a", "ab", "abc", "ac", "b", "bc", "c"]`, in any order

### Example 3: the input order is kept

```
letters = "cab"
```

Output: `["", "a", "ab", "b", "c", "ca", "cab", "cb"]`, in any order

The subset with `c` and `a` is `"ca"`, because `c` comes first in the input.

### Example 4: no letter

```
letters = ""
```

Output: `[""]`

There is still one possible pizza: the one with no topping.

## Constraints

- `0 <= len(letters) <= 16`
- All the letters are different
- Target complexity: `O(n * 2^n)` time, where `n` is the number of letters
- Standard library only, but do not use `itertools`: it would do the part you are
  here to learn

## Why backtracking is useful for this problem

Each letter is a small decision: take it or skip it. With 3 letters, you make 3
decisions in a row, and the answer is every possible series of decisions.

Writing the decisions as nested loops does not work, because you would need one loop
per letter, and the number of letters is only known when the code runs. Recursion
solves this: each call handles **one decision**, then calls itself for the next one.
(Other solutions exist for this problem, but this one extends to harder problems with
rules to respect.)

Here are all the decisions for `"ab"`:

```
                     ""
          take a /        \ skip a
               "a"          ""
     take b /    \ skip b     take b /  \ skip b
         "ab"    "a"            "b"     ""
```

Each path from the top to the bottom gives one subset. The bottom row is the answer.

Backtracking walks through this tree with **a single list** (the current pizza), and
repeats three steps:

1. **Choose:** change the list (add a letter)
2. **Explore:** make a recursive call for the next decisions
3. **Undo:** put the list back as it was (remove the letter)

The undo step is what gives the pattern its name: you go back to a decision and try
the other option. It must leave the list **exactly as it was** before the choice,
otherwise the choice you just finished leaks into the next branch.

Backtracking is a DFS (it follows one route to its end, then comes back). The
difference is what it explores: DFS usually moves through places that already exist,
like the cells of a grid. Backtracking moves through **choices**, and builds the tree
as it goes.

**How to recognize a backtracking problem:**

- The problem asks for **all** the possibilities: "list every...", "generate all..."
- Or it asks to find one arrangement that respects rules (Sudoku, N-Queens)
- The answer is built **step by step**, with a decision at each step
- The input is small (often 20 elements or fewer), because the number of possibilities
  explodes

The small input is a good clue in an interview. If the problem only asks for a
**count** or a **best value**, and the input is big, think about dynamic programming
or greedy first.

## Why the complexity is `O(n * 2^n)`

Each letter doubles the number of subsets, so there are `2^n` of them, and building
one string costs up to `n` steps. It looks slow, but you cannot do better: if the
answer contains `2^n` strings, you have to create all of them.

## Real use cases

- A Sudoku solver: try a digit, continue, and undo it when you reach a dead end
- A tic-tac-toe or Connect Four AI: play a move, look at what follows, undo it, try
  the next move
- Generating a map under rules (no isolated town, a minimum distance between towns):
  remove a placement when it leads to a dead end
- A school timetable or shift planner, where assignments must not conflict
- Trying every combination of options in a test suite

## Useful Python syntax

```python
# A list used as a stack: add at the end, remove from the end
path = []
path.append("x")  # path is ["x"]
path.pop()        # path is [] again: this is an undo

# Build a string from a list of letters
"".join(["a", "b"])  # "ab"
"".join([])          # ""

# A string is a snapshot: it does not change when the list changes later
path = ["a", "b"]
word = "".join(path)
path.pop()
print(word)  # still "ab"

# A nested function can use the lists of the function around it.
# It can modify them without passing them on every recursive call.
def outer(words: list[str]) -> list[str]:
    collected = []

    def helper(index: int) -> None:
        if index == len(words):  # base case: stop here
            return
        collected.append(words[index].upper())
        helper(index + 1)  # recursive call

    helper(0)
    return collected
```

## Before you code

Answer these on paper, using Example 2 (`"abc"`). Tell Claude your answers if you want
to check them.

1. Draw the decision tree. How many levels of decisions does it have? How many
   subsets are at the bottom?
2. The code takes `a`, then `b`, then `c`, and reaches the subset `"abc"`. Which
   subset comes next? What must the list contain to get there, and what has to happen
   to it first?
3. What information does a recursive call need to know which decision it is making?
4. How does a call know that there are no decisions left? What must it do at this
   moment?
5. Imagine you forget the undo step. After `"abc"`, what does the code save instead
   of the subset you found in question 2?

<details>
<summary>Hint: the two branches</summary>

There is no need for a loop over the letters. One call handles one letter and has two
branches: one where the letter is on the pizza, and one where it isn't. Ask yourself
what the list must contain just before each of the two branches.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
