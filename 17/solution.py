# Advent of Code Day 17
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            ranges = line.strip().split("x=")[1].split(", y=")
            for r in ranges:
                range_str = r.split("..")
                contents.append((int(range_str[0]), int(range_str[1])))

    return contents

def find_x(beg, end):
    steps = []
    velocity = end
    while velocity > 0:
        counter = velocity
        step = 1
        x = counter
        valid_steps = []
        while True:
            if is_valid(x, beg, end):
                valid_steps.append(step)
            counter -= 1
            x += counter
            step += 1
            if x > end:
                break
            if counter == 0:
                if len(valid_steps) != 0:
                    valid_steps.append(0)
                break
        if len(valid_steps) != 0:
            steps.append((velocity, valid_steps))
        velocity -= 1

    return steps

def find_y(steps, beg, end):
    velocities = []
    velocity = beg
    while velocity < abs(beg):
        counter = velocity
        y = 0
        for i in range(steps):
            y += counter
            counter -= 1
        if is_valid(y, beg, end):
            velocities.append(velocity)
        velocity += 1
    if len(velocities) == 0:
        return (beg-1, [])
    return (max(velocities), velocities)

def is_valid(value, beg, end):
    return (value >= beg and value <= end)

def cumulative_sum(value):
    result = 0
    for i in range(value+1):
        result += i
    return result

def best(bx, by, nx, ny):
    if ny > by:
        return (nx, ny)
    else:
        return (bx, by)

ranges = read_file("input.txt")

x_values = find_x(ranges[0][0], ranges[0][1])

best_x = ranges[0][1]
best_y = ranges[1][0]

pair_count = 0

for val in x_values:
    y_velocities = set() # use a set to get unique values
    for step in val[1]:
        if step == 0:
            for i in range(val[1][-2] +1, 400): # no real reason why 400 here, just a big enough number
                y_max, velocities = find_y(i, ranges[1][0], ranges[1][1])
                best_x, best_y = best(best_x, best_y, val[0], y_max)
                for vel in velocities:
                    y_velocities.add(vel)

        else:
            y_max, velocities = find_y(step, ranges[1][0], ranges[1][1])
            best_x, best_y = best(best_x, best_y, val[0], y_max)
            for vel in velocities:
                y_velocities.add(vel)

    pair_count += len(y_velocities)

result1 = cumulative_sum(best_y)

# Task 1: 14535
print("Task 1:", result1)

result2 = pair_count

# Task 2: 2270
print("Task 2:", result2)
