import pytest

from pieces.bishop import Bishop
from pieces.color import Color


def test_bishop_repr():
    bishop = Bishop("d4", Color.BLACK)
    output = repr(bishop)
    assert "Bishop" in output
    assert "black" in output
    assert "d4" in output


@pytest.mark.parametrize("bishop_pos,target_pos,target_color,expected", [
    ("c3", "f6", Color.BLACK, True),  # diagonal up right, opposite color
    ("c3", "a1", Color.BLACK, True),  # diagonal down left, opposite color
    ("c3", "e1", Color.BLACK, True),  # diagonal down right, opposite color
    ("c3", "a5", Color.BLACK, True),  # diagonal up left, opposite color
    ("c3", "c6", Color.BLACK, False),  # vertical
    ("c3", "f3", Color.BLACK, False),  # horizontal
    ("c3", "e4", Color.BLACK, False),  # irregular
    ("c3", "f6", Color.WHITE, False),  # diagonal up right, same color — should not capture
])
def test_bishop_can_capture(bishop_pos, target_pos, target_color, expected):
    bishop = Bishop(bishop_pos, Color.WHITE)
    target = Bishop(target_pos, target_color)
    assert bishop.can_capture(target) is expected
