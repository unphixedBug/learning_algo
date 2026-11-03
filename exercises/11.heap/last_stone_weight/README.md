# Last Stone Weight

**Pattern:** Heap | **Difficulty:** Easy

## Problem

You are given a list of stones, where `stones[i]` is the weight of the `i`-th stone.

On each turn, pick the two **heaviest** stones and smash them together. If the stones
have weights `x` and `y` with `x <= y`:

- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` is
  replaced with a new stone of weight `y - x`.

Repeat until there is at most one stone left. Return the weight of the last remaining
stone, or `0` if none remain.

## Function to write

```python
def last_stone_weight(stones: list[int]) -> int:
```

## Examples

### Example 1

```
stones = [2, 7, 4, 1, 8, 1]
```

Output: `1`

Explanation:
- Smash 8 and 7 -> 1. Stones left: `[2, 4, 1, 1, 1]`
- Smash 4 and 2 -> 2. Stones left: `[2, 1, 1, 1]`
- Smash 2 and 1 -> 1. Stones left: `[1, 1, 1]`
- Smash 1 and 1 -> 0 (both destroyed). Stones left: `[1]`
- Last stone weighs `1`

### Example 2

```
stones = [1]
```

Output: `1` (only one stone, nothing to smash)

## Constraints

- `1 <= len(stones) <= 30`
- `1 <= stones[i] <= 1000`
- Target complexity: `O(n log n)` time
- Built-in tools only: no libraries to install

## Why a heap is useful for this problem

A heap is a data structure that always keeps the **smallest (or largest) item on top**,
so you can grab it in `O(log n)` time instead of scanning the whole list every time.

Here, you repeatedly need "the two biggest stones right now". A plain list would force
you to re-sort or re-scan after every smash, which is `O(n)` per turn. A heap keeps the
largest stone accessible in `O(log n)`, each time you remove or add one.

**How to recognize a heap problem:**

- You repeatedly need the **smallest or largest** remaining item
- The set of items **changes over time** (items get added or removed), so sorting once
  isn't enough
- Keywords like "top k", "kth largest/smallest", "closest", "most/least frequent",
  "merge sorted streams", "schedule by priority"

### Real use cases

- **Task scheduling**: an OS or job queue always runs the highest-priority task next
- **Dijkstra's shortest path**: always expand the closest unvisited node next
- **Streaming "top K"**: keep the K largest values seen so far in a live data feed
- **Event simulation**: always process the next event in chronological order

## Python syntax that may be useful

Python's `heapq` module only provides a **min-heap** (smallest item on top).

```python
import heapq

heap = [5, 1, 8]
heapq.heapify(heap)        # turn a list into a heap in place, O(n)

heapq.heappush(heap, 3)    # add an item, O(log n)
smallest = heapq.heappop(heap)  # remove and return the smallest item, O(log n)

heap[0]                    # peek at the smallest item without removing it, O(1)
```

To simulate a **max-heap** (largest item on top), push the negated values:

```python
heap = [-x for x in stones]
heapq.heapify(heap)

heapq.heappush(heap, -new_value)
largest = -heapq.heappop(heap)
```

## Before you code

Answer these on paper, using Example 1.

1. Why does pushing negated numbers onto a min-heap give you a max-heap behavior?
2. After smashing the two heaviest stones, where does the resulting stone need to go
   so the heap stays correct?
3. What should the function return if `stones` has only one element? What about if the
   heap becomes completely empty?

<details>
<summary>Hint: check your answer to question 1</summary>

The min-heap always keeps the *smallest* number on top. If every number is negated,
the smallest negated number corresponds to the *largest* original number. Remember to
negate it back when you read it out.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
