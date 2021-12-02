def format_input(raw):
    instrs = [(instr.split(" ")[0], int(instr.split(" ")[1])) for instr in raw.split("\n")] # duplicate code but who cares
    return instrs

dirs = {
    "forward": [1, 0],
    "up": [0, -1],
    "down": [0, 1]
}

def part1(instrs):
    x, y = 0, 0
    for instr, delta in instrs:
        direction = dirs[instr]
        x += direction[0] * delta
        y += direction[1] * delta
    return x * y

def part2(instrs):
    aim = 0
    x, y = 0, 0
    for instr, delta in instrs:
        if instr == "forward":
            x += delta
            y += aim * delta
        elif instr == "up":
            aim -= delta
        elif instr == "down":
            aim += delta
    return x * y

if __name__ == "__main__":
    raw = open("data/2_part1.txt", "r").read()
    instrs = format_input(raw)
    prod = part1(instrs)
    print(prod)

    raw = open("data/2_part2.txt", "r").read()
    instrs = format_input(raw)
    prod = part2(instrs)
    print(prod)
