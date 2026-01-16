def build_shapes(shape_input):
    shapes = []

    for shape in shape_input:
        shapes.append(grid_to_shape(shape.splitlines()[1:]))

    return shapes


def grid_to_shape(grid):
    shapes = []
    for _ in range(4):
        shapes.append(grid_to_ints(grid))
        grid = rotate_grid(grid)

    grid = [list(row) for row in zip(*grid)]
    for _ in range(4):
        shapes.append(grid_to_ints(grid))
        grid = rotate_grid(grid)

    return frozenset(shapes)


def grid_to_ints(grid):
    result = [0 for _ in grid]

    for index, row in enumerate(grid):
        for cell in reversed(row):
            result[index] <<= 1
            result[index] += cell == "#"

    return tuple(result)


def rotate_grid(grid):
    new_grid = [["."] * len(x) for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[j][2 - i] = grid[i][j]

    return new_grid


def parse_regions(regions):
    result = []
    for r in regions.splitlines():
        dimensions, quantity = r.split(": ")

        result.append(tuple((tuple(int(x) for x in dimensions.split("x")), [int(x) for x in quantity.split(" ")])))

    return result


def solve_region(region, shapes):
    dimensions, quantity = region
    rem_shapes = {}
    for i, x in enumerate(quantity):
        if x == 0:
            continue

        rem_shapes[shapes[i]] = x

    grid = [0 for _ in range(dimensions[0])]

    return walk(dimensions, grid, rem_shapes)


def walk(dimensions, grid, rem_shapes, start_row=0, start_column=0):
    if sum(rem_shapes.values()) == 0:
        return True

    for i in range(start_row, dimensions[0] - 2):
        for j in range(start_column, dimensions[1] - 2):
            start_column = 0

            if get_shape_size(rem_shapes) > (dimensions[0] - i) * dimensions[1] - j:
                return False

            for shape, amount in rem_shapes.items():
                if amount == 0:
                    continue

                for variant in shape:
                    if not can_place_shape(grid, variant, i, j):
                        continue

                    place_shape(grid, variant, i, j)
                    rem_shapes[shape] -= 1

                    if walk(dimensions, grid, rem_shapes, i, j + 1):
                        return True

                    place_shape(grid, variant, i, j)
                    rem_shapes[shape] += 1

    return False


def get_shape_size(shapes):
    total = 0
    for shape_set, amount in shapes.items():
        for row in next(iter(shape_set)):
            total += amount * bin(row).count('1')

    return total


def can_place_shape(grid, shape, x, y):
    for i, s in enumerate(shape):
        if grid[x + i] & (s << y) != 0:
            return False

    return True


def place_shape(grid, shape, x, y):
    for i, s in enumerate(shape):
        grid[x + i] ^= s << y


def main():
    with open("data/12.txt") as file:
        contents = file.read().split("\n\n")

    shapes = build_shapes(contents[:-1])
    regions = parse_regions(contents[-1])

    print(sum(solve_region(r, shapes) for r in regions))


if __name__ == "__main__":
    main()
