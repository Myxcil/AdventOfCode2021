# New attempt
class Cube:
    def __init__(self, min_x: int, max_x: int, min_y: int, max_y: int, min_z: int, max_z: int):
        self.x = [min_x, max_x]
        self.y = [min_y, max_y]
        self.z = [min_z, max_z]

    def width(self) -> int:
        return self.x[1] - self.x[0] + 1

    def height(self) -> int:
        return self.y[1] - self.y[0] + 1

    def depth(self) -> int:
        return self.z[1] - self.z[0] + 1

    def size(self) -> int:
        return self.width() * self.height() * self.depth()

    def __eq__(self, other) -> bool:
        return self.x[0] == other.x[0] and self.x[1] == other.x[1] and \
               self.y[0] == other.y[0] and self.y[1] == other.y[1] and \
               self.z[0] == other.z[0] and self.z[1] == other.z1[1]

    def __hash__(self):
        return hash((self.x[0], self.x[1], self.y[0], self.y[1], self.z[0], self.z[1]))

    def __str__(self) -> str:
        return f'{self.x},{self.y},{self.z}'

    def __repr__(self) -> str:
        return str(self)

    def cut(self, min_x: int, max_x: int, min_y: int, max_y: int, min_z: int, max_z: int):
        new_cubes: [Cube] = []
        if max_x < self.x[0] or min_x > self.x[1] or \
                max_y < self.y[0] or min_y > self.y[1] or \
                max_z < self.z[0] or min_z > self.z[1]:
            new_cubes.append(self)
        else:
            cube = Cube(min_x, max_x, min_y, max_y, min_z, max_z)
            cube.x[0] = max(cube.x[0], self.x[0])
            cube.x[1] = min(cube.x[1], self.x[1])
            cube.y[0] = max(cube.y[0], self.y[0])
            cube.y[1] = min(cube.y[1], self.y[1])
            cube.z[0] = max(cube.z[0], self.z[0])
            cube.z[1] = min(cube.z[1], self.z[1])

            neg_x = self.x[0], cube.x[0]-1
            center_x = cube.x[0], cube.x[1]
            pos_x = cube.x[1]+1, self.x[1]
            neg_y = self.y[0], cube.y[0]-1
            center_y = cube.y[0], cube.y[1]
            pos_y = cube.y[1]+1, self.y[1]
            neg_z = self.z[0], cube.z[0]-1
            center_z = cube.z[0], cube.z[1]
            pos_z = cube.z[1]+1, self.z[1]

            for iz in [neg_z, center_z, pos_z]:
                for iy in [neg_y, center_y, pos_y]:
                    for ix in [neg_x, center_x, pos_x]:
                        if iz == center_z and iy == center_y and ix == center_x:
                            continue
                        if ix[0] > ix[1] or iy[0] > iy[1] or iz[0] > iz[1]:
                            continue
                        new_cubes.append(Cube(ix[0], ix[1], iy[0], iy[1], iz[0], iz[1]))
        return new_cubes


cubes: [Cube] = []
max_range = 0
with open("day22_input.txt", "r") as file:
    for line in file.readlines():
        set_on = line.startswith('on')
        if set_on:
            line = line[3:].strip()
        else:
            line = line[4:].strip()

        axis = line.split(',')
        x = [int(a) for a in axis[0][2:].split('..')]
        y = [int(a) for a in axis[1][2:].split('..')]
        z = [int(a) for a in axis[2][2:].split('..')]
        if max_range > 0 and (x[0] < -max_range or x[1] > max_range or y[0] < -max_range or y[1] > max_range or z[0] < -max_range or z[1] > max_range):
            continue

        cubes_temp: [Cube] = []
        for c in cubes:
            add_cubes = c.cut(x[0], x[1], y[0], y[1], z[0], z[1])
            cubes_temp.extend(add_cubes)
        if set_on:
            cubes_temp.append(Cube(x[0], x[1], y[0], y[1], z[0], z[1]))

        cubes = cubes_temp
print(f'{len(cubes)}: {sum(c.size() for c in cubes)}')
