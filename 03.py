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

    total = 0
    for b in banks:
        left = 0
        right = len(b) - 11
        digits = []
        for _ in range(12):
            d = max(b[left:right])
            digits.append(d)

            left += b[left:right].index(d) + 1
            right += 1

        total += int("".join(str(x) for x in digits))

    print(total)


if __name__ == "__main__":
    main()
