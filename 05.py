def consolidate_ranges(ranges: list[range]):
    sorted_ranges = sorted(ranges, key=lambda x: x.start)
    ranges.clear()
    ranges.append(sorted_ranges[0])

    for r in sorted_ranges[1:]:
        if ranges[-1].stop < r.start:
            ranges.append(r)
            continue

        new_r = range(ranges[-1].start, max(ranges[-1].stop, r.stop))
        ranges[-1] = new_r


def main():
    with open("data/05.txt") as file:
        r, i = file.read().split("\n\n")

    ranges = [range(int(x[0]), int(x[1]) + 1) for x in (line.split("-") for line in r.splitlines())]
    ingredients = [int(x) for x in i.splitlines()]

    fresh = 0
    for ingredient in ingredients:
        fresh += any(ingredient in r for r in ranges)

    print(fresh)

    consolidate_ranges(ranges)

    print(sum(len(x) for x in ranges))


if __name__ == "__main__":
    main()
