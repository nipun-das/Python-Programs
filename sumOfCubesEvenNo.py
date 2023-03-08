import math

lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))

sum = 0
for i in range(lower, upper):
    if i % 2 == 0:
        sum += math.pow(i, 3)

print(str(sum))
