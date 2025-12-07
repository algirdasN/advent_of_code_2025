from collections import defaultdict


def main():
    with open("data/07.txt") as file:
        grid = file.read().splitlines()

    start = grid[0].index("S")

    beams = set()
    beams.add(start)

    timelines = defaultdict(int)
    timelines[start] = 1

    total_hits = 0
    for row in grid[1:]:
        splitters = set(i for i, c in enumerate(row) if c == "^")
        hits = beams & splitters
        if not hits:
            continue

        total_hits += len(hits)
        for h in hits:
            beams.remove(h)
            beams.add(h - 1)
            beams.add(h + 1)

            t = timelines.pop(h)
            timelines[h - 1] += t
            timelines[h + 1] += t

    print(total_hits)
    print(sum(timelines.values()))


if __name__ == "__main__":
    main()
