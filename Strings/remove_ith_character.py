str = input("Enter string : ")
pos = int(input("Enter pos to remove from : "))

strnew = ""

if pos > 0 and pos <= len(str):
    strnew = strnew + str[:pos] + str[pos + 1 :]
else:
    print("Enter valid index")

print(f"New string : {strnew}")
