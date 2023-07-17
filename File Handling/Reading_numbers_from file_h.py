f = open("File Handling/files/numhorizontal.txt", "r")

sum = 0

for line in f:
    list = line.split()
    for item in list:
        n = int(item)
        sum += n
print(f"sum is {sum}")
