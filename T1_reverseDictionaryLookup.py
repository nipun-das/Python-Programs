def reverse_lookup(dict, value):
    keys = []
    for key in dict:
        if dict[key] == value:
            keys.append(key)
    return keys

my_dict = {"apple": 1, "banana": 2, "orange": 3, "kiwi": 2}
result = reverse_lookup(my_dict, 2)
print(result)

