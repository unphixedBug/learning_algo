# Guess the Number

**Pattern:** Binary search | **Difficulty:** Easy (level -1, warm-up)

This is a warm-up for `find_in_sorted_list`. It uses the same idea, but with no list, no indexes,
and no "not found" case.

## Problem

I choose a secret number between `1` and `n` (both included). You must find it.

You can make a guess by calling `check(guess)`. It answers with one of three strings:

| `check(guess)` returns | Meaning |
|---|---|
| `"higher"` | The secret is **bigger** than your guess |
| `"lower"` | The secret is **smaller** than your guess |
| `"correct"` | You found it |

Return the secret number. You must use **as few guesses as possible**: for `n = 1000000`, you have
at most **20 guesses**.

## Function to write

```python
def guess_number(n: int, check) -> int:
```

`check` is a **function** that you receive as an argument. You do not write it: the tests give it
to you. You only call it, like `check(50)`. See "Useful Python syntax" below.

## Examples

### Example 1

```
n = 10, the secret is 7
```

One good way to play:

```
guess 5  -> "higher"   the secret is in 6..10
guess 8  -> "lower"    the secret is in 6..7
guess 6  -> "higher"   the secret is in 7..7
guess 7  -> "correct"
```

Output: `7`

### Example 2

```
n = 100, the secret is 1
```

```
guess 50 -> "lower"    the secret is in 1..49
guess 25 -> "lower"    the secret is in 1..24
guess 12 -> "lower"    the secret is in 1..11
guess 6  -> "lower"    the secret is in 1..5
guess 3  -> "lower"    the secret is in 1..2
guess 1  -> "correct"
```

Output: `1`

### Example 3: only one possible number

```
n = 1, the secret is 1
```

Output: `1`

## Constraints

- `1 <= n <= 1000000000`
- `1 <= secret <= n`, so the secret always exists
- Each guess must be a whole number (`int`) between `1` and `n`
- At most `n.bit_length()` guesses (`20` for `n = 1000000`, `30` for `n = 1000000000`)
- Standard library only

## Why binary search is useful for this problem

### The slow way

You could guess `1`, then `2`, then `3`... For `n = 1000000` and a secret of `999999`, that is
almost a million guesses. Each answer only removes **one** number.

### The smart way

Now guess the **middle** number. Whatever the answer is, **half of the numbers disappear**:

```
n = 16, the secret is 11

possible: 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
guess 8 -> "higher": 1 to 8 are all too small, forget them

possible:                         9  10 11 12 13 14 15 16
guess 12 -> "lower": 12 to 16 are all too big, forget them

possible:                         9  10 11
guess 10 -> "higher": 9 and 10 are too small, forget them

possible:                               11
guess 11 -> "correct"
```

Only 4 guesses instead of 11.

**The important idea:** one answer tells you about **many numbers at once**. If `8` is too small,
then `7`, `6`, `5`... are too small too. You do not need to try them. This works because the
numbers are **in order**. That is the same reason why binary search needs a **sorted** list.

### How many guesses?

Each guess cuts the possible numbers in half. So the question is: "how many times can I cut `n` in
half before only one number is left?"

| `n` | Slow way (worst case) | Binary search (worst case) |
|---|---|---|
| 16 | 16 guesses | 5 guesses |
| 1,000 | 1,000 guesses | 10 guesses |
| 1,000,000 | 1,000,000 guesses | 20 guesses |
| 1,000,000,000 | 1,000,000,000 guesses | 30 guesses |

This is what `O(log n)` means: when `n` becomes **twice** as big, you need only **one** more guess.

### Remembering what is still possible

You do not need a list of the possible numbers. They are always **one block, with no holes**, so
two numbers are enough to describe it:

- `low`: the smallest number that is still possible
- `high`: the biggest number that is still possible

At the start, everything is possible: `low = 1` and `high = n`.

After each answer, you move **one** of them:

```
low = 9, high = 16, you guess 12

"lower"  -> 12 is too big, and so is everything above it.
            The biggest possible number is now 11.        -> high becomes 11
"higher" -> 12 is too small, and so is everything below it.
            The smallest possible number is now 13.       -> low becomes 13
```

Notice that the new value is `guess - 1` or `guess + 1`, not `guess`: you already know that `guess`
is wrong, so it is not possible anymore.

### Finding the middle

