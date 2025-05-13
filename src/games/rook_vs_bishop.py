import random
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.color import Color


class RookVsBishopGame:
    def __init__(self):
        self.bishop = Bishop("c3", Color.WHITE)
        self.rook = Rook("h1", Color.BLACK)
        self.history = []

    def toss_coin(self) -> str:
        return random.choice(["H", "T"])  # H = up, T = right

    def roll_dice(self) -> int:
        return random.randint(1, 6) + random.randint(1, 6)

    def play_round(self, round_number):
        direction = self.toss_coin()
        steps = self.roll_dice()

        print(f"Round {round_number}:")
        print(f"  Coin toss: {direction} ({'up' if direction == 'H' else 'right'})")
        print(f"  Dice roll: {steps}")
        self.rook.move(direction, steps)
        rook_pos = self.rook.position
        print(f"  Rook moved to: {rook_pos}")

        self.history.append((direction, steps, rook_pos))

        if self.bishop.can_capture(self.rook):
            print("Bishop captures the rook! Bishop wins.")
            return "bishop"

        return None

    def play_game(self, rounds):
        print("Starting Rook vs Bishop Game!")
        print(f"Bishop at {self.bishop.position}, Rook at {self.rook.position}")
        print("-" * 40)

        for round_number in range(1, rounds + 1):
            result = self.play_round(round_number)
            print("-" * 40)
            if result == "bishop":
                return "bishop"

        print(f"Rook survived {rounds} rounds! Rook wins.")
        return "rook"
