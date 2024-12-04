
def p1(strings_list: list[str]) -> int:
    def is_valid(x, y):
        return 0 <= x < len(strings_list) and 0 <= y < len(strings_list[0])

    def search_word(x, y, dx, dy):
        word = ""
        for _ in range(4):
            if not is_valid(x, y):
                return False
            word += strings_list[x][y]
            x += dx
            y += dy
        return word

    directions = [
        (0, 1), (1, 0), (1, 1), (-1, 1),  # right, down, down-right, up-right
        (0, -1), (-1, 0), (-1, -1), (1, -1)  # left, up, up-left, down-left
    ]

    total = 0
    for i in range(len(strings_list)):
        for j in range(len(strings_list[i])):
            for dx, dy in directions:
                if "XMAS" == search_word(i, j, dx, dy):
                    total += 1

    return total

def p2(strings_list: list[str]) -> int:
    def is_valid(x, y):
        return 0 <= x < len(strings_list) and 0 <= y < len(strings_list[0])

    total = 0
    for i in range(1, len(strings_list) - 1):
        for j in range(1, len(strings_list[i]) - 1):
            if strings_list[i][j] == "A":
                # look for patterns
                # (i-1, j-1) (i-1, j) (i-1, j+1)
                #  (i, j-1)   (i, j)   (i, j+1)
                # (i+1, j-1) (i+1, j) (i+1, j+1)
                diagonal_one = strings_list[i - 1][j - 1] + "A" + strings_list[i + 1][j + 1]
                diagonal_two = strings_list[i + 1][j - 1] + "A" + strings_list[i - 1][j + 1]
                if diagonal_one in ["MAS", "SAM"] and diagonal_two in ["MAS", "SAM"]:
                    total += 1

    return total
