from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


def find_per_elf_calories(data: list[str]):
    lists = [[]]
    for i in data:
        if i == "":
            lists.append([])
        else:
            lists[-1].append(int(i))

    return lists


def find_elf_total_calories(list_of_per_elf_calories: list[int]):
    return [sum(x) for x in list_of_per_elf_calories]


def find_most_calories(data):
    lists = find_per_elf_calories(data)
    max_score = max(find_elf_total_calories(lists))

    return max_score


def find_top_three_elves(data):
    calories_per_elf = find_per_elf_calories(data)

    total_calories_per_elf = find_elf_total_calories(calories_per_elf)
    total_calories_per_elf.sort(reverse=True)

    top_three_elves = total_calories_per_elf[:3]

    combined_score = sum(top_three_elves)

    return combined_score


@register_solution(2022, 1, 1)
def part_one(input_data: list[str]):
    answer = find_most_calories(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 1, 1)

    return answer


@register_solution(2022, 1, 2)
def part_two(input_data: list[str]):
    answer = find_top_three_elves(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 1)
    part_one(data)
    part_two(data)
