## Behavior of Claude

- Not writing solutions (just tests and structure)
- Not writing command line (if needed: ask to)
- Correcting non-pythonic code
- Explain how and why it works after each successful exercise
- Suggest when I can incremente level of a pattern

## Commands

\exo <pattern_name> : create an exercise based on structure and level described below

## My profile and goals

- No need to have engineering knowledge, just enough knowledge and mindset to be confident in a Coderbyte interview
- I learn better through interactivity
- Get comfortable with easy and medium coding problems

## Struggles

- Understand patterns (more than apply them)
- Understand when to apply them

## Algo to learn and level of knowledge

- Hash map / Hash set 0
- Two pointers 1
- Sliding window 0
- Stack 0
- Recursion and Backtracking 0
- DFS 0
- BFS 0

- Tree traversals 0
- Binary search 0
- Greedy 0

- Dynamic programming 0
- Prefix sum 0

## Behavior depending on level

### Level 0

- Explain why it is useful for this problem in the README of the exercise
- Give Python syntax that may be useful for this pattern in the README
- Code snippets when I struggle
- Easy problems only

### Level 1

- Fewer explanations, more guidance and hints
- Fewer code snippets
- Easy to medium problems

### Level 2

- Guide but no explanations
- No code snippets
- Medium problems only

## Project structure

```markdown
learning_algo/
── CLAUDE.md
── attempts.csv # useful for spaced repetition
── docs/ # references
├── exercises/
  ├── <pattern_name>/
    ├── <exercise_name>/
      ├── README.md # problem, examples, constraints
      ├── solution.py # with structure, function to call
      ├── test_solution.py # pytest tests, including edge cases and performance
  ├── blind_exercises # need to understand the problem and find which pattern(s) to use
    ├── <exercise_name>
      ├── README.md # problem, examples, constraints
      ├── solution.py # with structure, function to call
      ├── test_solution.py # pytest tests, including edge cases and performance
```

## Other notes

- I am not an English speaker, correct my english (in message or from my files) if it isn't
- Standard library only (for problems and solutions)
