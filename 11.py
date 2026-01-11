YOU = "you"
OUT = "out"
SVR = "svr"
DAC = "dac"
FFT = "fft"


def walk_simple(connections, curr, end):
    if curr == end:
        return 1

    return sum(walk_simple(connections, x, end) for x in connections[curr])


def walk_complex(connections, curr, end, valid_paths):
    if curr == end:
        return 1

    if curr not in valid_paths:
        valid_paths[curr] = sum(walk_complex(connections, x, end, valid_paths) for x in connections[curr])

    return valid_paths[curr]


def path_svr_to_out(connections):
    svr_to_dac = walk_complex(connections, SVR, DAC, {FFT: 0, OUT: 0})
    svr_to_fft = walk_complex(connections, SVR, FFT, {DAC: 0, OUT: 0})
    dac_to_fft = walk_complex(connections, DAC, FFT, {OUT: 0})
    fft_to_dac = walk_complex(connections, FFT, DAC, {OUT: 0})
    dac_to_out = walk_complex(connections, DAC, OUT, {FFT: 0})
    fft_to_out = walk_complex(connections, FFT, OUT, {DAC: 0})

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
