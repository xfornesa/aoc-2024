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
