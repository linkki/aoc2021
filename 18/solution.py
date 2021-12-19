# Advent of Code Day 18
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(eval(line.strip()))

    return contents

def add_numbers(n1, n2):
    return reduce_number([n1, n2])

def reduce_number(n):
    while True:
        new_n = explode_number(n)
        if new_n is None:
            if not split_number(n):
                break
        else:
            n = new_n
    return n

def explode_number(n):
    result = find_explosive(n, 0)
    if result[0] != "":
        n_str = str(n)
        count = 0
        for i in range(len(n_str)):
            if n_str[i] == '[':
                count += 1
            if n_str[i] == ']':
                count -= 1
            if count > 4:
                break
        
        left, right = n_str[i:].split(result[0], 1)
        left = n_str[:i] + left
        to_left = ""
        i = len(left)-1
        while i >= 0:
            if left[i] in "0123456789":
                inc = left[i]
                if left[i-1] in "0123456789":
                    inc = left[i-1] + inc
                    i -= 1
                    if left[i-1] in "0123456789":
                        inc = left[i-1] + inc
                        i -= 1
                to_left = str(int(inc) + result[1][0]) + to_left
                break
            to_left = left[i] + to_left
            i -= 1
        if i >=0:
            to_left = left[:i] + to_left
        
        to_right = ""
        i = 0
        while i < len(right):
            if right[i] in "0123456789":
                inc = right[i]
                if right[i+1] in "0123456789":
                    inc += right[i+1]
                    i += 1
                    if right[i+1] in "0123456789":
                        inc += right[i+1]
                        i += 1
                to_right += str(int(inc) + result[1][1])
                break
            to_right += right[i]
            i += 1
        if i < len(right)-1:
            to_right += right[i+1:]
        return eval(to_left+ "0"+ to_right)
    return None

def find_explosive(n, depth):
    result = ("", [])
    if type(n[0]) == int and type(n[1]) == int and depth >= 4:
        return (str(n), n)
    if type(n[0]) == list:
        result = find_explosive(n[0], depth+1)
    if result[0] == "":
        if type(n[1]) == list:
            result = find_explosive(n[1], depth+1)

    return result
    
def split_number(n):
    if type(n[0]) == list:
        if split_number(n[0]):
            return True
    else:
        if n[0] > 9:
            n[0] = [n[0]//2, n[0]-n[0]//2]
            return True

    if type(n[1]) == list:
        if split_number(n[1]):
            return True
    else:
        if n[1] > 9:
            n[1] = [n[1]//2, n[1]-n[1]//2]
            return True
    return False

def find_magnitude(n) -> int:
    result = 0
    if type(n) == int:
        result += n
    else:
        result += 3*find_magnitude(n[0])
        result += 2*find_magnitude(n[1])
    return result

file_contents = read_file("input.txt")

result = file_contents[0]
for number in file_contents:
    if number is not result:
        result = add_numbers(result, number)
print(result)

result1 = find_magnitude(result)

# Task 1: 3734
print("Task 1:", result1)

magnitudes = []

for i in range(len(file_contents)):
    for j in range(len(file_contents)):
        if i != j:
            magnitudes.append(find_magnitude(add_numbers(file_contents[i], file_contents[j])))

result2 = max(magnitudes)

# Task 2: 4837
print("Task 2:", result2)
