from typing import List


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
