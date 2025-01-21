import art
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def choose_difficulty():
    diff = input(f"Choose a difficulty. Type 'hard' or 'easy': ")
    if diff == 'hard':
        return HARD_LEVEL_TURNS
    elif diff == 'easy':
        return EASY_LEVEL_TURNS

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.")
    ans = randint(1,100)
    #print(f"Pssst, the correct answer is {ans}")

    turns = choose_difficulty()

    guess = 0
    while guess != ans:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, ans, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != ans:
            print("Guess again.")
game()