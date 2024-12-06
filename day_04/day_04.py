import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def get_words(grid, x, y):
    words = []

    words.append(grid[y][x] + grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3])
    words.append(grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x])
    words.append(grid[y][x] + grid[y][x - 1] + grid[y][x - 2] + grid[y][x - 3])
    words.append(grid[y][x] + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x])

    words.append(grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3])
    words.append(grid[y][x] + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3])
    words.append(grid[y][x] + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3])
    words.append(grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3])

    return words

def check_x_mas(grid, x, y):
    if grid[y][x] != "A":
        return False

    top_left = grid[y-1][x-1]
    top_right = grid[y-1][x+1]
    bottom_left = grid[y+1][x-1]
    bottom_right = grid[y+1][x+1]

    if top_left == "M" and top_right == "M" and bottom_left == "S" and bottom_right == "S":
        return True
    if top_right == "M" and bottom_right == "M" and top_left == "S" and bottom_left == "S":
        return True
    if bottom_left == "M" and bottom_right == "M" and top_left == "S" and top_right == "S":
        return True
    if top_left == "M" and bottom_left == "M" and top_right == "S" and bottom_right == "S":
        return True
    
    return False

if __name__ == "__main__":
    input = load_input()

    width = len(input[0])

    blank_line = ['.'] * (width + 6)

    grid = [blank_line, blank_line, blank_line]
    for line in input:
        grid.append(['.'] * 3 + list(line) + ['.'] * 3)
    grid += [blank_line, blank_line, blank_line]

    words = []
    for x in range(width):
        for y in range(len(input)):
            words += get_words(grid, x + 3, y + 3)

    xmas_words = [x for x in words if x == "XMAS"]
    print(len(xmas_words))

    x_mas_count = 0
    for x in range(width):
        for y in range(len(input)):
            if check_x_mas(grid, x + 3, y + 3):
                x_mas_count += 1
    
    print(x_mas_count)