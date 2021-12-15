# Advent of Code Day 12
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = {}
    with open(filename) as file:
        for line in file:
            beg, end = line.strip().split('-')
            if beg not in contents:
                contents[beg] = []
            if end != "start" and beg != "end":
                contents[beg].append(end)
            if end not in contents:
                contents[end] = []
            if end != "end" and beg != "start":
                contents[end].append(beg)

    return contents

def find_path(current : str, path_so_far : list) -> list:
    paths = []
    current_path = path_so_far.copy()
    if not (current.islower() and current in current_path):
        #print(current, path_so_far)
        current_path.append(current)
        if current == "end":
            paths.append(current_path)
        else:
            for destination in file_contents[current]:
                paths += find_path(destination, current_path)

    return paths

def find_path2(current : str, path_so_far : list, cheat : str) -> list:
    paths = []
    current_path = path_so_far.copy()
    if not (current.islower() and current in current_path):
        current_path.append(current)
        if current == "end":
            paths.append(current_path)
        else:
            if cheat == "":
                # use cheat
                if current.islower():
                    for destination in file_contents[current]:
                        paths += find_path2(destination, current_path, current)    
                # don't use cheat
                for destination in file_contents[current]:
                    paths += find_path2(destination, current_path, "")
            else: # continue as usual
                for destination in file_contents[current]:
                    paths += find_path2(destination, current_path, cheat)
    elif current == cheat: # revisiting the one cave chosen for the cheat
        current_path.append(current)
        for destination in file_contents[current]:
            paths += find_path2(destination, current_path, "USED")

    return paths


file_contents = read_file("input.txt")
result1 = 0
result2 = 0

# for debugging:
#for cave in file_contents:
#    print(cave, file_contents[cave])

for path in find_path("start", []):
    #print(path)
    result1 += 1

# Task 1: 3298
print("Task 1:", result1)

path_set = set() # each member in a set is unique

for path in find_path2("start", [], ""):
    # make a string from the list so the results can be added to the set 
    path_set.add(','.join(path)) 

result2 = len(path_set)

# Task 2: 93572
print("Task 2:", result2)
