#shopping cart

prices = [10,3,85,12,13,16,32,26]
total = 0

for item in prices:
    total += item

print(f"Your total is ${total}")


for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


number_list = [5,2,5,2,2]

for x in number_list:
    print(f"X"* x)
print("")

def shape():
    line = ""
    for x in number_list:
        line = ""
        for y in range(x):
            line += "X"
        print(line)

shape()           