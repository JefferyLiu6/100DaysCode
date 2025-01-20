import art
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10]
    choose = random.choice(cards)
    return choose

def calculate_score(cards):
    score = 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    for i in cards:
        score += i

    if score == 21 and len(cards) == 2:
        return 0

    else:
        return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    u_card = []
    c_card = []
    u_score = -1
    c_score = -1
    end = False

    for i in range(2):
        u_card.append(deal_card())
        c_card.append(deal_card())

    while not end:
        u_score = calculate_score(u_card)
        c_score = calculate_score(c_card)
        print(f"Your cards: {u_card}, current score: {u_score}")
        print(f"Computer's first card: {c_card[0]}")

        if u_score == 0 or c_score == 0 or u_score > 21:
            end = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                u_card.append(deal_card())
            else:
                end = True

        while c_score != 0 and c_score < 17:
            c_card.append(deal_card())
            c_score = calculate_score(c_card)

        print(f"Your final hand: {u_card}, final score: {u_score}")
        print(f"Computer's final hand: {c_card}, final score: {c_score}")
        print(compare(u_score, c_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()