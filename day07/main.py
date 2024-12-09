from enum import Enum
from itertools import product


def p1(strings_list: list[str]) -> int:
    result = 0
    #ie: 3267: 81 40 27
    for row in strings_list:
        equation = list(map(int, row.replace(':', '').split(' ')))
        expected_result = equation[0]
        equation_values = equation[1:] # remove the first element
        for operands in product([Operand.SUM, Operand.MULT], repeat=len(equation_values) - 1):
            # 81 + 40 + 27
            # 81 * 40 + 27
            # 81 * 40 * 27
            if apply_operands(equation_values, operands) == expected_result:
                result += expected_result
                break

    return result

def apply_operands(values, operands):
    result = values[0]
    for i in range(1, len(values)):
        if operands[i-1] == Operand.SUM:
            result += values[i]
        elif operands[i-1] == Operand.MULT:
            result *= values[i]
        elif operands[i-1] == Operand.CONCAT:
            result = int(str(result) + str(values[i]))
    return result

def p2(strings_list: list[str]) -> int:
    result = 0
    # ie: 3267: 81 40 27
    for row in strings_list:
        equation = list(map(int, row.replace(':', '').split(' ')))
        expected_result = equation[0]
        equation_values = equation[1:]  # remove the first element
        for operands in product([Operand.SUM, Operand.MULT, Operand.CONCAT], repeat=len(equation_values) - 1):
            if apply_operands(equation_values, operands) == expected_result:
                result += expected_result
                break

    return result

class Operand(Enum):
    SUM = 1
    MULT = 2
    CONCAT = 3