def format_input(raw):
    fish = [int(f) for f in raw.split(",")]
    return fish


# naive solution
def part1(fish, days):
    for _ in range(days):
        new_fish = []
        for f in fish:
            if f == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(f - 1)
        fish = new_fish
    return len(fish)


# performant solution
def part2(fish, days):
    fish_idx = [0] * 9
    for f in fish:
        fish_idx[f] += 1
    for _ in range(days):
        new_fish_idx = [0] * 9
        for i, f in enumerate(fish_idx):
            if i == 0:
                new_fish_idx[8] += f
                new_fish_idx[6] += f
            else:
                new_fish_idx[i - 1] += f
        fish_idx = new_fish_idx
    return sum(fish_idx)


if __name__ == "__main__":
    raw = open("data/6.txt", "r").read()
    fish = format_input(raw)
    print(part1(fish, 80))

    fish = format_input(raw)
    print(part2(fish, 256))
