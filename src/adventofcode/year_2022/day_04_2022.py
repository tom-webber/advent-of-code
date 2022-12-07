from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


def get_ranges(input: str):
    range_a, range_b = input.split(",")
    range_a = [int(i) for i in range_a.split("-")]
    range_b = [int(i) for i in range_b.split("-")]

    return (range_a, range_b)


def get_range_interaction(ranges: tuple[list]):
    a, b = ranges
    a_minus_b = [m - n for m, n in zip(a, b)]
    b_minus_a = [m - n for m, n in zip(b, a)]
    # print((a_minus_b, b_minus_a))
    return (a_minus_b, b_minus_a)


def do_ranges_fully_overlap(range_interaction: tuple[list]):
    # overlap if first element is >= 0 and second element is <=0 (or vice versa)
    # print(range_interaction)
    for i in range_interaction:
        if i[0] >= 0 and i[1] <= 0:
            return True
    return False


def get_range_overlap(ranges: tuple[list]):
    x, y = ranges
    overlap = range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)

    return bool(overlap)


@register_solution(2022, 4, 1)
def part_one(input_data: list[str]):

    answer = sum(
        [
            do_ranges_fully_overlap(get_range_interaction(get_ranges(x)))
            for x in input_data
        ]
    )
    print(answer)
    if not answer:
        raise SolutionNotFoundException(2022, 4, 1)

    return answer


@register_solution(2022, 4, 2)
def part_two(input_data: list[str]):

    answer = sum([get_range_overlap(get_ranges(x)) for x in input_data])

    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 4, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 4)
    part_one(data)
    part_two(data)
