import pytest
from pieces.rook import Rook
from pieces.color import Color


def test_rook_repr():
    rook = Rook("d4", Color.BLACK)
    output = repr(rook)
    assert "Rook" in output
    assert "black" in output
    assert "d4" in output


@pytest.mark.parametrize("rook_pos,target_pos,target_color,expected", [
    ("h1", "h8", Color.BLACK, True),   # Same column, enemy
    ("h1", "a1", Color.BLACK, True),   # Same row, enemy
    ("h1", "e4", Color.BLACK, False),  # Not aligned
    ("h1", "h8", Color.WHITE, False),  # Same column, same color
    ("h1", "a1", Color.WHITE, False),  # Same row, same color
])
def test_rook_can_capture(rook_pos, target_pos, target_color, expected):
    rook = Rook(rook_pos, Color.WHITE)
    target = Rook(target_pos, target_color)  # doesn't matter what kind of piece
    assert rook.can_capture(target) is expected