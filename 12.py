from collections import defaultdict


def format_input(raw):
    adj_list = [row.split("-") for row in raw.split("\n")]
    return adj_list


def dfs(node, neighbors, seen, small):
    if node.islower():
        seen.add(node)
    num_paths = 0
    if len(seen) >= 2 and node == "end":
        num_paths = 1
    else:
        for neigh in neighbors[node]:
            if neigh not in seen:
                num_paths += dfs(neigh, neighbors, seen, small)
    if node.islower():
        seen.remove(node)
    return num_paths


def part1(adj_list):
    neighbors = defaultdict(set)
    small_nodes = set()
    for in_node, out_node in adj_list:
        neighbors[in_node].add(out_node)
        neighbors[out_node].add(in_node)
        if in_node.islower():
            small_nodes.add(in_node)
        if out_node.islower():
            small_nodes.add(out_node)
    seen = set()
    return dfs("start", neighbors, seen, len(small_nodes))


def dfs2(node, neighbors, seen, has_double=False):
    local_double = False
    if node.islower():
        if node in seen and (node == "start" or node == "end" or has_double):
            return 0
        elif node in seen and not has_double:
            has_double = True
            local_double = True
        seen.add(node)
    num_paths = 0
    if node == "end":
        num_paths = 1 if len(seen) >= 2 else 0
    else:
        for neigh in neighbors[node]:
            if neigh not in seen or not has_double:
                num_paths += dfs2(neigh, neighbors, seen, has_double)
    if node.islower() and not local_double:
        seen.remove(node)
    return num_paths


def part2(adj_list):
    neighbors = defaultdict(set)
    for in_node, out_node in adj_list:
        neighbors[in_node].add(out_node)
        neighbors[out_node].add(in_node)
    seen = set()
    return dfs2("start", neighbors, seen)


if __name__ == "__main__":
    raw = open("data/12.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows))
    print(part2(rows))
