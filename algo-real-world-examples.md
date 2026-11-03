# Real-world examples for algorithm exercises

A reference file of concrete use cases, one section per algorithm. The examples come from my own project ideas. I am **not** going to build these projects now: they only exist to make each algorithm feel concrete.

## How Claude should use this file

- Before and/or after an exercise on an algorithm, give **one short example** (2 to 3 sentences) from the matching section: where the problem shows up in a real product, and how the algorithm solves it.
- Pick the example closest to the exercise variant (the "Maps to" line helps), and vary examples between exercises instead of repeating the same one.
- Frame it as "this is where this pattern shows up", not as a project for me to build.
- If no example fits the exercise naturally, say nothing or give a generic one. Do not force a connection.
- Mention an off-list algorithm (see the last section) only when the exercise is adjacent to it.

---

## Arrays, hashing, strings, sets

- **Recipe site (filters)**: build an inverted index `tag -> recipes` and intersect sets to answer "oven + soup + few dishes". *Maps to*: set intersection, hashmap lookups.
- **Spotify alarm**: keep a set of tracks already played recently so the same song never wakes me up twice. *Maps to*: Contains Duplicate, membership checks.
- **Exploration app**: store visited grid cells `(x, y)` in a set to know instantly whether a cell is already revealed. *Maps to*: visited sets.
- **Favorite genres picker**: count the genres of every album I rated highly with a hashmap, then take the most frequent. *Maps to*: Top K Frequent Elements, frequency counting.
- **Personal streaming playlists**: build a normalized key from genre + descriptor (e.g. "coldwave influenced alternative r&b") and group tracks under it. *Maps to*: Group Anagrams, grouping by key.
- **Social network with feeds**: decide who sees a post by combining sets (feed, mood, circle). *Maps to*: set operations.

## Prefix sum

- **Calorie counter**: from a log of meals, get the total calories between two timestamps in O(1) after one pass. *Maps to*: Range Sum Query.
- **TBoI item guessing game**: "average items found over my last N games" computed from cumulative totals instead of re-summing every time. *Maps to*: running totals, subarray sums.

## Two pointers

- **Fair matchmaking in a Pokémon-like game**: players sorted by average team level, two pointers pair players whose levels differ by at most N. *Maps to*: pairs in a sorted array with a difference condition.
- **Social feed**: merge two feeds that are each sorted by date into one timeline. *Maps to*: Merge Two Sorted Lists / Arrays.

## Stacks

- **Calculator**: check that parentheses are balanced and evaluate an expression with operator priority. *Maps to*: Valid Parentheses, Evaluate Reverse Polish Notation, Basic Calculator.
- **Threaded blog comments**: render a deeply nested thread iteratively with an explicit stack instead of recursion. *Maps to*: iterative DFS.

## Binary search

- **Daily movie suggestion**: my watch log is sorted by date, so finding the first film I saw more than 3 years ago takes O(log n). *Maps to*: lower/upper bound on a sorted array.
- **Live search**: in a sorted list of titles, find where the range of titles starting with the typed prefix begins. *Maps to*: Search Insert Position.
- **Evolution thresholds in a Pokémon-like game**: stages change at sorted level thresholds (stage 2 between level 14 and 18), so a creature's stage comes from binary search on its level. *Maps to*: finding a position among sorted boundaries.

## Linked list

- **LRU cache for a REST API**: a hashmap plus a doubly linked list gives O(1) lookup and O(1) move-to-front, evicting the least recently used entry. *Maps to*: LRU Cache, doubly linked list operations.

## Sliding window

- **Spotify alarm**: "never the same track within 30 days" means keeping a window over the last 30 days of plays. *Maps to*: fixed-size window with expiry.
- **Calorie counter**: the total always covers the last 24 hours, so meals older than 24 h leave the window and are subtracted. *Maps to*: window that expires items from the left.
- **API rate limiter** (e.g. for GitHub API calls): allow at most N requests per time window by dropping timestamps that fell out of it. *Maps to*: window over timestamps.
- **Connect Four**: detect four aligned tokens by sliding a window of length 4 across rows, columns and diagonals. *Maps to*: fixed-size window scan.

