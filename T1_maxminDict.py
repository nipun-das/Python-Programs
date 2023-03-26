dict = {"k1": 1, "k2": 2, "k3": 10, "k4": 4, "k5": 5}

max = None
min = None

for (key, value) in dict:
    if max is None or value > max:
        max = value
    if min is None or value < min:
        min = value
        
print("Max : ",max)
print("Min : ",min)
