from adventofcode.year_2023.day_01_2023 import part_one, part_two

test_input_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

test_input_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def test_part_one():
    assert part_one(test_input_1) == 142


def test_part_two():
    assert part_two(test_input_2) == 281
