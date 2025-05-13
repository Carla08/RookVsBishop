from typing import List

from rookvsbishop.pieces.piece import Piece


class Board:
    def __init__(self, pieces: List[Piece]):
        self.pieces = pieces  # A list of Piece instances

    def __repr__(self):
        state = "Current board state:\n"
        for piece in self.pieces:
            state += f"  {piece}\n"
        state += "-" * 30
        return state
