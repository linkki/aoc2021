# Advent of Code Day 11
# Science Lab Linkki, Virpi Sumu

import octopus

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

def print_octopuses(octopuses):
    for line in octopuses:
        for octo in line:
            print(octo.energy, end="")
        print()
    print()

file_contents = read_file("input.txt")
result1 = -1
result2 = -1

octopuses = []

for j in range(10):
    octoline = []
    for i in range(10):
        energy = int(file_contents[j][i])
        octoline.append(octopus.Octopus(energy, i, j))
    octopuses.append(octoline)

#print_octopuses(octopuses)

how_many_steps = 1000

for k in range(how_many_steps):
    #print(k+1)
    for j in range(10):
        for i in range(10):
            octopuses[j][i].increase_energy(octopuses)
    
    if octopus.Octopus.flashes_this_round == 100 and result2 == -1:
        result2 = k + 1
    
    for j in range(10):
        for i in range(10):
            octopuses[j][i].new_step()

    if k == 99:
        result1 = octopus.Octopus.flashes

    #print_octopuses(octopuses)



# Task 1: 1735
print("Task 1:", result1)

# Task 2: 400
print("Task 2:", result2)
