EMPTY = "."
ROLL = "@"


def main():
    with open("data/04.txt") as file:
        grid = [[x for x in line] for line in file.read().splitlines()]

    total = 0
    for i in range(len(grid)):
        min_x = max(i - 1, 0)
        max_x = min(i + 2, len(grid))
        for j in range(len(grid[i])):
            if grid[i][j] == EMPTY:
                continue

            min_y = max(j - 1, 0)
            max_y = min(j + 2, len(grid[i]))

            count_rolls = [item for row in grid[min_x:max_x] for item in row[min_y:max_y]].count(ROLL)

            total += count_rolls < 5

    print(total)


if __name__ == "__main__":
    main()
