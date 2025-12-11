START = "you"
OUT = "out"


def walk(connections, curr):
    if curr == OUT:
        return 1

    return sum(walk(connections, x) for x in connections[curr])


def main():
    with open("data/11.txt") as file:
        row = file.read().splitlines()

    connections = {}
    for r in row:
        split = r.split(" ")
        connections[split[0][:-1]] = split[1:]

    print(walk(connections, START))


if __name__ == "__main__":
    main()
