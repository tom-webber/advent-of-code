import math
from dataclasses import dataclass

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day

# constraint: only 12 red cubes, 13 green cubes, and 14 blue cubes

ball_colours = ["red", "blue", "green"]


def get_id(line: str):
    game = line.split(":")[0]
    id = int(game.split()[-1])
    return id


def get_samples(line: str):
    samples_text = line.split(":")[1]
    samples = [sample.strip() for sample in samples_text.split(";")]
    return samples


def get_ball_nums(samples: list[str]):
    ball_dict = {k: [] for k in ball_colours}
    for sample in samples:
        balls = sample.split(", ")
        for ball in balls:
            num, col = ball.split(" ")
            num = int(num)
            ball_dict[col].append(num)

    return ball_dict


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):
    max_poss_balls = {"red": 12, "blue": 14, "green": 13}

    valid_ids = []
    invalid_ids = []
    for item in input_data:
        game_id = get_id(item)
        samples = get_samples(item)
        ball_dict = get_ball_nums(samples)

        max_balls = {k: max(v) for k, v in ball_dict.items()}

        bigger_than_possible = {
            k: v for (k, v) in max_balls.items() if v > max_poss_balls[k]
        }

        if bigger_than_possible:
            invalid_ids.append(game_id)
        else:
            valid_ids.append(game_id)

    answer = sum(valid_ids)

    if not answer:
        raise SolutionNotFoundException(2023, 2, 1)

    print(answer)
    return answer


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    max_poss_balls = {"red": 12, "blue": 14, "green": 13}
    powers = []
    for item in input_data:
        game_id = get_id(item)
        samples = get_samples(item)
        ball_dict = get_ball_nums(samples)

        min_balls = {k: max(v) for k, v in ball_dict.items()}

        ball_nums = [min_balls[col] for col in ball_colours]
        cubes_power = math.prod(ball_nums)
        powers.append(cubes_power)

    answer = sum(powers)

    if not answer:
        raise SolutionNotFoundException(2023, 2, 2)

    print(answer)
    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
