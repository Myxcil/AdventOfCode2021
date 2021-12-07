# ---------------------------------------------------------------------------------------------------------------------
def simulate_breeding(_fish:[], _num_simulation_steps):
    for i in range(_num_simulation_steps):
        simulate_step(_fish)


# ---------------------------------------------------------------------------------------------------------------------
def simulate_step(_fish:[]):
    num_to_add = 0
    for i in range(len(_fish)):
        if _fish[i] == 0:
            num_to_add += 1
            _fish[i] = 6
        else:
            _fish[i] -= 1
    for i in range(num_to_add):
        _fish.append(8)


# ---------------------------------------------------------------------------------------------------------------------
list_of_fish = [int(a) for a in open("day6_input.txt", "r").readline().split(',')]

# ---------------------------------------------------------------------------------------------------------------------
# Part One
simulate_breeding(list_of_fish, 80)
print(f'number of fish after 80 days: {len(list_of_fish)}')

# ---------------------------------------------------------------------------------------------------------------------
# Part Two
fish_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
list_of_fish = [int(a) for a in open("day6_input.txt", "r").readline().split(',')]
for fish in list_of_fish:
    fish_counts[fish] += 1

for i in range(256):
    fish_counts.append(fish_counts.pop(0))
    fish_counts[6] += fish_counts[8]

print(f'number of fish after 256 days: {sum(fish_counts)}')
