import time
from graph import Graph


class Experiment:
    def __init__(self):
        self.__results: list[dict] = []

    def run_traversals(self, g: Graph, start: int = 0, verbose: bool = False):
        bfs_start = time.perf_counter_ns()
        bfs_order = g.bfs(start)
        bfs_end = time.perf_counter_ns()
        bfs_time = bfs_end - bfs_start

        dfs_start = time.perf_counter_ns()
        dfs_order = g.dfs(start)
        dfs_end = time.perf_counter_ns()
        dfs_time = dfs_end - dfs_start

        if verbose:
            print(f"  BFS order : {bfs_order}")
            print(f"  DFS order : {dfs_order}")

        return bfs_time, dfs_time, bfs_order, dfs_order

    def run_multiple_tests(self, graphs: dict):
        print("=" * 60)
        print("  PERFORMANCE EXPERIMENT")
        print("=" * 60)

        for label, (g, start) in graphs.items():
            print(f"\n[{label}] — Vertices: {g.vertex_count()}, Edges: {g.edge_count()}")

            verbose = g.vertex_count() <= 10

            if verbose:
                print("  Graph structure:")
                g.print_graph()
                print()

            bfs_time, dfs_time, _, _ = self.run_traversals(g, start=start, verbose=verbose)

            self.__results.append({
                "label": label,
                "vertices": g.vertex_count(),
                "edges": g.edge_count(),
                "bfs_ns": bfs_time,
                "dfs_ns": dfs_time,
            })

            print(f"  BFS time  : {bfs_time:>12,} ns  ({bfs_time / 1_000:.2f} µs)")
            print(f"  DFS time  : {dfs_time:>12,} ns  ({dfs_time / 1_000:.2f} µs)")

    def print_results(self):
        print("\n" + "=" * 60)
        print("  RESULTS SUMMARY TABLE")
        print("=" * 60)
        header = f"{'Graph':<12} {'Vertices':>8} {'Edges':>8} {'BFS (ns)':>14} {'DFS (ns)':>14} {'Faster'}"
        print(header)
        print("-" * 60)

        for r in self.__results:
            faster = "BFS" if r["bfs_ns"] <= r["dfs_ns"] else "DFS"
            row = (
                f"{r['label']:<12} "
                f"{r['vertices']:>8} "
                f"{r['edges']:>8} "
                f"{r['bfs_ns']:>14,} "
                f"{r['dfs_ns']:>14,} "
                f"{faster}"
            )
            print(row)

        print("=" * 60)