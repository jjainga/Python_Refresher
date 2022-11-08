def greet_user(first_name, last_name):
    print(f"Hi there {first_name, last_name}")
    print("Welcome aboard")


greet_user("Joshua", "Jainga")
greet_user("Lindsay", "Masters")

greet_user(last_name="Jainga", first_name="Joshua")

#key word arguments, you dont always have to use key word arguments, this is most utilized while using a lot of numerical variables


def total_cost(item_cost,shipping_cost,tax):
    total = 0
    total = item_cost + tax + shipping_cost


total_cost(item_cost=20, shipping_cost=4, tax=2)

#for the most part use potitial argumnets then key work arguments

#return values, return statements

def square(number):
    return number * number


result = square(3)

print(result)
print(square(4))

#by default all funciton return None, but you can change that by assigning something to return 