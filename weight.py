def weight_conversion():
    weight_pounds = input("What is your weight in lbs?")
    kilo = 0.45359237
    weight_kilo = int(weight_pounds)*kilo

    print("You are " + str(weight_kilo) + " kgs!")


weight_conversion()
