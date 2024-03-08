from ShapeRules  import ShapeRules
from Cell import Cell
from typing import List

class Shape:
    def __init__(self, cells:List[Cell], rules:ShapeRules):
        self.cells:List[Cell] = cells
        self.rules:ShapeRules = rules
