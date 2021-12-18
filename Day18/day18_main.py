def reduce(snail: [str]):
    needs_reduction = True
    while needs_reduction:
        depth = 0
        index = 0
        needs_reduction = False
        [print(f'{x} ', end='') for x in snail]
        print()
        while index < len(snail):
            if snail[index] == '[':
                if depth == 4:
                    explode(snail, index)
                    needs_reduction = True
                    break
                else:
                    depth += 1
            elif snail[index] == ']':
                depth -= 1
            else:
                if int(snail[index]) > 9:
                    split(snail, index)
                    needs_reduction = True
                    break
            index += 1


def get_next_pair(snail: [str], index: int) -> tuple[int, int, int]:
    for x in range(index, len(snail)-3):
        if snail[x] == '[' and snail[x+3] == ']':
            return int(snail[x+1]), int(snail[x+2]), x


def explode(snail: [str], index: int):
    pair = get_next_pair(snail, index)
    print(f'ex={pair}')
    for i in range(pair[2], -1, -1):
        if snail[i] not in '[]':
            value = int(snail[i])
            snail[i] = str(value + int(pair[0]))
            break

    for i in range(pair[2]+4, len(snail), 1):
        if snail[i] not in '[]':
            value = int(snail[i])
            snail[i] = str(value + int(pair[1]))
            break

    for i in range(4):
        del snail[index]
    snail.insert(index, '0')
    # [print(x, end='') for x in snail]
    # print()


def split(snail: [str], index: int):
    print(f'sp={snail[index]}')
    l_value = int(int(snail[index]) / 2)
    r_value = int(snail[index]) - l_value
    del snail[index]
    snail.insert(index, '[')
    snail.insert(index+1,  str(l_value))
    snail.insert(index+2,  str(r_value))
    snail.insert(index+3, ']')
    # [print(x, end='') for x in snail]
    # print()


def calc_snail_mag(snail: [str]) -> [str]:
    stack: [int] = []
    for i in range(len(snail)):
        if snail[i] not in '[]':
            stack.append(int(snail[i]))
        elif snail[i] == ']':
            stack.append(2*stack.pop() + 3*stack.pop())
    assert len(stack) == 1
    return stack.pop()


def add_snailfish_numbers(a: [str], b: [str]) -> [str]:
    result: [str] = ['[']
    result.extend(a)
    result.extend(b)
    result.append(']')
    reduce(result)
    return result


snailfish_rows: [str] = []
with open("day18_test_input.txt", "r") as file:
    for line in file.readlines():
        snailfish_rows.append([x for x in line.strip() if x != ','])


snail_sum = snailfish_rows[0]
for x in range(1, len(snailfish_rows)):
    snail_sum = add_snailfish_numbers(snail_sum, snailfish_rows[x])
