# Balanced Brackets

**Pattern:** Stack | **Difficulty:** Easy

## Problem

You are given a string that contains only the brackets `(`, `)`, `[`, `]`, `{` and `}`.

The string is **balanced** if:

- Every opening bracket is closed by a bracket of the **same type**
- Brackets are closed in the **correct order**: an inner pair must close before the pair
  around it
- Every closing bracket has a matching opening bracket **before** it

Return `True` if the string is balanced, and `False` otherwise.

## Function to write

```python
def is_balanced(text: str) -> bool:
```

## Examples

### Example 1: pairs side by side

```
text = "()[]{}"
```

Output: `True`

### Example 2: nested pairs

```
text = "{[()]}"
```

Output: `True`

### Example 3: wrong type

```
text = "(]"
```

Output: `False` (a `(` cannot be closed by a `]`)

### Example 4: right brackets, wrong order

```
text = "([)]"
```

Output: `False` (the `[` was opened last, so it must be closed before the `(`)

### Example 5: a bracket is never closed

```
text = "(()"
```

Output: `False`

### Example 6: nothing to close

```
text = ")("
```

Output: `False` (the `)` comes before any opening bracket)

### Example 7: an empty string

```
text = ""
```

Output: `True` (there is no bracket left unclosed)

## Constraints

- `0 <= len(text) <= 400000`
- `text` contains only the characters `()[]{}`
- Target complexity: `O(n)` time
- Standard library only

## Why a stack is useful for this problem

A **stack** is a pile: you can only add to the top and remove from the top, like a pile of
plates. The last item you put on is the first one you take off. This rule is called
**LIFO** (Last In, First Out).

```
push A      push B      push C      pop → C     pop → B

                        | C |
            | B |       | B |       | B |
| A |       | A |       | A |       | A |       | A |
```

Look at the opening brackets in `{[(`. The `(` came last, but it is the first one that must be
closed. **The last one opened is the first one closed**, which is exactly the LIFO rule.

Counting brackets is not enough, because counting forgets the **order**. `"([)]"` has one of
each bracket, and it is still not balanced. A stack remembers what is still waiting, with the
most recent item always on top, in reach.

**Real use cases:**

- **Calculators:** before computing `(1 + 2) * [3 - 4]`, a calculator checks that the
  parentheses are balanced. It can then evaluate the innermost group first.
- **Code editors and compilers:** Python tells you `closing parenthesis ')' does not match
  opening parenthesis '['` thanks to this check. HTML and JSON parsers do the same with nested tags
  and objects.
- **Undo:** each action goes on a stack, and Ctrl+Z cancels the most recent one first.
- **Browser "back" button:** each page you leave goes on a stack, and "back" returns to the most
  recent one.

**How to recognize a stack problem:**

- Items are **nested**, or one thing must finish before the thing around it can finish
- Each new item may **cancel or match the most recent** item still waiting
- The words **matching**, **valid**, **balanced**, **nested**, **undo** or **backspace** appear
- You read from left to right, but you sometimes need to look **back at the latest unfinished
  item**, not at all of them

## Useful Python syntax

A Python `list` works as a stack, as long as you only use its **end** as the top.

```python
# Creating and using a stack
stack = []
stack.append("a")           # push: ['a']
stack.append("b")           # push: ['a', 'b']
stack[-1]                   # peek: 'b' (reads the top, does not remove it)
stack.pop()                 # pop: returns 'b', the stack is now ['a']

# Checking if a stack is empty (the Pythonic way)
if not stack:               # True when the stack is empty
    ...
if stack:                   # True when the stack has at least one item
    ...

# Careful: reading an empty stack raises an error
empty = []
empty.pop()                 # IndexError
empty[-1]                   # IndexError

# A dict links one value to another
capitals = {"France": "Paris", "Japan": "Tokyo"}
capitals["Japan"]           # 'Tokyo'
"Japan" in capitals         # True  (searches the keys, in O(1) on average)
"Tokyo" in capitals         # False (does not search the values)
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `stack.append(x)` | `O(1)` on average | Adds at the end of a list |
| `stack.pop()` | `O(1)` | Removes from the end, nothing else moves |
| `stack[-1]` | `O(1)` | Goes straight to the position |
| `stack.insert(0, x)` | `O(n)` | Every other item must shift |
| `stack.pop(0)` | `O(n)` | Every other item must shift |

This is why the top of your stack must be the **end** of the list, never the start.

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. In `"{[()]}"`, write the opening brackets in the order they appear, then the closing brackets
   in the order they appear. What do you notice?
2. Walk through `"([)]"` one character at a time, and draw the stack after each one. At which
   character do you know that the string is not balanced? How do you know?
3. When you read a **closing** bracket, there are two different ways that it can be wrong. What
   are they? Look at examples 3 and 6.
4. Walk through `"(()"` by hand. The loop ends without any problem, yet the answer is `False`.
   What is left to check after the loop?
5. When you read a `]`, how does your code know that the matching opening bracket is `[`? Which
   data structure from the syntax section could help?

<details>
<summary>Hint: how to structure your code</summary>

Your loop has only two cases: the character is an **opening** bracket, or it is a **closing**
bracket. Decide what each case does to the stack. Then decide what must be true about the stack
when the loop ends.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