The middle of `low` and `high` is their average, rounded down: `(low + high) // 2`.

```
low = 9, high = 16  -> (9 + 16) // 2  = 25 // 2 = 12
low = 9, high = 11  -> (9 + 11) // 2  = 20 // 2 = 10
low = 11, high = 11 -> (11 + 11) // 2 = 22 // 2 = 11
```

## Real use cases

- **"Higher or lower" games** and quiz shows, of course.
- **`git bisect`:** finds the commit that introduced a bug. It tests the middle commit, then keeps
  only the half that contains the bug. 1000 commits need about 10 tests.
- **Finding the right setting:** the smallest font size that still fits on one line, the highest
  video quality that does not lag. You try the middle value and keep the good half.
- **Looking up a word in a paper dictionary:** you open it near the middle, never at page 1.

## Useful Python syntax

```python
# Floor division: divides, then rounds down to a whole number
25 // 2              # 12
20 // 2              # 10
25 / 2               # 12.5 (a float: not allowed as a guess here)

# A function can be passed to another function, then called inside it
def say_hello(name):
    return "Hello " + name

def greet_twice(greeter):
    print(greeter("Ana"))   # calls the function received as argument
    print(greeter("Bob"))

greet_twice(say_hello)      # Hello Ana, then Hello Bob

# Store the answer in a variable, so you call check() only once per guess
answer = check(12)
if answer == "correct":
    ...
elif answer == "higher":
    ...
else:
    ...

# A while loop runs as long as its condition is True
low, high = 1, 3
while low <= high:
    low += 1           # runs 3 times: low becomes 2, 3, then 4

# return inside a loop stops the whole function immediately
def first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None
```

**A common trap:** calling `check()` several times for the same guess.

```python
if check(guess) == "correct":     # 1 guess
    ...
elif check(guess) == "higher":    # 1 more guess, for the same number!
    ...
```

This counts as 2 guesses, so you may run out of guesses. Call it once and keep the answer.

## Step by step

Do these in order. After each step, tell Claude your answer if you want to check it.

### Step 1: play by hand

Take `n = 20` and the secret `13`. Start with `low = 1` and `high = 20`. For each guess, write a
line like this:

```
low = 1, high = 20, guess = (1 + 20) // 2 = 10, answer = "higher"
```

Then update `low` or `high` and write the next line. Stop when the answer is `"correct"`. How many
guesses did you need?

### Step 2: the three cases

Using your notes from step 1, complete these sentences:

- If the answer is `"correct"`, I ...
- If the answer is `"higher"`, I change `low` to ...
- If the answer is `"lower"`, I change `high` to ...

### Step 3: when to stop

Your code will repeat "guess, read the answer, update" in a `while` loop.

- Play `n = 1`, secret `1`. At the start, `low = 1` and `high = 1`. Must the loop run at least once?
- So which condition is correct: `while low < high` or `while low <= high`?

### Step 4: a classic bug

Imagine that you write `low = guess` instead of `low = guess + 1`. Play it by hand with `n = 2` and
the secret `2`:

```
low = 1, high = 2, guess = ?, answer = ?
low = ?, high = ?, guess = ?, answer = ?
...
```

What happens? This is why the `+ 1` and `- 1` matter.

### Step 5: write the code

Open `solution.py`. The comments guide you through each part. Then run the tests:

```
pytest exercises/06.binary_search/guess_the_number
```

If a test says **"Too many guesses"**, look again at steps 3 and 4.

<details>
<summary>Hint 1: the structure of the function</summary>

1. Create `low` and `high`.
2. Loop while there are still possible numbers.
3. Inside the loop: compute the middle, call `check` once, then handle the three cases.

</details>

<details>
<summary>Hint 2: do I need a return after the loop?</summary>

The secret always exists, so the function always returns inside the loop. But Python does not know
that. It is still good practice to put something after the loop, for example
`raise ValueError("The secret was not found")`. If this line ever runs, your updates are wrong.

</details>

Stuck? Ask Claude for a code snippet of the part that blocks you.

## Next exercise

When this one passes, go back to `find_in_sorted_list`. It is the same game:

- the numbers `1..n` become the indexes `0..len(nums) - 1` of a list
- `check(guess)` becomes a comparison between `nums[middle]` and `target`
- the new part: the target may not exist, so the loop can end without finding anything
