from collections import deque


def format_input(raw):
    rows = [[int(num) for num in row] for row in raw.split("\n")]
    return rows


dirs = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (1, 0), (0, 1)]


def part1(rows, n):
    y, x = len(rows), len(rows[0])

    total = 0
    for _ in range(n):
        to_flash = deque()
        already_flashed = set()
        for i in range(y):
            for j in range(x):
                rows[i][j] += 1
                if rows[i][j] == 10:
                    rows[i][j] = 0
                    already_flashed.add((i, j))
                    to_flash.append((i, j))

        while to_flash:
            i, j = to_flash.popleft()
            total += 1
            for di, dj in dirs:
                new_i, new_j = i + di, dj + j
                if (
                    (new_i, new_j) not in already_flashed
                    and 0 <= new_i < y
                    and 0 <= new_j < x
                ):
                    rows[new_i][new_j] += 1
                    if rows[new_i][new_j] == 10:
                        rows[new_i][new_j] = 0
                        already_flashed.add((new_i, new_j))
                        to_flash.append((new_i, new_j))

    return total


def part2(rows):
    y, x = len(rows), len(rows[0])

    step = 1
    while True:
        to_flash = deque()
        already_flashed = set()
        for i in range(y):
            for j in range(x):
                rows[i][j] += 1
                if rows[i][j] == 10:
                    rows[i][j] = 0
                    already_flashed.add((i, j))
                    to_flash.append((i, j))

        flashed = 0
        while to_flash:
            i, j = to_flash.popleft()
            flashed += 1
            for di, dj in dirs:
                new_i, new_j = i + di, dj + j
                if (
                    (new_i, new_j) not in already_flashed
                    and 0 <= new_i < y
                    and 0 <= new_j < x
                ):
                    rows[new_i][new_j] += 1
                    if rows[new_i][new_j] == 10:
                        rows[new_i][new_j] = 0
                        already_flashed.add((new_i, new_j))
                        to_flash.append((new_i, new_j))

        if flashed == y * x:
            return step

        step += 1


if __name__ == "__main__":
    raw = open("data/11.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows, 100))
    rows = format_input(raw)
    print(part2(rows))
