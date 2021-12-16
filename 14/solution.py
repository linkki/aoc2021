# Advent of Code Day 14
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    chars = {}
    template = {}
    rules = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(" -> ")
            if len(parts) == 1:
                for i in range(len(parts[0])):
                    if i < len(parts[0])-1:
                        key = "".join([parts[0][i], parts[0][i+1]])
                        if key not in template.keys():
                            template[key] = 0
                        template[key] += 1
                        
            elif len(parts) == 2:
                chars[parts[0][0]] = 0
                chars[parts[0][1]] = 0
                if parts[0] not in template.keys():
                    template[parts[0]] = 0
                beg = parts[0][0]
                end = parts[0][1]
                rules[parts[0]] = [beg + parts[1], parts[1] + end]

    return (chars, template, rules)

chars, template, rules = read_file("input.txt")
#print(template, "\n\n", rules, "\n\n", chars)

for i in range(40):
    new_template = {}
    for key in template.keys():
        new_template[key] = 0
    for pair in template:
        if template[pair] > 0:
            original = template[pair]
            for result in rules[pair]:
                new_template[result] += original
    template = new_template
    if i == 9: # for part 1
        first_template = new_template

for pair in first_template.keys():
    chars[pair[0]] += first_template[pair]
    chars[pair[1]] += first_template[pair]

for char in chars.keys():
    if chars[char] %2 == 0:
        chars[char] //= 2
    else:
        chars[char] = (chars[char] + 1) //2

result1 = max(chars.values()) - min(chars.values())

for char in chars.keys():
    chars[char] = 0

for pair in template.keys():
    chars[pair[0]] += template[pair]
    chars[pair[1]] += template[pair]

for char in chars.keys():
    if chars[char] %2 == 0:
        chars[char] //= 2
    else:
        chars[char] = (chars[char] + 1) //2

result2 = max(chars.values()) - min(chars.values())

# Task 1: 2068
print("Task 1:", result1)

# Task 2: 
print("Task 2:", result2)
