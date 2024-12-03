import re


def p1(strings_list: list[str]) -> int:
    result = 0
    for line in strings_list:
        mul_instructions = extract_mul_instructions(line)
        for mul_instruction in mul_instructions:
            a, b = extract_mul_parts(mul_instruction)
            result += a * b

    return result

def p2(strings_list: list[str]) -> int:
    result = 0
    mul_enabled = True
    for line in strings_list:
        mul_instructions = extract_mul_and_conditional_instructions(line)
        for mul_instruction in mul_instructions:
            if mul_instruction == "do()":
                mul_enabled = True
                continue
            if mul_instruction == "don't()":
                mul_enabled = False
                continue
            if mul_enabled:
                a, b = extract_mul_parts(mul_instruction)
                result += a * b
                continue

    return result

def extract_mul_instructions(s: str) -> list[str]:
    pattern = r'mul\(\d+,\d+\)'
    return re.findall(pattern, s)

def extract_mul_and_conditional_instructions(s: str) -> list[str]:
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'

    return re.findall(pattern, s)

def extract_mul_parts(s: str) -> list[int]:
    pattern = r'mul\((\d+),(\d+)\)'
    match = re.search(pattern, s)
    if match:
        return [int(match.group(1)), int(match.group(2))]
    return []
