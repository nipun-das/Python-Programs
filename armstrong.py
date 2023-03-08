import math

number = int(input("Enter number : "))

num = number
count = 0

while num != 0:
    last = num % 10
    count = count + 1
    num = num // 10

num = number

rev = 0
while num != 0:
    last = num % 10
    rev = rev + math.pow(last, count)
    num = num // 10

if number == rev:
    print("Armstrong!")
else:
    print("Not Armstrong!")
