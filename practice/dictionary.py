#dictionaries are used when you want to store values as key value pairs

customer = {
    "name" : "Joshua Jainga",
    "age" : 31,
    "is_verified": True
}
#you can reference the keys in the dictionary to get the values
print(customer["name"])
#you can also use the get method
print(customer.get("name"))

# you can also update the value 

customer["name"] = "Jordan Jainga"
customer["birthday"] = "September 30, 1991"

print(customer.get("name"))
print(customer.get("birthday"))

#practice

number = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four"
}

def phone_number():
    phone = input("Phone#: ")
    phoneNumber =""
    for i in phone:
        phoneNumber += f"{number.get(int(i))} "
    print(phoneNumber)

phone_number()
