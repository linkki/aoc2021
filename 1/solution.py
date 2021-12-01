# Advent of Code Day 1
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(int(line.strip()))

    return contents

numbers = read_file("input.txt")
current_number = numbers[0]
increased_count = 0

for number in numbers[1:]:
    if current_number < number:
        increased_count += 1
    current_number = number

# Task 1: 1139
print("Task 1:", increased_count)

current_number1 = numbers[0]
current_number2 = numbers[1]
current_number3 = numbers[2]
increased_count = 0

for number in numbers[3:]:
    current_sum = current_number1 + current_number2 + current_number3
    new_sum = current_number2 + current_number3 + number
    if current_sum < new_sum:
        increased_count += 1
    current_number1 = current_number2
    current_number2 = current_number3
    current_number3 = number

# Task 2: 1103
print("Task 2:", increased_count)
