from rookvsbishop.pieces.color import Color
from rookvsbishop.pieces.piece import Piece
from rookvsbishop.moves.chess_coordinates_converter import coords_to_notation


class Rook(Piece):
    def __init__(self, position: str, color: Color):
        super().__init__(position, color)

    def can_capture(self, other_piece):
        same_row = self.y == other_piece.y
        same_col = self.x == other_piece.x
        return (same_row or same_col) and self.color != other_piece.color

    def move(self, direction, steps):
        """
        Move the rook either up ('H') or right ('T') by a number of steps,
        wrapping around the board if needed.
        """
        if direction == "H":  # up
            self.y = (self.y + steps) % 8
        elif direction == "T":  # right
            self.x = (self.x + steps) % 8
        else:
            raise ValueError(f"Invalid direction: {direction}")

        # update position
        self.position = coords_to_notation(self.x, self.y)

