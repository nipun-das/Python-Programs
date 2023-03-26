dict = {"nissan": 1, "toyota": 2, "bmw": 10, "volkswagen": 4, "skoda": 5}

max = None
min = None

for key, value in dict.items():
    if max is None or value > max:
        max = value
        keymax = key
    if min is None or value < min:
        min = value
        keymin = key

print("Min :", min, "for key :", keymin)
print("Max :", max, "for key :", keymax)
