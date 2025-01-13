# Rock-Paper-Scissors Game

A simple Python-based Rock-Paper-Scissors game where you can play against the computer.

## How to Play

1. The game starts by prompting you to choose one of the following options:
   - `0` for Rock
   - `1` for Paper
   - `2` for Scissors

2. After you make your choice, the computer randomly selects its move.

3. The winner is determined based on the classic Rock-Paper-Scissors rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

4. The game announces the result: whether you win, lose, or it's a draw.

---

## Features

- **Human vs Computer Gameplay:** The player inputs their choice, and the computer generates a random choice.
- **Randomized Moves:** The computer's move is chosen randomly, making the game unpredictable.
- **Immediate Feedback:** Displays the player's choice, the computer's choice, and the result of the match.

---

## Code Explanation

### ASCII Art

The game uses ASCII art to visually represent the player's and computer's choices:
- **Rock**
- **Paper**
- **Scissors**

### Core Logic

1. The player's choice is read using the `input()` function.
2. The computer's choice is generated using `random.randint(0, 2)`.
3. The game logic compares the player's choice and the computer's choice to determine the outcome:
   - If the player wins: "You win!"
   - If the computer wins: "You lose!"
   - If it's a tie: "It's a draw!"

### Validation

Handles invalid inputs by informing the player and ending the game.

---

## Running the Game

1. Copy the code into a Python file (e.g., `rock_paper_scissors.py`).
2. Run the file in your terminal:
   ```bash
   python rock_paper_scissors.py
