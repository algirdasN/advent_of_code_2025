def main():
    with open("data/01.txt") as file:
        rotations = [int(line.replace("R", "").replace("L", "-")) for line in file.readlines()]

    dial = 50
    exact = 0
    total = 0
    for r in rotations:
        if dial == 0 and r < 0:
            dial = 100

        div, dial = divmod(dial + r, 100)

        exact += dial % 100 == 0

        total += abs(div)
        if dial == 0 and r < 0:
            total += 1

    print(exact)
    print(total)


if __name__ == "__main__":
    main()
