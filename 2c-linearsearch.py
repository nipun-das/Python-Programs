list = []
n = int(input("Enter no. of elements : "))
for i in range(0, n):
    print("Enter " + str(i + 1) + "th element :", end="")
    l = int(input())
    list.append(l)
print(list)


f = 0
key = int(input("Enter the key : "))
for i in range(0, n):
    if key == list[i]:
        print("Found at location : ", (i + 1))
        f = 1
        break
if f == 0:
    print("Not found!")
