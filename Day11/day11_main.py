import copy

from colors import *


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def print_octopus_map(map_: [[int]]):
    for y in range(len(map_)):
        for x in range(len(map_[y])):
            if map_[y][x] == 9:
                print(f'{Colors.FAIL}{map_[y][x]}{Colors.END}', end='')
            elif map_[y][x] == 0:
                print(f'{Colors.BLUE}{map_[y][x]}{Colors.END}', end='')
            else:
                print(map_[y][x], end='')
        print()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def simulation_step(map_: [[int]]) -> int:
    flash_stack: [tuple[int, int]] = []
    for y in range(len(map_)):
        for x in range(len(map_[y])):
            map_[y][x] += 1
            if map_[y][x] > 9:
                flash_stack.append([x, y])

    has_flashed: [tuple[int, int]] = []
    while len(flash_stack) > 0:
        x, y = flash_stack.pop(0)
        has_flashed.append([x, y])
        for dy in range(y-1, y+2, 1):
            if 0 <= dy < len(map_):
                for dx in range(x-1, x+2, 1):
                    if 0 <= dx < len(map_[y]):
                        if not (dx == x and dy == y):
                            map_[dy][dx] += 1
                            if map_[dy][dx] > 9 and ([dx, dy] not in has_flashed) and ([dx, dy] not in flash_stack):
                                flash_stack.append([dx, dy])

    for dx, dy in has_flashed:
        map_[dy][dx] = 0

    return len(has_flashed)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day11_input.txt", "r") as file:
    octopus_map: [[int]] = [[int(x) for x in line.strip()] for line in file.readlines()]

num_steps = 100
num_flashes = 0
for i in range(num_steps):
    num_flashes += simulation_step(octopus_map)
print(f'Part One: {num_flashes}')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day11_input.txt", "r") as file:
    octopus_map: [[int]] = [[int(x) for x in line.strip()] for line in file.readlines()]

all_flash = -1
step = 0
while True:
    step += 1
    num_flashes = simulation_step(octopus_map)
    if num_flashes == 100:
        break
print(f'Part Two: {step}')