## Trees

- **Animal encyclopedia (taxonomy)**: kingdom, phylum, class, order, species form a tree. The "common taxon of two species" is their lowest common ancestor. *Maps to*: Lowest Common Ancestor, tree depth.
- **Decision tree for choosing technologies**: each answer to a question leads to a child node until a recommendation is reached. *Maps to*: binary/n-ary tree navigation.
- **Tournament bracket in a "favorite picker"**: each match is a node whose value is the winner of its two children. *Maps to*: building a binary tree bottom-up.
- **Threaded blog comments**: a comment with replies is a node with children. *Maps to*: n-ary trees, max depth.
- **Skill tree in a Pokémon-like game**: a kick move unlocks a burning-foot move, which can unlock other moves. *Maps to*: rooted trees.

## Tree traversals

- **Encyclopedia breadcrumb**: walk from a species up through its parents to build the path "Animalia > Chordata > ...". *Maps to*: root-to-node path.
- **Search results grouped by branch**: a DFS lists every species under an order or class. *Maps to*: preorder / DFS traversal.
- **Threaded comments**: preorder renders the thread in reading order, level order loads top-level comments first and deeper replies on demand. *Maps to*: preorder vs level-order traversal.
- **Decision-tree questionnaire**: follow the path of answers from the root. *Maps to*: root-to-leaf traversal.

## BFS & DFS

- **Genres map**: BFS finds the fewest hops between two genres when every link counts the same. *Maps to*: shortest path in an unweighted graph.
- **Exploration app**: count how many separate revealed zones exist and measure each one by flood fill. *Maps to*: Number of Islands, Max Area of Island, flood fill.
- **Procedurally generated region**: BFS or DFS from the starting town checks that every town can be reached. *Maps to*: connectivity, Number of Connected Components.
- **Task list with dependencies**: DFS detects a cycle ("A needs B, B needs A"). *Maps to*: Course Schedule (cycle detection).
- **Skill tree**: BFS lists every move reachable from the ones already learned. *Maps to*: reachability, level-order exploration.

## Heap / priority queue

- **Spaced-repetition reminders**: a min-heap keyed on due date always returns the next item to review. *Maps to*: priority queue by timestamp.
- **Turn order with a speed bar in a Pokémon-like game**: the next creature to act is the one whose action time is the smallest. *Maps to*: scheduling with a min-heap.
- **Requests for "which samples are in this track"**: tracks requested most often rise to the top of the waiting list of their genre. *Maps to*: Top K Frequent Elements.
- **Merged social feed**: take the newest post across several already sorted feeds. *Maps to*: Merge K Sorted Lists.
- **Open-source project finder**: keep the N best-scoring projects while scanning thousands. *Maps to*: Kth Largest Element, top-k with a bounded heap.
- **Course recommendation site (level votes)**: keep a running median of level votes with two heaps, more robust than an average. *Maps to*: Find Median from Data Stream.
- **Task manager with notifications**: the next notification to fire is the earliest due one. *Maps to*: event scheduling.
- **Genre pathfinding with weights**: Dijkstra picks the cheapest unexplored genre next using a min-heap. *Maps to*: Dijkstra's priority queue.

## Backtracking (and recursion)

- **Tic-tac-toe / Connect Four AI**: try a move, explore the consequences recursively, undo, try the next one. *Maps to*: recursive search with undo, N-Queens style problems.
- **Procedural region generation**: place towns and routes under constraints (no isolated town, minimum distance) and undo a placement when it leads to a dead end. *Maps to*: constraint satisfaction, Sudoku-style placement.
- **Enemy AI in a Pokémon-like game**: explore sequences of moves a few turns ahead and discard the bad branches. *Maps to*: game-tree search.

## Tries

- **Live search / autocomplete**: typing "inc" instantly lists every title starting with it. *Maps to*: Implement Trie, Design Search Autocomplete System.
- **Food database in a calorie counter**: autocomplete over thousands of foods while typing. *Maps to*: prefix search.
- **Item guessing game (The Binding of Isaac)**: validate and autocomplete item names as the player types. *Maps to*: prefix lookup, word validation.
- **Tag autocomplete in a learning plugin**: suggest existing tags (learning, work, culture...) as you type. *Maps to*: prefix search over a small vocabulary.
- **Geohash-like prefixes in an exploration app**: cells sharing a longer prefix are closer together, so grouping by prefix groups nearby cells. *Maps to*: prefix trees over strings.

