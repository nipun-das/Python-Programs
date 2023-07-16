list = []
n = int(input("Enter no. of elements in list : "))
for i in range(0, n):
    print("Enter " + str(i + 1) + "th number : ", end="")
    l = int(input())
    list.append(l)
print("List : ", list)

max = list[0]
for i in range(0, len(list)):
    if max < list[i]:
        max = list[i]


print("Max in list is : ", max)
