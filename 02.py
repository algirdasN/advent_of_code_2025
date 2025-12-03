import re

SIMPLE_PATTERN = re.compile(r"^(.+)\1$")
COMPLEX_PATTERN = re.compile(r"^(.+)\1+$")


def main():
    with open("data/02.txt") as file:
        ranges = file.readline().split(",")

    simple = 0
    total = 0
    for r in ranges:
        low, high = (int(x) for x in r.split("-"))

        for i in range(low, high + 1):
            s = str(i)

            if SIMPLE_PATTERN.match(s):
                simple += i

            if COMPLEX_PATTERN.match(s):
                total += i

    print(simple)
    print(total)


if __name__ == "__main__":
    main()
