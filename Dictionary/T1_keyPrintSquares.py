import math

# n = int(input("Enter the number of key-value pairs: "))

dict = {}

for i in range(1, 16):
    # key = int(input("Enter the key: "))
    key = i
    value = math.pow(key, 2)
    dict[key] = value

print(dict)
