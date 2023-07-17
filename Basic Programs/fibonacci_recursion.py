def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


limit = int(input("Enter the limit : "))

for i in range(1, limit + 1):
    print(f"Fibonacci({i}) =", fibonacci(i))
