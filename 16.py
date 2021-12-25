from math import prod


OPS = [
    sum,
    prod,
    min,
    max,
    None,
    lambda x: int(x[0] > x[1]),
    lambda x: int(x[0] < x[1]),
    lambda x: int(x[0] == x[1]),
]


def format_input(raw):
    b = bin(int(raw, 16))[2:]
    return "0" * ((4 - len(b) % 4) % 4) + b


def get_header(data):
    return int(data[:3], 2), int(data[3:6], 2)


def get_literal(packet, count):
    nums = [
        packet[i + 6 : i + 11]
        for i in range(0, len(packet) - 6, 5)
        if len(packet[i + 6 : i + 11]) == 5
    ]
    literal = ""
    for i, num in enumerate(nums):
        literal += num[1:]
        if num[0] == "0":
            if len(nums) != i + 1:
                get_packet(packet[6 + (i + 1) * 5 :], count)
            break


def get_operator(packet, count):
    packet_size = 15 if packet[6] == "0" else 11
    l = int(packet[7 : 7 + packet_size], 2)
    if packet[6] == "0":
        get_packet(packet[7 + packet_size : 7 + packet_size + l], count)
        get_packet(packet[7 + packet_size + l :], count)
    else:
        get_packet(packet[7 + packet_size :], count)


def get_packet(packet, count):
    if packet == "0" * len(packet):
        return
    packet_version, type_id = get_header(packet)
    count[0] += packet_version
    if type_id == 4:
        get_literal(packet, count)
    else:
        get_operator(packet, count)


def get_literal2(packet):
    literal = ""
    for i in range(6, len(packet), 5):
        literal += packet[i + 1 : i + 5]
        if packet[i] == "0":
            break
    return int(literal, 2), i + 5


def get_operator2(packet):
    nums = []
    i = 18
    if packet[6] == "0":
        l = int(packet[7:22], 2)
        i = 22
        while i < l + 22:
            result, l_sub = get_packet2(packet[i:])
            i += l_sub
            nums.append(result)
    else:
        num_sub_packets = int(packet[7:18], 2)
        for _ in range(num_sub_packets):
            result, l_sub = get_packet2(packet[i:])
            i += l_sub
            nums.append(result)
    return nums, i


def get_packet2(packet):
    _, id = get_header(packet)
    if id == 4:
        return get_literal2(packet)
    nums, bit_index = get_operator2(packet)
    result = 0
    if 0 <= id <= 7:
        result = OPS[id](nums)
    return result, bit_index


def part1(data):
    count = [0]
    get_packet(data, count)
    return count[0]


def part2(data):
    result, _ = get_packet2(data)
    return result


if __name__ == "__main__":
    raw = open("data/16.txt", "r").read()
    data = format_input(raw)
    print(part1(data))
    print(part2(data))
