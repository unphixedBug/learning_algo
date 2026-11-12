# Folder Size: Summary

**Pattern:** Recursion

## Final solution

```python
def folder_size(folder: list) -> int:
    total = 0

    for item in folder:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += folder_size(item)

    return total
```

## How it works

The loop goes through the items of one folder. A file adds its size to the total. A
subfolder is a smaller folder, so the function asks itself for its size and adds the
answer.

With `[10, [20, 5], 2]`:

```
folder_size([10, [20, 5], 2])        total = 0
  item 10: file                      total = 10
  item [20, 5]: folder -> waits
      folder_size([20, 5])           total = 0   <- a DIFFERENT total
        item 20                      total = 20
        item 5                       total = 25
      returns 25
  total += 25                        total = 35  <- resumes where it stopped
  item 2: file                       total = 37
returns 37
```

## Why it works

- **Each call has its own `total`:** while the inner call runs, the `10` of the top call
  waits on the stack, and the inner call can't change it. This is also why calling the
  function twice gives the same result: nothing is kept between calls.
- **The base case is implicit:** a folder with no subfolder (or an empty folder) makes no
  recursive call, so the loop ends and returns. No need for `if not folder: return 0`.
- **Loop for width, recursion for depth:** a flat folder of 100,000 files makes a single
  call, because the loop handles it. There is one nested call per level only, so 200
  levels stay far below Python's limit of about 1000.
- **The recipe, applied:**
  - **Base case:** a folder without subfolders
  - **Smaller problem:** `item`, when it is a list
  - **Combine:** `total += folder_size(item)`

## Complexity

- **Time: `O(n)`:** each item (file or subfolder) is visited once.
- **Space: `O(d)`:** one call waits on the stack for each level, where `d` is the depth.

## Key lessons

**A recursive call returns a value: use it.** My last bug was `folder_size(item)` alone
on its line. The subfolder's size was computed, then thrown away, so only the top-level
files were counted. A call without `=`, `+=` or `return` in front of it is almost always
a bug when the function returns something.

**Recurse on the smaller part, not on the whole input.** My first attempt called the
function again on `arr` (the same folder) instead of `item` (the subfolder). The input
never shrinks, so the calls never stop: `RecursionError`.

**Don't `return` inside the loop when you need every item.** `return sum(arr)` on the
first file stopped the whole function, and `sum()` also fails on a list that contains
lists (`TypeError`). Build a running total, and return it after the loop.

**No helper function when the signature already fits.** `folder_size` takes a folder and
returns a size: that is exactly the question to ask about a subfolder. An inner helper is
only useful to carry extra state (an index, a shared accumulator, ...).

**Read the passing tests to find the bug.** The 8 passing tests had one thing in common:
no file inside a subfolder. That pointed straight to the discarded recursive result.

## Python syntax I learned

**`isinstance(x, list)`:** checks the type of a value. Prefer it to `type(x) == list`.

**A function call is an expression:** `folder_size(item)` *is* a number, like `item`, so
both branches can do the same thing:

```python
total += item               # file: its size is already there
total += folder_size(item)  # folder: ask the function for its size
```

## In an interview

- Say out loud: "a subfolder is also a folder, so I can call the same function on it".
- Name the base case, the smaller problem and the combine step before coding.
- Explain why the stack depth is the number of levels, not the number of items.
- Test `[]`, `[[]]`, a flat list and a file placed after a subfolder by hand.

## Level

I needed a snippet for the combine step (`total += folder_size(item)`). One more level 0
exercise, with a different combine (such as `max` for the depth of a folder), before
moving to level 1.
