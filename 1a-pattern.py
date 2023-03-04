n = 5
for row in range(1, n+1):
    for col in range(1, row+1):
        print("*", end=" ")
    print("")
for row in range(2, n+1):
    for col in range(row, n+1):
        print("*", end=" ")
    print("")

'''
output : 

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''
