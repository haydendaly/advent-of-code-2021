from networkx import DiGraph, shortest_path_length


def format_input(raw):
    rows = raw.split("\n")
    grid = {
        (i, j): int(char) for i, row in enumerate(rows) for j, char in enumerate(row)
    }
    y, x = len(rows), len(rows[0])
    return grid, y, x


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# naive -> thought problem was initially only down and right
# def part1_naive(grid):
#     @lru_cache(maxsize=None)
#     def dfs(i, j):
#         y, x = len(grid), len(grid[0])
#         if i == y - 1 and j == x - 1:
#             return 0
#         smallest = float("inf")
#         for di, dj in dirs:
#             new_i, new_j = i + di, j + dj
#             if new_i < y and new_j < x:
#                 smallest = min(smallest, dfs(new_i, new_j) + int(grid[new_i][new_j]))
#         return smallest

#     return dfs(0, 0)


def shortest(graph, y, x):
    return shortest_path_length(graph, (0, 0), (y - 1, x - 1), weight="weight")


def part1(grid, y, x):
    graph = DiGraph()
    for i, j in grid.keys():
        for di, dj in dirs:
            new_i, new_j = i + di, j + dj
            if (new_i, new_j) in grid.keys():
                weight = grid[new_i, new_j]
                graph.add_edge((i, j), (new_i, new_j), weight=weight)
    return shortest(graph, y, x)


def part2(grid, y, x):
    graph = DiGraph()
    for i in range(5 * y):
        for j in range(5 * x):
            weight = (grid[i % y, j % x] - 1 + (i // y) + (j // x)) % 9 + 1
            for di, dj in dirs:
                if 0 <= i + di < 5 * y and 0 <= j + dj < 5 * x:
                    graph.add_edge((i + di, j + dj), (i, j), weight=weight)
    return shortest(graph, 5 * y, 5 * x)


if __name__ == "__main__":
    raw = open("data/15.txt", "r").read()
    grid, y, x = format_input(raw)
    print(part1(grid, y, x))
    print(part2(grid, y, x))
