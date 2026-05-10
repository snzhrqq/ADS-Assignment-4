from collections import deque
from vertex import Vertex
from edge import Edge


class Graph:
    def __init__(self):
        self.__vertices: dict[int, Vertex] = {}
        self.__adj_list: dict[int, list[Vertex]] = {}
        self.__edges: list[Edge] = []

    def add_vertex(self, v: Vertex) -> None:
        vid = v.get_id()
        if vid not in self.__vertices:
            self.__vertices[vid] = v
            self.__adj_list[vid] = []

    def add_edge(self, from_id: int, to_id: int) -> None:
        if from_id not in self.__vertices or to_id not in self.__vertices:
            raise ValueError(f"Both vertices must exist.")
        src = self.__vertices[from_id]
        dst = self.__vertices[to_id]
        self.__adj_list[from_id].append(dst)
        self.__edges.append(Edge(src, dst))

    def print_graph(self) -> None:
        print("Graph Adjacency List:")
        for vid in sorted(self.__adj_list):
            neighbors = ", ".join(str(n) for n in self.__adj_list[vid])
            print(f"  [{vid}] -> [{neighbors}]")

    def bfs(self, start: int) -> list[int]:
        if start not in self.__vertices:
            raise ValueError(f"Vertex {start} does not exist.")

        visited: set[int] = set()
        order: list[int] = []
        queue: deque[int] = deque()

        visited.add(start)
        queue.append(start)

        while queue:
            current_id = queue.popleft()
            order.append(current_id)

            for neighbor in self.__adj_list[current_id]:
                nid = neighbor.get_id()
                if nid not in visited:
                    visited.add(nid)
                    queue.append(nid)

        return order

    def dfs(self, start: int) -> list[int]:
        if start not in self.__vertices:
            raise ValueError(f"Vertex {start} does not exist.")

        visited: set[int] = set()
        order: list[int] = []
        stack: list[int] = []

        visited.add(start)
        stack.append(start)

        while stack:
            current_id = stack.pop()
            order.append(current_id)

            for neighbor in reversed(self.__adj_list[current_id]):
                nid = neighbor.get_id()
                if nid not in visited:
                    visited.add(nid)
                    stack.append(nid)

        return order

    def vertex_count(self) -> int:
        return len(self.__vertices)

    def edge_count(self) -> int:
        return len(self.__edges)