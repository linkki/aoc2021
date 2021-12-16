# Advent of Code Day 15
# Science Lab Linkki, Virpi Sumu

# for checking how long execution takes
import time
start_time = time.time()

# for part 1
def read_file(filename):
    contents = []
    min_risk_totals = []
    with open(filename) as file:
        for line in file:
            contents.append([int(c) for c in line.strip()])
            min_risk_totals.append([100000 for c in line.strip()])

    return (contents, min_risk_totals)

# for part 2: uses original input to create a map 5 by 5 times the original size
def read_file2(filename):
    contents = []
    contents_five = []
    min_risk_totals = []
    with open(filename) as file:
        for line in file:
            contents.append([int(c) for c in line.strip()])
    
    length = 5

    for j in range(length):
        for y in range(len(contents)):
            line = []
            for i in range(length):
                for x in range(len(contents)):
                    new_value = contents[y][x] + i + j
                    if new_value > 9:
                        new_value -= 9
                    line.append(new_value)
            contents_five.append(line)
            min_risk_totals.append([2500000 for i in range(length*len(contents))])

    return (contents_five, min_risk_totals)

def print_totals(totals):
    for line in totals:
        for total in line:
            print(str(total).ljust(3)[:3], end="")
        print()
    print()


# early recursive attempt, took too long
#import sys
#sys.setrecursionlimit(100000)
def calculate_path(risks: list, totals: list, y: int, x: int, risk: int):
    if totals[y][x] <= risk:
        return
    totals[y][x] = risk
    if y > 0:
        to_up = calculate_path(risks, totals, y-1, x, totals[y][x] + risks[y-1][x])
    if y < len(risks)-1:
        to_down = calculate_path(risks, totals, y+1, x, totals[y][x] + risks[y+1][x])
    if x > 0:
        to_left = calculate_path(risks, totals, y, x-1, totals[y][x] + risks[y][x-1])
    if x < len(risks)-1:
        to_right = calculate_path(risks, totals, y, x+1, totals[y][x] + risks[y][x+1])

# used in part 1
# every time the path shortens when going up or to the left, the analysis is repeated for the entire grid
def calculate_path2(risks: list, totals: list):
    for j in range(len(totals)):
        for i in range(len(totals)):
            # to right
            if i < len(risks) - 1:
                new_value = totals[j][i] + risks[j][i+1]
                if new_value < totals[j][i+1]:
                    totals[j][i+1] = new_value
            # to down
            if j < len(risks) - 1:
                new_value = totals[j][i] + risks[j+1][i]
                if new_value < totals[j+1][i]:
                    totals[j+1][i] = new_value
            # to left
            if i > 0:
                new_value = totals[j][i] + risks[j][i-1]
                if new_value < totals[j][i-1]:
                    totals[j][i-1] = new_value
                    return False
            # to up
            if j > 0:
                new_value = totals[j][i] + risks[j-1][i]
                if new_value < totals[j-1][i]:
                    totals[j-1][i] = new_value
                    return False
    
    return True

# used in part two 
# optimises away the top parts of the grid when repeating the run-through 
def calculate_path3(risks: list, totals: list, y, x):
    for j in range(y, len(risks)):
        # if using x here as the start of range, will never go through the left part of the grid
        for i in range(0, len(risks)):
            # to right
            if i < len(risks) - 1:
                new_value = totals[j][i] + risks[j][i+1]
                if new_value < totals[j][i+1]:
                    totals[j][i+1] = new_value
            # to down
            if j < len(risks) - 1:
                new_value = totals[j][i] + risks[j+1][i]
                if new_value < totals[j+1][i]:
                    totals[j+1][i] = new_value
            # to left
            if i > 0:
                new_value = totals[j][i] + risks[j][i-1]
                if new_value < totals[j][i-1]:
                    totals[j][i-1] = new_value
                    return (j, i-1)
            # to up
            if j > 0:
                new_value = totals[j][i] + risks[j-1][i]
                if new_value < totals[j-1][i]:
                    totals[j-1][i] = new_value
                    return (j-1, i)
    return (0,0)

risks, totals = read_file("input.txt")
risks2, totals2 = read_file2("input.txt")

# first step "costs nothing"
totals[0][0] = 0

# recursive attempt, will not finish with the actual input
#calculate_path(risks, totals, 0, 0, 0)

while not calculate_path2(risks, totals):
    continue

result1 = totals[len(risks)-1][len(risks)-1]

# Task 1: 717
print("Task 1:", result1)

# first step "costs nothing"
totals2[0][0] = 0

last_changed = calculate_path3(risks2, totals2, 0, 0)

# takes about 2.5 minutes to execute on an 8 year old laptop
while True:
    if last_changed == (0,0):
        break
    else:
        last_changed = calculate_path3(risks2, totals2, last_changed[0], last_changed[1])

result2 = totals2[len(risks2)-1][len(risks2)-1]

# Task 2: 2993
print("Task 2:", result2)

print(f"--- {time.time() - start_time} seconds ---")