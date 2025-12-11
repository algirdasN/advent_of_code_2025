def check_h_intersection(square, h_edges):
    min_x = min(square[0][0], square[1][0])
    max_x = max(square[0][0], square[1][0])
    min_y = min(square[0][1], square[1][1])
    max_y = max(square[0][1], square[1][1])

    for x_range, y in h_edges:
        if not min_y < y < max_y:
            continue

        if x_range.stop <= min_x or x_range.start >= max_x:
            continue

        return False

    return True


def check_v_intersection(square, v_edges):
    min_x = min(square[0][0], square[1][0])
    max_x = max(square[0][0], square[1][0])
    min_y = min(square[0][1], square[1][1])
    max_y = max(square[0][1], square[1][1])

    for x, y_range in v_edges:
        if not min_x < x < max_x:
            continue

        if y_range.stop <= min_y or y_range.start >= max_y:
            continue

        return False

    return True


def main():
    with open("data/09.txt") as file:
        points = [eval("(" + x + ")") for x in file.read().splitlines()]

    h_edges = []
    v_edges = []

    for i in range(len(points)):
        if points[i - 1][1] == points[i][1]:
            h_edges.append(
                (range(min(points[i - 1][0], points[i][0]), max(points[i - 1][0], points[i][0])), points[i][1]))
        else:
            v_edges.append(
                (points[i][0], range(min(points[i - 1][1], points[i][1]), max(points[i - 1][1], points[i][1]))))

    areas = {}
    for index, i in enumerate(points):
        for j in points[index + 1:]:
            areas[(i, j)] = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)

    sorted_areas = sorted(areas.items(), key=lambda x: x[1], reverse=True)

    print(sorted_areas[0][1])

    for square, area in sorted_areas:
        if check_h_intersection(square, h_edges) and check_v_intersection(square, v_edges):
            print(area)
            break


if __name__ == "__main__":
    main()
