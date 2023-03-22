dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

f = 0

key_check = input("Enter the key to check : ")

for key in dict:
    if key_check == key:
        f = 1
        break
if f == 1:
    print("Yes,", key_check, "exists!")
else:
    print("No,", key_check, "does not exist!")
