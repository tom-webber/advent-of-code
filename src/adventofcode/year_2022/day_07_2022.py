import re
from dataclasses import dataclass, field

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


@dataclass
class Elf_file:
    name: str
    file_size: int

    def parse(input: str):
        file_size, name = input.split(" ")
        return Elf_file(name, int(file_size))

    def is_parseable(input: str):
        return bool(re.fullmatch(r"\d+ [\w\.]+", input))

    def __repr__(self):
        return f'<File name="{self.name}" size={self.file_size}>'


class Elf_folder:
    def __init__(self, dirname, parent=None):
        self.name = dirname
        self.parent = parent
        self.children = []
        self.files = []
        self.size = 0

    def update_size(self, filesize):
        self.size += filesize
        if self.parent:
            self.parent.update_size(filesize)

    def add_file(self, file):
        self.files.append(file)
        self.update_size(file.file_size)

    def __repr__(self):
        return (
            f'<Dir name="{self.name}" size={self.size}'
            f" children={len(self.children)} files={len(self.files)}>"
        )


def get_dir_sizes(
    directory: Elf_folder,
    threshold: int,
    small_dirs: list[int],
    threshold_type: str = "<",
):
    if threshold_type == "<":
        if directory.size < threshold:
            small_dirs.append(directory.size)
            # print(f"name: {directory.name}, size: {directory.size}, total: {small_dirs}")
    elif threshold_type == ">=":
        if directory.size >= threshold:
            small_dirs.append(directory.size)
    for child in directory.children:
        get_dir_sizes(child, threshold, small_dirs, threshold_type)

    return small_dirs


def get_file_directory(input_data: list[str]) -> Elf_folder:

    root = Elf_folder("/")
    current_wd = root

    for row in input_data:
        # command
        if row.startswith("$"):
            parts = row.split(" ")
            # change directory
            if parts[1] == "cd":
                # move to parent
                if parts[2] == "..":
                    current_wd = current_wd.parent
                # move into child
                else:
                    for child in current_wd.children:
                        if child.name == parts[2]:
                            current_wd = child
                            break
        # directories
        elif row.startswith("dir"):
            _, name = row.split(" ")
            current_wd.children.append(Elf_folder(name, parent=current_wd))
        # files
        elif Elf_file.is_parseable(row):
            current_wd.add_file(Elf_file.parse(row))

    return root


@register_solution(2022, 7, 1)
def part_one(input_data: list[str]):

    root = get_file_directory(input_data)

    small_dir_sizes = []
    small_dir_sizes = get_dir_sizes(root, 100000, small_dir_sizes, threshold_type="<")

    answer = sum(small_dir_sizes)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 7, 1)

    return answer


@register_solution(2022, 7, 2)
def part_two(input_data: list[str]):

    root = get_file_directory(input_data)
    fs_size = 70_000_000
    fs_current_free = fs_size - root.size
    fs_needed = 30_000_000
    needed = fs_needed - fs_current_free

    dir_sizes = []
    dir_sizes = get_dir_sizes(root, needed, dir_sizes, threshold_type=">=")
    print(dir_sizes)
    answer = min(dir_sizes)
    print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 7, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 7)
    part_one(data)
    part_two(data)
