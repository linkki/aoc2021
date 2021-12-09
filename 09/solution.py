# Advent of Code Day 9
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append([int(c) for c in line.strip()])

    return contents

file_contents = read_file("input.txt")

result1 = 0

for i in range(len(file_contents)):
    for j in range(len(file_contents[0])):
        how_many_checked = 0
        # left
        if j == 0:
            how_many_checked += 1
        elif file_contents[i][j] < file_contents[i][j-1]:
            how_many_checked += 1
        # right
        if j == len(file_contents[i]) - 1:
            how_many_checked += 1
        elif file_contents[i][j] < file_contents[i][j+1]:
            how_many_checked += 1
        # up
        if i == 0:
            how_many_checked += 1
        elif file_contents[i][j] < file_contents[i-1][j]:
            how_many_checked += 1
        # down
        if i == len(file_contents) - 1:
            how_many_checked += 1
        elif file_contents[i][j] < file_contents[i+1][j]:
            how_many_checked += 1
        
        if how_many_checked == 4:
            result1 += 1 + file_contents[i][j]

# Task 1: 572
print("Task 1:", result1)

result2 = 0

basins = []

checked = [ [0 for i in range(len(file_contents[0]))] for j in range(len(file_contents)) ]

def check_neighbours(x, y):
    if checked[y][x] == 1:
        return 0
    else:
        checked[y][x] = 1
    if file_contents[y][x] == 9:
        return 0
    size = 1
    if x != 0:
        size += check_neighbours(x-1, y)
    if x != len(file_contents[y]) -1 :
        size += check_neighbours(x+1, y)
    if y != 0:
        size += check_neighbours(x, y-1)
    if y != len(file_contents) -1:
        size += check_neighbours(x, y+1)
    
    return size

for i in range(len(file_contents)):
    for j in range(len(file_contents[0])):
        basin = check_neighbours(j,i)
        if basin != 0:
            basins.append(basin)

from functools import reduce

result2 = reduce(lambda product, item: product * item, sorted(basins)[-3:], 1)

# Task 2: 847044
print("Task 2:", result2)
