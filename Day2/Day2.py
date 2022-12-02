from collections import deque

answer = deque(['rock', 'paper', 'scissors'])
opponent_options = deque(['A', 'B', 'C'])
player_options = deque(['X', 'Y', 'Z'])

WIN = 6
DRAW = 3
LOSS = 0


def throw_hands_1(opponent: int, player: int) -> int:
    rotate = False
    points = player + 1

    if abs(player - opponent) == 2:
        rotate = True
        answer.rotate(1)
        opponent = answer.index(answer[opponent - 2])
        player = answer.index(answer[player - 2])

    if answer.index(answer[opponent]) == player:
        points = points + DRAW
    elif player > opponent:
        points = points + WIN
    else:
        points = points + LOSS

    if rotate:
        answer.rotate(-1)

    return points


def throw_hands_2(opponent: int, strat: str) -> int:
    match strat:
        case 'Z':
            return WIN + (opponent + 2 if opponent != 2 else 1)
        case 'Y':
            return DRAW + opponent + 1
        case 'X':
            return LOSS + (opponent + (3 if opponent == 0 else 0))


def main():
    with open('input.txt') as file:
        part_1_points = 0
        part_2_points = 0
        for line in file.readlines():
            part_1_points += throw_hands_1(
                opponent_options.index(line[0]),
                player_options.index(line[2]))

            part_2_points += throw_hands_2(
                opponent_options.index(line[0]),
                line[2])

        print(f"Part 1: {part_1_points}\n"
              f"Part 2: {part_2_points}")


if __name__ == '__main__':
    main()
