# Advent of Code Day 3
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

file_contents = read_file("input.txt")

result1 = 0

input_length = len(file_contents)
input_line_length = len(file_contents[0])
most_common_bits = [0]*input_line_length

for i in range(input_line_length):
    ones_count = sum([int(line[i]) for line in file_contents])
    if ones_count > input_length/2:
        most_common_bits[i] = 1
    else: 
        most_common_bits[i] = 0

gamma = 0
epsilon = 0
base = 1

for bit in list(reversed(most_common_bits)):
    if bit == 1:
        gamma += base
    else:
        epsilon += base
    base *= 2

result1 = gamma * epsilon

# Task 1: 2724524
print("Task 1:", result1)

result2 = 0

oxygen_list = file_contents
co2_list = file_contents

for i in range(input_line_length):
    ones_count_o = sum([int(line[i]) for line in oxygen_list])
    if ones_count_o >= len(oxygen_list)/2:
        most_common_bit_o = 1
    else: 
        most_common_bit_o = 0

    #print(f"most common at {i}: {most_common_bit_o}, length {len(oxygen_list)}")

    ones_count_c = sum([int(line[i]) for line in co2_list])
    if ones_count_c >= len(co2_list)/2:
        most_common_bit_c = 1
    else: 
        most_common_bit_c = 0

    if len(oxygen_list) > 1:
        oxygen_list = list(filter(lambda x: int(x[i]) == most_common_bit_o , oxygen_list))

    if len(co2_list) > 1:
        co2_list = list(filter(lambda x: int(x[i]) != most_common_bit_c , co2_list))

    #print(oxygen_list, co2_list)

base = 1
oxygen = 0
co2 = 0

for bit in list(reversed(oxygen_list[0])):
    if bit == '1':
        oxygen += base
    base *= 2

base = 1

for bit in list(reversed(co2_list[0])):
    if bit == '1':
        co2 += base
    base *= 2

result2 = oxygen*co2
# Task 2: 2775870
print("Task 2:", result2)
