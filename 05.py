def main():
    with open("data/05.txt") as file:
        r, i = file.read().split("\n\n")

    ranges = [range(int(x[0]), int(x[1]) + 1) for x in (line.split("-") for line in r.splitlines())]
    ingredients = [int(x) for x in i.splitlines()]

    fresh = 0
    for ingredient in ingredients:
        fresh += any(ingredient in r for r in ranges)

    print(fresh)


if __name__ == "__main__":
    main()
