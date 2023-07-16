str = input("Enter string : ")

print("Python slicing")
print("--------------------------------")
# Get all items
print(str[:])

# Get all the Items After a Specific Position
print(str[2:])

# Get all the Items Before a Specific Position
print(str[:3])

# Get all the Items from One Position to Another Position
print(str[2:5])

# Get the Items at Specified Intervals
print(str[::2])

# Using Python List Slice to Get the n-first Elements from a List
print(str[:6])

# Using Python List Slice to Reverse a List
print(str[::-1])

# Using Python List Slice to Substitute Part a List
my_list = [2, 4, 6, 5, 3, 9, 7]
my_list[0:2] = ["black", "white"]
print(my_list)

# Using Python list slice to delete elements
my_list = ["black", "yellow", "gray", "blue", 5, 3, 9, 7]
del my_list[3:6]
print(my_list)

print("--------------------------------")

print("Program solution : ")

strRev = str[::-1]

if(str==strRev):
    print("Palindrome!")
else:
    print("Not palindrome!")

'''

Enter string : malayalam
Python slicing
--------------------------------
malayalam
layalam
mal
lay
mlylm
malaya
malayalam
['black', 'white', 6, 5, 3, 9, 7]
['black', 'yellow', 'gray', 9, 7]
--------------------------------
Program solution : 
Palindrome!

'''