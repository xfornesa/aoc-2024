from collections import Counter

def p1(pair_of_lists: (list[int], list[int])) -> int:
    l, r = pair_of_lists
    l.sort()
    r.sort()
    total_distance = sum(abs(a - b) for a, b in zip(l, r))

    return total_distance

def p2(pair_of_lists: (list[int], list[int])) -> int:
    l, r = pair_of_lists
    counter = Counter(r)
    similarity_score = sum(a * counter.get(a, 0) for a in l)

    return similarity_score
