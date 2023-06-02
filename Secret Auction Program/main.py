# from replit import clear
print("Welcome to the secret auction program.")
bidding_finished = False
bids = {}


def find_highest_bidder(bidding_record):
    # print(bidding_record)
    for bidder in bidding_record:
        highest_bid = 0
        winner = ""
        bid_amount = bidding_record[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes or 'no.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        #For clearing screen
        print("\x1B[2J")  
