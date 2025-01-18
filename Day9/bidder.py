import art
print(art.logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if bidding_record[i] > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bits = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bits[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bits)
    elif should_continue == "yes":
        print("\n" * 20)
