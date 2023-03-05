n = int(input("Enter limit : "))
if n == 0 or n == 1:
    print("There are no prime numbers upto "+(str(n)))
else:
    for num in range(2, n+1):
        isPrime = True
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                isPrime = False
                break
        if isPrime:
            print(str(num)+" ", end="")
