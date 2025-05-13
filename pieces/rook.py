from pieces.color import Color
from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, position: str, color: Color):
        super().__init__(position, color)

    def can_capture(self, other_piece):
        pass
