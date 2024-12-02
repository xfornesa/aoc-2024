def p1(array_of_ints: list[list[int]]) -> int:
    result = 0
    for row in array_of_ints:
        is_increasing = all(earlier < later for earlier, later in zip(row, row[1:]))
        is_decreasing = all(earlier > later for earlier, later in zip(row, row[1:]))
        has_proper_distance = all(abs(earlier - later) <= 3 for earlier, later in zip(row, row[1:]))
        if (is_increasing or is_decreasing) and has_proper_distance:
            result += 1

    return result


def p2(array_of_ints: list[list[int]]) -> int:
    result = 0
    for row in array_of_ints:
        for i in range(len(row)):
            sublist = row[:i] + row[i + 1:]

            is_increasing = all(earlier < later for earlier, later in zip(sublist, sublist[1:]))
            is_decreasing = all(earlier > later for earlier, later in zip(sublist, sublist[1:]))
            has_proper_distance = all(abs(earlier - later) <= 3 for earlier, later in zip(sublist, sublist[1:]))
            if (is_increasing or is_decreasing) and has_proper_distance:
                result += 1
                break

    return result

