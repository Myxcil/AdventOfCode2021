# -------------------------------------------------------------------------------------------------------------------------------------------------------------
open_marker = {'(': ')', '[': ']', '{': '}', '<': '>'}
close_marker = dict((v, k) for (k, v) in open_marker.items())
points_corrupted = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_completed = {')': 1, ']': 2, '}': 3, '>': 4}


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_corrupted(chunk: str) -> int:
    stack: [chr] = []
    for x in chunk:
        if x in open_marker:
            stack.append(x)
        else:
            pc = stack.pop()
            if pc != close_marker[x]:
                return points_corrupted[x]
    return 0


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def append_missing(chunk: str) -> int:
    stack: [chr] = []
    score = 0
    for x in chunk:
        if x in open_marker:
            stack.append(x)
        else:
            pc = stack.pop()

    while len(stack) > 0:
        pc = stack.pop()
        score *= 5
        score += points_completed[open_marker[pc]]
    return score


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
chunks: [str]
with open("day10_input.txt", "r") as file:
    chunks = [x.strip() for x in file.readlines()]

score = 0
for c in chunks:
    score += is_corrupted(c)
print(f'Part One: {score}')


incomplete = [c for c in chunks if is_corrupted(c) == 0]
scores = []
for c in incomplete:
    scores.append(append_missing(c))
scores.sort()
print(f'Part Two {scores[round(len(scores)/2)]}')
