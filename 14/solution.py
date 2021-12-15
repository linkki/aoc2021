# Advent of Code Day 14
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    template = []
    rules = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(" -> ")
            if len(parts) == 1:
                for c in parts[0]:
                    template.append(c)
            elif len(parts) == 2:
                rules[parts[0]] = parts[1]

    return (template, rules)

template, rules = read_file("input.txt")

from collections import Counter

for i in range(10):
    counter = 0
    for n in range(len(template) - 1):
        key = "".join(template[n+counter:n+counter+2])
        if key in rules:
            template.insert(n+1+counter, rules[key])
            counter += 1
    print(len(template), Counter(template))


c = Counter(template)

result1 = c.most_common()[0][1] - c.most_common()[len(c)-1][1]

# Task 1: 2068
print("Task 1:", result1)


result2 = 0

# Task 2: 
print("Task 2:", result2)
