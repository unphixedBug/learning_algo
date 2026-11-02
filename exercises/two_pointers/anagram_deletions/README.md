# Anagram Deletions

**Pattern:** Two pointers | **Difficulty:** Easy

## Problem

Two words are anagrams if they contain exactly the same letters, the same number of
times, in any order. For example, `listen` and `silent` are anagrams.

You are given two words. You can delete any letter from either word.

Return the **minimum number of letters to delete** so that the two words become
anagrams of each other. Deleting every letter is allowed: two empty words count as
anagrams.

## Function to write

```python
def anagram_deletions(first: str, second: str) -> int:
```

## Examples

### Example 1

```
first = "cde"
second = "abc"
```

Output: `4` (they only share `c`, so delete `d`, `e`, `a` and `b`)

### Example 2: already anagrams

```
first = "listen"
second = "silent"
```

Output: `0`

### Example 3: repeated letters

```
first = "aab"
second = "abb"
```

Output: `2` (delete one `a` from `first` and one `b` from `second`, leaving `ab` twice)

### Example 4: one word runs out first

```
first = "abcd"
second = "ab"
```

Output: `2` (delete `c` and `d`)

## Constraints

- `0 <= len(first), len(second) <= 40000`
- The words only contain lowercase letters from `a` to `z`
- Sort both words first, using the built-in `sorted()`, then use two pointers
- Do not use a dictionary or `collections.Counter` in this exercise, so that you practice
  the pattern (the tests cannot check this)
- Target complexity: `O(n log n)` time, because of the sorting

## Why two pointers are useful for this problem

In `pair_sum_sorted`, both pointers started at opposite ends of one list and moved
toward each other. Here you use the other common form: **one pointer per sequence, and
both start at the beginning and move forward**.

Two pointers are useful here for the same reason as before: **sorting lets you throw
letters away for good**. After sorting, equal letters are next to each other, and every
letter ahead of a pointer is the same or later in the alphabet. So comparing the two
current letters tells you what to do with one of them, without looking at the rest of
the words.

**How to recognize this form of two pointers:**

- You have **two sorted sequences**, or two you can sort
- You need to **compare or match** their elements

**To be honest about this problem:** counting letters with a hash map is also a good
way to solve it, and it is faster, in `O(n)`. Many problems can be solved with more than
one pattern. You will see the hash map version later, and comparing the two will help
you choose between them.

## Before you code

Answer these on paper, using Example 3. Once sorted, the words are `aab` and `abb`. Tell
Claude your answers if you want to check them.

1. Both pointers are on `a`. The letters are equal. What should you do?
2. Now the pointers are on `a` (in `first`) and `b` (in `second`). Which letter can never
   find a match, and why?
3. In Example 4, the pointers reach the end of `ab` while `cd` is left in the other word.
   What must happen to those letters?

<details>
<summary>Hint: check your answer to question 2</summary>

The `a` can never find a match. The words are sorted, so every remaining letter in
`second` is `b` or later. This `a` must be deleted, and only its pointer moves forward.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.
