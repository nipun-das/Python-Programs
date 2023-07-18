print("In descreasing order of frequency")
sorted_dict_desc = dict(sorted(dict.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict_desc)