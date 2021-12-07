# Advent of Code Day 7
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents = [int(number) for number in line.split(',')]

    return contents

file_contents = read_file("input.txt")

from functools import reduce

result1 = []
minimum = min(file_contents)
maximum = max(file_contents)

for number in range(minimum, maximum):
    result1.append(reduce(lambda sum, item: sum + abs(number-item), file_contents, 0))

# Task 1: 
print("Task 1:", min(result1))

result2 = []
sums = [sum(range(0, number+1)) for number in range(minimum, maximum+1)]

for number in range(minimum, maximum):
    result2.append(reduce(lambda sum, item: sum + sums[abs(number-item)], file_contents, 0))

# Task 2: 
print("Task 2:", min(result2))
