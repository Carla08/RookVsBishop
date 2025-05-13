import pytest

from pieces.color import Color
from pieces.rook import Rook


def test_rook_repr():
    rook = Rook("d4", Color.BLACK)
    output = repr(rook)
    assert "Rook" in output
    assert "black" in output
    assert "d4" in output


@pytest.mark.parametrize("rook_pos,target_pos,target_color,expected", [
    ("h1", "h8", Color.BLACK, True),  # Same column, enemy
    ("h1", "a1", Color.BLACK, True),  # Same row, enemy
    ("h1", "e4", Color.BLACK, False),  # Not aligned
    ("h1", "h8", Color.WHITE, False),  # Same column, same color
    ("h1", "a1", Color.WHITE, False),  # Same row, same color
])
def test_rook_can_capture(rook_pos, target_pos, target_color, expected):
    rook = Rook(rook_pos, Color.WHITE)
    target = Rook(target_pos, target_color)  # doesn't matter what kind of piece
    assert rook.can_capture(target) is expected


@pytest.mark.parametrize("start_pos,direction,steps,expected_pos", [
    ("h1", "H", 2, "h3"),
    ("h1", "T", 2, "b1"),  # wraps: h(7)+2 → 9 → 1
    ("g7", "H", 2, "g1"),  # y=6+2 → 8 → 0
    ("g7", "T", 1, "h7"),
])
def test_rook_move(start_pos, direction, steps, expected_pos):
    rook = Rook(start_pos, Color.BLACK)
    rook.move(direction, steps)
    assert rook.position == expected_pos


def test_rook_move_invalid_direction():
    rook = Rook("a1", Color.BLACK)
    with pytest.raises(ValueError, match="Invalid direction"):
        rook.move("Z", 3)
