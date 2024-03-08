from typing import List

from . import *
class Grid:
    def __init__(self, unsolved:List[List[Cell]], shapes:List[Shape]):
        self.initialBoard:List[List[Cell]] = unsolved
        self.board:List[List[Cell]] = unsolved #todo to copy an array, not the link
        self.shapes:List[Shape] = shapes

    def solve(self) -> Grid:
         raise NotImplementedError() #todo

    def reset(self) -> None:
        raise NotImplementedError() #todo

    def insert(self, val:int, x:int, y:int) -> None:
        self.board[x][y].Set(val)

    def isValid(self) -> bool:
        for shape in self.shapes:
            if not shape.rules.isValid(shape):
                return False
        return True
