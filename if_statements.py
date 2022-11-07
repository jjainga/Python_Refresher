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
    print(f"{int(down_payment):,}")

