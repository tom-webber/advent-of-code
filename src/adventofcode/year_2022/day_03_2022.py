from string import ascii_lowercase, ascii_uppercase

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day

priorities = {
    **dict(zip([i for i in ascii_lowercase], list(range(1, 27)))),
    **dict(zip([i for i in ascii_uppercase], list(range(27, 53)))),
}


def split_line_equally(line: str) -> list[str]:
    line_len = len(line)
    # print(f"line_len: {line_len}")
    indices = [0, int(line_len / 2)]
    parts = [line[i:i_next] for i, i_next in zip(indices, indices[1:] + [None])]
    return parts


def get_common_letters(parts: list[str]) -> set[str]:
    set_list = [set(part) for part in parts]
    overlaps = set.intersection(*set_list)

    return overlaps


@register_solution(2022, 3, 1)
def part_one(input_data: list[str]):
    pris = []
    for i in input_data:
        parts = split_line_equally(i)
        overlaps = get_common_letters(parts)
        pri = priorities[list(overlaps)[0]]
        pris.append(pri)

    answer = sum(pris)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 3, 1)

    return answer


@register_solution(2022, 3, 2)
def part_two(input_data: list[str]):
    pris = []
    for i, data in enumerate(input_data):
        if i % 3 == 0:
            bags = []
        bags.append(data)
        if i % 3 == 2:
            overlaps = get_common_letters(bags)
            pri = priorities[list(overlaps)[0]]
            pris.append(pri)

    answer = sum(pris)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 3, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 3)
    part_one(data)
    part_two(data)
