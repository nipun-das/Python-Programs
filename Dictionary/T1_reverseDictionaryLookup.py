def reverse_lookup(dict, value):
    keys = []
    for key in dict:
        if dict[key] == value:
            keys.append(key)
    return keys


dict = {"apple": 1, "banana": 2, "orange": 3, "grapes": 2}

value = int(input("Enter the value to lookup : "))

result = reverse_lookup(dict, value)
print(result)
