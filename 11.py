from collections import defaultdict

YOU = "you"
OUT = "out"
SVR = "svr"
DAC = "dac"
FFT = "fft"


def walk_simple(connections, curr, end):
    if curr == end:
        return 1

    return sum(walk_simple(connections, x, end) for x in connections[curr])


def walk_complex(connections, curr, end, valid_paths: defaultdict[str, int], invalid: set):
    if curr == end:
        return 1

    if curr in valid_paths:
        return valid_paths[curr]

    if curr in invalid:
        return 0

    total = sum(walk_complex(connections, x, end, valid_paths, invalid) for x in connections[curr])

    if total == 0:
        invalid.add(curr)
    else:
        valid_paths[curr] = total

    return total


def path_svr_to_out(connections):
    svr_to_dac = walk_complex(connections, SVR, DAC, defaultdict(int), {FFT, OUT})
    svr_to_fft = walk_complex(connections, SVR, FFT, defaultdict(int), {DAC, OUT})
    dac_to_fft = walk_complex(connections, DAC, FFT, defaultdict(int), {OUT})
    fft_to_dac = walk_complex(connections, FFT, DAC, defaultdict(int), {OUT})
    dac_to_out = walk_complex(connections, DAC, OUT, defaultdict(int), {FFT})
    fft_to_out = walk_complex(connections, FFT, OUT, defaultdict(int), {DAC})

    return svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out


def main():
    with open("data/11.txt") as file:
        row = file.read().splitlines()

    connections = {}
    for r in row:
        split = r.split(" ")
        connections[split[0][:-1]] = split[1:]

    print(walk_simple(connections, YOU, OUT))
    print(path_svr_to_out(connections))


if __name__ == "__main__":
    main()
