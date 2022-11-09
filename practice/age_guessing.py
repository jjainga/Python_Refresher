import datetime

def age_solver():
    birth_year = input("What was the year your were born in?")
    birth_month = input("What month were your born in? (Month number, example: January = 1)")
    birth_day = input("What day of the month where your born on?")

    today = datetime.date.today()
    year = today.year
    age = year - int(birth_year)

    print("You are " +str(age) +" years old!")

age_solver()


