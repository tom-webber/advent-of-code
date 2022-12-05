from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day

rps_key_1 = {"rock": ["A", "X"], "paper": ["B", "Y"], "scissors": ["C", "Z"]}
rps_key_2 = {"X": 0, "Y": 3, "Z": 6}

vs_score_key = {
    6: [("rock", "paper"), ("paper", "scissors"), ("scissors", "rock")],
    3: [("paper", "paper"), ("scissors", "scissors"), ("rock", "rock")],
    0: [("paper", "rock"), ("scissors", "paper"), ("rock", "scissors")],
}

move_score_key = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}


def get_move(letter: str):
    move = [k for k, v in rps_key_1.items() if letter in v][0]

    return move


def parse_input(data, part: int):
    move_pairs = []

    for line in data:
        opp_item, my_item = line.split(" ")
        if part == 1:
            move_pairs.append((get_move(opp_item), get_move(my_item)))
        if part == 2:
            opp_move = get_move(opp_item)
            my_condition = rps_key_2[my_item]
            condition_results = vs_score_key[my_condition]
            my_move = [item for item in condition_results if item[0] == opp_move][0][1]
            print(my_move)

            move_pairs.append((opp_move, my_move))

    return move_pairs


def get_move_score(move):
    return move_score_key[move[1]]


def get_vs_score(move_pair):
    vs_score = [k for k, v in vs_score_key.items() if move_pair in v][0]
    return vs_score


def get_score(data, part: int):
    moves = parse_input(data, part=part)

    move_sum = sum([get_move_score(item) for item in moves])
    vs_sum = sum([get_vs_score(item) for item in moves])

    answer = move_sum + vs_sum
    # print(answer)
    return answer


@register_solution(2022, 2, 1)
def part_one(input_data: list[str]):
    input = input_data[:10]
    print(parse_input(input, part=1))
    answer = get_score(input_data, part=1)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 2, 1)

    return answer


# @register_solution(2022, 2, 2)
def part_two(input_data: list[str]):
    input = input_data[:10]
    print(parse_input(input, part=2))
    answer = get_score(input_data, part=2)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 2, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 2)
    part_one(data)
    part_two(data)
