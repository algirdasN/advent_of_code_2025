def build_shapes(shape_input):
    shapes = []

    for shape in shape_input:
        shapes.append(grid_to_shape(shape.splitlines()[1:]))

    return shapes


def grid_to_shape(grid):
    shape_set = set()
    for _ in range(4):
        shape_set.add(grid_to_ints(grid))
        grid = rotate_grid(grid)

    grid = [list(row) for row in zip(*grid)]
    for _ in range(4):
        shape_set.add(grid_to_ints(grid))
        grid = rotate_grid(grid)

    return shape_set


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
    rem_shapes = []
    for i, x in enumerate(quantity):
        for _ in range(x):
            rem_shapes.append(shapes[i])

    grid = [0 for _ in range(dimensions[0])]

    return walk(dimensions, grid, rem_shapes)


def walk(dimensions, grid, rem_shapes):
    if len(rem_shapes) == 0:
        return True

    next_shape = rem_shapes[0]

    for i in range(dimensions[0] - 2):
        for j in range(dimensions[1] - 2):
            for shape in next_shape:
                if not can_place_shape(grid, shape, i, j):
                    continue

                place_shape(grid, shape, i, j)
                if walk(dimensions, grid, rem_shapes[1:]):
                    return True

                place_shape(grid, shape, i, j)

    return False


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
    pass
    total = 0
    for r in regions:
        total += solve_region(r, shapes)

    print(total)


if __name__ == "__main__":
    main()
