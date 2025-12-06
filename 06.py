def normalize_worksheet(worksheet):
    max_len = max(len(x) for x in worksheet)

    for i in range(len(worksheet)):
        row_len = len(worksheet[i])
        if row_len < max_len:
            worksheet[i] += " " * (max_len - row_len)


def main():
    with open("data/06.txt") as file:
        worksheet = file.read().splitlines()

    normalize_worksheet(worksheet)

    numbers_simple = zip(*[x.split() for x in worksheet[:-1]])
    operations = worksheet[-1].split()

    total = 0
    for i, n in enumerate(numbers_simple):
        total += eval(operations[i].join(n))

    print(total)

    numbers_complex = [[]]

    for i in range(len(worksheet[0])):
        number = "".join(x[i] for x in worksheet[:-1]).strip()
        if len(number) == 0:
            numbers_complex.append([])
            continue

        numbers_complex[-1].append(number)

    total = 0
    for i, n in enumerate(numbers_complex):
        total += eval(operations[i].join(n))

    print(total)


if __name__ == "__main__":
    main()
