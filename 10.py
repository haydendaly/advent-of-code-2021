def format_input(raw):
    rows = raw.split("\n")
    return rows


def part1(rows):
    closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for row in rows:
        seen = []
        for sym in row:
            if sym not in closing:
                if not seen:
                    break
                top = seen.pop()
                if top != sym:
                    score += points[sym]
                    break
            else:
                seen.append(closing[sym])
    return score


def part2(rows):
    closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    valid = []
    for row in rows:
        seen = []
        for i, sym in enumerate(row):
            if sym not in closing:
                if not seen:
                    break
                top = seen.pop()
                if top != sym:
                    score += points[sym]
                    break
            else:
                seen.append(closing[sym])
        if i == len(row) - 1 and len(seen) > 0:
            valid.append(seen)

    prod_points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for seen in valid:
        temp_prod = 0
        for sym in reversed(seen):
            temp_prod *= 5
            temp_prod += prod_points[sym]
        scores.append(temp_prod)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    raw = open("data/10.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows))
    print(part2(rows))
