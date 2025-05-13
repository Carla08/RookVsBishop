from typing import List

from pieces.piece import Piece


class Board:
    def __init__(self, pieces: List[Piece]):
        self.pieces = pieces  # A list of Piece instances

    def __repr__(self):
        print("Current board state:")
        for piece in self.pieces:
            print(f"\n  {piece}")
        print("-" * 30)  # end of the state
