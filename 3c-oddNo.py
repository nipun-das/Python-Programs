list = []
n = int(input("Enter no. of elements in list : "))
for i in range(0, n):
    print("Enter "+str(i+1)+"th number : ", end="")
    l = int(input())
    list.append(l)
print("List : ", list)

print("Odd no.s are : ", end="")
for no in list:
    if no % 2 == 1:
        print(str(no)+" ", end="")
