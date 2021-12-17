def do_step_x(p: int, v: int) -> tuple[int, int]:
    p += v
    if v > 0:
        v -= 1
    elif v < 0:
        v += 1
    return p, v


def do_step_y(p: int, v: int) -> tuple[int, int]:
    p += v
    v -= 1
    return p, v


def do_step(p: tuple[int, int], v: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    npx, nvx = do_step_x(p[0], v[0])
    npy, nvy = do_step_y(p[1], v[1])
    return (npx, npy), (nvx, nvy)


def inside_rect_x(p: int, min_x: int, max_x: int) -> bool:
    return min_x <= p <= max_x


def inside_rect_y(p: int, min_y: int, max_y: int) -> bool:
    return min_y <= p <= max_y


def inside_rect(p: tuple[int, int], min_xy: tuple[int, int], max_xy: tuple[int, int]) -> bool:
    return inside_rect_x(p[0], min_xy[0], max_xy[0]) and inside_rect_y(p[1], min_xy[1], max_xy[1])


def simulate(vx: int, vy: int) -> tuple[bool, int]:
    position = (0, 0)
    velocity = (vx, vy)

    top_y = position[1]
    while position[0] <= target_max[0] and position[1] >= target_min[1]:
        position, velocity = do_step(position, velocity)
        top_y = max(top_y, position[1])
        if inside_rect(position, target_min, target_max):
            print(f'HIT: v0=({vx},{vy})')
            return True, top_y
    return False, 0


with open("day17_input.txt", "r") as file:
    line = file.readline().strip()
    x0, x1 = [int(x) for x in line[line.index('x=')+2:line.index(',')].split('..')]
    y0, y1 = [int(x) for x in line[line.index('y=') + 2:].split('..')]
    target_min = (x0, y0)
    target_max = (x1, y1)
    print(f'area= ({target_min}, {target_max})')


max_y = 0
best_v = (0, 0)

inside_count = 0
num_iterations = 60000

vx = 1
vy = target_min[1]

while num_iterations > 0:
    num_iterations -= 1
    hit, ty = simulate(vx, vy)
    if hit:
        inside_count += 1
        if ty > max_y:
            max_y = ty
            best_v = (vx, vy)

    vx += 1
    if vx > target_max[0]:
        vx = 1
        vy += 1

print(best_v, max_y, inside_count)

