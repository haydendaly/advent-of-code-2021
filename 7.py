def format_input(raw):
    crabs = [int(crab) for crab in raw.split(",")]
    return crabs


def part1(crabs):
    min_fuel = float("inf")
    for mid in range(min(crabs), max(crabs)):
        fuel = 0
        for crab in crabs:
            fuel += abs(mid - crab)
        min_fuel = min(min_fuel, fuel)
    return min_fuel


def get_sum_of_inc_seq(mid, crab):
    l = abs(mid - crab)
    return l * (l + 1) // 2


def part2(crabs):
    min_fuel = float("inf")
    for mid in range(min(crabs), max(crabs)):
        fuel = 0
        for crab in crabs:
            fuel += get_sum_of_inc_seq(mid, crab)
        min_fuel = min(min_fuel, fuel)
    return min_fuel


if __name__ == "__main__":
    raw = open("data/7.txt", "r").read()
    crabs = format_input(raw)
    print(part1(crabs))
    print(part2(crabs))
