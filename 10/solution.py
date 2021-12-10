# Advent of Code Day 10
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

def check_last_opener(c, l):
    if l == '(':
        matching = ')'
    elif l == '[':
        matching = ']'
    elif l == '{':
        matching = '}'
    elif l == '<':
        matching = '>'
    
    if c == matching:
        return True
    else:
        return False

def calculate_closing_score(charlist: list):
    score = 0
    for c in reversed(charlist):
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
    return score


file_contents = read_file("input.txt")

result1 = 0
result2 = 0
closing_scores = []

for line in file_contents:
    openers = []
    wrong_char = 'N'
    for c in line:
        if c in "([{<":
            openers.append(c)
        else:
            if check_last_opener(c, openers[-1]): # closing char matches
                openers.pop()
            else: # corrupted line
                wrong_char = c
                break

    if wrong_char == ')':
        result1 += 3
    elif wrong_char == ']':
        result1 += 57
    elif wrong_char == '}':
        result1 += 1197
    elif wrong_char == '>':
        result1 += 25137
    else: # line not corrupted, so must be incomplete line
        closing_scores.append(calculate_closing_score(openers))

# Task 1: 339537
print("Task 1:", result1)

# find the closing score in the middle of the list
result2 = sorted(closing_scores)[len(closing_scores)//2]

# Task 2: 2412013412
print("Task 2:", result2)
