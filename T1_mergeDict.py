dict1 = {"apple": "1", "orange": "2", "banana": "3"}
dict2 = {"grapes": "4", "pineapple": "5"}

for key, value in dict2.items():
    dict1[key] = value

print(dict1)
