number_list = [12,1,34,534,23,93,12,65,76,3,23,8,79]

def largest(x):
    x.sort()
    print(x[-1])

largest(number_list)


def largets_manual(y):
    x = 0
    a = 0
    for i in y:
        if i >= a:
            a = i
            if a >= x:
                x = a
    print(x)

largets_manual(number_list)

#2D array

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matrix[0][2])

def matrix_loop(v):
    for item in v:
        for t in item:
            print(t)

matrix_loop(matrix)



#List methods

number_list_methods = [3,5,7,8,9,2,10,3,5,8,2,4,7,8,1,]

number_list_methods.append(15)
number_list_methods.insert(0,10)
number_list_methods.remove(5)
number_list_methods.pop()
number_list_methods.index(3)
num = number_list_methods.copy()
#look up to find more

#remove the duplicates from a list

def dup_removal(x):
    a = []
    print(x)
    for i in x:
        if i not in a:
            a.append(i)
    print(a)

dup_removal(number_list_methods)
