from collections import deque


class Move:
    def __init__(self, value, num_wirings, used_wirings):
        self.value: int = value
        self.num_switches: int = num_wirings
        self.used_switches: list[int] = used_wirings


def light_to_int(lights: str):
    result = 0
    for light in lights[-2:0:-1]:
        result <<= 1
        result += light == "#"

    return result


def wiring_to_int(wiring):
    return sum(2 ** int(x) for x in wiring[1:-1].split(","))


def check_light(light, wirings):
    moves = deque()
    for w in wirings:
        moves.append(Move(w, 1, [w]))

    if any(m.value == light for m in moves):
        return 1

    while moves:
        move = moves.popleft()
        for w in wirings:
            if w in move.used_switches:
                continue

            new_value = move.value ^ w
            new_num = move.num_switches + 1
            if new_value == light:
                return new_num

            new_used = move.used_switches + [w]
            moves.append(Move(new_value, new_num, new_used))

    return None


def main():
    with open("data/10.txt") as file:
        rows = file.read().splitlines()

    lights: list[int] = []
    wirings: list[list[int]] = []

    for r in rows:
        items = r.split()
        lights.append(light_to_int(items[0]))
        wirings.append([wiring_to_int(x) for x in items[1:-1]])

    print(sum(check_light(l, w) for l, w in zip(lights, wirings)))


if __name__ == "__main__":
    main()
