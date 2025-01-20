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