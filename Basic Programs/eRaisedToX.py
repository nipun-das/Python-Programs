# e^x = 1 + x + x^2 / 2! + x^3 / 3! ....

import math

x = int(input("Enter x : "))
n = int(input("Enter no. of terms : "))
sum = 1

for i in range(1, n + 1):
    numerator = math.pow(x, i)
    denominator = math.factorial(i)
    sum = sum + numerator / denominator
print(sum)
