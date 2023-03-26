import math

n = int(input("Enter the number of key-value pairs: "))

dict = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = math.pow(key, 2)
    dict[key] = value

print(dict)
