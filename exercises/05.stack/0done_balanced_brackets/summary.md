# Balanced Brackets: Summary

**Pattern:** Stack

## Final solution

```python
def is_balanced(text: str) -> bool:
    brackets = []

    for char in text:
        if char in ["(", "[", "{"]:
            brackets.append(char)
        elif brackets and char == ")" and brackets[-1] == "(":
            brackets.pop()
        elif brackets and char == "]" and brackets[-1] == "[":
            brackets.pop()
        elif brackets and char == "}" and brackets[-1] == "{":
            brackets.pop()
        else:
            return False

    return not brackets
```

## How it works

Each opening bracket goes on the stack. Each closing bracket must match the top of the stack, which is then removed.

With `"{[()]}"`:

| `char` | Action | Stack after |
|---|---|---|
| `{` | Push | `{` |
| `[` | Push | `{[` |
| `(` | Push | `{[(` |
| `)` | Matches `(`, pop | `{[` |
| `]` | Matches `[`, pop | `{` |
| `}` | Matches `{`, pop | empty |

The stack is empty at the end, so the function returns `True`.

With `"([)]"`, the stack is `([` when `)` arrives. The top is `[`, not `(`, so the function returns `False` right away.

## Why it works

- **The stack follows the rule of the problem:** the last bracket opened must be the first one closed, which is the LIFO rule.
- **Only the top matters:** a closing bracket can only match the most recent unclosed bracket, so there is no need to look further down.
- **A closing bracket can be wrong in two ways:** the stack is empty (`")("`), or the top has the wrong type (`"(]"`). Both reach the `else` and return `False`.
- **The check after the loop is needed:** with `"(()"`, no closing bracket is wrong, but one opening bracket is never closed. `not brackets` catches this.
- **The empty string works:** the loop never starts, and an empty stack gives `True`.

## Complexity

- **Time: `O(n)`:** the loop visits each character once, and `append`, `pop` and `[-1]` are `O(1)`. `char in ["(", "[", "{"]` is also `O(1)` here, because the list always has 3 items.
- **Space: `O(n)`:** in the worst case, such as `"((((("`, every character goes on the stack.

## Key lessons

**Check that the stack isn't empty before reading it.** `brackets[-1]` and `brackets.pop()` raise an `IndexError` on an empty list. Thanks to short-circuiting, `brackets and ...` stops before reading when the stack is empty.

**"Nothing went wrong during the loop" isn't always enough.** Ask what must still be true when the loop ends. In a stack problem, this is often that the stack is empty.

**Counting brackets isn't enough.** `"([)]"` has one of each bracket and still isn't balanced, because counting forgets the order.

## Python syntax I learned

**A list can be used directly as a condition:** an empty list counts as `False`, and a non-empty list counts as `True`.

```python
if not stack:    # the stack is empty
    ...
if stack:        # the stack has at least one item
    ...
```

**Return a boolean expression directly:** `not brackets` is already `True` or `False`.

```python
return True if not brackets else False  # too long
return not brackets                     # same result
```

## Mistakes I made

| Mistake | Problem | Fix |
|---|---|---|
| Reading `brackets[-1]` without checking the stack | `")("` raises an `IndexError` instead of returning `False` | Add `brackets and` before reading the top |
| `return True` after the loop | `"(()"` returns `True` even though a bracket is never closed | `return not brackets` |
| `return True if not brackets else False` | It works, but it's longer than needed | `return not brackets` |

## Other approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Stack with one `elif` per type (mine)** | `O(n)` | `O(n)` | Clear, but repeats the same logic for each type |
| **Stack with a dict** | `O(n)` | `O(n)` | Adding a bracket type only takes one new dict entry |

```python
OPENING_FOR = {")": "(", "]": "[", "}": "{"}


def is_balanced(text: str) -> bool:
    stack = []

    for char in text:
        if char in OPENING_FOR:
            if not stack or stack.pop() != OPENING_FOR[char]:
                return False
        else:
            stack.append(char)

    return not stack
```

- **`not stack or stack.pop() != ...`:** if the stack is empty, Python skips the right side, so `pop()` never runs on an empty stack.
- **`pop()` inside the condition:** a mismatch makes the function return immediately, so it doesn't matter that the bracket was removed.
- **I kept my version for now:** the complexity is the same, but I should use the dict the next time I need to match pairs.

## In an interview

- Explain why counting isn't enough, using `"([)]"`.
- List the failure cases out loud: wrong type, empty stack on a closing bracket, and brackets left in the stack at the end.
- Test `""`, `")("` and `"(()"` by hand before saying you're done.
- An interviewer may notice the repeated `elif`s, so the dict version is the better one to write.

## Level

Stay at level 0 for Stack for now, because this was the first exercise. The push and pop logic was right from the start, but the two edge cases needed hints. Move to level 1 if the next exercise goes well without help on the logic.

## English corrections

| I wrote | More natural |
|---|---|
| "i am on stack/balanced_bracket exercise, is my debut solution correct or am i on the wrong path" | "I am working on the stack/balanced_brackets exercise. Is my initial solution correct, or am I on the wrong path?" |
| "review and more pythonic solution" | "Please review my code and show me a more Pythonic solution." |
| "the tests pass, what about complexity ?" | "The tests pass. What about the complexity?" |
| "i would keep mine for now" | "I'll keep mine for now." |

- Always capitalize "I".
- "Debut" means a first public appearance, such as an actor's debut. Use "initial" or "first" for a first version of something.
- Use "I'll" for a decision. "I would" needs a condition.
- English has no space before a question mark.
