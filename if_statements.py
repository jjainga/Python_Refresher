is_hot = True
is_cold = False

if is_hot:
    print('''
It's a hot day
Remember to drink enough water
    ''')
elif is_cold:
    print('''
It's a cold day
Wear some warm clothes
    ''')
else:
    print("Have a lovely day!")

print("Go cougs")


# down payment example

house_price = 1000000

good_credit = False

if good_credit:
    down_payment = house_price * .1
    print(f"{int(down_payment):,}")
elif good_credit is not True:
    down_payment = house_price * .2
    print(f"Down Payment: ${int(down_payment):,}")


has_high_income = True
has_good_credit = False

if has_good_credit and has_high_income:
    print("Eligible for loan")
elif has_good_credit is not True or has_high_income is not True:
    print("Not Eligible for loan")

