# Valid Palindrome

**Pattern:** Two pointers | **Difficulty:** Easy

## Problem

A palindrome reads the same from left to right and from right to left, like `level`.

You are given a text. Return `True` if it is a palindrome, and `False` otherwise.

Only letters and digits count:

- Ignore spaces and punctuation
- Ignore uppercase and lowercase differences (`A` and `a` are the same)

A text with no letters or digits counts as a palindrome.

## Function to write

```python
def is_palindrome(text: str) -> bool:
```

## Examples

### Example 1

```
text = "level"
```

Output: `True`

### Example 2: spaces, punctuation and uppercase

```
text = "A man, a plan, a canal: Panama"
```

Output: `True` (only `amanaplanacanalpanama` counts)

### Example 3

```
text = "race a car"
```

Output: `False` (only `raceacar` counts, and the fourth letter from each end differs: `e` and `a`)

### Example 4: nothing to compare

```
text = ".,!"
```

Output: `True`

## Constraints

- `0 <= len(text) <= 400000`
- `text` only contains printable ASCII characters
- Target complexity: `O(n)` time and `O(1)` extra space
- Do not build a cleaned or reversed copy of the text in this exercise, so that you practice
  the pattern (the tests cannot check this)
- Built-in tools only: no libraries to install

## Why two pointers are useful for this problem

This uses the same form as `pair_sum_sorted`: one pointer at each end, moving toward
each other.

The definition of a palindrome already describes two pointers: the first character must
match the last one, the second must match the second to last, and so on. So you compare
characters **in pairs, from the outside in**.

This gives you two advantages compared with building a reversed copy:

- **No extra memory:** you only need two indices, not a second text
- **You can stop early:** the first pair that differs gives you the answer

There is one important difference from `pair_sum_sorted`: **nothing needs to be sorted**.
Here the pattern works because of the symmetry of the problem, not because of sorted
order. Two pointers are not only for sorted lists.

**How to recognize this form of two pointers:**

- The problem is about **symmetry**, or about comparing both ends of a sequence
- You are asked to use **no extra memory**

## Before you code

Answer these on paper, using `"a, b a"`. Tell Claude your answers if you want to check them.

1. Which pairs of characters do you compare, and in which order?
2. A pointer lands on a `,` or a space. What should it do? Does the other pointer move too?
3. When can you stop and return `True`? Why is there no need to compare the middle `b`?

<details>
<summary>Hint: the tools you need</summary>

Two string methods do most of the work:

- `character.isalnum()` tells you if a character is a letter or a digit
- `character.lower()` gives you the lowercase version

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
