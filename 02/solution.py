# Advent of Code Day 2
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

result1 = 0

forward_total = 0
depth_total = 0

file_contents = read_file("input.txt")

for line in file_contents:
    direction, amount = line.split()
    if direction == "forward":
        forward_total += int(amount)
    elif direction == "up":
        depth_total -= int(amount)
    elif direction == "down":
        depth_total += int(amount)

result1 = forward_total*depth_total

# Task 1: 1499229
print("Task 1:", result1)

result2 = 0
aim = 0
forward_total = 0
depth_total = 0

for line in file_contents:
    direction, amount = line.split()
    if direction == "forward":
        forward_total += int(amount)
        depth_total += aim * int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)

result2 = forward_total*depth_total

# Task 2: 1340836560
print("Task 2:", result2)