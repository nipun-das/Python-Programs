list = []

size = int(input("Enter size of list : "))

for i in range(0, size):
    print("Enter ", (i + 1), " th element : ", end="")
    l = int(input())
    list.append(l)
print(list)

pos = int(input("Enter the position to insert : "))
item = int(input("Enter the item: "))

list = list[:pos] + [item] + list[pos:]
print(list)
