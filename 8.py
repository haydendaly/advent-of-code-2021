def format_input(raw):
    pairs = [
        (row.split(" | ")[0].split(" "), row.split(" | ")[1].split(" "))
        for row in raw.split("\n")
    ]
    return pairs


class Decoder(object):
    def __init__(self, codec):
        num_mapping = dict()
        easy = {2: 1, 3: 7, 4: 4, 7: 8}

        for c in codec:
            if len(c) in easy:
                c_str = "".join(sorted(c))
                num_mapping[easy[len(c)]] = c_str

        for c in codec:
            if len(c) == 6:
                c_set = set(c)
                c_str = "".join(sorted(c))
                if c_set.issuperset(set(num_mapping[4])):
                    num_mapping[9] = c_str
                elif c_set.issuperset(set(num_mapping[1])):
                    num_mapping[0] = c_str
                else:
                    num_mapping[6] = c_str

        for c in codec:
            if len(c) == 5:
                c_set = set(c)
                c_str = "".join(sorted(c))
                if c_set.issuperset(set(num_mapping[1])):
                    num_mapping[3] = c_str
                elif c_set.issubset(set(num_mapping[6])):
                    num_mapping[5] = c_str
                else:
                    num_mapping[2] = c_str

        self.inv_mapping = {value: key for key, value in num_mapping.items()}

    def decode(self, code):
        result = int("".join([str(self.inv_mapping["".join(sorted(c))]) for c in code]))
        return result


def part1(pairs):
    count = 0
    for codec, code in pairs:
        for num in code:
            if len(num) in (2, 3, 4, 7):
                count += 1
    return count


def part2(rows):
    total = 0
    for codec, code in pairs:
        total += Decoder(codec).decode(code)
    return total


if __name__ == "__main__":
    raw = open("data/8.txt", "r").read()
    pairs = format_input(raw)
    print(part1(pairs))
    print(part2(pairs))
