# Hashing (Hash map / Hash set): Summary

**Current level:** 0

## The pattern

Trade memory for speed: instead of searching through the data again and again, remember what
you've already read in a structure that answers "have I seen this key?" or "how many times?" in
`O(1)`.

| | Hash set (`set`) | Hash map (`dict`) |
|---|---|---|
| Answers | "Have I seen this?" | "Have I seen this, and what do I know about it?" |
| Example | duplicates, membership | counts, first index, a value tied to a key |

## When to use it

- You keep asking "**have I already seen this?**" or "**does this exist?**"
- You need to **count** things, or find **duplicates**
- A nested-loop / re-scanning solution works but is `O(n²)`
- The data is **not sorted**, and sorting wouldn't help (or would cost more than it saves)

## Don't confuse a hash map with...

- **A single-pass scan:** a scan only needs the last little bit of state (current run, best so
  far). A hash map remembers something about *every distinct key* seen, not just the most recent
  item.
- **A `deque`:** a `deque` is about **position** — fast insert/remove at the two ends of a
  sequence. A hash map/set is about **key lookup**, with no notion of "ends" at all. A problem
  about a sliding window's edges wants a `deque` (or just indexes); a problem about "has this
  been seen, how many times, since when" wants a `dict`/`set`.

## Traps

- **One pass isn't always enough.** If the answer for an item depends on information you only
  know *after* seeing the whole input (e.g. a character's final count), you need two passes: one
  to build the map, one to use it.
- **`enumerate()` on a `dict` numbers the dict's keys, not their position in the original
  data.** If you need the real index in the input, `enumerate` the input itself and use the dict
  only for `O(1)` lookups by key.
- **Hash set vs. hash map:** reach for `set` only when "have I seen this?" is the whole
  question. The moment you need to remember *something about* the key (a count, an index, a
  value), you need a `dict`.

## Exercises

| Exercise | Difficulty | What it teaches | Where I struggled |
|---|---|---|---|
| `first_unique_char` | Easy | Frequency counting with a `dict`/`Counter`, then a second pass over the original data | Looping over the dict instead of the original string, mixing up `dict` with `deque` |

(`two_sum_unsorted` — membership + "where did I see it" — is set up but not finished yet.)

## Next step

Stay at level 0 for now. Move to level 1 once an exercise needs little to no help choosing
between `set`/`dict` and structuring the passes.
