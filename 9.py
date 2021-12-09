from heapq import heappush, heappushpop
from math import prod


def format_input(raw):
    grid = [[int(num) for num in list(row)] for row in raw.split("\n")]
    return grid


def get_neighbors(grid, i, j):
    y, x = len(grid), len(grid[0])
    neighbors = []
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in dirs:
        if 0 <= i + di < y and 0 <= j + dj < x:
            neighbors.append((i + di, j + dj))
    return neighbors


def get_low_points(grid):
    y, x = len(grid), len(grid[0])
    mins = []
    for i in range(y):
        for j in range(x):
            is_min = True
            for new_i, new_j in get_neighbors(grid, i, j):
                if grid[new_i][new_j] <= grid[i][j]:
                    is_min = False
                    break
            if is_min:
                mins.append((i, j))
    return mins


def part1(grid):
    mins = get_low_points(grid)
    return sum(grid[i][j] for i, j in mins) + len(mins)


def part2(grid):
    basins = []
    low_points = get_low_points(grid)
    for low_i, low_j in low_points:
        neighbors = get_neighbors(grid, low_i, low_j)
        seen = set(neighbors)
        size = 1
        while neighbors:
            i, j = neighbors.pop()
            size += 1
            for new_i, new_j in get_neighbors(grid, i, j):
                if grid[i][j] < grid[new_i][new_j] < 9 and (new_i, new_j) not in seen:
                    neighbors.append((new_i, new_j))
                    seen.add((new_i, new_j))
        if len(basins) < 3:
            heappush(basins, size)
        else:
            heappushpop(basins, size)
    return prod(basins)


if __name__ == "__main__":
    raw = open("data/9.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows))
    print(part2(rows))
