#car game, make car start/stop/ or quiet the game


def car_game():
    action = ""
    while action != "QUIT":
        action = input(">").upper()
        if action == "HELP":
            print(''' 
            Try
            >start - to start the car
            >stop - to stop the car
            >quit - to end the game
            ''')
        elif action == "START":
            print(f"Car started... ready to go")
        elif action == "STOP":
            print(f"Car stopped.")
        elif action == "QUIT":
            print(f"Game ended")
            break
        else:
            print(f"I don't understand... please try again")

car_game()