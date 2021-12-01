# Advent of Code Day 1
# Tiedeluokka Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(int(line.strip()))

    return contents

numbers = read_file("input.txt")
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

print(increased_count)