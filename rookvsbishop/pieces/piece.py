from rookvsbishop.pieces.color import Color
from rookvsbishop.moves.chess_coordinates_converter import notation_to_coords


class Piece:
    def __init__(self, position: str, color: Color):
        self.position = position
        self.color = color
        self.x, self.y = notation_to_coords(position)

    def __repr__(self):
        return f"{self.color.value} {self.__class__.__name__} is in {self.position}"

    def can_capture(self, other_piece):
        pass
