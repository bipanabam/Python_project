import random
from art import logo, vs
from game_data import data

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def compare(A, B):
    """Compares followers of A and B."""
    followers_a = A['follower_count']
    followers_b = B['follower_count']
    if followers_a > followers_b:
        return 'A'
    else:
        return 'B'

print(logo)

def game():
    score = 0
    account_b = random.choice(data)

    answer = ''
    guess = ''
    while guess == answer:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data) 

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").title()
        if not(guess == 'A' or guess == 'B'):
            print("Please enter valid option.")
            guess = input("Who has more followers? Type 'A' or 'B': ").title()

        answer = compare(account_a, account_b)
        if guess == answer:
            score += 1
            #For clearing screen
            print("\x1B[2J")
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

game()