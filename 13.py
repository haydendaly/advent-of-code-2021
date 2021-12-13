def format_input(raw):
    all_rows = raw.split("\n\n")
    points = [
        (int(row.split(",")[0]), int(row.split(",")[1]))
        for row in all_rows[0].split("\n")
    ]
    folds = [
        (row.split("=")[0][-1], int(row.split("=")[1]))
        for row in all_rows[1].split("\n")
    ]
    return points, folds


def part1(points, folds):
    new_points = set()
    fold_axis, fold_point = folds[0]
    for x, y in points:
        if fold_axis == "x":
            if x > fold_point:
                new_points.add((2 * fold_point - x, y))
            else:
                new_points.add((x, y))
        else:
            if y > fold_point:
                new_points.add((x, 2 * fold_point - y))
            else:
                new_points.add((x, y))
    return len(new_points)


def part2(points, folds):
    for fold_axis, fold_point in folds:
        new_points = set()
        for x, y in points:
            if fold_axis == "x":
                if x > fold_point:
                    new_points.add((2 * fold_point - x, y))
                else:
                    new_points.add((x, y))
            else:
                if y > fold_point:
                    new_points.add((x, 2 * fold_point - y))
                else:
                    new_points.add((x, y))
        points = new_points

    # print letters
    grid = [[" "] * 40 for _ in range(6)]
    for x, y in points:
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    raw = open("data/13.txt", "r").read()
    points, folds = format_input(raw)
    print(part1(points, folds))
    part2(points, folds)
