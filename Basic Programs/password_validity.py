password = input("Enter password : ")
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in password:
    if i.isalpha() and ord(i) >= 65 and ord(i) <= 90:
        c1 += 1
    if i.isdigit() and int(i) >= 0 and int(i) <= 9:
        c2 += 1
    if i.isalpha() and ord(i) >= 97 and ord(i) <= 122:
        c3 += 1
    if i == "$" or i == "#" or i == "@":
        c4 += 1

leng = len(password)
if c1 >= 1 and c2 >= 1 and c3 >= 1 and c4 >= 1 and leng >= 6:
    print("Valid")
else:
    print("Not valid")
