def count_increases(elements):
    prev_value = -1
    num_increases = 0
    for d in elements:
        if 0 <= prev_value < d:
            num_increases = num_increases + 1
        prev_value = d
    print(f'# of increases: {num_increases}')


lines = []
for line in open("day1_input.txt", "r"):
    lines.append(int(line))

# Part One
# Count the number of times a depth measurement increases from the previous measurement.
count_increases(lines)

# Part Two
accDepth = []
maxCount = int(len(lines) / 3) * 3
for i in range(maxCount):
    accDepth.append(lines[i] + lines[i + 1] + lines[i + 2])
count_increases(accDepth)
