# STOLEN!!! :(
Signal = frozenset[str]
SignalPattern = tuple[Signal, ...]
FourDigitOutputValue = tuple[Signal, ...]


def seven_segment_solver(signal_pattern: SignalPattern) -> dict[Signal, int]:
    one, three, zero, nine = frozenset(), frozenset(), frozenset(), frozenset()
    signal_map = {}
    fives: set[frozenset[str]] = set()
    sixes: set[frozenset[str]] = set()

    for signal in signal_pattern:
        signal_length = len(signal)
        if signal_length == 2:
            signal_map[signal] = 1
            one = signal
        elif signal_length == 4:
            signal_map[signal] = 4
        elif signal_length == 7:
            signal_map[signal] = 8
        elif signal_length == 3:
            signal_map[signal] = 7
        elif signal_length == 5:
            fives.add(signal)
        else:
            sixes.add(signal)

    for five in fives:
        if one.issubset(five):
            signal_map[five] = 3
            three = five
    fives.remove(three)

    for six in sixes:
        if not (three - one).issubset(six):
            signal_map[six] = 0
            zero = six
    sixes.remove(zero)

    for six in sixes:
        if one.issubset(six):
            signal_map[six] = 9
            nine = six
        else:
            signal_map[six] = 6
            six = six

    for five in fives:
        if five.issubset(nine):
            signal_map[five] = 5
        else:
            signal_map[five] = 2

    return signal_map


def parse_input(filepath) -> list[tuple[SignalPattern, FourDigitOutputValue]]:
    output = []
    with open(filepath, "r") as f:
        for line in f.read().strip().split("\n"):
            l, r = line.split(" | ")
            sig_pattern, output_values = (
                tuple((frozenset(i) for i in l.split())),
                tuple(frozenset(i) for i in r.split()),
            )
            output.append((sig_pattern, output_values))
    return output


def part_a():
    fp = r"day8_input.txt"
    data = parse_input(fp)

    n = 0
    for signal_pattern, output_value in data:
        for value in output_value:
            if len(value) in {2, 4, 3, 7}:
                n += 1
    return n


def part_b():
    fp = r"day8_input.txt"
    data = parse_input(fp)
    n = 0
    for signal_pattern, output_value in data:
        parser = seven_segment_solver(signal_pattern)
        n += int("".join([str(parser[val]) for val in output_value]))
    return n


if __name__ == "__main__":
    print(part_a())
    print(part_b())
