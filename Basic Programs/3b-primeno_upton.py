lim = int(input("Enter limit : "))

if lim == 0 or lim == 1:
    print("There are no prime numbers upto " + (str(lim)))
else:
    for i in range(2, lim + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
