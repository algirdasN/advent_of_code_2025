EMPTY = "."
ROLL = "@"


def count_neighbor_rolls(grid, x, y):
    min_x = max(x - 1, 0)
    max_x = min(x + 2, len(grid))

    min_y = max(y - 1, 0)
    max_y = min(y + 2, len(grid[x]))

    return [item for row in grid[min_x:max_x] for item in row[min_y:max_y]].count(ROLL) - (grid[x][y] == ROLL)


def remove(grid, x, y):
    if grid[x][y] == EMPTY:
        return 0

    if count_neighbor_rolls(grid, x, y) >= 4:
        return 0

    grid[x][y] = EMPTY

    min_x = max(x - 1, 0)
    max_x = min(x + 2, len(grid))

    min_y = max(y - 1, 0)
    max_y = min(y + 2, len(grid[x]))

    total_removed = 1
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            total_removed += remove(grid, i, j)

    return total_removed


def main():
    with open("data/04.txt") as file:
        grid = [[x for x in line] for line in file.read().splitlines()]

    accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == EMPTY:
                continue
            accessible += count_neighbor_rolls(grid, i, j) < 4

    print(accessible)

    total_removed = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total_removed += remove(grid, i, j)

    print(total_removed)


if __name__ == "__main__":
    main()
