n = int(input("Enter number : "))
num = n
# using while loop
rev = 0
while n > 0:
    last = n % 10
    rev += last
    n = n // 10
print("Sum of digits using while loop = ", rev)

n = num
sum = 0
for i in str(n):
    sum += int(i)
print("Sum of digits without while loop = ", sum)

"""
Enter number : 1234
Sum of digits using while loop =  10
Sum of digits without while loop =  10

"""
