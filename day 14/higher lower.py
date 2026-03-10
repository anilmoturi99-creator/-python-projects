#display the logo
from art import logo,vs
from game_data import data
import random

#formate the account data into printable format
def format_data(account):
    """ takes the account data and returns printable format."""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name},a {account_descr} from {account_country}"
def check_answer(user_guess,a_followers,b_followers):
    """takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
print(logo)
score=0
game_should_continue=True
account_b=random.choice(data)
while game_should_continue:
    #generate a random account from data
    # making account position B becomes the next account at position A
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"compare A:{format_data(account_a)}")
    print(vs)
    print(f"against B:{format_data(account_b)}")
    #ask user for guess
    guess=input("who has more followers ? type 'A' or 'B':").lower()
    #clear the screen
    print("\n" * 20)
    print(logo)
    print(guess)
    #cheack if user is correct
    #get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    #give user feedback on their
    #keep score
    if is_correct:
        score+=1
        print(f"you are Right! your current Score:{score}")
    else:
        print(f"Sorry.that's wrong.Final Score:{score}")
        game_should_continue=False











