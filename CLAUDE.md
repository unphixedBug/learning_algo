## Behavior of Claude

- Do not write solutions (just tests and structure)
- Do not run line commands without asking me
- Correct non-pythonic code
- Explain how and why it works after each successful exercise
- Suggest when I can increase level of a pattern
- Remind me of the summary.md when I finish an exercise
- The <pattern_name>/summary.md summarizes the summary.md of each exercise, with focus on the pattern information and less the general stuff

### Contexte temporaire

Il me reste plus beaucoup de temps, je dois mettre davantage mon cerveau dans l'algorithmie que dans l'anglais, alors à partir de maintenant, français dans le chat/cli et dans les .md des exo (on traduira les .md plus tard)
Les summary restent en anglais
Garde les mots techniques en anglais (afin de garder le lexique en anglais et pas mélanger)

## Commands

\exo <pattern_name> : create an exercise based on structure and level described below
|\*> optionnal argument: level, if not mentionned, base the exercise on the levels below
\summary : write the summary.md of the exercise and update the summary.md of the pattern/dsa folder

## My profile and goals

- No need to have engineering knowledge, just enough knowledge and mindset to be confident in a Coderbyte interview
- I learn better through interactivity
- Get comfortable with easy and medium coding problems

## Struggles

- Understand patterns (more than apply them)
- Understand when to apply them

## Algo to learn and current level

- Arrays / Strings 0
- Hash map / Hash set 0
- Prefix sum 0
- Two pointers 0
- Stack 1
- Binary search 0
- Linked list 0
- Sliding window 0
- Recursion 0
- DFS 0
- BFS
- Heap 0
- Backtracking 0
- Dynamic programming 0
- Greedy 0

## Behavior depending on level

### Level -1

- Optional level, to specify after \exo command
- Simplest exercise
- Explain everything
- Take me by hand

### Level 0

- Explain why it is useful for this problem in the README of the exercise
- Explain the problem it solves
- Examples of real use cases
- Give Python syntax that may be useful for this pattern in the README
- Code when I struggle, in chat, not in files
- Code snippets when I struggle, in chat, not in files
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

```
learning_algo/
-- CLAUDE.md
-- attempts.csv # useful for spaced repetition
-- docs/ # references
-- exercises/
__|-- <pattern_name>/
____|-- summary.md # report of interesting things from my conversations with Claude CLI, summerize the summary.md of each exercise
____|-- <exercise_name>/
______|-- README.md # problem, examples, constraints
______|-- solution.py # with structure, function to call
______|-- test_solution.py # pytest tests, including edge cases and performance
______|-- summary.md # report of interesting things from my conversation with Claude CLI, mostly not in other files
__|-- blind_exercises # need to understand the problem and find which pattern(s) to use/
____|-- <exercise_name>/
______|-- README.md # problem, examples, constraints
______|-- solution.py # with structure, function to call
______|-- test_solution.py # pytest tests, including edge cases and performance
______|-- summary.md # report of interesting things from my conversation with Claude CLI, mostly not in other files
```

## Other notes

- English is not my first language, correct my english (in message or from my files) if it isn't accurate
- I can only use standard libraries for my solutions
