# Assignment 4: Graph Traversal and Representation System

## A. Project Overview

This project implements a graph traversal system in Python. A **graph** is a data structure consisting of **vertices** (nodes) and **edges** (connections between nodes). Graphs are used to model networks, maps, dependencies, and many other real-world systems.

- A **vertex** represents a single entity in the graph, identified by a unique integer ID.
- An **edge** represents a directed connection from one vertex to another.
- This project uses a **directed graph**, meaning edges have a direction (from source to destination).

Two fundamental graph traversal algorithms are implemented:

- **BFS (Breadth-First Search)** — explores the graph level by level, visiting all neighbors of a node before going deeper.
- **DFS (Depth-First Search)** — explores the graph by going as deep as possible along each branch before backtracking.

---

## B. Class Descriptions

### `Vertex` — `vertex.py`

Represents a single node in the graph.

- **Private field:** `__id` — unique integer identifier for the vertex.
- **Methods:** constructor, `get_id()` getter, `__str__()` and `__repr__()` for readable output.

### `Edge` — `edge.py`

Represents a directed connection between two vertices.

- **Private fields:** `__source` (starting Vertex), `__destination` (ending Vertex).
- **Methods:** constructor, `get_source()`, `get_destination()`, `__str__()` and `__repr__()`.

### `Graph` — `graph.py`

Represents the graph structure using an **adjacency list**.

- **Private fields:**
  - `__vertices` — dictionary mapping vertex ID to Vertex object.
  - `__adj_list` — dictionary mapping vertex ID to a list of neighboring Vertex objects.
  - `__edges` — list of all Edge objects in the graph.
- **Methods:** `add_vertex()`, `add_edge()`, `print_graph()`, `bfs()`, `dfs()`, `vertex_count()`, `edge_count()`.

#### Adjacency List Representation

An adjacency list stores each vertex alongside a list of its direct neighbors. For example:

```
[0] -> [1, 2]
[1] -> [3, 4]
[2] -> [5, 6]
```

This means vertex 0 has edges to vertices 1 and 2, vertex 1 has edges to 3 and 4, and so on. Compared to an adjacency matrix, this representation is more memory-efficient for sparse graphs.

### `Experiment` — `experiment.py`

Handles performance testing and result reporting.

- **Methods:** `run_traversals()`, `run_multiple_tests()`, `print_results()`.
- Uses `time.perf_counter_ns()` to measure execution time in nanoseconds.

### `Main` — `main.py`

Entry point of the program. Creates three graphs (small, medium, large), populates them with vertices and edges, and runs the full experiment pipeline.

---

## C. Algorithm Descriptions

### BFS — Breadth-First Search

**Step-by-step:**
1. Mark the start vertex as visited and add it to a queue.
2. While the queue is not empty:
   - Dequeue the front vertex and record it in the traversal order.
   - For each unvisited neighbor, mark it as visited and enqueue it.

**Use cases:**
- Finding the shortest path in an unweighted graph.
- Level-order traversal of a tree.
- Checking if a graph is connected.

**Time complexity:** O(V + E), where V is the number of vertices and E is the number of edges.

---

### DFS — Depth-First Search

**Step-by-step:**
1. Mark the start vertex as visited and push it onto a stack.
2. While the stack is not empty:
   - Pop the top vertex and record it in the traversal order.
   - For each unvisited neighbor, mark it as visited and push it onto the stack.

**Use cases:**
- Cycle detection in a graph.
- Topological sorting.
- Solving maze/path problems.

**Time complexity:** O(V + E), where V is the number of vertices and E is the number of edges.

---

## D. Experimental Results

Graphs of three sizes were created with random directed edges and traversed from vertex 0. Execution time was measured using `time.perf_counter_ns()`.

### Execution Time Comparison Table

| Graph         | Vertices | Edges | BFS (ns) | DFS (ns) | Faster |
|---------------|----------|-------|----------|----------|--------|
| Small  (10)   | 10       | 10    | 34,409   | 8,447    | DFS    |
| Medium (30)   | 30       | 60    | 3,825    | 2,086    | DFS    |
| Large  (100)  | 100      | 300   | 35,561   | 34,897   | DFS    |

### Observations

- DFS was faster than BFS in all three test cases.
- Both algorithms share the same theoretical complexity O(V + E), but DFS has lower constant overhead in practice because it uses a simple list as a stack, while BFS uses a `deque`.
- Execution times at this scale are very small (nanoseconds to microseconds), so results can vary slightly between runs due to CPU scheduling and Python interpreter overhead.
- As graph size grows from 10 to 100 vertices, execution time increases, which is consistent with O(V + E) behavior.

---

## E. Screenshots

### Graph Structure Output (Small Graph — 10 vertices)

```
Graph Adjacency List:
  [0] -> [1, 2]
  [1] -> [3, 4]
  [2] -> [5, 6]
  [3] -> [7]
  [4] -> [8]
  [5] -> [9]
  [6] -> [9]
  [7] -> []
  [8] -> []
  [9] -> []
```

### BFS Traversal Output (Small Graph)

```
BFS order : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

BFS visits vertex 0 first, then all its neighbors (1, 2), then their neighbors (3, 4, 5, 6), and so on — level by level.

### DFS Traversal Output (Small Graph)

```
DFS order : [0, 1, 3, 7, 4, 8, 2, 5, 9, 6]
```

DFS visits vertex 0, immediately goes deep into branch 1 → 3 → 7, then backtracks to explore 4 → 8, then moves to branch 2 → 5 → 9, then finishes with 6.

### Performance Results

```
============================================================
  RESULTS SUMMARY TABLE
============================================================
Graph        Vertices    Edges       BFS (ns)       DFS (ns) Faster
------------------------------------------------------------
Small  (10)        10       10         34,409          8,447 DFS
Medium (30)        30       60          3,825          2,086 DFS
Large (100)       100      300         35,561         34,897 DFS
============================================================
```

---

## F. Reflection

Working on this assignment gave me a clear understanding of how graphs are structured and how traversal algorithms explore them differently. Implementing both BFS and DFS from scratch made it easy to see the core difference: BFS uses a queue and explores neighbors layer by layer, while DFS uses a stack and goes as deep as possible before backtracking. The adjacency list representation was straightforward to implement in Python using dictionaries and felt natural compared to a 2D matrix, especially for sparse graphs where most vertices are not directly connected.

The main challenge was understanding why BFS and DFS produce different traversal orders even when starting from the same vertex. For the small graph, BFS produced `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` — a clean level-by-level sequence — while DFS produced `[0, 1, 3, 7, 4, 8, 2, 5, 9, 6]`, diving deep into one branch before exploring others. This made the behavioral difference very concrete. I also learned that although both algorithms have the same O(V + E) time complexity, DFS tends to be slightly faster in practice due to lower overhead from using a plain stack. The experiment confirmed this across all three graph sizes.

---

## Repository Structure

```
assignment4-graphs/
├── src/
│   ├── vertex.py
│   ├── edge.py
│   ├── graph.py
│   ├── experiment.py
│   └── main.py
├── docs/
│   └── screenshots/
├── README.md
└── .gitignore
```

## How to Run

```bash
cd src
python main.py
```

Python 3.10 or higher is required.