def format_input(raw):
    lines = list(map(int, raw.split("\n")))
    return lines

def part1(depths):
    prev = float("inf")
    diffs = 0
    for depth in depths:
        if depth > prev:
            diffs += 1
        prev = depth
    return diffs

def part2(depths):
    start = 0
    prev = float('inf')
    curr = depths[0] + depths[1]
    diffs = 0

    for end in range(2, len(depths)):
        curr += depths[end]
        if curr > prev:
            diffs += 1
        prev = curr
        curr -= depths[start]
        start += 1
    
    return diffs

if __name__ == "__main__":
    raw = open("data/1_part1.txt", "r").read()
    depths = format_input(raw)
    print(part1(depths))

    raw = open("data/1_part2.txt", "r").read()
    depths = format_input(raw)
    print(part2(depths))
