from pieces.color import Color
from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, position: str, color: Color):
        super().__init__(position, color)

    def can_capture(self, other_piece):
        same_row = self.y == other_piece.y
        same_col = self.x == other_piece.x
        return (same_row or same_col) and self.color != other_piece.color
