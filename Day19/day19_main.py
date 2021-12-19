def find_overlaps(scanner_a: [tuple[int, int, int]], scanner_b: [tuple[int, int, int]]) -> tuple[int, int, int]:
    for ia in range(len(scanner_a)):
        distances_a: [int] = []
        for ja in range(len(scanner_a)):
            dx = scanner_a[ja][0] - scanner_a[ia][0]
            dy = scanner_a[ja][1] - scanner_a[ia][1]
            dz = scanner_a[ja][2] - scanner_a[ia][2]
            distances_a.append(dx*dx + dy*dy + dz*dz)

        for ib in range(len(scanner_b)):
            overlaps: [tuple[int, int]] = []
            for jb in range(len(scanner_b)):
                dx = scanner_b[jb][0] - scanner_b[ib][0]
                dy = scanner_b[jb][1] - scanner_b[ib][1]
                dz = scanner_b[jb][2] - scanner_b[ib][2]
                dist = dx*dx + dy*dy + dz*dz
                if dist in distances_a:
                    index = distances_a.index(dist)
                    overlaps.append((index, jb))
                    if len(overlaps) == 12:
                        oa, ob = overlaps[0]
                        ox = scanner_b[ob][0] - scanner_a[oa][0]
                        oy = scanner_b[ob][1] - scanner_a[oa][1]
                        oz = scanner_b[ob][2] - scanner_a[oa][2]
                        return ox, oy, oz


scanners: [[tuple[int, int, int]]] = []
with open("day19_test2_input.txt", "r") as file:
    new_scanner: [tuple[int, int, int]] = None
    for line in file.readlines():
        line = line.strip()
        if line.startswith('--- scanner'):
            if new_scanner is not None:
                scanners.append(new_scanner)
            new_scanner = []
        elif len(line) > 1:
            x, y, z = [int(s) for s in line.split(',')]
            new_scanner.append((x, y, z))
    if new_scanner is not None:
        scanners.append(new_scanner)

overlapping: [tuple[int, int]] = []
offset: dict[tuple[int, int], tuple[int, int, int]] = dict()
for i in range(len(scanners)-1):
    for j in range(i+1, len(scanners)):
        overlaps = find_overlaps(scanners[i], scanners[j])
        if overlaps is not None:
            print(f'{i},{j}: {overlaps}')
[print(x) for x in offset.items()]
