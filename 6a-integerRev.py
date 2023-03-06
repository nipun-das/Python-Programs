integer = int(input("Enter integer : "))
intege = integer


# 2 ways to do

# method 1 - considering input as integer
rev = 0
factor = 1

while integer != 0:
    last = integer % 10
    rev = rev * 10 + last
    integer = integer // 10

print()
print("M1 ---> The reverse of", intege, "is", rev)


print()

# method 2 - considering input as string
integerStr = str(intege)

rev_num = integerStr[::-1]
print("M2 ---> The reverse of", integerStr, "is", rev_num)


'''

Enter integer : 12340563

M1 ---> The reverse of 12340563 is 36504321

M2 ---> The reverse of 12340563 is 36504321

'''