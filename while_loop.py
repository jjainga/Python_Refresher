import random

i = 1
while i <= 5:
    print("*" * i)
    i +=1
print ("Done")


#guessing game


def guess_game():
    attempt = 1
    secret_number = random.randrange(1,100)
    guess = input("Guess a number from 1 to 100:")
    while attempt < 3:
        attempt += 1
        print(f"The secret number was {secret_number}")
        secret_number = random.randrange(1,100)
        guess = input("Guess a number from 1 to 100:")
        if guess == secret_number:
            print(f"You win!")
            break
    else:
        print(f"Game over!")

guess_game()