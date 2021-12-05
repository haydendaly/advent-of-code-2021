def format_input(raw):
    str_points = [row.split(" -> ") for row in raw.split("\n")]
    point_pairs = [
        (
            (int(pair[0].split(",")[0]), int(pair[0].split(",")[1])),
            (int(pair[1].split(",")[0]), int(pair[1].split(",")[1])),
        )
        for pair in str_points
    ]
    return point_pairs


def part1(point_pairs, max_x=10, max_y=10):
    canvas = [[0] * max_x for _ in range(max_y)]
    for pair in point_pairs:
        x1, x2 = pair[0][0], pair[1][0]
        y1, y2 = pair[0][1], pair[1][1]
        # if horizontal or vertical
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                canvas[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                canvas[y1][j] += 1

    intersections = 0
    for row in canvas:
        for num in row:
            if num >= 2:
                intersections += 1
    return intersections


def part2(point_pairs, max_x=10, max_y=10):
    canvas = [[0] * max_x for _ in range(max_y)]
    for pair in point_pairs:
        x1, x2 = pair[0][0], pair[1][0]
        y1, y2 = pair[0][1], pair[1][1]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                canvas[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                canvas[y1][j] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            i = y1
            del_i = (y2 - y1) / abs(y2 - y1)
            del_j = 1 if x2 > x1 else -1
            for j in range(x1, x2 + del_j, del_j):
                canvas[int(i)][j] += 1
                i += del_i

    intersections = 0
    for row in canvas:
        for num in row:
            if num >= 2:
                intersections += 1
    return intersections
    return rows


if __name__ == "__main__":
    raw = open("data/5.txt", "r").read()
    point_pairs = format_input(raw)
    print(part1(point_pairs, 1000, 1000))

    print(part2(point_pairs, 1000, 1000))
