number = int(input("Enter number : "))

n = number
rev = 0
while n != 0:
    last = n % 10
    rev = rev * 10 + last
    n = n // 10
print(str(rev))
