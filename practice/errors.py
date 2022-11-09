

def error_check():
    try:
        user_age = int(input("Age: "))
        income = 20000
        risk = income / user_age
        return user_age
    except ZeroDivisionError:
        return "Age cannot be 0"
    except ValueError:
        return "Invalid Value"


print(error_check())