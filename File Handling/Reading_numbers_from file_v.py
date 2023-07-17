f = open("File Handling/files/numvertical.txt", "r")

sum = 0

for line in f:
    line = line.strip()
    n = int(line)
    sum += n
print(f"sum is {sum}")
