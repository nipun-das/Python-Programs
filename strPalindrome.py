# check string palindrome without using any functions

string = input("Enter the string: ")

if string == string[::-1]:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
