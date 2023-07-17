def reverse_number(number):
    reversed_number = str(number)[::-1]
    return int(reversed_number)

def sum_of_digits(number):
    number_str = str(number)
    sum_digits = 0
    for digit in number_str:
        sum_digits += int(digit)
    return sum_digits

if __name__ == "__main__":
        num = int(input("Enter a number: "))
        reversed_num = reverse_number(num)
        sum_digits = sum_of_digits(num)

        print(f"Reversed Number: {reversed_num}")
        print(f"Sum of Digits: {sum_digits}")
