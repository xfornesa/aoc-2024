from typing import List, Tuple


def read_pairs(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        for line in file:
            a, b = map(int, line.split())
            pairs.append((a, b))
    return pairs

def read_pair_of_int_lists(file_path) -> (list[int], list[int]):
    l, r = [], []
    with open(file_path, 'r') as file:
        for line in file:
            a, b = map(int, line.split())
            l.append(a)
            r.append(b)
    return l, r

def read_array_of_ints(file_path) -> list[list[int]]:
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            list_of_integers = list(map(int, line.split()))
            array.append(list_of_integers)

    return array

def read_strings_list(file_path) -> list[str]:
    strings = []
    with open(file_path, 'r') as file:
        for line in file:
            strings.append(line.strip())

    return strings

def read_array_of_chars(file_path) -> list[list[str]]:
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            list_of_chars = line.split()
            array.append(list_of_chars)

    return array

def read_sections(file_path):
    parts = []
    current_section = []
    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                parts.append(current_section)
                current_section = []
                continue
            current_section.append(line.strip())
    parts.append(current_section)

    return parts

# Output: [(47, 53), (97, 13), (97, 61), (97, 47), (75, 29)]
def parse_pairs(strings_list: list[str]) -> list[tuple[int, ...]]:
    return [tuple(map(int, s.split('|'))) for s in strings_list]

def parse_ints(strings_list: list[str]) -> list[list[int]]:
    return [list(map(int, s.split(','))) for s in strings_list]
