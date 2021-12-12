from collections import defaultdict


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def path_count(graph, node, visited=set(), twice=False):
    if node == 'end':
        return 1

    count = 0
    new_visited = visited | {node} if node.islower() else visited
    for to in graph[node]:
        if to == 'start':
            continue

        if to in visited:
            if twice:
                continue
            count += path_count(graph, to, new_visited, True)
        else:
            count += path_count(graph, to, new_visited, twice)
    return count


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day12_input.txt", "r") as file:
    caves = defaultdict(list)
    for line in file.readlines():
        cave1, cave2 = line.strip().split('-')
        caves[cave1].append(cave2)
        caves[cave2].append(cave1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
print(path_count(caves, "start", twice=True))
print(path_count(caves, "start"))
