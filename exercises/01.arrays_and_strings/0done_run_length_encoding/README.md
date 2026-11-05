# Run-Length Encoding

**Pattern:** Arrays and strings (single-pass scan) | **Difficulty:** Easy

## Problem

You are given a string. Compress it by replacing each **group of consecutive identical
letters** with the size of the group, followed by the letter.

Return the compressed string.

## Function to write

```python
def run_length_encode(text: str) -> str:
```

## Examples

### Example 1

```
text = "wwwggopp"
```

Output: `"3w2g1o2p"` (three `w`, two `g`, one `o`, two `p`)

### Example 2: every group has one letter

```
text = "abc"
```

Output: `"1a1b1c"`

The result can be longer than the original. That is expected.

### Example 3: a letter comes back later

```
text = "aaabaa"
```

Output: `"3a1b2a"` (the `a`s are not next to each other, so they form two separate groups)

### Example 4: a group of 10 or more

```
text = "aaaaaaaaaaaa"
```

Output: `"12a"`

### Example 5: an empty string

```
text = ""
```

Output: `""`

## Constraints

- `0 <= len(text) <= 400000`
- `text` contains only letters, `a-z` and `A-Z`
- Uppercase and lowercase are different letters: `"aA"` gives `"1a1A"`
- Target complexity: `O(n)` time
- Standard library only

## Why a single-pass scan is useful for this problem

Most array and string problems are solved by **reading the items from left to right once,
while remembering a small amount of information** about what you have just read. Hash maps,
two pointers and sliding windows all build on this idea, which is why it comes first.

Here, the answer depends on **which letters are next to each other**. You never need to look
far away: comparing a letter with its neighbor tells you if a group continues or ends. So
there is no reason to go back and read the same letter twice, and one pass is enough.

**Real use cases:**

- **Logs:** a system log writes `last message repeated 5 times` instead of the same line 5 times.
- **Images:** a line of 1,000 white pixels can be stored as "1000 white". Some image formats, such as BMP and TIFF, can use this method.
- **Fax machines:** a scanned page is mostly long runs of white, so faxes compress it this way.

**How to recognize a single-pass scan problem:**

- The problem talks about **consecutive** or **adjacent** items, or a **run** of items
- The order of the items matters, so sorting them would destroy the answer
- You can decide what to do with each item using only **what you have already read**
- The words **longest streak**, **current group**, or **best so far** appear

## Useful Python syntax

```python
# Reading a string or a list by position
text = "hello"
text[0]                     # 'h'
text[-1]                    # 'o' (the last item)
len(text)                   # 5

# Looping
for letter in text:         # each letter
    ...
for i in range(1, len(text)):  # the positions 1, 2, 3, 4 (skips position 0)
    ...

# Building a string from pieces
parts = []
parts.append("hello")
parts.append("world")
"".join(parts)              # 'helloworld'
" ".join(parts)             # 'hello world'

# Putting a number inside a string
count = 3
f"{count}x"                 # '3x'
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `text[i]` | `O(1)` | Goes straight to the position |
| `text[i:j]` | `O(j - i)` | A slice **copies** the items |
| `parts.append(x)` | `O(1)` on average | Adds at the end of a list |
| `parts.insert(0, x)` | `O(n)` | Every other item must shift |
| `x in my_list` | `O(n)` | Checks the items one by one |
| `"".join(parts)` | `O(total length)` | Builds the final string once |

**Strings are immutable:** you can never change a string, only create a new one. So
`result += "abc"` may copy all of `result` every time, which is `O(n²)` overall in the worst
case. CPython often avoids this copy, but the language does not guarantee it. The reliable
Python habit is to collect the pieces in a list and call `"".join(...)` once at the end.

## Before you code

Answer these on paper, using `"aaabaa"`. Tell Claude your answers if you want to check them.

1. While reading from left to right, which **two pieces of information** do you need to
   remember at each moment?
2. What exact event tells you that a group has ended? What must you do when it happens?
3. Walk through `"abb"` by hand. When the loop finishes, has the last group been added to the
   result? Why or why not?
4. Why would counting every letter in a `dict` give a wrong answer for `"aaabaa"`?
5. What would happen with an empty string if your code starts by reading `text[0]`?

<details>
<summary>Hint: how to structure your code</summary>

Think of your code in three parts: what you set up **before** the loop, what you do for each
letter **during** the loop, and what is left to do **after** the loop.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
