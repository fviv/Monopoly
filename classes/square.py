from abc import ABC

class Square(ABC):
    def __init__(self,position, name, color):
        self.position = position
        self.name = name
        self.color = color


