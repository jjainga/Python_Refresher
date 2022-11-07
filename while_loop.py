import random

i = 1
while i <= 5:
    print("*" * i)
    i +=1
print ("Done")


#guessing game


def guess_game():
    secret_number = random.randrange(1,100)
    guess = input("Guess a number from 1 to 100:")
    while guess != secret_number:
        print(f"The secret number was {secret_number}")
        secret_number = random.randrange(1,100)
        guess = input("Guess a number from 1 to 100:")

guess_game()