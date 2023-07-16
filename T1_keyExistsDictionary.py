dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

key_check = input("Enter the key to check : ")

for key in dict:
    if key_check == key:
        print("Yes,", key_check, "exists!")
        break
else:
    print("No,", key_check, "does not exist!")
