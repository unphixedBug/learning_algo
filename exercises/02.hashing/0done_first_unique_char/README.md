# First Unique Character

**Pattern:** Hash map / Hash set (frequency counting) | **Difficulty:** Easy

## Problem

You are given a string `s` made of lowercase English letters.

Return the **index of the first character that appears exactly once**. If no such character
exists, return `-1`.

## Function to write

```python
def first_unique_char(s: str) -> int:
```

## Examples

### Example 1

```
s = "leetcode"
```

Output: `0` (`l` appears once, and it is the first character)

### Example 2

```
s = "loveleetcode"
```

Output: `2` (`l` and `o` both repeat later, `v` does not)

### Example 3: every character repeats

```
s = "aabb"
```

Output: `-1`

### Example 4: an empty string

```
s = ""
```

Output: `-1`

### Example 5: a single character

```
s = "z"
```

Output: `0`

### Example 6: the unique character is not the first one checked twice

```
s = "ccv"
```

Output: `2` (`c` appears twice, `v` appears once)

## Constraints

- `0 <= len(s) <= 100000`
- `s` contains only lowercase English letters
- Target complexity: `O(n)` time and `O(1)` extra space (there are only 26 possible letters)
- Standard library only

## Why a hash map is useful for this problem

The question has two parts hidden inside it: "how many times does each letter appear?", then
"which is the **first** one with a count of exactly `1`?".

The naive approach asks, for each character, "how many times does this appear in the whole
string?" with something like `s.count(ch)`. That single line costs `O(n)`, and you would run it
for every character, so `O(n²)` overall.

A hash map removes the repeated counting. One pass builds a `dict` of `{character: count}` in
`O(n)`. A second pass walks the string again, and for each character you now get its count in
`O(1)` — no more searching.

**Hash map or hash set?**

- A hash set only knows "have I seen this?"
- Here you need **how many times**, so a hash map (`dict`) is required, not a set.

**Real use cases:**

- **Log analysis:** find the first error type that occurred only once, as a signal of a rare,
  possibly interesting event.
- **Text/spelling tools:** spot the rare letters in a word.
- **"Odd one out" puzzles:** find the first item that does not repeat.

**How to recognize a frequency-counting hash map problem:**

- The words **count**, **frequency**, **exactly once**, or **duplicate** appear
- You need to know **how many times** something occurred, not just whether it occurred
- A naive solution recomputes a count from scratch for every item, so it is `O(n²)`

## Useful Python syntax

```python
counts = {}

# Building counts by hand
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
# counts == {'b': 1, 'a': 3, 'n': 2}

# Looping with both index and value
for i, ch in enumerate("banana"):
    ...

# Checking a count
counts["a"] == 1   # False, 'a' appears 3 times
```

**The cost of common operations:**

| Operation | Cost | Why |
|---|---|---|
| `counts[ch] = counts.get(ch, 0) + 1` | `O(1)` | A single lookup and a single write |
| `s.count(ch)` | `O(n)` | Scans the whole string |
| `ch in counts` | `O(1)` | A single lookup |

**Trap:** calling `s.count(ch)` once per character you loop over turns an `O(n)` loop into an
`O(n²)` program, since each call re-scans the whole string.

## Before you code

Answer these on paper, using `s = "loveleetcode"`. Tell Claude your answers if you want to check
them.

1. What are the counts of each letter in this string? Which letters have a count of `1`?
2. Among the letters with a count of `1`, which one has the **smallest index**? Why do you need
   a second pass over the string to find it, instead of just reading the counts dictionary
   directly?
3. Why can't you answer the question in a single pass, the way `max_consecutive_ones` could?
   What do you not yet know about a character the first time you see it?
4. In Example 6 (`"ccv"`), walk through both passes by hand. What does the counts dictionary look
   like after pass 1? What happens during pass 2?

<details>
<summary>Hint: how to structure your code</summary>

Two separate loops over `s`:

1. The first loop fills a `dict` with how many times each character appears.
2. The second loop goes through `s` again, in order, and returns the index of the first
   character whose count is `1`. If the loop finishes with nothing found, return `-1`.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
