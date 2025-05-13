from pieces.color import Color
from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, position: str, color: Color):
        super().__init__(position, color)

    def can_capture(self, other_piece):
        """
        Bishop doesn't care about distance as long as in diagonal.
        To be in diagonal that means the distance is equal from x and y. This mean the delta from that piece
        to bishop x and y is equal.
        The best way to understand this is to think of a square and the diagonal is what is between the bishop
        and that other piece
        :param other_piece:
        :return: bool
        """

        dx = abs(self.x - other_piece.x)
        dy = abs(self.y - other_piece.y)
        return dx == dy and self.color != other_piece.color
