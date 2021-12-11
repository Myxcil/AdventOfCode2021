from colors import *


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def print_map(map_2d: [[int]], low_points: set[tuple[int, int]]):
    for y in range(len(map_2d)):
        for x in range(len(map_2d[y])):
            if (x, y) in low_points:
                print(f'{Colors.WARNING}{map_2d[y][x]}{Colors.END}', end='')
            else:
                print(map_2d[y][x], end='')
            print(' ', end='')
        print()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def print_map_basins(map_2d: [[int]], basin_array: [[bool]]):
    for y in range(len(map_2d)):
        for x in range(len(map_2d[y])):
            if basin_array[y][x]:
                print(f'{Colors.WARNING}{map_2d[y][x]}{Colors.END}', end='')
            else:
                print(map_2d[y][x], end='')
            print(' ', end='')
        print()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_low_point(map_2d: [[int]], x: int, y: int) -> bool:
    height_xy = map_2d[y][x]
    if x > 0 and map_2d[y][x-1] <= height_xy:
        return False
    if x < len(map_2d[y])-1 and map_2d[y][x+1] <= height_xy:
        return False
    if y > 0 and map_2d[y-1][x] <= height_xy:
        return False
    if y < len(map_2d)-1 and map_2d[y+1][x] <= height_xy:
        return False
    return True


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_lowest_points(map_2d: [[int]]) -> set[tuple[int, int]]:
    lowest: set[tuple[int, int]] = set()
    for y in range(len(map_2d)):
        for x in range(len(map_2d[y])):
            if is_low_point(map_2d, x, y):
                lowest.add((x, y))
    return lowest


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def assess_risk_level(map_2d: [[int]]) -> int:
    risk_level = 0
    for y in range(len(map_2d)):
        for x in range(len(map_2d[y])):
            if is_low_point(map_2d, x, y):
                risk_level += 1 + map_2d[y][x]
    return risk_level


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_basins(map_2d: [[int]], low_points: set[tuple[int, int]]) -> tuple[[[tuple[int, int]]], [[bool]]]:
    basin_array: [[bool]] = [[False for _ in y] for y in map_2d]
    basins: [[tuple[int, int]]] = []
    for x, y in low_points:
        basin: [tuple[int, int]] = []
        extract_basin(x, y, map_2d, basin_array, basin)
        basins.append(basin)
    return basins, basin_array


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def extract_basin(x: int, y: int, map_2d: [[int]], basin_array: [[bool]], basin: [tuple[int, int]]):
    if basin_array[y][x]:
        return

    if map_2d[y][x] == 9:
        return

    basin.append((x, y))
    basin_array[y][x] = True

    if y > 0 and map_2d[y-1][x] != 9:
        extract_basin(x, y-1, map_2d, basin_array, basin)
    if y < len(map_2d)-1 and map_2d[y+1][x] != 9:
        extract_basin(x, y+1, map_2d, basin_array, basin)
    if x > 0 and map_2d[y][x-1] != 9:
        extract_basin(x-1, y, map_2d, basin_array, basin)
    if x < len(map_2d[y])-1 and map_2d[y][x+1] != 9:
        extract_basin(x+1, y, map_2d, basin_array, basin)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day9_input.txt", "r") as file:
    height_map: [[int]] = []
    for line in file.readlines():
        height_map.append([int(x) for x in line.strip()])

lowest_points = find_lowest_points(height_map)
# print_map(height_map, lowest_points)
print(f'#1 risk-level: {assess_risk_level(height_map)}')

basin_list, basin_flag = find_basins(height_map, lowest_points)
# print_map_basins(height_map, basin_flag)
basin_list.sort(key=len, reverse=True)
print(f'#2 total-size: {len(basin_list[0]) * len(basin_list[1]) * len(basin_list[2])}')
