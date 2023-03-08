up = int(input("Enter limit : "))

a = -1
b = 1

for i in range(1, up):
    c = a + b
    print(c, " ", end="")
    a = b
    b = c
