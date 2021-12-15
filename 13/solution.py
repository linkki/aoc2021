# Advent of Code Day 13
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    dots = []
    folds = []
    with open(filename) as file:
        for line in file:
            if line[0] == 'f':
                fold = line.strip().split()[2]
                folds.append((fold[0], int("".join(fold[2:]))))
            elif len(line.strip()) != 0:
                dot = line.strip().split(',')
                dots.append((int(dot[0]), int(dot[1])))

    return (dots, folds)

def print_dots(dots):
    width = max([dot[0] for dot in dots]) +1
    height = max([dot[1] for dot in dots]) +1
    dot_grid = [['.' for i in range(width)] for j in range(height)]

    for dot in dots:
        dot_grid[dot[1]][dot[0]] = '#'
    for line in dot_grid:
        for c in line:
            print(c, end="")
        print()

dots, folds = read_file("input.txt")
#print(dots[0])
#print(folds[0])

result1 = 0

new_dots = []

def fold_new_dot(dot: tuple, axis: str, value: int):
    #breakpoint()
    if axis == 'y':
        if dot[1] < value:
            return dot
        else:
            new_dot = (dot[0], value - (dot[1] - value))
            return new_dot
    else:
        if dot[0] < value:
            return dot
        else:
            new_dot = (value - (dot[0] - value), dot[1])
            return new_dot

for i in range(len(folds)):
    for dot in dots:
        new_dot = fold_new_dot(dot, folds[i][0], folds[i][1])
        if new_dot not in new_dots:
            new_dots.append(new_dot)
    if i == 0:
        result1 = len(new_dots)
    dots = new_dots
    new_dots = []
    

print_dots(dots)

# Task 1: 664
print("Task 1:", result1)

result2 = "in printout above"
# Task 2: EFJKZLBL
print("Task 2:", result2)
