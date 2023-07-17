num = int(input("Enter number : "))

if num == 0 or num == 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")
