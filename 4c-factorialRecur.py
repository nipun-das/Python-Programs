n = int(input("Enter number : "))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)

print("The factorial of", n, "is", recur_factorial(n))
