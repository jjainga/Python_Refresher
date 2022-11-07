#car game, make car start/stop/ or quiet the game


def car_game():
    action = input(">")
    while action:
        if action.upper() == "HELP":
            print(''' 
            Try
            >start
            >stop
            >quit
            ''')
            action = input(">")
        elif action.upper() == "START":
            print(f"Car started... ready to go")
            action = input(">")
        elif action.upper() == "STOP":
            print(f"Car stopped.")
            action = input(">")
        elif action.upper() == "QUIT":
            print(f"Game ended")
            break
        else:
            print(f"I don't understand... please try again")
            action = input(">")

car_game()