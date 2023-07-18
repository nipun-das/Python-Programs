str = input("Enter string : ")

diction = {}

for i in str:
    if i in diction:
        diction[i] += 1
    else:
        diction[i] = 1

print(diction)


print("In descreasing order of frequency")
sorted_dict_desc = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict_desc)
