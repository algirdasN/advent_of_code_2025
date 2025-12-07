def main():
    with open("data/07.txt") as file:
        grid = file.read().splitlines()

    beams = set()
    beams.add(grid[0].index("S"))

    total_hits = 0
    for row in grid[1:]:
        splitters = set(i for i, c in enumerate(row) if c == "^")
        hits = beams & splitters
        if not hits:
            continue

        total_hits += len(hits)
        for h in hits:
            beams.remove(h)
            beams.add(max(h - 1, 0))
            beams.add(min(h + 1, len(row) - 1))

    print(total_hits)


if __name__ == "__main__":
    main()
