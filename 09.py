def main():
    with open("data/09.txt") as file:
        points = [eval("(" + x + ")") for x in file.read().splitlines()]

    areas = {}
    for index, i in enumerate(points):
        for j in points[index + 1:]:
            areas[(i, j)] = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)

    print(sorted(areas.values(), reverse=True)[0])


if __name__ == "__main__":
    main()
