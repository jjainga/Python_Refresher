weight = input("What is your weight?:")
weight_unit = input("(L)bs or (K)gs?:")

if weight_unit.upper() == "K":
    new_weight = int(weight) / 0.45359237
    print("You are " + str(round(new_weight)) + "lbs!")
elif weight_unit.upper() =="L":
    new_weight = int(weight) * 0.45359237
    print("You are " + str(round(new_weight)) + "kgs!")
else:
    print(f"Please enter a L or K for unit")

