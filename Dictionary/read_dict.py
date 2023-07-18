dict = {}

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value {i + 1}: ")
    dict[key] = value

print("Dictionary:", dict)
