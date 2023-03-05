number = 1
n = 4

for row in range(1, n+1):
    for col in range(1, row+1):
        print(number, end="")
        number = number+1
    print()
    number = 1

'''
1
12
123
1234

'''
