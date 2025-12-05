def consolidate_ranges(ranges: list[range]):
    ranges_copy = [r for r in ranges]
    ranges.clear()

    while ranges_copy:
        r = ranges_copy.pop(0)
        for other_r in ranges_copy:
            min_start = min(r.start, other_r.start)
            max_stop = max(r.stop, other_r.stop)
            if len(r) + len(other_r) >= max_stop - min_start:
                ranges_copy.remove(other_r)
                ranges_copy.append(range(min_start, max_stop))
                break
        else:
            ranges.append(r)


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
