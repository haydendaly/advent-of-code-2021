def format_input(raw):
    return [[int(c) for c in p[2:].split("..")] for p in raw.split(": ")[1].split(", ")]


def simulate(i_range, j_range, di, dj):
    i_min, i_max = min(i_range), max(i_range)
    j_min, j_max = min(j_range), max(j_range)
    i, j, h_max = 0, 0, -float("inf")
    for _ in range(500):
        i, j = i + di, j + dj
        h_max = max(h_max, j)
        if i_min <= i <= i_max and j_min <= j <= j_max:
            return h_max
        elif (
            (dj < 0 and j < j_min)
            or (di > 0 and i > i_max)
            or (di == 0 and (i < i_min or i > i_max))
        ):
            return -float("inf")
        elif di != 0:
            di = (di - 1) if di > 0 else (di + 1)
        dj -= 1
    return -float("inf")


def part1(i_range, j_range):
    h_max = -float("inf")
    for di in range(150):
        for dj in range(-150, 500):
            h_max = max(h_max, simulate(i_range, j_range, di, dj))
    return h_max


def part2(i_range, j_range):
    count = 0
    for di in range(150):
        for dj in range(-150, 500):
            h = simulate(i_range, j_range, di, dj)
            if h != -float("inf"):
                count += 1
    return count


if __name__ == "__main__":
    raw = open("data/17.txt", "r").read()
    r = format_input(raw)
    print(part1(*r))
    print(part2(*r))
