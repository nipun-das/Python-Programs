n = int(input("Enter the no. of elements : "))
list = []
for i in range(n):
    print(f"Enter the {i}th element")
    l = int(input())
    list.append(l)

list.sort()

if n % 2 == 0:
    m1 = list[n // 2]
    m2 = list[n // 2 - 1]
    m = (m1 + m2) / 2
else:
    m = list[n // 2]
print("Median : ", m)
