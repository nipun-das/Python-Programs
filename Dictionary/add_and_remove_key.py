# ADDING--------------------------------------------------------------------
my_dict = {"apple": 5, "banana": 3}

# Adding a new key-value pair
my_dict["orange"] = 7

print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'orange': 7}

my_dict = {"apple": 5, "banana": 3}

# Updating an existing key's value
my_dict["apple"] = 10

print(my_dict)  # Output: {'apple': 10, 'banana': 3}


# REMOVING-------------------------------------------------------------------
my_dict = {"apple": 5, "banana": 3}

# Removing a key-value pair using pop
my_dict.pop("apple")

print(my_dict)  # Output: {'banana': 3}
