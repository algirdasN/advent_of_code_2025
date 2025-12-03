def main():
    with open("data/03.txt") as file:
        banks = [[int(x) for x in line] for line in file.read().splitlines()]

    total = 0
    for b in banks:
        tens = max(b[:-1])
        i = b.index(tens)
        ones = max(b[i + 1:])
        total += tens * 10 + ones

    print(total)


if __name__ == "__main__":
    main()
