#This is bad, doesnt keep code dry. Try using inheritance


class Dog:
    def walk(self):
        print("Walk")

class Cat:
    def walk(self):
        print("Walk")


#Instead have a mamal class and then pass the walk method to dog and cat
#below we have the dag and cat class inheriting the walk method fromt he mammal class
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def __init__(self,name):
        self.name = name
    
    def bark():
        print("Bark Bark")


class Cat(Mammal):
    def __init__(self,name):
        self.name = name
    
    def meow():
        print("prrrrrrrrrr")


dog1 = Dog("Charlie")
dog1.walk()