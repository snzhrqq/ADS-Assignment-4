import random
from vertex import Vertex
from graph import Graph
from experiment import Experiment


def build_graph(num_vertices: int, num_edges: int, seed: int = 42) -> Graph:
    random.seed(seed)
    g = Graph()

    for i in range(num_vertices):
        g.add_vertex(Vertex(i))

    added = set()
    attempts = 0
    while len(added) < num_edges and attempts < num_edges * 10:
        attempts += 1
        src = random.randint(0, num_vertices - 1)
        dst = random.randint(0, num_vertices - 1)
        if src != dst and (src, dst) not in added:
            g.add_edge(src, dst)
            added.add((src, dst))

    return g


def main():
    print("=" * 60)
    print("  GRAPH TRAVERSAL SYSTEM — BFS & DFS")
    print("=" * 60)

    small = Graph()
    for i in range(10):
        small.add_vertex(Vertex(i))

    edges_small = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6), (3, 7), (4, 8),
        (5, 9), (6, 9),
    ]
    for src, dst in edges_small:
        small.add_edge(src, dst)

    medium = build_graph(num_vertices=30, num_edges=60, seed=7)
    large = build_graph(num_vertices=100, num_edges=300, seed=99)

    experiment = Experiment()
    graphs = {
        "Small  (10)": (small, 0),
        "Medium (30)": (medium, 0),
        "Large (100)": (large, 0),
    }

    experiment.run_multiple_tests(graphs)
    experiment.print_results()


if __name__ == "__main__":
    main()