def count_occurrences(input_list, element):
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)

print(f"The element {element_to_count} occurs {occurrences} times in the list.")
