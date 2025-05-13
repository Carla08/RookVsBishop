from board.board import Board
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.color import Color


def test_board_initialization():
    bishop = Bishop("c3", Color.WHITE)
    rook = Rook("h1", Color.BLACK)
    board = Board([bishop, rook])
    assert bishop in board.pieces
    assert rook in board.pieces


def test_board_repr():
    bishop = Bishop("c3", Color.WHITE)
    rook = Rook("h1", Color.BLACK)
    board = Board([bishop, rook])
    output = repr(board)

    assert "Bishop" in output
    assert "Rook" in output
    assert "c3" in output
    assert "h1" in output
    assert "Current board state:" in output
