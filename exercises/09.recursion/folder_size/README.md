# Folder Size

**Pattern:** Recursion | **Difficulty:** Easy

## Problem

Your computer is running out of space, and you want to know how much a folder uses.

A folder is a list. Each item in this list is either:

- a **file**, written as an integer: its size
- a **subfolder**, written as a list that follows the same rules

Return the total size of all the files in the folder, including the files inside its
subfolders, at any depth. An empty folder has a size of `0`.

## Function to write

```python
def folder_size(folder: list) -> int:
```

## Examples

### Example 1: only files

```
folder = [10, 20, 5]
```

Output: `35`

### Example 2: one subfolder

```
folder = [10, [20, 5], 2]
```

Output: `37`

The subfolder has a size of `20 + 5 = 25`, and `10 + 25 + 2 = 37`.

### Example 3: several levels

```
folder = [10, [20, 5], [[3]], 2]
```

Output: `40`

### Example 4: an empty folder

```
folder = []
```

Output: `0`

### Example 5: only empty folders

```
folder = [[], [[]], []]
```

Output: `0`

## Constraints

- A folder has at most `200` levels of subfolders
- A folder and its subfolders contain at most `200,000` items in total
- `0 <= file size <= 10^9`
- Do not modify the input
- Target complexity: `O(n)` time, where `n` is the total number of items
- Standard library only, and write a recursive function: this is what you are here to
  learn

## Why recursion is useful for this problem

You could handle one level of subfolders with two nested loops, and two levels with
three loops. But the number of levels is only known when the code runs, so you cannot
know how many loops to write.

Look at the shape of the data instead. **A subfolder is also a folder.** So "what is
the size of this subfolder?" is the same question as the one your function already
answers, on a smaller input. Your function can ask itself.

Here is Example 3 as a tree. Each folder only adds up what is directly inside it:

```
folder                     10 + 25 + 3 + 2 = 40
|-- file 10
|-- folder                 20 + 5 = 25
|   |-- file 20
|   |-- file 5
|-- folder                 3
|   |-- folder             3
|       |-- file 3
|-- file 2
```

The top folder does not need to know what happens inside its subfolders. It asks for
their size and receives a number. This is the mental trick of recursion: **when you
write the recursive call, trust that it returns the right answer.** Do not try to
follow every level in your head. Check one level only.

**The recipe for any recursive function:**

1. **Base case:** what is the smallest input, the one you can answer without calling
   the function again?
2. **Smaller problem:** which part of the input has the same shape as the whole input?
3. **Combine:** once you receive the answer for the smaller part, how do you use it?

Every recursive call must get closer to a base case. Without that, the calls never
stop, and Python raises a `RecursionError`.

**What happens in the machine:** when a function calls itself, the current call waits
on a stack, with its own local variables. When the inner call returns, the waiting
call continues from where it stopped. Each call has its own variables, even though
they have the same names.

**How to recognize a recursion problem:**

- The data **contains smaller versions of itself**: folders, nested lists, JSON,
  trees, comment threads
- The depth is **only known when the code runs**, so you can't write the right number
  of loops
- You can describe the answer using the answer to a smaller version of the same problem

**When not to use it:** a simple loop is better for a flat list. Python stops at about
1000 nested calls, so recursion fits when the number of levels is small, not when the
number of items is big.

**Recursion and the other patterns:** recursion is a tool more than a pattern, and
other patterns are built on it.

| Pattern | What it adds to recursion |
| --- | --- |
| DFS | Remembers the places already visited |
| Backtracking | Makes a choice, explores, then undoes the choice |
| Dynamic programming | Saves the results, because the same calls come back |

Here, each subfolder is visited once, and there is no choice to undo: this is plain
recursion.

## Why the complexity is `O(n)`

Each file and each subfolder is handled once, and each one takes a constant amount of
work. The stack also uses memory: `O(d)`, where `d` is the deepest level, because one
call waits for each level.

## Real use cases

- Disk usage tools, such as the Linux `du` command or the Windows folder properties
- Searching for a value in a JSON document of unknown depth
- Counting the replies of a comment thread, where replies can have replies
- Counting the employees under a manager in a company tree
- Displaying a website menu with nested categories

## Useful Python syntax

```python
# Check the type of a value
isinstance(5, int)       # True
isinstance([1, 2], list) # True
isinstance(5, list)      # False

# Prefer isinstance to comparing with type(): type(x) == list is not pythonic

# A recursive function, on a different problem: 4! = 4 * 3 * 2 * 1
def factorial(n: int) -> int:
    if n <= 1:                      # base case: the answer is known
        return 1
    return n * factorial(n - 1)     # smaller problem + combine

# What happens when you call factorial(3):
#
# factorial(3) waits for factorial(2)
#     factorial(2) waits for factorial(1)
#         factorial(1) returns 1        <- base case: the calls stop here
#     factorial(2) returns 2 * 1 = 2
# factorial(3) returns 3 * 2 = 6

# Each call has its own local variables
def show_levels(level: int) -> None:
    label = f"level {level}"        # a different label in each call
    if level < 2:
        show_levels(level + 1)
    print(label)                    # prints level 2, then level 1, then level 0

show_levels(0)

# The limit of nested calls
import sys
sys.getrecursionlimit()  # usually 1000
```

## Before you code

Answer these on paper, using Example 3 (`[10, [20, 5], [[3]], 2]`). Tell Claude your
answers if you want to check them.

1. Calculate the size by hand. Which folder's size can you calculate first, and why
   that one?
2. List the calls of `folder_size` that happen, with the input of each one. How many
   are there?
3. An item can be one of two things. What does your function do with each of them?
4. `factorial` has a line that clearly stops the calls. What stops the calls in this
   problem? What happens with `[]`?
5. While `folder_size([20, 5])` is running, the top call has already added `10` to its
   total. Where is this `10` kept? Can the inner call change it?

<details>
<summary>Hint: if the files after a subfolder are not counted</summary>

Look at Example 2. When the call for `[20, 5]` finishes, the top folder still has the
file `2` to count. Read your code and check what happens just after the recursive
call. Does the top call continue?

</details>

<details>
<summary>Hint: if the big flat folder raises a RecursionError</summary>

A folder with 100,000 files has only one level. Ask yourself how many nested calls
your code makes for it. You need one nested call per level of folders, not one per
item.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
