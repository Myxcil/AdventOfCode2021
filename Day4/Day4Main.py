# ---------------------------------------------------------------------------------------------------------------------
class Row:
    def __init__(self, file):
        self.values = [int(i) for i in file.readline().strip('\n').split()]
        if len(self.values) == 5:
            self.drawn = []
            for x in self.values:
                self.drawn.append(False)

    def reset(self):
        for index in range(len(self.drawn)):
            self.drawn[index] = False

    def is_valid(self):
        return len(self.values) == 5

    def mark_values(self, value):
        for index in range(len(self.values)):
            if self.values[index] == value:
                self.drawn[index] = True

    def is_bingo(self):
        all_drawn = True
        for d in self.drawn:
            all_drawn = all_drawn & d
        return all_drawn

    def sum_non_drawn(self):
        total = 0
        for index in range(len(self.values)):
            if not self.drawn[index]:
                total = total + self.values[index]
        return total


# ---------------------------------------------------------------------------------------------------------------------
class Board:
    def __init__(self, file):
        self.rows = []
        for index in range(5):
            self.rows.append(Row(file))

    def is_valid(self):
        for row in self.rows:
            if not row.is_valid():
                return False
        return True

    def print(self):
        for row in self.rows:
            print(row.values)
            print(row.drawn)

    def reset(self):
        for row in self.rows:
            row.reset()

    def mark_values(self, value):
        for row in self.rows:
            row.mark_values(value)

    def is_bingo(self):
        for row in self.rows:
            if row.is_bingo():
                return True

        for col in range(5):
            col_bingo = True
            for row in self.rows:
                col_bingo = col_bingo & row.drawn[col]
            if col_bingo:
                return True

        return False

    def sum_non_drawn(self):
        total = 0
        for row in self.rows:
            total = total + row.sum_non_drawn()
        return total


# ---------------------------------------------------------------------------------------------------------------------
def create_boards(file):
    list_of_boards = []
    while True:
        b = Board(file)
        if not b.is_valid():
            break

        list_of_boards.append(b)
        input_file.readline()

    return list_of_boards


def run_bingo(boards):
    for drawn_value in numbers_drawn:
        for board in boards:
            board.mark_values(drawn_value)

        for board in boards:
            if board.is_bingo():
                return board, drawn_value


def run_crooked_bingo(boards):
    for drawn_value in numbers_drawn:
        for board in boards:
            board.mark_values(drawn_value)
            if len(boards) == 1 and board.is_bingo():
                return board, drawn_value
        boards = [a for a in boards if not a.is_bingo()]


# ---------------------------------------------------------------------------------------------------------------------
# Part One
# ---------------------------------------------------------------------------------------------------------------------
input_file = open("day4_input.txt", "r")
numbers_drawn = [int(i) for i in input_file.readline().strip('\n').split(',')]
input_file.readline()

bingo_boards = create_boards(input_file)
winner, winning_value = run_bingo(bingo_boards)
print(f'Winning score: {winner.sum_non_drawn() * winning_value}')


# ---------------------------------------------------------------------------------------------------------------------
# Part Two
# ---------------------------------------------------------------------------------------------------------------------
for b in bingo_boards: b.reset()
winner, winning_value = run_crooked_bingo(bingo_boards)
print(f'Crooked score: {winner.sum_non_drawn() * winning_value}')
