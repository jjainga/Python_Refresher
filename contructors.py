class Point:
    #this is a contructor, used to contruct an object
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")


    def draw(self):
        print("draw")


 #a contructor is a function that gets call at the time the object is created   
point1 = Point(10,20)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"My name is {self.name}")


person1 = Person("Joshua")

person1.talk()