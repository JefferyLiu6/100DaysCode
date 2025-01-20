# Blackjack Game

This is a Python implementation of the popular card game **Blackjack**. The program allows users to play a simplified version of the game against the computer.

---

## Features

- Simulates a game of Blackjack with basic rules.
- Handles scoring and game logic, including:
  - Blackjack detection.
  - Adjusting the value of the Ace (`11` to `1`) to prevent busting.
  - Dealer's rules to hit until the score reaches 17 or higher.
- Provides an interactive gameplay experience.

---

## Rules

1. The goal is to get as close to 21 as possible without going over.
2. Aces (`11`) can count as `1` if the total score exceeds `21`.
3. Player starts with two cards and can choose to "hit" (draw another card) or "stand" (end their turn).
4. Dealer draws until their total is `17` or higher.
5. Blackjack (an Ace and a card worth `10`) wins automatically unless both the player and dealer have it (resulting in a draw).

---

## Usage

1. Clone this repository or copy the script to your local environment.
2. Ensure you have Python 3.x installed.
3. Run the script:
   ```bash
   python blackjack.py
   ```
4. Follow the interactive prompts to play the game.

### Example Interaction

#### Input:
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y
Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
```

#### Output:
```
Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 10, 3], final score: 19
You lose 😤
```

---