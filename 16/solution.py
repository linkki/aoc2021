# Advent of Code Day 16
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

def convert_to_binary(hexadecimal: str) -> str:
    result = ""
    for c in hexadecimal:
        hexbin = format(int(c, 16), 'b').zfill(4)
        result += hexbin
    return result

def chop_packet(packet: str) -> tuple:
    v = int(packet[:3], 2)
    t = int(packet[3:6], 2)
    p = packet[6:]
    return (v,t,p)

def parse_literal(literal: str) -> tuple:
    result = ""
    packet_number = 0
    while True:
        result += literal[5*packet_number + 1 : 5*(packet_number+1)]
        if literal[packet_number*5] == '0':
            break

        packet_number += 1

    return ((packet_number +1)*5, int(result, 2))

def parse_operator(operator: str) -> tuple:
    if operator[0] == '0':
        length = int(operator[1:16], 2)
        return (0, length, operator[16:16+length])
    else:
        how_many = int(operator[1:12], 2)
        return (1, how_many, operator[12:])

def parse_packet(packet: str, packets: list):
    if int(packet, 2) == 0:
        return (0,len(packet))
    v,t,p = chop_packet(packet)
    version_sum = v
    packet_length = 0

    if t == 4:
        literal_length, value = parse_literal(p)
        packet_length += (6+literal_length)
        packets.append(value)
    else:
        op_type, op_l, op_p = parse_operator(p)
        result = (0,0)
        new_packets = []
        if op_type == 0:
            while packet_length < op_l:
                result = parse_packet(op_p[packet_length:], new_packets)
                version_sum += result[0]
                packet_length += result[1]
            packet_length += (6+16)
        else:
            for i in range(op_l):
                result = parse_packet(op_p[packet_length:], new_packets)
                version_sum += result[0]
                packet_length += result[1]
            packet_length += (6+12)
        packets.append((t, new_packets))

    return (version_sum, packet_length)

def product(values: list):
    result = 1
    for value in values:
        result *= value
    return result

def calculate_packet(operation: int, packets: list) -> int:
    result = []
    for packet in packets:
        if type(packet) == tuple:
            result.append(calculate_packet(packet[0], packet[1]))
        else:
            result.append(packet)
    if operation == 0:
        return sum(result)
    elif operation == 1:
        return product(result)
    elif operation == 2:
        return min(result)
    elif operation == 3:
        return max(result)
    elif operation == 4:
        return result[0]
    elif operation == 5:
        return 1 if result[0] > result[1] else 0
    elif operation == 6:
        return 1 if result[0] < result[1] else 0
    elif operation == 7:
        return 1 if result[0] == result[1] else 0

file_contents = read_file("input.txt")
packet = convert_to_binary(file_contents[0])

packets = []
result1 = parse_packet(packet, packets)

# Task 1: 871
print("Task 1:", result1[0])

result2 = calculate_packet(4, packets)

# Task 2: 68703010504
print("Task 2:", result2)
