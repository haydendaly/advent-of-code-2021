def format_input(raw):
    rows = raw.split("\n")
    return rows

def part1(rows):
    gamma, epsilon = 0, 0
    totals = [0] * len(rows[0])
    for row in rows:
        for i, num in enumerate(row):
            if row[i] == "1":
                totals[i] += 1
    half = len(rows) // 2
    i = 1
    for num in reversed(totals):
        if num > half:
            gamma += i
        else:
            epsilon += i
        i *= 2
    return gamma * epsilon

def most_common_bit(rows, i):
    half = len(rows) / 2
    ones = 0
    for row in rows:
        if row[i] == "1":
            ones += 1
    return 1 if ones >= half else 0

def part2(rows):
    least, most = rows.copy(), rows.copy()
    for i in range(len(rows[0])):
        least_bit = abs(most_common_bit(least, i) - 1)
        most_bit = most_common_bit(most, i)
        new_least, new_most = [], []
        for row in least:
            if int(row[i]) == least_bit:
                new_least.append(row)
        for row in most:
            if int(row[i]) == most_bit:
                new_most.append(row)
        if len(new_least) >= 1:
            least = new_least
        if len(new_most) >= 1:
            most = new_most

    oxygen_generator_rating = int(most[0], 2)
    co2_scrubber_rating = int(least[0], 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating

if __name__ == "__main__":
    raw = open("data/3_part1.txt", "r").read()
    rows = format_input(raw)
    prod = part1(rows)
    print(prod)

    raw = open("data/3_part2.txt", "r").read()
    rows = format_input(raw)
    rating = part2(rows)
    print(rating)
