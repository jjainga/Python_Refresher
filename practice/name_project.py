name = input("Please input your name:")

if len(name) < 3:
    print("Name cannot be less than 3 characters")
elif len(name) > 50:
    print("Name cannot be more than 50 characters")
else:
    print(name)
