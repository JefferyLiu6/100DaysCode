import random 
import art
import game_data

def get_item():
    item = random.choice(game_data.data)
    return item

def compare(A, B):
    print(f"Compare A: , a {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: , a {B['description']}, from {B['country']}.")
    print("Who has more followers? Type 'A' or 'B': ")

def check_ans(itemA, itemB, response):
    if itemA['follower_count'] > itemB['follower_count']:
        if response == 'A':
            return itemA, True
        else:
            return itemB,False
    if itemA['follower_count'] < itemB['follower_count']:
        if response == 'B':
            return itemB, True
        else:
            return itemA, False

def play(): 
    score = 0
    end = False
    A = get_item()
    while not end:
        print(art.logo)

        B = get_item()
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(art.vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        ans = input(f"Who has more followers? Type 'A' or 'B': ")
        item, check = check_ans(A, B, ans)
        if check == True:
            score += 1
            A = item           
            print(f"You're right! Current score: {score}.")
        else: 
            print(f"Sorry, that's wrong. Final socre: {score}")
            end = True

play()