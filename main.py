import argparse
import warnings

from rookvsbishop.games.rook_vs_bishop import RookVsBishopGame


def main():
    parser = argparse.ArgumentParser(description="Play Rook vs Bishop")
    parser.add_argument(
        "--rounds",
        type=int,
        help="Number of rounds to play (default is 15)"
    )
    args = parser.parse_args()

    rounds = args.rounds
    if rounds is None:
        rounds = 15
        warnings.warn("No number of rounds provided. Defaulting to 15.")

    game = RookVsBishopGame()
    winner = game.play_game(rounds)
    print(f"\n🏁 Game Over! Winner: {winner.capitalize()}")


if __name__ == "__main__":
    main()
