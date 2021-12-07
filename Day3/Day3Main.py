def parse_binary_numbers(file):
    number_list = []
    max_bits = 0
    for line in open(file,"r").read().splitlines():
        number_list.append(line)
        max_bits = max(max_bits, len(line))
    return number_list, max_bits


def count_bits(number_list, position):
    num_bits_at_position = 0
    for num in number_list:
        if num[position] == '1':
            num_bits_at_position = num_bits_at_position + 1
    return num_bits_at_position


def determine_significant_bit(number_list, position):
    set_bits = count_bits(number_list, position)
    if len(number_list) - set_bits <= set_bits:
        return 1
    else:
        return 0


def evaluate_most_common(number_list):
    for bit_pos in range(num_bits):
        curr_bit = str(determine_significant_bit(number_list, bit_pos))
        number_list[:] = [x for x in number_list if x[bit_pos] == curr_bit]
        if len(number_list) == 1:
            break;


def evaluate_least_common(number_list):
    for bit_pos in range(num_bits):
        curr_bit = str(determine_significant_bit(number_list, bit_pos))
        number_list[:] = [x for x in number_list if x[bit_pos] != curr_bit]
        if len(number_list) == 1:
            break;


binary_numbers, num_bits = parse_binary_numbers("day3_input.txt")

# Part One
gamma_rate = ""
epsilon_rate = ""
for bit in range(num_bits):
    next_bit = determine_significant_bit(binary_numbers, bit)
    gamma_rate = gamma_rate[:bit] + str(next_bit) + gamma_rate[bit+1:]
    flipped_bit = 0
    if next_bit == 0:
        flipped_bit = 1
    epsilon_rate = epsilon_rate[:bit] + str(flipped_bit) + epsilon_rate[bit + 1:]

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(f'power consumption: {gamma_rate * epsilon_rate}')

# Part Two
filtered_list = binary_numbers.copy()
evaluate_most_common(filtered_list)
oxygen_generator_rating = int(filtered_list[0],2)
print(filtered_list)
print(oxygen_generator_rating)

filtered_list = binary_numbers.copy()
evaluate_least_common(filtered_list)
co2_scrubber_rating = int(filtered_list[0], 2)
print(co2_scrubber_rating)

print(f'life support rating: {oxygen_generator_rating * co2_scrubber_rating}')