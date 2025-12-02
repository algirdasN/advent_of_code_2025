def main():
    with open("data/02.txt") as file:
        ranges = file.readline().split(",")

    total = 0
    for r in ranges:
        low, high = (int(x) for x in r.split("-"))

        for i in range(low, high + 1):
            s = str(i)
            l = len(s)
            if l % 2 != 0:
                continue
            if s[:l // 2] == s[l // 2:]:
                total += i

    print(total)

if __name__ == "__main__":
    main()
