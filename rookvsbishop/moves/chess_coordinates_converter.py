from typing import Tuple

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8']

file_to_x = {file: i for i, file in enumerate(FILES)}
rank_to_y = {rank: i for i, rank in enumerate(RANKS)}

x_to_file = {i: file for i, file in enumerate(FILES)}
y_to_rank = {i: rank for i, rank in enumerate(RANKS)}


def notation_to_coords(pos: str) -> Tuple[int, int]:
    """
    Converts chess notation (e.g., 'a1') to (x, y).
    """
    if len(pos) != 2:
        raise ValueError(f"Invalid position: {pos}")

    file = pos[0].lower()
    rank = pos[1]

    if file not in file_to_x or rank not in rank_to_y:
        raise ValueError(f"Invalid position: {pos}")

    return file_to_x[file], rank_to_y[rank]


def coords_to_notation(x: int, y: int) -> str:
    """
    Converts (x, y) to chess notation (e.g., 'a1').
    """
    if x not in x_to_file or y not in y_to_rank:
        raise ValueError(f"Invalid coordinates: ({x}, {y})")

    return x_to_file[x] + y_to_rank[y]
