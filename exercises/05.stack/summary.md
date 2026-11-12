# Stack: Summary

**Current level:** 0

## The pattern: the last one in is the first one out

A stack is a pile: you only add to the top and remove from the top. This rule is called **LIFO** (Last In, First Out).

It keeps the items that are still waiting, with the most recent one always in reach. Each item is pushed and popped at most once, so a full scan usually costs `O(n)` time and up to `O(n)` extra memory.

## When to use it

- Items are **nested**, or one thing must finish before the thing around it can finish
- Each new item may **cancel or match the most recent** item still waiting
- The problem mentions **matching**, **valid**, **balanced**, **nested**, **undo**, **cancel** or **backspace**
- You read from left to right, but you need to look back at the **latest unfinished item**, not at all of them
- Each new step reads or removes only the **most recent value(s)** of a history

**Don't confuse it with counting.** A counter forgets the order. `"([)]"` has one of each bracket and still isn't balanced.

**Don't confuse it with a running total.** A total forgets the values it adds up, so it can't undo the last one. When a step can cancel the past, keep the history on a stack.

## Two ways to use a stack

| Use | What's on the stack | Answer at the end | Example |
|---|---|---|---|
| **Matching** | Items still waiting for their partner | Usually "is the stack empty?" | `balanced_brackets` |
| **History** | Every value that is still valid | Computed from what's left, such as `sum(stack)` | `score_keeper` |

## How to think about it

Before coding, answer these questions:

1. What goes **on** the stack, and what does it mean for an item to be there?
2. What makes me **remove** an item?
3. What happens if the stack is **empty** when I need to read it?
4. What must be true about the stack **when the loop ends**?

## The structure

A Python `list` works as a stack, as long as the end of the list is the top.

```python
stack = []

for item in items:
    if should_wait(item):
        stack.append(item)
    elif not stack or not matches(stack[-1], item):
        return False
    else:
        stack.pop()

return not stack
```

`should_wait` and `matches` stand for the rules of each problem.

For a history stack, each step pushes a new value (possibly computed from `stack[-1]` and `stack[-2]`) or pops the last one, and the answer is computed from the stack after the loop.

| Operation | Cost |
|---|---|
| `stack.append(x)` | `O(1)` on average |
| `stack.pop()` | `O(1)` |
| `stack[-1]` | `O(1)` |
| `stack.insert(0, x)` or `stack.pop(0)` | `O(n)`, so never use the start of the list as the top |

## Traps

- **Reading an empty stack:** `stack[-1]` and `stack.pop()` raise an `IndexError`. Check the stack first, and let short-circuiting protect the read: `not stack or ...`.
- **Forgetting the check after the loop:** items left on the stack may mean that the answer is wrong, as in `"(()"`.
- **Repeating logic for each type:** when items come in pairs, use a dict to link them instead of writing one `elif` per type.
- **Replacing instead of pushing:** an operation that reads the top items (like `"+"`) usually leaves them in place and pushes its result on top.
- **Validating with a bare `return`:** it gives `None` instead of the promised type. Raise an exception, or skip the check when the input is guaranteed to be valid.

## In an interview

- Explain why the most recent item is the only one that matters. That's the reason for using a stack.
- List the failure cases out loud before coding.
- Test an empty input, a closing item with nothing to match, and an item that is never closed.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `balanced_brackets` | Easy | Matching each closing item with the most recent opening item | The empty stack and the check after the loop |
| `score_keeper` | Easy | Using a stack as an undoable history | Nothing on the logic |

## Next step

Move to level 1: the logic of `score_keeper` was right without help.
