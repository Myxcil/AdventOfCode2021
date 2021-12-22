class RebootStep:
    def __init__(self, line: str):
        if line.startswith("on"):
            self.on = 1
            axii = line[3:].split(',')
        else:
            self.on = 2
            axii = line[4:].split(',')

        self.x = [int(a) for a in axii[0][2:].split('..')]
        self.y = [int(a) for a in axii[1][2:].split('..')]
        self.z = [int(a) for a in axii[2][2:].split('..')]

    def __str__(self):
        return f'{self.on}: {self.x}, {self.y}, {self.z}'

    def __repr__(self):
        return str(self)


reboot_steps: [RebootStep] = []
with open("day22_input.txt", "r") as file:
    reboot_steps = [RebootStep(x.strip()) for x in file.readlines()]
# print(reboot_steps)

cuboids: dict[tuple[int, int, int], int] = {}
max_size = 50

for rs in reboot_steps:
    for z in range(rs.z[0], rs.z[1] + 1):
        if z < -max_size or z > max_size:
            continue
        for y in range(rs.y[0], rs.y[1] + 1):
            if y < -max_size or y > max_size:
                continue
            for x in range(rs.x[0], rs.x[1] + 1):
                if x < -max_size or x > max_size:
                    continue
                if not (x,y,z) in cuboids.keys() or rs.on != cuboids[x, y, z]:
                    cuboids[(x, y, z)] = rs.on

print(sum(value == 1 for value in cuboids.values()))