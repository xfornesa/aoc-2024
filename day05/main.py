def p1(page_ordering_rules: list[tuple[int, ...]], pages_to_produce_list: list[list[int]]) -> int:
    total = 0
    for pages_to_produce in pages_to_produce_list:
        if is_valid_page(pages_to_produce, page_ordering_rules):
            total += pages_to_produce[int(len(pages_to_produce)/2)]
    return total


def is_valid_page(pages_to_produce: list[int], page_ordering_rules):
    pages_printed = set()
    for page_to_produce in pages_to_produce:
        dependencies = set([pair[1] for pair in filter(lambda x: x[0] == page_to_produce, page_ordering_rules)])
        if not dependencies.isdisjoint(pages_printed):
            return False
        pages_printed.add(page_to_produce)

    return True


def fix_page(pages_to_produce: list[int], page_ordering_rules: list[tuple[int, ...]]):
    while not is_valid_page(pages_to_produce, page_ordering_rules):
        pages_printed = set()
        for i, page_to_produce in enumerate(pages_to_produce):
            dependencies = set([pair[1] for pair in filter(lambda x: x[0] == page_to_produce, page_ordering_rules)])
            offending_pages = dependencies.intersection(pages_printed)
            if offending_pages:
                j = pages_to_produce.index(offending_pages.pop())
                pages_to_produce[i], pages_to_produce[j] = pages_to_produce[j], pages_to_produce[i]
            pages_printed.add(page_to_produce)
    return pages_to_produce


def p2(page_ordering_rules: list[tuple[int, ...]], pages_to_produce_list: list[list[int]]) -> int:
    total = 0
    for pages_to_produce in pages_to_produce_list:
        if not is_valid_page(pages_to_produce, page_ordering_rules):
            pages_to_produce_fixed = fix_page(pages_to_produce, page_ordering_rules)
            total += pages_to_produce_fixed[int(len(pages_to_produce_fixed)/2)]
    return total
