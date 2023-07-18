n = int(input("Enter the no. of elements : "))
list = []
for i in range(n):
    print(f"Enter the {i}th element")
    l = int(input())
    list.append(l)

temp = list[0]
list[0] = list[n - 1]
list[n - 1] = temp

print("List : ", list)
