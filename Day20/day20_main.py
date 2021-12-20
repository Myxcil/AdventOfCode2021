outside_val: chr = '.'


def get_9x9_number(input_image: [[chr]], x: int, y: int) -> int:
    result: int = 0
    shift: int = 8
    for iy in range(y-1, y+2):
        for ix in range(x-1, x+2):
            if 0 <= iy < len(input_image) and 0 <= ix < len(input_image[0]):
                if input_image[iy][ix] == '#':
                    result += 1 << shift
            elif outside_val == '#':
                result += 1 << shift
            shift -= 1
    return result


def enhance_image(input_image: [[chr]], algo: [chr]) -> [[chr]]:
    new_image_map: [[chr]] = []
    for y in range(-1, len(input_image)+1):
        row: [chr] = []
        for x in range(-1, len(input_image[0])+1):
            index = get_9x9_number(input_image, x, y)
            row.append(algo[index])
        new_image_map.append(row)
    return new_image_map


def print_image(input_image: [[chr]]):
    for y in range(len(input_image)):
        for x in range(len(input_image[0])):
            print(input_image[y][x], end='')
        print()
    print()


input_algo: [chr]
image_map: [[chr]]
with open("day20_input.txt", "r") as file:
    input_algo = [c for c in file.readline().strip()]
    file.readline()
    image_map = [[c for c in row.strip()] for row in file.readlines()]

# print_image(image_map)

for _ in range(50):
    image_map = enhance_image(image_map, input_algo)
    if outside_val == '.':
        outside_val = input_algo[0]
    else:
        outside_val = input_algo[-1]
# print_image(enhanced_img)
print(sum(row.count('#') for row in image_map))

