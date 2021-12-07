# ---------------------------------------------------------------------------------------------------------------------
def sum_abs_differences(_list: [], _center: int):
    total = 0
    for i in _list:
        total += abs(i - _center)
    return total


# ---------------------------------------------------------------------------------------------------------------------
def sum_abs_differences_ex(_list: [], _center: int, _cost: []):
    total = 0
    for i in _list:
        total += _cost[abs(i-_center)]
    return total


# ---------------------------------------------------------------------------------------------------------------------
horizontal_positions = [int(i) for i in open("day7_input.txt", "r").readline().split(',')]
width = 0
for i in horizontal_positions:
    width = max(width,i)
width += 1

print(f'width={width}')
print(horizontal_positions)

min_fuel = -1
min_index = -1
for i in range(width):
    tf = sum_abs_differences(horizontal_positions, i)
    # print(f'center={i}, total={tf}')
    if min_fuel < 0 or min_fuel > tf:
        min_fuel = tf
        min_index = i
print(min_index, min_fuel)

# Part Two
min_fuel = -1
min_index = -1
cost = []
for i in range(width):
    cost.append(sum(range(i+1)))
print(cost)

for i in range(width):
    tf = sum_abs_differences_ex(horizontal_positions, i, cost)
    # print(f'center={i}, total={tf}')
    if min_fuel < 0 or min_fuel > tf:
        min_fuel = tf
        min_index = i
print(min_index, min_fuel)