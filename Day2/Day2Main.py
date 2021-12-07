class SubCommand:
    def __init__(self, line):
        s = line.split()
        self.direction = s[0]
        self.units = int(s[1])

    def __str__(self):
        return f'{self.direction} {self.units}'


sub_commands = []
for line in open("day2_input.txt", "r"):
    sub_commands.append(SubCommand(line))

# Part One
# What do you get if you multiply your final horizontal position by your final depth?
horizontal = 0
vertical = 0
for sc in sub_commands:
    if sc.direction == "forward":
        horizontal = horizontal + sc.units
    elif sc.direction == "up":
        vertical = vertical - sc.units
    else:
        vertical = vertical + sc.units
print(f'result {horizontal * vertical}')


# Part Two
horizontal = 0
vertical = 0
aim = 0

for sc in sub_commands:
    if sc.direction == "up":
        aim = aim - sc.units
    elif sc.direction == "down":
        aim = aim + sc.units
    else:
        horizontal = horizontal + sc.units
        vertical = vertical + aim * sc.units
print(f'result {horizontal * vertical}')
