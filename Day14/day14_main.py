from collections import defaultdict

with open("day14_input.txt", "r") as file:
    polymer_template: [chr] = [x for x in file.readline().strip()]
    pair_insertions: dict[str, chr] = dict()
    for line in file.readlines():
        if line[0] == '\n':
            continue
        key, value = line.strip().split(' -> ')
        pair_insertions[key] = value[0]

counter_map = defaultdict(int)
for i in range(len(polymer_template)-1):
    monomer_pair = "".join(polymer_template[i:i+2])
    counter_map[monomer_pair] += 1

for _ in range(40):
    new_counter_map = defaultdict(int)
    for pair, count in counter_map.items():
        next_monomer = pair_insertions[pair]
        new_counter_map[pair[0]+next_monomer] += count
        new_counter_map[next_monomer+pair[1]] += count
    counter_map = new_counter_map

letter_count = defaultdict(int)
for pair, count in counter_map.items():
    letter_count[pair[0]] += count
letter_count[polymer_template[-1]] += 1

counts: list[int] = list(letter_count.values())
counts.sort()
print(counts[-1] - counts[0])
