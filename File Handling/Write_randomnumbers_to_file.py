import random
f = open("File Handling/files/integers.txt",'w')
for i in range(500):
    n = random.randint(1,500)
    f.write(str(n)+'\n')
f.close()