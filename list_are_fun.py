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