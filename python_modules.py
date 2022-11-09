#random values
import random

def random_number():
    for i in range(3):
        print(random.randint(10,20))


# random_number()



class Dice():
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def roll(self):
        return random.randint(self.low, self.high)


dice1 = Dice(1,6)
dice2 = Dice(1,6)

print(f"({dice1.roll()}, {dice2.roll()})")