start = 1500
end = 2700

for number in range(start, end + 1):
    if number % 7 == 0 and number % 5 == 0:
        print(number, " is divisible by 7 and multiple of 5")
