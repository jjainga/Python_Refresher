#car game, make car start/stop/ or quiet the game


def car_game():
    action = ""
    car_status = False
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
            if car_status:
                print(f"Car is already started...")
            else:
                print(f"Car started... ready to go")
                car_status = True
        elif action == "STOP":
            if not car_status:
                print(f"Car is already stopped.")
            else:
                print(f"Car stopped.")
                car_status = False
        elif action == "QUIT":
            print(f"Game ended")
            break
        else:
            print(f"I don't understand... please try again")

car_game()