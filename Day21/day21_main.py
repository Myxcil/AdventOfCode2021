player_score: [int] = [0, 0]
player_pos: [int] = [3, 7]

next_dice_roll: int = 1
num_dice_rolls: int = 0


def roll_dice_3x() -> int:
    global next_dice_roll
    global num_dice_rolls
    res = 0
    for _ in range(3):
        res += next_dice_roll
        next_dice_roll += 1
        num_dice_rolls += 1
        if next_dice_roll > 100:
            next_dice_roll = 1
    return res


def run_game() -> int:
    while True:
        for p in range(2):
            result = roll_dice_3x()
            player_pos[p] = (player_pos[p] + result) % 10
            player_score[p] += player_pos[p] + 1
            # print(f'{p}: {player_score[p]}')
            if player_score[p] >= 1000:
                not_p = ~p & 1
                return player_score[not_p] * num_dice_rolls


print(f'#1 {run_game()}')


cache: dict[tuple[int, int, int, int], tuple[int, int]] = dict()


def recursive_play(pos_0, score_0, pos_1, score_1) -> [tuple[int, int]]:
    if score_0 >= 21:
        return 1, 0
    if score_1 >= 21:
        return 0, 1
    if (pos_0, score_0, pos_1, score_1) in cache:
        return cache[(pos_0, score_0, pos_1, score_1)]

    val = 0, 0
    for dice_0 in [1, 2, 3]:
        for dice_1 in [1, 2, 3]:
            for dice_2 in [1, 2, 3]:
                new_pos = (pos_0 + dice_0 + dice_1 + dice_2) % 10
                new_score = score_0 + new_pos + 1
                a, b = recursive_play(pos_1, score_1, new_pos, new_score)
                val = val[0] + b, val[1] + a
    cache[(pos_0, score_0, pos_1, score_1)] = val
    return val


print(f'#2 {max(recursive_play(9, 0, 7, 0))}')

