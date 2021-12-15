import math
from colors import Colors


def get_node_cost(x: int, y: int, map2d: [[int]]) -> int:
    add_x = int(x / len(map2d[0]))
    add_y = int(y / len(map2d))
    x = x % len(map2d[0])
    y = y % len(map2d)
    map_value = map2d[y][x] + add_x + add_y
    if map_value > 9:
        map_value -= 9
    return map_value


def print_map(map2d_):
    for y in range(len(map2d_)):
        for x in range(len(map2d_[0])):
            print(map2d_[y][x], end='')
        print()
    print()


def print_map_and_path(map2d_, path: [tuple[int, int]], scale: int):
    for y in range(scale * len(map2d_)):
        for x in range(scale * len(map2d_[0])):
            c = get_node_cost(x, y, map2d_)
            if (x,y) in path:
                print(f'{Colors.BLUE}{c}{Colors.END}', end='')
            else:
                print(c, end='')
        print()
    print()


class Node:
    def __init__(self, parent, x, y, cost):
        self.parent = parent
        self.x = x
        self.y = y
        self.cost = cost
        self.cost_from_start = 0
        self.estimated_cost = 0
        self.total_cost = 0

    def __str__(self):
        return f'{self.total_cost}'

    def __repr__(self):
        return str(self)


def estimate_cost(start: tuple[int, int], end: tuple[int, int]) -> float:
    diff_x = end[0] - start[0]
    diff_y = end[1] - start[1]
    return math.sqrt(diff_x*diff_x + diff_y*diff_y)


def find_path(map2d: [[int]], start: tuple[int, int], end: tuple[int, int], scale: int = 1) -> tuple[[tuple[int, int]], [int]]:
    node = Node(None, start[0], start[1], map2d[start[1]][start[0]])
    node.estimated_cost = estimate_cost(start, end)
    node.cost_from_start = 0
    node.total_cost = node.cost_from_start + node.estimated_cost

    nodes: dict[tuple[int, int], Node] = dict()
    nodes[start] = node

    open_stack: [tuple[int, int]] = [start]
    closed_set: [tuple[int, int]] = set()

    width = len(map2d[0]) * scale
    height = len(map2d) * scale

    while len(open_stack) > 0:
        open_stack.sort(key=lambda x: nodes[x].total_cost)
        node = nodes[open_stack.pop(0)]

        if node.x == end[0] and node.y == end[1]:
            new_path: list[tuple[int, int]] = list()
            path_cost: list[int] = list()
            while node.parent is not None:
                new_path.append((node.x, node.y))
                path_cost.append(node.cost)
                node = node.parent
            new_path.reverse()
            path_cost.reverse()
            return new_path, path_cost

        def check_neighbor(dx: int, dy: int):
            if dy < 0 or dy >= width or dx < 0 or dx >= height:
                return

            if (dx, dy) in closed_set:
                return

            closed_set.add((dx, dy))

            next_cost = node.cost_from_start + get_node_cost(dx, dy, map2d)
            if (dx, dy) in open_stack and next_cost >= nodes[(dx, dy)].cost_from_start:
                return

            if not (dx, dy) in open_stack:
                next_node = Node(node, dx, dy, get_node_cost(dx, dy, map2d))
                next_node.cost_from_start = next_cost
                next_node.estimated_cost = estimate_cost((dx, dy), end)
                nodes[dx, dy] = next_node
                open_stack.append((dx, dy))
            else:
                open_stack[dx, dy].cost_from_start = next_cost

            next_node.total_cost = next_node.cost_from_start + next_node.estimated_cost

        check_neighbor(node.x - 1, node.y)
        check_neighbor(node.x + 1, node.y)
        check_neighbor(node.x, node.y - 1)
        check_neighbor(node.x, node.y + 1)


with open("day15_input.txt", "r") as file:
    cavern_map: [[int]] = [[int(x) for x in line.strip()] for line in file.readlines()]

scale = 5
end_x = (scale * len(cavern_map[0]))-1
end_y = (scale * len(cavern_map))-1

path, cost = find_path(cavern_map, (0, 0), (end_x, end_y), scale)
# print(cost)
print(sum(cost))
# print_map_and_path(cavern_map, path, scale)
