a = []
n = int(input("Enter no. of elements in list"))
for i in range(0, n):
    print("Enter "+str(i+1)+"th number : ", end="")
    l = int(input())
    a.append(l)
print("List : ", a)
j = 0
avg = 0
sum = 0
num = n
while (num > 0):
    sum = sum + a[j]
    print(a[j])
    j = j + 1
    num = num-1
avg = sum/n
print("Avg = ", avg)
