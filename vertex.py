class Vertex:
    def __init__(self, id: int):
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def __repr__(self) -> str:
        return f"Vertex({self.__id})"

    def __str__(self) -> str:
        return str(self.__id)