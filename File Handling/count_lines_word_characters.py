f = open("File Handling/files/text.txt", "r")

nl = 0
nw = 0
nc = 0

for line in f:
    nl = nl + 1
    wordlist = line.split()
    for item in wordlist:
        nw = nw + 1
        for i in item:
            nc = nc + 1
            
print(f"Lines : {nl}\nWords : {nw}\nCharacters : {nc}")
