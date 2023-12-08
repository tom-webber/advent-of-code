import re
import sys

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day

numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_str = [str(i) for i in range(1, 10)]
all_digits = numbers_str + digit_str
str_numbers_dict = dict(zip(numbers_str, digit_str))


def get_number(junked_string: str) -> int:
    all_nums_string = re.sub(pattern=r"[^\d]*", repl="", string=junked_string)
    first_num = all_nums_string[0]
    last_num = all_nums_string[-1]
    out_num = int(f"{first_num}{last_num}")
    return out_num


def get_tweaked_num(junked_str: str) -> int:
    all_nums_string = find_all_digits(junked_str)
    first_num = all_nums_string[0]
    last_num = all_nums_string[-1]
    if not first_num.isdigit():
        first_num = str_numbers_dict[first_num]
    if not last_num.isdigit():
        last_num = str_numbers_dict[last_num]
    out_num = int(f"{first_num}{last_num}")
    return out_num


# def find(word, source_string):
#     try:
#         return source_string.index(word), word
#     except ValueError:
#         return sys.maxsize, None


def find_all_digits(source_string):
    return re.findall(r"(?=(" + "|".join(all_digits) + r"))", source_string)


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    sum_nums = 0

    for item in input_data:
        num = get_number(item)
        sum_nums += num

    answer = sum_nums
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    sum_nums = 0

    for item in input_data:
        num = get_tweaked_num(item)
        sum_nums += num

    answer = sum_nums
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
