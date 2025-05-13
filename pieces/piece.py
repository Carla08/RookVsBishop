from pieces.color import Color


class Piece:
    def __init__(self, position: str, name: str, color: Color):
        self.position = position
        self.name = name
        self.color = color

    def __repr__(self):
        return f"{self.color.value} {self.__class__.__name__} is in {self.position}"

    def can_capture(self, other_piece):
        pass
