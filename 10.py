import sys
from collections import deque
from time import perf_counter

import sympy as sp


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


def wiring_to_int(wiring: list[int]):
    return sum(2 ** x for x in wiring)


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


def solve_min_switches(min_equation, ranges, constraints):
    if len(ranges) == 0:
        return min_equation

    min_solution = sys.maxsize
    new_ranges = ranges.copy()
    s, r = new_ranges.popitem()
    for i in r:
        new_constraints = [c.subs(s, i) for c in constraints]

        if any(int(x) != x or x < 0 for x in new_constraints if len(x.free_symbols) == 0):
            continue

        solution = solve_min_switches(min_equation.subs(s, i), new_ranges, new_constraints)

        if int(solution) == solution:
            min_solution = min(min_solution, solution)

    return min_solution


def solve_joltage(joltage, wiring):
    equations = [-x for x in joltage]

    for i in range(len(wiring)):
        exec(f"switch{i} = sp.Symbol('switch{i}', integer=True)")

    symbols = [v for k, v in locals().items() if k.startswith(f"switch")]

    for i, e in enumerate(wiring):
        for w in e:
            equations[w] += symbols[i]

    max_ranges = {s: max(j for e, j in zip(equations, joltage) if s in e.free_symbols) for s in symbols}

    constraints = sp.solve(equations, symbols)

    min_equation = sum(constraints.get(x, x) for x in symbols)

    ranges = {s: range(0, max_ranges[s] + 1) for s in symbols if s not in constraints}

    ans = solve_min_switches(min_equation, ranges, constraints.values())

    return ans


def main():
    with open("data/10.txt") as file:
        rows = file.read().splitlines()

    lights: list[int] = []
    wirings: list[list[list[int]]] = []
    joltages: list[list[int]] = []

    for r in rows:
        items = r.split()
        lights.append(light_to_int(items[0]))
        wirings.append([[int(y) for y in x[1:-1].split(",")] for x in items[1:-1]])
        joltages.append([int(x) for x in items[-1][1:-1].split(",")])

    print(sum(check_light(l, [wiring_to_int(x) for x in w]) for l, w in zip(lights, wirings)))
    print(sum(solve_joltage(j, w) for j, w in zip(joltages, wirings)))


if __name__ == "__main__":
    main()
