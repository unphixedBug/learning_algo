# Sliding Window: Summary

**Current level:** 0

## The pattern: update the edges instead of starting over

A window is a group of items next to each other. When it moves one step, only the items at its edges change, so you update what you already know instead of calculating it again.

Each move costs `O(1)`, so a full scan goes from `O(n * k)` to `O(n)`, usually with `O(1)` extra memory.

## When to use it

- The data is a **list or a string**, and the order matters
- The question is about items **next to each other**: **consecutive**, **contiguous**, **subarray**, **substring** or **in a row**
- The words **largest**, **smallest**, **longest** or **shortest** often appear
- Going from one group to the next changes only **a few items at the edges**

**Don't confuse it with a prefix sum.** A sliding window moves from left to right, and is usually used to find one best range. A prefix sum can answer many ranges, in any order.

## How to think about it

Before coding, answer these questions:

1. What do I need to **know about the current window**? (This is the state, such as its sum.)
2. Which item **enters** and which item **leaves** at each move? What are their indexes?
3. How do I **update the state** using only those items?
4. What is the **first window**, and does it count as a candidate for the answer?

## The structure

This is the fixed-size version. The item that enters is at index `i`, and the item that leaves is at index `i - k`.

```
index:    0  1  2  3  4  5
nums:     2  1  5  1  3  2

         [2, 1, 5]            first window
            [1, 5, 1]         i = 3: nums[3] enters, nums[0] leaves
```

```python
if k > len(items):
    return None

state = compute(items[:k])
answer = state

for i in range(k, len(items)):
    state = update(state, entering=items[i], leaving=items[i - k])
    answer = best(answer, state)

return answer
```

`compute`, `update` and `best` stand for the rules of each problem. For a maximum sum, they are `sum`, `state + entering - leaving` and `max`.

| Operation | Cost |
|---|---|
| `total += x` | `O(1)` |
| `nums[i]` | `O(1)` |
| `nums[a:b]` | `O(b - a)`, because it copies the items |
| `sum(items)` | `O(len(items))`, so never call it for each window |

## Traps

- **Mixing up the state and the answer:** the state always describes the current window, even when it's bad. Updating it from the best answer gives wrong sums.
- **Forgetting the first window:** a loop over the entering items only sees the windows after the first one, so set `answer` from the first window.
- **Starting the answer at `0`:** with only negative numbers, `0` wins even though no window has that sum.
- **Missing the last window:** check that the loop reaches the last item. A window that is the whole list means that the loop never runs, which must still work.
- **Rebuilding the window at each step:** a slice or a `sum` inside the loop looks short but costs `O(k)`, and a slice doesn't follow your indexes when they change.

## In an interview

- Name the slow `O(n * k)` approach first, then explain what neighboring windows share.
- Say what the state and the answer each mean before coding.
- Test by hand a list of negative numbers, a window that is the whole list, and a list that is too short.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `max_sum_window` | Easy | Keeping a fixed-size window's sum up to date with one subtraction and one addition | Finding the update formula, and keeping the current sum separate from the best sum |

## Next step

Stay at level 0 for now. Do another fixed-size window exercise, then move to level 1 if it goes mostly alone. After that, the next idea to learn is a window that grows and shrinks.
