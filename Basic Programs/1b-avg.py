a = []
n = int(input("Enter no. of elements in list : "))
for i in range(0, n):
    print("Enter " + str(i + 1) + "th number : ", end="")
    l = int(input())
    a.append(l)
print("List : ", a)
j = 0
avg = 0
sum = 0
num = n
while num > 0:
    sum = sum + a[j]
    print(a[j])
    j = j + 1
    num = num - 1
avg = sum / n
print("Avg = ", avg)

"""
Enter no. of elements in list : 5
Enter 1th number : 1
Enter 2th number : 2
Enter 3th number : 3
Enter 4th number : 4
Enter 5th number : 5
List :  [1, 2, 3, 4, 5]
1
2
3
4
5
Avg =  3.0

"""
