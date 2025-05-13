# test/moves/test_chess_coordinates_converter.py

import pytest

from moves.chess_coordinates_converter import coords_to_notation
from moves.chess_coordinates_converter import notation_to_coords


@pytest.mark.parametrize("notation,expected_coords", [
    ("a1", (0, 0)),
    ("h1", (7, 0)),
    ("a8", (0, 7)),
    ("d5", (3, 4)),
    ("c3", (2, 2)),
])
def test_notation_to_coords(notation, expected_coords):
    assert notation_to_coords(notation) == expected_coords


@pytest.mark.parametrize("coords,expected_notation", [
    ((0, 0), "a1"),
    ((7, 0), "h1"),
    ((0, 7), "a8"),
    ((3, 4), "d5"),
    ((2, 2), "c3"),
])
def test_coords_to_notation(coords, expected_notation):
    assert coords_to_notation(*coords) == expected_notation


@pytest.mark.parametrize("invalid_notation", ["z1", "a9", "11", "", "k2"])
def test_notation_to_coords_invalid(invalid_notation):
    with pytest.raises(ValueError, match="Invalid position"):
        notation_to_coords(invalid_notation)


@pytest.mark.parametrize("invalid_coords", [(-1, 0), (8, 3), (2, -1), (4, 8)])
def test_coords_to_notation_invalid(invalid_coords):
    with pytest.raises(ValueError, match="Invalid coordinates"):
        coords_to_notation(*invalid_coords)
