from enum import Enum


def find_guard(matrix: list[str]) -> tuple[int, int]:
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j
    return -1, -1


def count_visited_cells(matrix):
    result = 0
    for row in matrix:
        for cell in row:
            if cell == 'X':
                result += 1
    return result


def p1(matrix: list[str]) -> int:
    current_coords = find_guard(matrix)
    direction = Direction.UP
    while True:
        matrix[current_coords[0]] = visit(current_coords, matrix)
        next_move = move(current_coords, direction)
        if left_the_maze(next_move, matrix):
            # Out of bounds, so finish
            break
        if is_a_wall(matrix, next_move):
            direction = direction.turn_right()
            continue

        current_coords = next_move
    return count_visited_cells(matrix)


def is_a_wall(matrix, next_move):
    return matrix[next_move[0]][next_move[1]] == '#'


def is_a_visited_cell(matrix, next_move):
    return matrix[next_move[0]][next_move[1]] == 'X'


def left_the_maze(next_coords, matrix) -> bool:
    return (
            next_coords[0] < 0
            or next_coords[0] >= len(matrix)
            or next_coords[1] < 0
            or next_coords[1] >= len(matrix[0])
            )


def p2(source: list[str]) -> int:
    total_obstructions = 0
    for i, row in enumerate(source):
        for j, cell in enumerate(row):
            matrix = source.copy()
            # Set an obstructions in i,j
            matrix[i] = matrix[i][:j] + "#" + matrix[i][j + 1:]
            # If found a loop, then it's an obstruction

            current_coords = find_guard(matrix)
            direction = Direction.UP
            cells_visited: set[str] = set()
            while True:
                next_move = move(current_coords, direction)
                if left_the_maze(next_move, matrix):
                    # Out of bounds, so finish
                    break
                if is_a_wall(matrix, next_move):
                    direction = direction.turn_right()
                    continue
                if is_a_loop(cells_visited, current_coords, direction):
                    total_obstructions += 1
                    break

                cells_visited.add(str(current_coords) + str(direction))
                current_coords = next_move

    return total_obstructions


def is_a_loop(cells_visited, current_coords, direction):
    return str(current_coords) + str(direction) in cells_visited


def move(current_coords, direction):
    return current_coords[0] + direction.coords()[0], current_coords[1] + direction.coords()[1]


def visit(current_coords, matrix):
    return matrix[current_coords[0]][:current_coords[1]] + "X" + matrix[current_coords[0]][
                                                                 current_coords[1] + 1:]


class Direction(Enum):
    UP: tuple[int, int] = (-1, 0)
    RIGHT: tuple[int, int] = (0, 1)
    DOWN: tuple[int, int] = (1, 0)
    LEFT: tuple[int, int] = (0, -1)

    def turn_right(self):
        direction_order = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        new_index = (direction_order.index(self) + 1) % len(direction_order)
        return direction_order[new_index]

    def coords(self) -> tuple[int, int]:
        return self.value[0], self.value[1]
