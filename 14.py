from collections import defaultdict


def format_input(raw):
    rows = raw.split("\n\n")
    base = rows[0]
    translations = defaultdict(str)
    for row in rows[1].split("\n"):
        pair = row.split(" -> ")
        translations[pair[0]] = pair[1]
    return base, translations


def part1(base, translations, n=10):
    base = list(base)
    for t in range(n):
        new_base = []
        l = len(base)
        for i in range(l):
            if i == l - 1:
                new_base.append(base[i])
                continue
            key = "".join([base[i], base[i + 1]])
            new_base.append(base[i])
            if translations[key] != "":
                new_base.append(translations[key])
        base = new_base

    count = defaultdict(int)
    for char in base:
        count[char] += 1
    return get_common(count)


def get_common(count):
    min_freq, max_freq = float("inf"), -float("inf")
    for freq in count.values():
        if freq > max_freq:
            max_freq = freq
        if freq < min_freq:
            min_freq = freq
    return max_freq - min_freq


def part2(base, translations, n=40):
    pairs = defaultdict(int)
    base = list(base)
    for i in range(len(base) - 1):
        key = "".join([base[i], base[i + 1]])
        pairs[key] += 1

    for _ in range(n):
        new_pairs = defaultdict(int)
        for pair, freq in pairs.items():
            trans = translations[pair]
            if trans != "":
                first, second = "".join([pair[0], trans]), "".join([trans, pair[1]])
                new_pairs[first] += freq
                new_pairs[second] += freq
            else:
                new_pairs[pair] += freq
        pairs = new_pairs

    count = defaultdict(int)
    for pair, freq in pairs.items():
        count[pair[0]] += freq
    return get_common(count) + 1


if __name__ == "__main__":
    raw = open("data/14.txt", "r").read()
    base, translations = format_input(raw)
    print(part1(base, translations, 10))
    print(part2(base, translations, 40))
