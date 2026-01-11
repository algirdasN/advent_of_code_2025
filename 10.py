import itertools
import math
import sys
from collections import deque

import sympy as sp
from sympy import GreaterThan, LessThan


def light_to_int(lights: str):
    result = 0
    for light in lights[-2:0:-1]:
        result <<= 1
        result += light == "#"

    return result


def wiring_to_int(wiring: list[int]):
    return sum(2 ** x for x in wiring)


def check_light(light, wirings):
    queue = deque([(0, 0)])  # (current_state, num_switches)
    visited = {0}

    while queue:
        current, count = queue.popleft()
        if current == light: return count

        for w in wirings:
            nxt = current ^ w
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, count + 1))
    return None


def shrink_ranges(max_ranges, free_symbols, constraints):
    ranges = []

    for s in free_symbols:
        min_val = 0
        max_val = max_ranges[s]

        for c in constraints:
            if c.free_symbols != {s}:
                continue

            canonical = sp.reduce_inequalities(c >= 0, s).canonical
            if isinstance(canonical, GreaterThan):
                min_val = max(min_val, math.ceil(canonical.rhs))
            if isinstance(canonical, LessThan):
                max_val = min(max_val, math.floor(canonical.rhs))

        ranges.append(range(min_val, max_val + 1))

    return ranges


def solve_min_switches(min_equation, ranges, constraints):
    combinations = itertools.product(*ranges)
    min_solution = sys.maxsize

    for combo in combinations:
        for c in constraints:
            val = c(*combo)
            if val < 0 or val % 1 != 0:
                break
        else:
            min_solution = min(min_solution, min_equation(*combo))

    return min_solution


def solve_joltage(joltage, wirings):
    equations = [-x for x in joltage]

    symbols = [sp.Symbol(f's{i}', integer=True) for i in range(len(wirings))]

    for i, e in enumerate(wirings):
        for w in e:
            equations[w] += symbols[i]

    max_ranges = {s: max(j for e, j in zip(equations, joltage) if s in e.free_symbols) for s in symbols}

    constraints = sp.solve(equations, symbols)

    min_equation = sum(constraints.get(x, x) for x in symbols)

    if len(min_equation.free_symbols) == 0:
        return min_equation

    free_symbols = [s for s in symbols if s not in constraints]

    ranges = shrink_ranges(max_ranges, free_symbols, constraints.values())

    return solve_min_switches(sp.lambdify(free_symbols, min_equation), ranges,
                              [sp.lambdify(free_symbols, c) for c in constraints.values()])


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
