def reverse_lookup(dict, value):
    keys = []
    for key in dict:
        if dict[key] == value:
            keys.append(key)
    return keys


dict = {"apple": 1, "banana": 2, "orange": 3, "grapes": 2}
result = reverse_lookup(dict, 2)
print(result)
