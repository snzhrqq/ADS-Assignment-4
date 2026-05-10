from vertex import Vertex


class Edge:
    def __init__(self, source: Vertex, destination: Vertex):
        self.__source = source
        self.__destination = destination

    def get_source(self) -> Vertex:
        return self.__source

    def get_destination(self) -> Vertex:
        return self.__destination

    def __repr__(self) -> str:
        return f"Edge({self.__source} -> {self.__destination})"

    def __str__(self) -> str:
        return f"Edge({self.__source} -> {self.__destination})"

