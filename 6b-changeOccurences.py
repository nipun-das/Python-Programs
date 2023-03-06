# Write a .py program to get a string and change all occurences
# of its first character to '$', except the first character itslef.

def change_first_char(str):
    if len(str) < 2:
        return str
    first_char = str[0]
    new_string = first_char + str[1:].replace(first_char, "$")
    return new_string


str = input("Enter a string: ")
modified = change_first_char(str)
print("New string:", modified)

'''

Enter a string: heyhowhellohi
New string: hey$ow$ello$i

'''