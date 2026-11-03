# Reverse a Linked List

**Pattern:** Linked list | **Difficulty:** Easy

## Problem

You are given `head`, the first node of a singly linked list. It is `None` if the list is empty.

Reverse the list **by changing the links between the nodes**, then return the new first node.

You must keep the same node objects:

- Do not create new nodes
- Do not change the `value` of a node

## Function to write

```python
def reverse_list(head: ListNode | None) -> ListNode | None:
```

The `ListNode` class is already written for you in `solution.py`.

## Examples

### Example 1: several nodes

```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
```

The function returns the node with the value `5`.

### Example 2: two nodes

```
Input:  1 -> 2 -> None
Output: 2 -> 1 -> None
```

### Example 3: one node

```
Input:  7 -> None
Output: 7 -> None
```

### Example 4: an empty list

```
Input:  None
Output: None
```

### Example 5: duplicate values

```
Input:  1 -> 1 -> 2 -> None
Output: 2 -> 1 -> 1 -> None
```

## Constraints

- `0 <= number of nodes <= 200000`
- `-1000 <= node.value <= 1000`
- Target complexity: `O(n)` time and `O(1)` extra space
- Standard library only

The list can be too long for a recursive solution, because Python stops at about 1000 nested calls
by default. Use a loop.

## Why a linked list is useful for this problem

A **linked list** is a chain of nodes. Each node holds a value and a link to the next node. The
variable `head` only gives you the first node: to reach the others, you follow the links one by
one.

```
head
 |
 v
[1 | next] --> [2 | next] --> [3 | next] --> None
```

A Python `list` keeps its items side by side, so it can jump straight to any position. A linked
list cannot jump, but it can insert or remove a node by changing a few links, without shifting
everything else.

This problem teaches the main skill of the pattern: **changing links without losing the rest of the
chain**. The nodes do not move. Only the arrows change direction:

```
Before:  1 -> 2 -> 3 -> None
After:   None <- 1 <- 2 <- 3
```

Each node only knows the node **after** it. Nothing can take you back to the previous node, and as
soon as you overwrite a link, you may lose everything that came after it. That is the real challenge
of this exercise.

**Real use cases:**

- **LRU cache for a REST API:** a hash map plus a doubly linked list finds an entry in `O(1)`, and
  moves it to the front in `O(1)`. It then removes the least recently used entry when the cache is
  full.
- **Music playlist:** "next" and "previous" follow links, and adding a track to the queue only changes
  a few of them.
- **Browser history:** each page links to the page before it and the page after it.
- **`collections.deque` in Python:** it is built on a doubly linked list of blocks, which is why it
  adds and removes at both ends in `O(1)`.

**How to recognize a linked list problem:**

- The input is a `head` node, or the problem shows `1 -> 2 -> 3`. This pattern is usually named in
  the problem, so recognizing it is easy
- The words **node**, **next**, **head** or **tail** appear
- You must **reorder, insert or remove** nodes, and you are told not to copy the values elsewhere
- Items are added or removed in the middle often, but rarely read by position

## Useful Python syntax

```python
# A node is an ordinary object with two attributes
first = ListNode(1)
second = ListNode(2)
first.next = second         # 1 -> 2 -> None

first.value                 # 1
first.next                  # the node that holds 2
first.next.value            # 2
second.next                 # None

# Walking through a list, from the first node to the last
current = first
while current is not None:
    print(current.value)
    current = current.next

# Compare with None using "is", not "=="
if current is None:
    ...

# Careful: following a link from None raises an error
empty = None
empty.next                  # AttributeError

# Assigning several variables on one line
x, y = 1, 2
x, y = y, x                 # swap: x is 2 and y is 1
```

**The most important distinction of this pattern:**

```python
current = current.next      # moves the variable: the list does not change
current.next = other        # changes a link: the list is now different
```

A variable is only a **label** placed on a node. Moving a label changes nothing in the list.
Assigning to `.next` is the only thing that changes the chain.

**The cost of common operations:**

| Operation | Python `list` | Linked list | Why |
|---|---|---|---|
| Read the item at position `i` | `O(1)` | `O(n)` | A linked list must follow the links from `head` |
| Insert or remove at the start | `O(n)` | `O(1)` | A `list` shifts every item, a linked list changes one link |
| Insert or remove after a node you already have | `O(n)` | `O(1)` | Only the links around that node change |
| Search for a value | `O(n)` | `O(n)` | Both must check the items one by one |

## Before you code

Answer these on paper. Tell Claude your answers if you want to check them.

1. Draw `1 -> 2 -> 3 -> None`, then draw the reversed list. For each node, what does `next` point to
   before and after? What must the `next` of node `1` become?
2. You are on node `2`, and you set its `next` to node `1`. How can you now reach node `3`? What
   should you have done before changing the link?
3. Node `2` needs to point back to node `1`, but a node does not know the node before it. How can
   your code still have that information when it reaches node `2`?
4. When your loop ends, which node is the new first node? Is the variable you used to walk through
   the list still pointing to it?
5. Run your idea by hand on an empty list and on a single node. Do you need a special case for them?

<details>
<summary>Hint: how to structure your code</summary>

At each step, your code needs to know about three nodes: the one you are on, the one before it, and
the one after it. Decide what each of them is **before the first step**. Then write the steps in an
order that never loses the rest of the chain.

</details>

If `pytest` never finishes, press `Ctrl+C`: your loop probably never ends, for example because the
links now form a circle or the walking variable never moves.

Stuck? Ask Claude for a code snippet of the part that blocks you.