## Graphs

- **Genres map**: genres are nodes, links are "influenced by" or "close to", weights are how hard a genre is to get into. *Maps to*: shortest path, weighted graphs.
- **Social network with circles**: followers and contacts form a graph, and circles are subsets of neighbors. *Maps to*: adjacency lists, neighbors.
- **Exploration app and region generation**: grid cells or towns as nodes, adjacency as edges. *Maps to*: Number of Islands, connected components.
- **Task dependencies**: tasks as nodes, "depends on" as directed edges. *Maps to*: Course Schedule, directed graphs.

## Dynamic programming

- **Calorie counter suggestions**: choose foods to reach a protein target without exceeding a calorie limit, where each food can be used once. *Maps to*: 0/1 Knapsack.
- **Move limits in a Pokémon-like game**: pick the best set of moves for a team when official fights cap total cost or capacity. *Maps to*: Knapsack, bounded optimization.
- Only these two natural cases exist in my ideas, so for other DP exercises (stairs, house robber, coin change...) skip the example unless it genuinely fits.

## Greedy

- **Festival poster generator**: place artists from most to least popular, with decreasing sizes, filling each row as it comes. *Maps to*: sorting then making the locally best choice.
- **Enemy AI in a Pokémon-like game**: each turn pick the move with the highest expected damage, with no lookahead. *Maps to*: locally optimal choice per step.
- **"Which technologies?" recommender**: score every technology against the answers and propose the best matches. *Maps to*: greedy selection by score.
- **Genre pathfinding with A\***: always expand the node that looks closest to the target according to a heuristic. *Maps to*: best-first search.

---

## Off-list algorithms worth a mention when adjacent

| Algorithm | Where it shows up |
|---|---|
| Dijkstra, A\* | Genres map: cheapest path between genres |
| Topological sort | Skill-tree unlocks, task dependencies, order of gyms in a game |
| Union-Find | Merging explored zones in the exploration app |
| Spaced repetition (SM-2, by Piotr Wozniak) | Review scheduling in the learning plugin |
| Minimax | Enemy AI, Connect Four AI |
| Minimum spanning tree, Wave Function Collapse | Procedural region generation |
| Exponential backoff | API calls when the rate limit is hit |
| Elo | Ranking items in a favorite picker |

---

## Project one-liners (for reference)

- **Genres map ("Genres-gps")**: find a path from a genre I know to a genre I want to reach but that feels too inaccessible.
- **Social network with feeds**: one account with several feeds (personal, pro, humor), moods, and circles of contacts.
- **Exploration app**: a map that is blurred until you walk through an area, with pins for places to remember.
- **Calorie counter**: nutrients and calories over a rolling 24 hours.
- **Learning plugin and flashcards**: save links or notes, review them with spaced repetition.
- **Daily movie suggestion**: films I loved long ago or disliked long ago, from a CSV of my ratings.
- **Spotify alarm**: wake up to a suitable track from the current top 100, never repeating within a month.
- **Open-source project finder**: filter GitHub and GitLab projects to find ones to contribute to.
- **Tech chooser**: a questionnaire that recommends technologies.
- **Samples and instruments requests**: ask and answer which sounds are used in a track.
- **Course recommendation site**: community-rated online courses with voted levels.
- **Animal encyclopedia**: a Pokédex-style encyclopedia organized by taxonomy.
- **Favorite picker**: an elimination tournament to find a favorite among many items.
- **Festival poster generator**: a lineup poster whose layout follows artist popularity.
- **Recipe site**: my own recipes with tags, difficulty, price and dishes.
- **TBoI guessing game**: name as many items from The Binding of Isaac as possible.
- **Pokémon-like game**: a creature-battle game with speed bar, skill tree, generated region and fair matchmaking.
- **Portfolio ideas**: calculator, live search, task manager, Connect Four, REST API, blog with comments, to-do with dependencies.
