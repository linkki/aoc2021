# Advent of Code Day 8
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            row = []
            for item in line.strip().split(' | '):
                strings = []
                for string in item.split():
                    strings.append("".join(sorted(string)))
                row.append(strings)

            contents.append(row)

    return contents

file_contents = read_file("input.txt")

result1 = 0

counter = 0
for item in file_contents:
    for string in item[1]:
        if len(string) in [2,3,4,7]:
            counter += 1

result1 = counter

# Task 1: 495
print("Task 1:", result1)

result2 = 0
for line in file_contents:
    numbers = [""]*10
    for item in sorted(line[0], key=len):
        if len(item) == 2:
            numbers[1] = item
        elif len(item) == 3:
            numbers[7] = item
        elif len(item) == 4:
            numbers[4] = item
        elif len(item) == 7:
            numbers[8] = item
        elif len(item) == 5: # 2,3,5
            four_filtered = "".join(list(filter(lambda c : c not in numbers[1], numbers[4])))
            if numbers[1][0] in item and numbers[1][1] in item:
                numbers[3] = item
            elif four_filtered[0] in item and four_filtered[1] in item:
                numbers[5] = item
            else:
                numbers[2] = item

        elif len(item) == 6: # 0,6,9
            if (numbers[4][0] in item) and (numbers[4][1] in item) and (numbers[4][2] in item) and (numbers[4][3] in item):
                numbers[9] = item
            elif numbers[1][0] not in item or numbers[1][1] not in item:
                numbers[6] = item
            else:
                numbers[0] = item

    new_number = []
    for item in line[1]:
        new_number.append(str(numbers.index(item)))
    
    result2 += int("".join(new_number))

# Task 2: 1055164
print("Task 2:", result2)
