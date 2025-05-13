# ♜ Rook vs Bishop

A simple chess simulation where a rook tries to survive 15 random moves while a stationary bishop waits to capture it. The game is run entirely in Python using object-oriented design and includes a CLI powered by Poetry.

---

## 🚀 Getting Started

### 1. Install [Poetry](https://python-poetry.org/docs/#installation)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

> 🔧 After installing, you may need to restart your terminal or add Poetry to your path:
>
> ```bash
> export PATH="$HOME/.local/bin:$PATH"
> ```

---

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/rookvsbishop.git
cd rookvsbishop
```

---

### 3. Install Dependencies

```bash
poetry install
```

---

## ▶️ Running the Game

Run the game with the default number of rounds (15):

```bash
poetry run rookvsbishop
```

Run with a custom number of rounds:

```bash
poetry run rookvsbishop --rounds 10
```

> ⚠️ If no `--rounds` is specified, the program will default to 15 and issue a warning.

---

## 🧪 Running Tests

To run all unit tests:

```bash
poetry run pytest
```

---

## 🗂 Project Structure

```
rookvsbishop/
├── board/        # Board representation
├── games/        # Game logic
├── moves/        # Coordinate conversion helpers
├── pieces/       # Chess pieces (Rook, Bishop, etc.)
├── main.py       # CLI entry point
└── test/         # Unit tests for all modules
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
