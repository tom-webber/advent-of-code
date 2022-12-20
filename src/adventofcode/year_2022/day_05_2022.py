from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


def get_num_stacks(input_data: list[str]):
    for i, data in enumerate(input_data[0:12]):
        try:
            stacks = int(data.translate(str.maketrans("", "", " \n\t\r")))
            return i, int(str(stacks)[-1])
        except:
            pass


def get_stacks(stack_index: int, num_stacks: int, stack_data) -> dict:
    stacks = {}
    for stack in range(num_stacks):
        stack_idx = (stack * 4, stack * 4 + 3)
        stack_letters = []
        for i in reversed(range(stack_index)):
            for item in [
                line.translate(str.maketrans("", "", " \n\t\r[]"))
                for line in stack_data[i][stack_idx[0] : stack_idx[1]]
                if line.translate(str.maketrans("", "", " \n\t\r[]"))
            ]:
                stack_letters.append(item)
            stack_letters[:] = [x for x in stack_letters if x]
        stacks[stack + 1] = stack_letters
    return stacks


def parse_instructions(line) -> dict:
    # input like 'move 1 from 2 to 1'
    words = line.split(" ")
    instructions = {}
    for i in range(len(words)):
        if i % 2:
            instructions[words[i - 1]] = int(words[i].strip())
    return instructions


def move_blocks(instructions: dict, stacks: dict, part: int = 1) -> dict:
    in_transit = stacks[instructions["from"]][-instructions["move"] :]
    stacks[instructions["from"]] = stacks[instructions["from"]][: -instructions["move"]]
    if part == 1:
        stacks[instructions["to"]] = stacks[instructions["to"]] + in_transit[::-1]
    elif part == 2:
        stacks[instructions["to"]] = stacks[instructions["to"]] + in_transit
    return stacks


def get_top_block(stacks: dict) -> str:
    return "".join([stacks[k][-1] for k in stacks.keys() if stacks[k]])


@register_solution(2022, 5, 1)
def part_one(input_data: list[str]):
    stack_index, num_stacks = get_num_stacks(input_data)

    stacks = get_stacks(stack_index, num_stacks, input_data[0:stack_index])

    for i in input_data[stack_index + 2 :]:
        inst = parse_instructions(i)
        stacks = move_blocks(inst, stacks)

    answer = get_top_block(stacks)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 5, 1)

    return answer


@register_solution(2022, 5, 2)
def part_two(input_data: list[str]):
    stack_index, num_stacks = get_num_stacks(input_data)

    stacks = get_stacks(stack_index, num_stacks, input_data[0:stack_index])

    for i in input_data[stack_index + 2 :]:
        inst = parse_instructions(i)
        stacks = move_blocks(inst, stacks, part=2)

    answer = get_top_block(stacks)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 5, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 5, strip=False)
    part_one(data)
    part_two(data)
