def main():
    with open("data/06.txt") as file:
        worksheet = file.read().splitlines()

    numbers = zip(*[x.split() for x in worksheet[:-1]])
    operations = worksheet[-1].split()

    total = 0
    for i, n in enumerate(numbers):
        total += eval(operations[i].join(n))

    print(total)


if __name__ == "__main__":
    main()
