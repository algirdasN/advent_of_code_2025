def main():
    with open("data/01.txt") as file:
        rotations = [int(line.replace("R", "").replace("L", "-")) for line in file.readlines()]

    dial = 50
    total = 0
    for r in rotations:
        dial += r
        total += dial % 100 == 0

    print(total)

if __name__ == "__main__":
    main()