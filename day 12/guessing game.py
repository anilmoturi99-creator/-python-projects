import random
from art import logo
print(logo)
print("Welcome to the  Number guessing game!")
#generate a random number between 1 and 100
secret_number=random.randint(1,100)
# choose difficulty
difficulty=input("type 'easy' to play easy levels or type 'hard' to play difficulty level: ").lower()
if difficulty =="easy":
    attempts=10
else:
    attempts=5

print(f"you have {attempts} attempts")
while attempts > 0:
    guess_num=int(input("guess the number: "))
    if guess_num==secret_number:
        print("you guessed correctly! you win")
        break
    elif guess_num > secret_number:
        print("too high")
        attempts-=1
        print(f"you have remaining:{attempts} attempts ")
    else:
        guess_num < secret_number
        print("too low")
        attempts -= 1
        print(f"you have remaining:{attempts} attempts ")
    if attempts == 0:
        print(f"you ran out of attempts. you lose the game.the number was {secret_number}")
























