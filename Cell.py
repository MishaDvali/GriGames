from typing import List
from Shape import Shape

class Cell:
    def __init__(self, val:int, possibleVals:set, inShapes:list, x:int, y:int):
        self.val:int = val
        self.possibleVals:set = possibleVals
        self.inShapes:List[Shape] = inShapes
        self.x:int = x
        self.y:int = y

    def Set(self, val) -> None:
        raise NotImplementedError() #todo

