
# ---------------------------------------------------------------------------------------------------------------------
class Point:
    def __init__(self, _line):
        c = _line.split(',')
        self.x = int(c[0])
        self.y = int(c[1])

    def __str__(self):
        return f'({self.x},{self.y})'


# ---------------------------------------------------------------------------------------------------------------------
class Line:
    def __init__(self, _line):
        p = _line.split(" -> ")
        self.start = Point(p[0])
        self.end = Point(p[1])

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def __repr__(self):
        return str(self)

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x


def show_matrix(_matrix, _width, _height):
    for y in range(_height):
        for x in range(_width):
            print(f'{_matrix[x][y]:4}', end='')
        print()


def render_line_hv(_matrix, _width, _height, _line: Line):
    if _line.is_horizontal():
        if _line.start.x < _line.end.x:
            for x in range(_line.start.x, _line.end.x+1, 1):
                _matrix[x][_line.start.y] += 1
        else:
            for x in range(_line.end.x, _line.start.x+1, 1):
                _matrix[x][_line.start.y] += 1
        return True
    elif _line.is_vertical():
        if _line.start.y < _line.end.y:
            for y in range(_line.start.y, _line.end.y+1, 1):
                _matrix[_line.start.x][y] += 1
        else:
            for y in range(_line.end.y, _line.start.y+1, 1):
                _matrix[_line.start.x][y] += 1
        return True
    return False


def render_line(_matrix, _width, _height, _line: Line):
    if not render_line_hv(_matrix, _width, _height, _line):
        if _line.start.x < _line.end.x:
            x0 = _line.start.x
            x1 = _line.end.x
            y0 = _line.start.y
            y1 = _line.end.y
        else:
            x0 = _line.end.x
            x1 = _line.start.x
            y0 = _line.end.y
            y1 = _line.start.y

        if y0 < y1:
            y_step = 1
        else:
            y_step = -1

        y = y0;
        for x in range(x0, x1+1, 1):
            _matrix[x][y] += 1
            y += y_step


def count_overlaps(_matrix, _width, _height, _min_overlaps):
    num_overlaps = 0
    for y in range(_height):
        for x in range(_width):
            if _matrix[x][y] >= _min_overlaps:
                num_overlaps += 1
    return num_overlaps


# ---------------------------------------------------------------------------------------------------------------------
# Part One
# ---------------------------------------------------------------------------------------------------------------------
lines = [Line(a) for a in open("day5_input.txt", "r").readlines()]
width = 0
height = 0
for line in lines:
    width = max(width, line.start.x, line.end.x)
    height = max(height, line.start.y, line.end.y)
width += 1
height += 1
print(f'{width}x{height}')


matrix = [[0 for y in range(height)] for x in range(width)]

for line in lines:
    render_line_hv(matrix, width, height, line)

safe_points = count_overlaps(matrix, width, height, 2)
print(f'overlap count: {safe_points}')
print()

# ---------------------------------------------------------------------------------------------------------------------
# Part Two
# ---------------------------------------------------------------------------------------------------------------------
matrix = [[0 for y in range(height)] for x in range(width)]

for line in lines:
    render_line(matrix, width, height, line)

safe_points = count_overlaps(matrix, width, height, 2)
print(f'overlap +diagonal count: {safe_points}')
