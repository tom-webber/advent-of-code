from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


def unique_list(list_to_test):
    return len(list_to_test) == len(set(list_to_test))


def get_unique_chars_pos_from_str(string: str, num_unique: int):
    len_str = len(string)
    for i in range(len_str):
        chars = [s for s in string[i : i + num_unique]]

        if unique_list(chars):
            return i + num_unique


@register_solution(2022, 6, 1)
def part_one(input_data: list[str]):
    answer = get_unique_chars_pos_from_str(input_data[0], num_unique=4)
    print(answer)
    if not answer:
        raise SolutionNotFoundException(2022, 6, 1)

    return answer


@register_solution(2022, 6, 2)
def part_two(input_data: list[str]):
    answer = get_unique_chars_pos_from_str(input_data[0], num_unique=14)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 6)
    part_one(data)
    part_two(data)
