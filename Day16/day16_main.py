import math


def binary_to_int(start: int, length: int) -> int:
    return int("".join(bit_stream[start:start+length]), 2)


def read_literal_value_5bits_chunks(i: int) -> tuple[int, int]:
    construction_bits: [str] = []
    while True:
        construction_bits.append(bit_stream[i+1])
        construction_bits.append(bit_stream[i+2])
        construction_bits.append(bit_stream[i+3])
        construction_bits.append(bit_stream[i+4])
        i += 5
        if bit_stream[i-5] == '0':
            break
    return int("".join(construction_bits), 2), i


def read_packet_header(i: int) -> tuple[int, int, int]:
    return binary_to_int(i, 3), binary_to_int(i+3, 3), i+6


def operator_sum(operands: [int]) -> int:
    return sum(operands)


def operator_mul(operands: [int]) -> int:
    return math.prod(operands)


def operator_min(operands: [int]) -> int:
    return min(operands)


def operator_max(operands: [int]) -> int:
    return max(operands)


def operator_greater(operands: [int]) -> int:
    if operands[0] > operands[1]:
        return 1
    return 0


def operator_less(operands: [int]) -> int:
    if operands[0] < operands[1]:
        return 1
    return 0


def operator_equal(operands: [int]) -> int:
    if operands[0] == operands[1]:
        return 1
    return 0


operator_dict = {
    0: operator_sum,
    1: operator_mul,
    2: operator_min,
    3: operator_max,
    5: operator_greater,
    6: operator_less,
    7: operator_equal
}


def read_operator_packet(operator: int, i: int) -> tuple[int, int]:
    operand_stack: [int] = []
    if bit_stream[i] == '0':
        packet_length = binary_to_int(i + 1, 15)
        i += 16
        # print(f'packet_length={packet_length}')
        stop_at = i + packet_length
        while i < stop_at:
            ret, i = read_packet(i)
            operand_stack.append(ret)
    else:
        num_packets = binary_to_int(i + 1, 11)
        i += 12
        # print(f'num_packets={num_packets}')
        for _ in range(num_packets):
            ret, i = read_packet(i)
            operand_stack.append(ret)

    return operator_dict[operator](operand_stack), i


def read_packet(i: int) -> tuple[int, int]:
    version, type_id, i = read_packet_header(i)
    version_numbers.append(version)
    # print(f'version={version}, type_id={type_id}')
    if type_id == 4:
        result, i = read_literal_value_5bits_chunks(i)
        # print(literal_value)
    else:
        result, i = read_operator_packet(type_id, i)
    return result, i


bit_stream: [str] = []
with open("day16_input.txt", "r") as file:
    for x in file.read().strip():
        value = format(bin(int(x, 16))[2:], '0>4')
        bit_stream.extend(value)
# [print(x, end='') for x in bit_stream]
# print()

version_numbers: [int] = []
total, i = read_packet(0)
print(total)
# print(f'version sum: {sum(version_numbers)}')
