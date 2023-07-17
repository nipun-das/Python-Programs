f = open("File Handling/files/loremipsum.txt","r")

while(True):
    line = f.readline()
    if line == "":          # indicates end of file
        break
    print(line)