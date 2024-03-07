from ShapeRules  import ShapeRules
from typing import list

class Shape:
    def __init__(self, cells:list, rules:ShapeRules):
        self.cells:list = cells
        self.rules:ShapeRules = rules
