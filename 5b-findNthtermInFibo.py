# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# no recursion
def fibonacci(n):

    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
    print(f[0], "", f[1], " ", end="")
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
        print(f[i - 1] + f[i - 2], " ", end="")
        # print(str(f[i - 1] + f[i - 2]) + " ", end="")
    print()    
    return f[n]


# using recursion
# Python program to display the Fibonacci sequence


def fibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2)


n = int(input("Enter limit to print upto : "))

print("Fibonacci sequence:")

print(str(n) + "th term is : ", fibonacci(n - 1))

print()

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacciRecursion(i), " ", end="")
print()
print(str(n) + "th term is : ", fibonacciRecursion(n - 1))
