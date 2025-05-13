from unittest.mock import patch

from games.rook_vs_bishop import RookVsBishopGame


@patch("games.rook_vs_bishop.random.choice", return_value="H")
@patch("games.rook_vs_bishop.random.randint", side_effect=[1, 1])
def test_play_round_rook_survives(mock_randint, mock_choice):
    game = RookVsBishopGame()
    result = game.play_round(1)

    # Rook moved H (up) 1+1 = 2 -> from h1 to h3
    assert game.rook.position == "h3"
    assert result is None
    assert len(game.history) == 1
    assert game.history[0] == ("H", 2, "h3")


@patch("games.rook_vs_bishop.random.choice", return_value="H")
@patch("games.rook_vs_bishop.random.randint", side_effect=[3, 4])
def test_bishop_captures_rook(mock_randint, mock_choice):
    game = RookVsBishopGame()

    # Move rook 6 steps to the right from h1 -> wrap to f1 (c3 to f1 = diagonal -> bishop captures)
    result = game.play_round(1)

    assert result == "bishop"
    assert game.history[0][2] == "h8"


@patch("games.rook_vs_bishop.random.choice", side_effect=["T"] * 3)
@patch("games.rook_vs_bishop.random.randint", side_effect=[1, 1] * 3)
def test_rook_survives_15_rounds(mock_randint, mock_choice):
    game = RookVsBishopGame()
    winner = game.play_game(rounds=3)

    assert winner == "rook"
    assert len(game.history) == 3
