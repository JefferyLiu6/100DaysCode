# Number Guessing Game

This is a Python implementation of a **Number Guessing Game**, where the user attempts to guess a randomly chosen number between 1 and 100 within a limited number of attempts.

---

## Features

- Choose between two difficulty levels:
  - **Easy**: 10 attempts.
  - **Hard**: 5 attempts.
- Provides feedback after each guess:
  - "Too high" if the guess is greater than the answer.
  - "Too low" if the guess is less than the answer.
- Informs the user if they run out of attempts.

---

## Usage

1. Clone this repository or copy the script to your local environment.
2. Ensure you have Python 3.x installed.
3. Run the script:
   ```bash
   python number_guessing_game.py
   ```
4. Follow the interactive prompts to play the game.

### Example Interaction

#### Input:
```
Choose a difficulty. Type 'hard' or 'easy': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
```

#### Output:
```
Too low.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 75
```
